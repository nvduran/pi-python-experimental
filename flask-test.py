import io
from picamera2 import Picamera2, Preview
from flask import Flask, Response, send_file

app = Flask(__name__)

picam2 = Picamera2()
picam2.start()

@app.route('/capture')
def capture():
    stream = io.BytesIO()
    picam2.capture_file(stream, format='jpeg')
    stream.seek(0)
    return send_file(stream, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)
