from prefect import flow


@flow(log_prints=True)
def my_flow(name: str = "world"):
    print(f"Hello, {name}!")
