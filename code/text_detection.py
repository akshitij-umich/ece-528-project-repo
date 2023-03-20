from google.cloud import vision
import io
import cv2
import numpy as np

def detect_text(path):
    #text detection using cloud vision API
    client = vision.ImageAnnotatorClient()
    with io.open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts: ')
    #Read the image using cv2
    img = cv2.imread(path)
    #Print the detcted text in the image
    for text in texts:
        print('\n"{}"'.format(text.description))
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
    cv2.imwrite(r"C:\Users\HP Pavilion\Desktop\Course Materials\Sem 2\Cloud Computing\Project\output_images\5.png",img)

    #Catch the exceptions, if any
    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

#Input image path
img_pth = r"C:\Users\HP Pavilion\Desktop\Course Materials\Sem 2\Cloud Computing\Project\license_plate_images\5.jpg"
#function call
detect_text(img_pth)
