import requests
from prefect import flow


@flow(log_prints=True)
def fetch_weather(lat: float = 38.9, lon: float = -77.0):
    weather = requests.get(
        "https://api.open-meteo.com/v1/forecast/",
        params=dict(latitude=lat, longitude=lon, hourly="temperature_2m"),
    )
    most_recent_temp = float(weather.json()["hourly"]["temperature_2m"][0])
    print(f"Most recent temp C: {most_recent_temp} degrees")
    return


if __name__ == "__main__":
    fetch_weather.from_source(
        source="https://github.com/discdiver/quick-deploy.git",
        entrypoint="get_weather_gcp.py:fetch_weather",
    ).deploy(
        name="test-infra-setup",
        work_pool_name="my-gcp-pool-from-cli",
    )
