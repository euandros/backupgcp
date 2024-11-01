# Google Cloud Storage Backup Script

Este repositório contém um script Python que realiza o upload de arquivos de um diretório local para um bucket no Google Cloud Storage (GCS). O script lista os arquivos presentes no diretório, organiza-os por data de modificação e os envia para o bucket especificado.

## Funcionalidades

- Lista todos os arquivos de um diretório local.
- Ordena os arquivos de acordo com a data de modificação.
- Realiza o upload dos arquivos para um bucket no Google Cloud Storage.
- Suporte para organização dos arquivos dentro de pastas no bucket.

## Pré-requisitos

Antes de executar o script, você precisará das seguintes dependências e configurações:

1. **Google Cloud SDK** instalado e configurado:
   - Criar uma conta no [Google Cloud](https://cloud.google.com/).
   - Criar um bucket no [Google Cloud Storage](https://cloud.google.com/storage).
   - Gerar uma credencial de serviço no GCP e fazer o download do arquivo `cred.json`.

2. **Variáveis de ambiente** configuradas:
   - `GCP-BUCKET`: Nome do bucket no Google Cloud Storage.
   - `GCP-BUCKET-FOLDER`: (Opcional) Nome da pasta dentro do bucket onde os arquivos serão enviados.
   - `GCP-LOCAL-FOLDER`: Caminho local do diretório onde os arquivos estão armazenados.

3. **Bibliotecas Python**:

   - Instalar as dependências com o seguinte comando:
     
     ```bash
     pip install google-cloud-storage
     ```

## Como usar

1. **Configurar as variáveis de ambiente**:

   Assegure-se de que as seguintes variáveis de ambiente estejam configuradas corretamente no seu sistema:
   
   - `GCP-BUCKET`: Nome do seu bucket no GCS.
   - `GCP-BUCKET-FOLDER`: (Opcional) Diretório dentro do bucket no qual os arquivos serão armazenados.
   - `GCP-LOCAL-FOLDER`: Caminho local para a pasta com os arquivos que deseja enviar.

   Exemplo de configuração em um arquivo `.env`:
   ```bash
   export GCP-BUCKET="nome-do-bucket"
   export GCP-BUCKET-FOLDER="backups/2024"
   export GCP-LOCAL-FOLDER="/caminho/para/diretorio/local"

2. **Rodar o script**:

   Após configurar as variáveis de ambiente, execute o script da seguinte maneira:
    ```bash
    python3 upload_to_gcs.py
    ```

   O script listará os arquivos no diretório local, mostrará a data de última modificação de cada arquivo, e em seguida enviará os arquivos para o bucket GCS.

## Estrutura do Código

- **envio(filename, file)**: Função responsável por fazer o upload dos arquivos para o bucket.
- O script lista todos os arquivos do diretório local, organiza-os por data de modificação, e os envia ao bucket no caminho especificado.

## Exemplo de Saída

  Ao executar o script, você verá algo semelhante ao seguinte:
   ```bash
   12/01/2024 :: 15:30:45  --> backup1.sql
   12/02/2024 :: 08:20:12  --> backup2.sql
   Enviando arquivos para o Bucket na GCP
   ```

## Melhorias Futuras

- Adicionar tratamento de erros para garantir a robustez do upload em casos de falha.
- Paralelização dos uploads para aumentar a eficiência.
- Implementar uma opção de exclusão automática de arquivos antigos no diretório local após o upload.
