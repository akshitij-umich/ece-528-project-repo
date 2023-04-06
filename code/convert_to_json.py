import json
import text_detection

def convert_to_json(output_str):
    data = {'state': output_str[0], 'license': output_str[1]}
    json_data = json.dumps(data)
    with open('output.json', 'w') as f:
        f.write(json_data)