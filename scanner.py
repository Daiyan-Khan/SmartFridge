import cv2

# set up camera object
cap = cv2.VideoCapture(0)

# QR code detection object
detector = cv2.QRCodeDetector()

while True:
    # get the image
    _, img = cap.read()
    # get bounding box coords and data
    data, bbox, _ = detector.detectAndDecode(img)
    
    # if there is a bounding box, draw one, along with the data
    if(bbox is not None):
        for i in range(len(bbox[0])):
            cv2.line(img, tuple(bbox[0][i]), tuple(bbox[0][(i+1) % 4]), color=(255, 0, 255), thickness=2)
        cv2.putText(img, data, (int(bbox[0][0][0]), int(bbox[0][0][1]) - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (0, 255, 0), 2)
        if data:
            print("data found:", data)
    # display the image preview
    cv2.imshow("code detector", img)
    if cv2.waitKey(1) == ord("q"):
        break
# free camera object and exit
cap.release()
cv2.destroyAllWindows()
