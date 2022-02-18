from flask import Flask,render_template,request,redirect,url_for,flash
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__,generate_blob_sas,BlobSasPermissions
import os
from datetime import datetime, timedelta
from flask_session import Session
from werkzeug.utils import secure_filename
account_name = 'attachmentcollector'
account_key = 'bvOIqFsSxY+UjObP/IEbZ8hNrtsSHXUbWmHoCtl40tRs44NprPTPodEHeuLqlHc4Mk+ODfIyvOJqBlWotgcg8g=='
container_name = 'gmail-lite'
connect_str = "DefaultEndpointsProtocol=https;AccountName=attachmentcollector;AccountKey=bvOIqFsSxY+UjObP/IEbZ8hNrtsSHXUbWmHoCtl40tRs44NprPTPodEHeuLqlHc4Mk+ODfIyvOJqBlWotgcg8g==;EndpointSuffix=core.windows.net"
UPLOADED_FOLDER = "uploads"
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOADED_FOLDER



@app.route("/",methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        f = request.files['file']
        try:
            print("Azure Blob Storage v" + __version__ + " - Python quickstart sample")
            blob_service_client = BlobServiceClient.from_connection_string(connect_str)
            local_file_name = secure_filename(f.filename)
            f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename)))
            blob_client = blob_service_client.get_blob_client(container="gmail-lite", blob=local_file_name)
            with open(f"{UPLOADED_FOLDER}/{local_file_name}", "rb") as data:
                blob_client.upload_blob(data, overwrite=True)

        except Exception as ex:
            print('Exception:')
            print(ex)
            return "error something went wrong"


        os.remove(f"{UPLOADED_FOLDER}/{local_file_name}")
        # download_file_path = f"{UPLOADED_FOLDER}/{local_file_name}"
        # with open(download_file_path, "wb") as download_file:
        #     download_file.write(blob_client.download_blob().readall())
        sas_blob = generate_blob_sas(account_name=account_name, 
                                container_name=container_name,
                                blob_name=local_file_name,
                                account_key=account_key,
                                permission=BlobSasPermissions(read=True),
                                expiry=datetime.utcnow() + timedelta(hours=1))
        url = 'https://'+"attachmentcollector"+'.blob.core.windows.net/'+'gmail-lite'+'/'+local_file_name+'?'+sas_blob
        return render_template('download.html',url=url)
    return render_template('index.html')

