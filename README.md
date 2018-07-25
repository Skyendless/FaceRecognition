## FaceRecognition
Face Recognition based on facenet and mtcnn


## Inspiration 

The code was heavily inspired by facenet projects ： https://github.com/davidsandberg/facenet
 
 
## How to train my datasets?

  Maybe you want to automatically categorize your private photo collection. Or you have a security camera that you want to automatically recognize the members of your family. Then it's likely that you would like to train a classifier on your own dataset. In this case classifier.py program can be used also for this.In this example the 5 first images of each class was used for training and the next 5 images was used for testing.
  
  The classes that was used are:

    Ariel_Sharon
    Arnold_Schwarzenegger
    Colin_Powell
    Donald_Rumsfeld
    George_W_Bush
    Gerhard_Schroeder
    Hugo_Chavez
    Jacques_Chirac
    Tony_Blair
    Vladimir_Putin

The training of the classifier is done in a similar way as before:

python src/classifier.py TRAIN ~/datasets/my_dataset/train/ ~/models/model-20170216-091149.pb ~/models/my_classifier.pkl --batch_size 1000
The training of the classifier takes a few seconds (after loading the pre-trained model) and the output is shown below. Since this is a very simple dataset the accuracy is very good.

Number of classes: 10
Number of images: 50
Loading feature extraction model
Model filename: /home/david/models/model-20170216-091149.pb
Calculating features for images
Training classifier
Saved classifier model to file "/home/david/models/my_classifier.pkl"

This is how the directory containing the test set is organized:

/home/david/datasets/my_dataset/test
├── Ariel_Sharon
│   ├── Ariel_Sharon_0006.png
│   ├── Ariel_Sharon_0007.png
│   ├── Ariel_Sharon_0008.png
│   ├── Ariel_Sharon_0009.png
│   └── Ariel_Sharon_0010.png
├── Arnold_Schwarzenegger
│   ├── Arnold_Schwarzenegger_0006.png
│   ├── Arnold_Schwarzenegger_0007.png
│   ├── Arnold_Schwarzenegger_0008.png
│   ├── Arnold_Schwarzenegger_0009.png
│   └── Arnold_Schwarzenegger_0010.png
├── Colin_Powell
│   ├── Colin_Powell_0006.png
│   ├── Colin_Powell_0007.png
...
...

Classification on the test set can be ran using:

python src/classifier.py CLASSIFY ~/datasets/my_dataset/test/ ~/models/model-20170216-091149.pb ~/models/my_classifier.pkl --batch_size 1000
Classification on the test set can be ran using:

python src/classifier.py CLASSIFY ~/datasets/my_dataset/test/ ~/models/model-20170216-091149.pb ~/models/my_classifier.pkl --batch_size 1000

Number of classes: 10
Number of images: 50
Loading feature extraction model
Model filename: /home/david/models/model-20170216-091149.pb
Calculating features for images
Testing classifier
Loaded classifier model from file "/home/david/models/my_classifier.pkl"
   0  Ariel Sharon: 0.452
   1  Ariel Sharon: 0.376
   2  Ariel Sharon: 0.426
...
...
...
  47  Vladimir Putin: 0.418
  48  Vladimir Putin: 0.453
  49  Vladimir Putin: 0.378
Accuracy: 1.000


## How to run?
 
 1,Install Dependencies 1.tensorflow 2.opencv with python ,ect..
 
 2，dowanload the pre-trained model from followde web: https://drive.google.com/open?id=1EXPBSXwTaqrSC0OhUdXNmKSh9qJUQ55- . then save it to fold named model_checkpoints.
 
 3,run real_time_face_recognition.py  if you want face recongnition in real time or run image_recognition.py if you just want a picture test.
 
 
