import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Settings:
    PROJECT_TITLE: str = "fastapi Car service exercise"
    PROJECT_VERSION: str = "0.1.0"
    
    POSTGRES_USER : str = os.getenv("POSTGRES_USER","postgres")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD","Singhrhea%40123")
    POSTGRES_SERVER : str = os.getenv("POSTGRES_SERVER","localhost")
    POSTGRES_PORT : str = os.getenv("POSTGRES_PORT",5432) # default postgres port is 5432
    POSTGRES_DB : str = os.getenv("POSTGRES_DB","Car")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    
settings = Settings()