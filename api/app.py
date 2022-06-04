from flask import Flask, jsonify, send_file
import boto3
import requests
import io
import os

app = Flask(__name__)

@app.get('/health')
def health():
    return jsonify({"health": "alive"})

@app.get('/')
def get_file():
    key_id = os.getenv('AWS_ACCESS_KEY_ID')
    secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')

    s3_client = boto3.client(
        's3',
        aws_access_key_id=key_id,
        aws_secret_access_key=secret_key
    )

    bucket = os.getenv('FILES_BUCKET')
    key = os.getenv('FILE_BUCKET_KEY')

    url = s3_client.generate_presigned_url(
        ClientMethod='get_object',
        Params = {
            'Bucket': bucket,
            'Key': key
        }
    )

    response = requests.get(url)

    file = io.BytesIO(response.content)
    return send_file(file, mimetype='application/pdf', attachment_filename='certificate.pdf')