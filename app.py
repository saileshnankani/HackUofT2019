import os

from flask import Flask, request

from src.api.ai import extract_image_details
#from src.api.firebase import extract_from_image_db, query_to_expired_db

app = Flask(__name__)

base = os.getcwd()
ext = '/data/imgs/'

broccoli = base + ext + 'broccoli/' + '0.jpg'
banana = base + ext + 'fruits/Training/Banana/' +'0_100.jpg'
data = [banana, broccoli]

image = data[0]

def test(file):
	files = []
	for num, val in enumerate(data):
		labels = extract_image_details(filename=file)
	return f"<p> The AI has found your picture to be {labels} <p>" 

@app.route('/')
def main():
    return '<h1>Hello world!</h1>'

@app.route('/detect', methods=['POST'])
def image():
	# Input: URL to DB (Firebase)
	# Note: Json Dumps might be useful
	#img_file = extract_from_image_bucket(img)
    data = extract_image_details(img_file)
    #query = query_to_expired_db(data) # in DB File
    #send_to_user(query) # In this file
    return "Success"

if __name__ == '__main__':
    app.run(debug=True)