from dagster import Definitions, load_assets_from_modules
from data_pipeline import assets  # noqa: TID252

# Load all assets
all_assets = load_assets_from_modules([assets])

defs = Definitions(
    assets=all_assets,
)
