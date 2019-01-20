import os

import boto3
from flask import Flask, request

from src.api.ai import extract_image_details
from src.api.aws import aws_lookup, query_to_expired_db

app = Flask(__name__)
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'UofTHacks2019.json' # Set's environment variables

@app.route('/')
def main():
    return '<h1>Hello world!!</h1>'

@app.route('/detect')
def image_analysis():
	# Input: URL to AWS S3 image
	# Output: Json results of the image

    download_path = "1.jpg" # Testing variable (Same with 0.jpg)
    img_file = aws_lookup(img='0.jpg', download_path=download_path) #Output: Image
    data = extract_image_details('1.jpg') # Output: String
    query = query_to_expired_db(data) # Output: String
    #send_to_user(query) # Output: Json
    return query


if __name__ == '__main__':
    app.run(debug=True)
