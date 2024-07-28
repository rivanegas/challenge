import psycopg2
import pandas as pd

class PostgresDB:
    def __init__(self, config):
        self.config = config
        self.connection = None

    def connect(self):
        """Crea una conexión a la base de datos PostgreSQL usando la configuración proporcionada."""
        try:
            self.connection = psycopg2.connect(self.config.get_database_url())
            print("Conexión a PostgreSQL exitosa.")
        except Exception as e:
            print(f"Error al conectar a PostgreSQL: {e}")

    def close(self):
        """Cierra la conexión a la base de datos."""
        if self.connection:
            self.connection.close()
            print("Conexión a PostgreSQL cerrada.")

    def create_table(self, table_name, columns):
        """Crea una tabla en la base de datos con parámetros dinámicos."""
        column_definitions = ', '.join(columns)
        create_table_query = f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            {column_definitions}
        );
        '''
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(create_table_query)
                self.connection.commit()
                print(f"Tabla '{table_name}' creada exitosamente.")
        except Exception as e:
            print(f"Error al crear la tabla: {e}")

    def insert_dataframe(self, table_name, dataframe):
        """Inserta datos desde un DataFrame en la tabla."""
        if dataframe.empty:
            print("El DataFrame está vacío. No se insertarán datos.")
            return

        columns = ', '.join(dataframe.columns)
        placeholders = ', '.join(['%s'] * len(dataframe.columns))
        insert_query = f'''
        INSERT INTO {table_name} ({columns}) VALUES ({placeholders});
        '''

        data = dataframe.values.tolist()

        try:
            with self.connection.cursor() as cursor:
                cursor.executemany(insert_query, data)
                self.connection.commit()
                print("Datos insertados exitosamente desde DataFrame.")
        except Exception as e:
            print(f"Error al insertar datos desde DataFrame: {e}")

    def query_data(self, table_name):
        """Consulta y muestra los datos de la tabla con nombre dinámico."""
        select_query = f'SELECT * FROM {table_name};'
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(select_query)
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
        except Exception as e:
            print(f"Error al consultar datos: {e}")
           