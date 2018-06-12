#coding:utf-8
#author:huws

import cv2

import face

def add_overlays(frame, faces):
    if faces is not None:
        for face in faces:
            face_bb = face.bounding_box.astype(int)
            cv2.rectangle(frame,
                          (face_bb[0], face_bb[1]), (face_bb[2], face_bb[3]),
                          (0, 255, 0), 4)
            if face.name is not None:
                cv2.putText(frame, face.name, (face_bb[0], face_bb[1]),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0),
                            thickness=4, lineType=2)

# load test image
image_path='/home/huws/Pictures/test1.jpg'
img = cv2.imread(image_path)

# load face_recognition model
face_recognition = face.Recognition()

faces = face_recognition.identify(img)

add_overlays(img, faces)

img = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)),interpolation=cv2.INTER_CUBIC)

cv2.imshow('output', img)

cv2.waitKey(0)

cv2.destroyAllWindows()

