## FaceRecognition
Face Recognition based on facenet and mtcnn


## Inspiration 

The code was heavily inspired by facenet projects ： https://github.com/davidsandberg/facenet
 
 
## How to train my datasets?

  Maybe you want to automatically categorize your private photo collection. Or you have a security camera that you want to automatically recognize the members of your family. Then it's likely that you would like to train a classifier on your own dataset. In this case classifier.py program can be used also for this.In this example the 5 first images of each class was used for training and the next 5 images was used for testing.
  
further detail:https://github.com/davidsandberg/facenet/wiki/Train-a-classifier-on-own-images


## How to run?
 
 1,Install Dependencies 1.tensorflow 2.opencv with python ,ect..
 
 2，dowanload the pre-trained model from followde web: https://drive.google.com/file/d/1EXPBSXwTaqrSC0OhUdXNmKSh9qJUQ55-/view. then save it to fold named model_checkpoints.
 
 3,run real_time_face_recognition.py  if you want face recongnition in real time or run image_recognition.py if you just want a picture test.
 
 
