from picamera import PiCamera
from time import sleep
import zbarlight

# Initialize the camera
camera = PiCamera()

# Set camera resolution (adjust as needed)
camera.resolution = (640, 480)

# Start capturing video
camera.start_preview()

while True:
    # Capture a frame
    sleep(1)  # Adjust the sleep duration as needed to control frame rate
    camera.capture('frame.jpg')

    # Read the captured image and decode QR codes
    with open('frame.jpg', 'rb') as image_file:
        image_data = image_file.read()
        codes = zbarlight.scan_codes('qrcode', image_data)

        if codes:
            for code in codes:
                print("QR Code data:", code.decode('utf-8'))

# Stop capturing and close the camera
camera.stop_preview()
