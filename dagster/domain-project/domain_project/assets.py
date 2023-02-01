from dagster import job, op, get_dagster_logger, asset, StringSource, resource
import pandas as pd
from urllib.parse import urlparse
import os

@asset (config_schema={"DATA_PATH": str})
def load(context) -> pd.DataFrame:
    data = pd.read_csv(context.op_config["DATA_PATH"])
    return data

@asset
def normalize(load) -> pd.DataFrame:
    load['domain_of_url'] = load['url'].apply(lambda x: urlparse(x).netloc)
    return load

@asset (config_schema={"SAVE_PATH": str})
def save(context, normalize) -> None:
    normalize.to_csv(context.op_config["SAVE_PATH"], index=False)

@resource(config_schema={"DATA_PATH": StringSource})
def data_path(init_context):
    return init_context.resource_config["DATA_PATH"]

@resource(config_schema={"SAVE_PATH": StringSource})
def save_path(init_context):
    return init_context.resource_config["SAVE_PATH"]
