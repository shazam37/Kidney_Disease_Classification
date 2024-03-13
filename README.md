# Kidney_Disease_Classification

People widely claim that the pain from kidney stones are comparable to one experienced during childbirth. Well kidney stones aren't fatal but they are one of the worst nightmares for those who have suffered from it. The amount of suffering depends on the size of the stones. The stones are generally formed from the crystals of Calcium/Magnesium found in the body. They get accumulated over time and if not passed through urine can grow in size. Once it reaches a certain radius, it starts blocking the urinary pathway which results in the sharp ugly pain. 

Owing to its criticality (not in the literal sense!), the diagnosis of kidney stone at the earliest can save one from immense trouble. Kidney stones are usually detected through CT-Scan. They are sort of a black and white images where we detect any anomaly through observing a contrasting difference. It requires a trained eye to identify stones in a scanned image, which only a certified medical professional is capable of doing. But kidney stones (and other medical anomalies too) follow a certain pattern. If we feed plenty of such labelled images (stone and no-stone) to a Machine Learning model then it can recognise the logic behind the patterns and if given a new such image, it can classify the presence of stone with a good level of accuracy (depends on the training).

![kidney_stone](https://github.com/shazam37/Kidney_Disease_Classification/assets/119686545/213ee5d2-7156-46f6-bd2d-a55faeb12291)

Convolutional Neural Networks (CNN) are a type of deep learning algorithm which can learn the patterns and features of an image. It employs several types of kernels (of a fixed size decided by us), each built to detect different features. They are slided over an image (represented as a matrix) in steps and matrix multiplication is done. Lets say if we took 4 kernels and the kernel dimension was 4x4 then the output of such an operation will give 4 images of same dimensions (the output dimension depends on the the size of the image and the kernel and can be determined through a simple formula). This whole operation is called convolution. 

![convolution](https://github.com/shazam37/Kidney_Disease_Classification/assets/119686545/6af8b1f0-0845-4a8a-b0d8-59e74be268f6)

The next step again involves a kernel but of a single type. Its job is to slide over the convoluted images and cherry pick the max/average/mode/median values (depending on our choice). It constructs a new matrix which preserves only the essential features of an image. The number of pooling matrices again depends on the dimensions of our kernel and the convoluted matrices. 

The convolution and pooling operations are stacked together multiple times depending on the amount of complexity we need. Finally the last pooling layer is flattened into a 1D array and fed into our vanilla Multi Layered Perceptrons (or Artifical Neural Networks). They are trained against their label values. 

In our case, instead of making our custom CNN architecture, we choose to go with a large vision model which is already pretrained on a plethora of images: VGG16. Its architecture consists of several layers of Convolution and Pooling operations:

![VGG16](https://github.com/shazam37/Kidney_Disease_Classification/assets/119686545/7b688efd-8768-41ba-92b7-ff78b2119c26)

All we need to do is augment our images as per the requirement of the architecture and simply feed them to the model. We freeze every layer in the model except the last layer which outputs the label. 

Coming back to our objective, the labelled CT-Scan Images of Kidney Stones and Normal Kidneys can be obtained from Kaggle and stored on a cloud (I chose to store it on google drive). We can obtain the pretrained VGG16 model checkpoints from the huggingface library and fine tune it on our custom images. I obtained a fine-tuned accuracy of around 90% afer training the model on around 200 epochs. The model training was monitored through MLFlow. It gives a nice interface to compare the outcomes from several experiments:

![Screenshot from 2024-03-13 23-32-47](https://github.com/shazam37/Kidney_Disease_Classification/assets/119686545/17f6fcd7-215e-4b23-a6a2-5f2312bb5a30)

We finally wrap the entire pipeline into an application using Flask. You can install the required dependencies and run app.py. You can train your own model by chaing the params.yaml file and running the '/train' route in flask application. Finally you can feed in a CT Scan Image of Kidneys to classify them as stone or normal. The app interface looks like: 

![Screenshot from 2024-03-13 23-42-38](https://github.com/shazam37/Kidney_Disease_Classification/assets/119686545/2e3d85ff-587c-49b1-bd88-3c35534114bd)

We can feed an image for prediction and it will generate a response: 

![Screenshot from 2024-03-13 23-48-32](https://github.com/shazam37/Kidney_Disease_Classification/assets/119686545/6e8c056d-bb28-42ef-98fc-a7e57889ec9d)

Such predictions should however be approached with utmost caution. They are not meant to replace the expertise of a medical professional but rather to aid them and clarify their assertions. Besides such crucial decision by an ML model requires the reduction of False Negatives as we don't want a patient having a kidney stone to be classified as normal. Various techniques can be used for that purpose. The future revision of this project will ensure to target the false negatives specifically. 

By the time, happy playing around with the project! 



