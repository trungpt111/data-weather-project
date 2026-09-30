{{ config(
    materialized = 'table'
)}}

select 
    city,
    date(weather_local_time),
    round(avg(temperature)::numeric,2) as avg_temperature,
    round(avg(wind_speed)::numeric,2) as avg_wind_speed
from {{ ref('wearther_report')}}
group by
    city,
    date(weather_local_time)
order by
    city,
    date(weather_local_time)
