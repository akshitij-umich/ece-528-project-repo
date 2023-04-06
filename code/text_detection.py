from google.cloud import vision
import io
import cv2
import numpy as np
import state_license_function
import json

def detect_text(path):
    #text detection using cloud vision API
    client = vision.ImageAnnotatorClient()
    with io.open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    if texts:
        detected_text = texts[0].description
    print(detected_text)
    text_list = detected_text.split("\n")
    print(text_list)
    #extract state with function call
    state_name = state_license_function.state_name(detected_text)

    #extract license with function call
    license_number = state_license_function.license_number(text_list)

    #Read the image using cv2
    img = cv2.imread(path)
    #Print the detcted text in the image
    for text in texts:
        #print('\n"{}"'.format(text.description))
        vertices = []
        for vertex in text.bounding_poly.vertices:
            vertices.append((vertex.x, vertex.y))
        # Draw the bounding box on the image
        cv2.polylines(img, [np.array(vertices)], True, (0, 255, 0), thickness=2)

    #Display the image with bounding boxes
    # cv2.imshow('Image', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    #Save the image with bounding box around the detected text
    # cv2.imwrite(r"C:\Users\HP Pavilion\Desktop\Course Materials\Sem 2\Cloud Computing\Project\output_images\5.png",img)

    #Catch the exceptions, if any
    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
    
    return state_name,license_number
    

# #Input image path
# img_pth = r"C:\Users\HP Pavilion\Desktop\Course Materials\Sem 2\Cloud Computing\Project\license_plate_images\7.jpg"
# #function call
# output = detect_text(img_pth)


# data = {'state': output[0], 'license': output[1]}

# # Convert dictionary to JSON string
# json_data = json.dumps(data)
# print(json_data)
# # with open('output.json', 'w') as f:
# #     f.write(json_data)