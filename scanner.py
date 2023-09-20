from picamera2 import Picamera2, Preview
from PIL import Image
from time import sleep, strftime
import zbarlight
import requests
import csv

# Initialize the camera
camera = Picamera2()

# Set camera resolution (adjust as needed)
camera.resolution = (300, 300)
detected_items = []

# Start capturing video
camera_config = camera.create_preview_configuration()
camera.configure(camera_config)
camera.start_preview(Preview.QTGL)
camera.start()

# Define CSV file path
csv_filename = 'fridge_inventory.csv'

# Check if the CSV file exists; if not, create it and write the header
if not csv_filename:
    with open(csv_filename, 'w', newline='') as csvfile:
        # Define CSV fieldnames
        fieldnames = ['Date', 'Time', 'Item', 'Action']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # Write CSV header
        writer.writeheader()

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

        current_detected_items = set()

        if codes:
            for code in codes:
                item = code.decode('utf8')
                current_detected_items.add(item)
                if item not in detected_items:
                    detected_items.append(item)
                    
                    # Get the current date and time
                    current_date = strftime('%Y-%m-%d')
                    current_time = strftime('%H:%M:%S')
                    
                    # Append a new row to the CSV file for item addition
                    with open(csv_filename, 'a', newline='') as csvfile:
                        fieldnames = ['Date', 'Time', 'Item', 'Action']
                        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                        writer.writerow({'Date': current_date, 'Time': current_time, 'Item': item, 'Action': 'Added'})
                    
                    print(item, "added in fridge")
                    json_data = {"value1": item}
                    requests.post("https://maker.ifttt.com/trigger/pic_taken/with/key/dqisEg_LCCBlGCCu3DDNbPSY7F0lYojB3y-UTwBn0fX",json=json_data)
       
        else:
            if detected_items:
                removed_item = detected_items[0]
                detected_items.pop(0)
                
                # Get the current date and time
                current_date = strftime('%Y-%m-%d')
                current_time = strftime('%H:%M:%S')
                
                # Append a new row to the CSV file for item removal
                with open(csv_filename, 'a', newline='') as csvfile:
                    fieldnames = ['Date', 'Time', 'Item', 'Action']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writerow({'Date': current_date, 'Time': current_time, 'Item': removed_item, 'Action': 'Removed'})
                
                print(removed_item, "removed from list")
                json_data = {"value1": removed_item}
                requests.post("https://maker.ifttt.com/trigger/itemremoved/with/key/dqisEg_LCCBlGCCu3DDNbPSY7F0lYojB3y-UTwBn0fX",json=json_data)
               
# Stop capturing and close the camera
camera.stop_preview()
