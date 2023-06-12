from prefect import flow


@flow(log_prints=True)
def buy():
    """Buy securities"""
    print("Bought securities! 💸")
