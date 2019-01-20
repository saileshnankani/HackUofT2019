import os
import boto3

from src.api.ai import extract_image_details

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'UofTHacks2019.json'

s3 = boto3.resource('s3')

upload_path = os.getcwd() + "/data/imgs/broccoli/0.jpg"
download_path = "1.jpg"
bucket = 'images.u.of.t.hacks.2019'
image = "0.jpg"

s3.meta.client.upload_file(upload_path, bucket, image)
file = s3.meta.client.download_file(bucket, image, download_path)

details = extract_image_details(filename=path)
print(details) # Should return highest rank classified object