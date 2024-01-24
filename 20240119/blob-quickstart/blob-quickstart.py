import os, uuid, dotenv
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

import shutil


dotenv.load_dotenv()

def cleanup(container_client, local_path):
    print("\nDeleting blob container...")
    container_client.delete_container()
    
    print("Deleting the local source and downloaded files...")
    shutil.rmtree(local_path)
    

def list_blob(container_client):
    print("\nListing blobs...")
    
    blob_list = container_client.list_blobs()
    for blob in blob_list:
        print("\t" + blob.name)


try:
    print("Azure Blob Storage Python quickstart sample")

    connect_str = os.getenv('CONNECTION_STRING')
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    
    container_name = str(uuid.uuid4())
    container_client = blob_service_client.create_container(container_name)
    
    local_path = "./data"
    # os.mkdir(local_path)
    local_file_name = str(uuid.uuid4()) + ".txt"
    upload_file_path = os.path.join(local_path, local_file_name)
    
    with open(upload_file_path, "w") as file:
        file.write("Hello, World!")
    
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)
    
    print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)
    
    with open(upload_file_path, "rb") as data:
        blob_client.upload_blob(data)
    
    list_blob(container_client)
    cleanup(container_client, local_path)
    

except Exception as ex:
    print('Exception:')
    print(ex)