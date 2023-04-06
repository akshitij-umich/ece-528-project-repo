ECE-528 - Final Project - License Plate Detection using Cloud Vision API

Initial Steps:
1. Create a Project in GCP
2. Enable the Service Account
3. Enable Cloud Vision API
4. Install Cloud SDK on the local machine
5. Authenticate the GCP credentials in cloud SDK and login to account
7. Select the project
6. Install the dependencies:
   i. Cloud Vision -> pip install --upgrade google-cloud-vision
   ii. Numpy -> pip install numpy
   iii. OpenCV -> pip install cv2

Steps to run the application:
1. Provide the image path in the img_path variable in main.py to read the image
2. Run the main.py script.

Program flow:
1. main.py reads the image given in the img_path.
2. The detect_text from text_detection.py will be called. detect_text will extract the text from the image.
3. detext_text calls state_name and license_number from state_license_function.py to extract the state name and license number from the detected text.
4. The state name and license number will be returned by text_detection.py.
5. The main.py then calls convert_to_json.py to convert the output string into a JSON file and store it in the local machine.
6. The main.py calls storage.py which helps upload the JSON file to cloud storage.

GCP Flow:
1. There is existing_data.json in the cloud storage.
2. Incoming data (new_data.json) is uploaded into the storage bucket.
3. A cloud function is set to trigger when a file uploads to bucket action.
4. Cloud function is triggered and the contents (state name and license) of the new_data.json and existing_data.json are checked.
5. If there is a match, the string object "JSON objects match!" will be printed on the logs console.
6. A metric is set up to check for the string object "JSON objects match!". Upon matching, an alert policy is triggered.
7. The alert policy uses notification channels to deliver the alert message to recipients via email.