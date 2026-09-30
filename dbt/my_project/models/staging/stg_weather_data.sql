{{ config(
    materialized = 'table',
    unique_key = 'id' 
)}}

with source as (
    select * 
    from {{ source('dev', 'raw_weather_data')}}
    )
, 
dedup as (
    select *,
        row_number() over(partition by time order by inserted_at) as rk
    from source
    )

-- select * from dedup
select id,
    city,
    temperature,
    weather_descriptions,
    wind_speed,
    time as weather_local_time,
    (inserted_at + (utc_offset || 'hours')::interval) as inserted_at_local
from dedup
where rk = 1

