# Self-Driving-1

This project endeavors to replicate NVIDIA's CNN architecture outlined in the paper https://arxiv.org/abs/1604.07316. Utilizing Udacity's free simulator, we will capture image data of the path and wheel angle. Subsequently, we will train a Convolutional Neural Network to interpret raw pixels from three cameras (left, right, and center) into steering commands. Ultimately, we aim to validate the model's performance on a car within the simulator, utilizing a varied map configuration.

The below image shows us the mechanism involved in training (on the left) and the corresponding CNN architecture that is being implemented (on the right). Kindly read the paper to have a better visual of the images and the architecture used.

I will share the link to the article here, where I provide detailed explanations on how the code works and the underlying theory behind it.

![Training](/assets/Training_Mechanism.png?raw=true)

## Steps to replicate

### Step 1 

* Download the Udacity simulator from their GIT repository, kindly download the version 1 as version 2 has some bugs in it. https://github.com/udacity/self-driving-car-sim

### Step 2

* Git clone the project into your local system
```bash

git clone https://github.com/Vaibhav1196/Self-Driving-1.git

```

* We will use google Colab to explore, preprocess and train our model. Open the ipynb file "AutoCar.ipynb" file in a google colab instance and run each cell with T4-GPU selected. 

* If you observe the first cell in the Python Notebok we will use the data that was already collected using the same simulator https://github.com/rslim087a/track.git. If you wish to collect the data by yourself you will have to run the udacity simulator with a map selected in "TRAINING MODE" and press the record button to captutre the images onto the local computer.

* Remember once the training is complete you will have to download the trained model file "model.h5" into the local system.

&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;![Record](/assets/Record.png?raw=true)


### Step 3

* Here we will set up the local system that will use the model and execute the "driver.py" script to communicate and predict the steering angle with the simulator

* Follow the commands below to setup the environment

```bash

# Create the anaconda virtual environment
conda create -n car python=3.9 -y

# Activate the environment 
conda activate car

# Download required modules from the requirement.txt file
pip install -r requirements.txt

# Download these extra modules with the specif versions as indicated below
pip install python-engineio==3.13.2
pip install python-socketio==4.6.1

```

### Step 4

* Now we can execute the "driver.py" script that communicates with the simulator, that is it takes in the image make a prediction on the steering angle and sends it back to the simulator

* Follow the below commands to lauch the flask server with the "driver.py" script

```bash
# Stay inside the Self-Driving-1 folder 
cd Self-Driving-1 

# Activate the conda environment that we had created
conda activate car

# Execute the python driver.py script and it must be listening on port 4567 on which even the simulator listens
python driver.py

```

* The below image of the terminal shows that the server is up and running and is listening on port 4567

&ensp;&ensp;&ensp;![Record](/assets/Server.png?raw=true)

* Now that the server is running open the simulator but in "AUTONOMOUS MODE" with any of the two maps selected. The below video shows selfdriving in action.


https://github.com/Vaibhav1196/Self-Driving-1/assets/52819113/2f2ca5ac-db75-43c7-ba0e-a8c5cf8cc2ad

