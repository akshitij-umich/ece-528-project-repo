ECE-528 - Final Project - License Plate Detection using Cloud Vision API

Initial Steps:
1. Create a Project in GCP
2. Enable the Service Account
3. Enable Cloud Vision API
4. Install Cloud SDK in local machine
5. Authenticate the GCP credentials in cloud SDK and login to account
7. Select the project
6. Install the dependencies:
   i. Cloud Vision -> pip install --upgrade google-cloud-vision
   ii. Numpy -> pip install numpy
   iii. OpenCV -> pip install cv2

Code:
1. Provide the image path in the img_path variable to read the image
2. Provide the output directory and image name in cv2.imwrite to save the image with bounding boxes.
3. The detected text output can be read from the terminal.