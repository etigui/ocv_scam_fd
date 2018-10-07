import numpy as np
from imutils.object_detection import non_max_suppression
import imutils
import cv2
import utils
import time

def main():

    # Path
    daily_dir_path = "C:\\wamp64\www\\detection\\"

    # Cam and cascade init
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()

    # Define scene to detect
    a, b, c, d = define_scene(frame)

    # Process on each frame
    while (True):

        # Create daily directory
        directory = utils.create_daily_dir(daily_dir_path)

        # Read webcam frame
        ret, frame = cap.read()

        # Copy and crop the frame
        original_frame = frame.copy()
        cropped_frame = frame[a:b, c:d]

        # Check if face and person detected
        if face_detection(cropped_frame) and person_detection(cropped_frame):
            file = utils.create_file(directory)
            cv2.imwrite(file, original_frame)
            time.sleep(1)

        # Check if quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release cam
    cap.release()
    cv2.destroyAllWindows()


def define_scene(frame):
    r = cv2.selectROI("Select place", frame)
    return int(r[1]), int(r[1] + r[3]), int(r[0]), int(r[0] + r[2])


def face_detection(frame):
    detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.2, 5)
    for (x, y, w, h) in faces:
        return True
    return False


def person_detection(frame):
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    frame = imutils.resize(frame, width=min(400, frame.shape[1]))
    rects, weights = hog.detectMultiScale(frame, winStride=(4, 4), padding=(8, 8), scale=1.05)
    rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
    pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)
    for (xA, yA, xB, yB) in pick:
        return True
    return False


if __name__ == "__main__":
    main()