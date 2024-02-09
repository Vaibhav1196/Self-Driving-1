import socketio
import eventlet
from flask import Flask

import numpy as np
from keras.models import load_model

import base64
from io import BytesIO

from PIL import Image
import cv2


"""Here we will use a combination of Flask & SocketIO to communicate with the simulator"""

# define the socketio server, this initializes the socketio server
sio = socketio.Server()

# Flask application initialization, 
# Flask is a web framework used for building web applictaions in Python
app = Flask(__name__) 


# This variable is used to control the speed of the vechicle
speed_limit = 10

# ***************************************************************************************

# We will define the preprocessing function for the image data 
# Note that the preprocessing has to be the same as that which was used in training
def img_preprocess(img):
    img = img[60:135,:,:]
    img = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)
    img = cv2.GaussianBlur(img,(3,3),0)
    img = cv2.resize(img,(200,66))
    img = img/255
    return img

# ***************************************************************************************

# function that emits the steering and throttle to the simulator
# It emits a "steer" event with the steering and throttle values
# We did not predict throttle but it is needed for it to work
def send_control(steering_angle,throttle):
    sio.emit('steer',data={
            'steering_angle': steering_angle.__str__(),
            'throttle': throttle.__str__()
    })

# ***************************************************************************************

# This is a SocketIO event handler that listens for a connect event
# When the client connects to the server the connect function is executed
@sio.on('connect')
def connect(sid,environ):
    print('Connected')
    send_control(1,0)

# ***************************************************************************************

@sio.on('telemetry')
def telemetry(sid,data):

    speed = float(data['speed'])

    # Read the bytes of image data received using BytesIO
    # Decode the base64 format of the image 
    # Use the Image module of PIL to read the image matrix
    image = Image.open(BytesIO(base64.b64decode(data['image'])))
    # convert the image tp numpy array from PIL format 
    image = np.asarray(image)
    # Apply the image preprocessing on the image
    image = img_preprocess(image)
    # Here we add an extra dimension to the image 
    # This essentially creates a batch of one image (represents batch size)
    # example if image has shape (h,w,chan) then np.array([img]) => (1,h,w,chan)
    # Here 1 is the batch size
    image = np.array([image])

    steering_angle = float(model.predict(image))
    throttle = 1.0 - speed/speed_limit

    print('{}{}{}'.format(steering_angle, throttle, speed))
    # send the control with the steering_angle and the throttle
    send_control(steering_angle, throttle)



# ***************************************************************************************



if __name__ == "__main__":
    # Load the model
    model = load_model("model/model.h5")
    # call socketio, this combines both socketio server and flask app to work together
    app = socketio.Middleware(sio,app)
    # This launches the Flask server using the eventlet web server
    # It listens on port 4567 for incoming connections from the simulator
    eventlet.wsgi.server(eventlet.listen(('',4567)),app)


# ***************************************************************************************











