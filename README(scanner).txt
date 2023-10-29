# Fridge Inventory System with Raspberry Pi

## Introduction
This project demonstrates how to create a fridge inventory system using a Raspberry Pi and a camera module. The system detects QR codes representing items in the fridge, logs item additions and removals to a CSV file, and sends notifications via IFTTT (If This Then That) when items are added or removed.

## Prerequisites
- Raspberry Pi (with Raspbian OS installed)
- Raspberry Pi Camera Module
- Python 3.x
- `picamera2`, `PIL`, `zbarlight`, and `requests` Python libraries

## Setup

### 1. Hardware Setup
- Connect the Raspberry Pi Camera Module to the Raspberry Pi's camera port.
- Ensure the Raspberry Pi is powered and connected to a monitor, keyboard, and mouse.

### 2. Install Required Python Libraries
```bash
pip install picamera2 pillow zbarlight requests
```

### 3. Create IFTTT Webhooks
- Create two IFTTT applets using Webhooks:
  - Applet 1: Triggered by the event "pic_taken"
  - Applet 2: Triggered by the event "itemremoved"
- Configure these applets to send notifications via email or any other desired method when triggered.

## Running the Code

1. Copy and paste the provided Python code into a file, e.g., `fridge_inventory.py`.

2. Run the code on your Raspberry Pi:
   ```bash
   python fridge_inventory.py
   ```

## Usage

- When an item with a QR code is placed in front of the camera, the system will detect it, log the item addition to a CSV file, and send a notification using IFTTT.
- When an item is removed from the camera's view, the system will log the removal to the CSV file and send a notification.

## CSV Logging

- All item additions and removals are logged to a CSV file named `fridge_inventory.csv`.
- The CSV file contains columns for Date, Time, Item, and Action (Added or Removed).

## Troubleshooting

- Ensure that the camera is correctly connected to the Raspberry Pi.
- Check that the required Python libraries are installed.
- Verify your IFTTT applets are configured correctly and the Webhooks key is inserted into the code.

## Conclusion

This Raspberry Pi-based fridge inventory system allows you to keep track of items in your fridge and receive notifications when items are added or removed. It's a useful project for home organization and inventory management.