import os

from flask import Flask

from src.api.ai import extract_image_details

app = Flask(__name__)

base = os.getcwd()
ext = '/data/imgs/'

broccoli = base + ext + 'broccoli/' + '0.jpg'
#banana = base + ext + '' +'0_100.jpg'
data = [broccoli]

@app.route('/')
def main():
    return '<h1>Hello world!</h1>'

@app.route('/detect')
def test():
	files = []
#	for num, val in enumerate(data):
	labels = extract_image_details(filename=data[0])
	return f"<p> The AI has found your picture to be {labels} <p>" 

if __name__ == '__main__':
    app.run(debug=True)