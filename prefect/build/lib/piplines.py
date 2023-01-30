from prefect import task, flow
import pandas as pd
from urllib.parse import urlparse
import os
import click

@task
def load(path: str) -> pd.DataFrame:
    data = pd.read_csv(path)
    return data

@task
def normalize(data: pd.DataFrame) -> pd.DataFrame:
    data['domain_of_url'] = data['url'].apply(lambda x: urlparse(x).netloc)
    return data

@task
def save(data: pd.DataFrame, path: str):
    data.to_csv(path, index=False)

@click.command()
@click.option("--data_path", "-r", type=str)
@click.option("--output_path", "-w", type=str)
@flow
def start_pipline(data_path, output_path):
    data = load(data_path)
    data = normalize(data)
    save(data, output_path)