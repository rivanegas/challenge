import pandas as pd
from flask import request
from flask_restful import Resource
from db.config import DatabaseConfig
from db.database import PostgresDB
from db.tables import table_schemas

class UploadCSV(Resource):
    def post(self):
        # Imprimir el contenido de la solicitud
        print(f"Content-Type: {request.content_type}")
        print(f"Files: {request.files}")
        # Verificar que se envió al menos un archivo
        if 'files' not in request.files:
            return {'message': 'No files provided'}, 400

        # Crear instancia de la configuración de base de datos
        db_config = DatabaseConfig()
        db = PostgresDB(config=db_config)
        db.connect()

        files = request.files.getlist('files')

        for file in files:
            if file.filename.endswith('.csv'):
                # Leer el archivo CSV en un DataFrame de pandas
                dataframe = pd.read_csv(file)
                print(dataframe.dtypes)

                # Determinar el nombre de la tabla desde el nombre del archivo
                table_name = file.filename.rsplit('.', 1)[0]

                # Verificar si la tabla existe en los esquemas definidos
                if table_name in table_schemas:
                    db.create_table(table_name, table_schemas[table_name])
                    db.insert_dataframe(table_name, dataframe)
                else:
                    return {'message': f'Table schema for {table_name} not found'}, 400

        db.close()
        return {'message': 'Files successfully processed'}, 200
