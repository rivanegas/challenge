import os
from dotenv import load_dotenv

class DatabaseConfig:
    def __init__(self):
        # Cargar las variables de entorno desde el archivo .env
        load_dotenv()

        self.dbname = os.getenv('DB_NAME')
        self.user = os.getenv('DB_USER')
        self.password = os.getenv('DB_PASSWORD')
        self.host = os.getenv('DB_HOST')
        self.port = os.getenv('DB_PORT')

    def get_database_url(self):
        return (
            f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.dbname}"
        )
