from flask import Flask, render_template, Response
import cv2
app = Flask(__name__)
camera = cv2.VideoCapture(0)

def generate_video():
    while True:
        success,frame = camera.read()
        if not success:
            break
        else:
            ret, buffer= cv2.imencode('.jpg',frame)
            frame =buffer.tobytes()
        yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def welcome():
    return  render_template('index.html')

@app.route('/livestream')
def video_feed():
    return Response(generate_video(),mimetype='multipart/x-mixed-replace; boundary=frame')





if __name__ == '__main__':
    app.run(debug =True)