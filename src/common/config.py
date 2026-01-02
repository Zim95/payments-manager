# standard library
import os

# modules
from browseterm_db.common.config import DBConfig

# DATABASE CONFIG
DB_USERNAME: str = os.getenv("DB_USERNAME")
DB_PASSWORD: str = os.getenv("DB_PASSWORD")
DB_HOST: str = os.getenv("DB_HOST")
DB_PORT: str = os.getenv("DB_PORT")
DB_NAME: str = os.getenv("DB_NAME")
DB_DATABASE_NAME: str = os.getenv("DB_DATABASE_NAME")
# DB Config
DB_CONFIG: DBConfig = DBConfig(
    username=DB_USERNAME,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT,
    name=DB_NAME,
    database_name=DB_DATABASE_NAME
)
