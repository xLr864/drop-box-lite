import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

try:
    # print("Azure Blob Storage v" + __version__ + " - Python quickstart sample")
    # connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
    # # print(connect_str)
    # blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    # containers = blob_service_client.list_containers()
    # for c in containers:
    #     print(c.name)
    # local_file_name = "Dinesh_Pandit.txt"
    # blob_client = blob_service_client.get_blob_client(container="gmail-lite", blob=local_file_name)
    # with open(f"{local_file_name}", "rb") as data:
    #     blob_client.upload_blob(data)
    print(os.getenv('ACCESS_KEY_STORAGE'))


except Exception as ex:
    print('Exception:')
    print(ex)