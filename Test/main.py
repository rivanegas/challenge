from flask import Flask
from flask_restful import Api
from endpoint import UploadCSV

app = Flask(__name__)
api = Api(app)

# Ruta para subir archivos CSV
api.add_resource(UploadCSV, '/upload_csv')

if __name__ == '__main__':
    app.run(debug=True)