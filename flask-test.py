import io
from picamera2 import Picamera2
from flask import Flask, Response

app = Flask(__name__)

# http://127.0.0.1:5000/video_feed

picam2 = Picamera2()
picam2.start()

def generate_frames():
    stream = io.BytesIO()
    while True:
        picam2.capture_file(stream, format='jpeg')
        stream.seek(0)
        frame = stream.read()
        stream.seek(0)
        stream.truncate()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)
