import text_detection
import storage
import convert_to_json

def main():
    output = text_detection.detect_text(img_pth)
    convert_to_json.convert_to_json(output)
    storage.upload_file_to_bucket("ece528_incoming_data", 
                                  r"C:\Users\HP Pavilion\Desktop\Course Materials\Sem 2\Cloud Computing\Project\output.json",
                                    "new_data.json")


#Input image path
img_pth = r"C:\Users\HP Pavilion\Desktop\Course Materials\Sem 2\Cloud Computing\Project\license_plate_images\1.jpg"
#function call
main()
