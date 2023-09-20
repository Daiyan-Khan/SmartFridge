from picamera2 import Picamera2, Preview
from PIL import Image
from time import sleep
import zbarlight
import requests
# Initialize the camera
camera = Picamera2()

# Set camera resolution (adjust as needed)
camera.resolution = (300, 300)

# Start capturing video
camera_config = camera.create_preview_configuration()
camera.configure(camera_config)
camera.start_preview(Preview.QTGL)
camera.start()
while True:
    # Capture a frame
    sleep(1)  # Adjust the sleep duration as needed to control frame rate
   
   
    camera.capture_file("frame.jpg")
    sleep(2)

    # Read the captured image and decode QR codes
    with open('frame.jpg', 'rb') as image_file:
        image_data = Image.open(image_file)
        image_data.load()
        codes = zbarlight.scan_codes(['qrcode'], image_data)

        if codes:
            for code in codes:
                item = code.decode('utf8')
                print("QR Code data:", item)
                requests.post('https://maker.ifttt.com/trigger/pic_taken/{"value1" : "item"}/with/key/dqisEg_LCCBlGCCu3DDNbPSY7F0lYojB3y-UTwBn0fX')
# Stop capturing and close the camera
camera.stop_preview()
