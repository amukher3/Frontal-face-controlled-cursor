# Frontal-face-based-Mouse-controller
Controlling the mouse with frontal face movements

A Novel and extremely simple way to control the mouse wirelessly,just with face movements, is presented here. Using `Haar cascades` to detect the frontal face and then passing the detected co-ordinates as parameters to `pyautogui` to move the cursor to the desired co-ordinates. 

***Dependencies that need to be installed ***:

`pip install cv2` or `pip3 install cv2`

`pip install pyautogui` or `pip3 install pyautogui`

***Procedure***:
1) After installing the dependencies download the `Haar Cascade` the _.xml_ file for frontal face detection. 
2) Set the _location_ of the _.xml_ file that you downloaded to the directory where you want to keep it i.e set `cv2.CascadeClassifier(.../desired_location)`. 
2) Run the script and Enjoy!

_**NB: For best results set the camera as far as possible from the face this would increase the receptive field and help sweep the entire screen just with frontal face movements. While setting the camera far from the face it needs to be made sure that the face is still being detected a small blue square indicates the face is being detected.**_

***Author:Abhishek Mukherjee***
***Email:abhi0787@gmail.com***

