import os
import time
from os import environ
from google.cloud import storage

# Configuração do Google Cloud Storage
bucketName = environ.get('GCP-BUCKET')
bucketFolder = environ.get('GCP-BUCKET-FOLDER')  # Ex: 'backups/2024/'
LocalFolder = environ.get('GCP-LOCAL-FOLDER')

# Lista todos os arquivos do diretório informado
list_of_files = filter(lambda x: os.path.isfile(os.path.join(LocalFolder, x)), os.listdir(LocalFolder))

# Coloca os arquivos em ordem ascendente, tendo por base a última modificação
list_of_files = sorted(list_of_files, key=lambda x: os.path.getmtime(os.path.join(LocalFolder, x)))

# Imprime na tela o caminho do arquivo e a marca de tempo da última alteração
for file_name in list_of_files:
    file_path = os.path.join(LocalFolder, file_name)
    timestamp_str = time.strftime('%m/%d/%Y :: %H:%M:%S', time.gmtime(os.path.getmtime(file_path)))
    print(timestamp_str, ' -->', file_name)

# Inicializa o cliente do Google Cloud Storage
client = storage.Client.from_service_account_json('cred.json')
bucket = client.get_bucket(bucketName)

def envio(filename, file):
    """Envio dos arquivos listados no diretório informado para o Bucket."""
    print('Enviando arquivos para o Bucket na GCP')
    
    # Define o caminho dentro do bucket (exemplo: backups/2024/nome_do_arquivo)
    bucket_path = f'{bucketFolder}/{filename}' if bucketFolder else filename
    
    # Cria um blob com o caminho definido
    blob = bucket.blob(bucket_path)
    
    # Envia o arquivo local para o bucket no caminho definido
    blob.upload_from_filename(file)

# Enviar arquivos para o Bucket
files = os.listdir(LocalFolder)
for f in files:
    envio(f, os.path.join(LocalFolder, f))
