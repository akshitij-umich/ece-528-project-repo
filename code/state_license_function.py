import re

#Function to extract state using regex
def state_name(input_str):
    states = [
        'Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado',
        'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho',
        'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana',
        'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota',
        'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada',
        'New Hampshire', 'New Jersey', 'New Mexico', 'New York',
        'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon',
        'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota',
        'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington',
        'West Virginia', 'Wisconsin', 'Wyoming'
    ]

    #To match state names
    state_pattern = re.compile(r'\b(?:%s)\b' % '|'.join(states), re.IGNORECASE)

    # Find all matches
    matches = re.findall(state_pattern, input_str)
    if matches:
        return matches[0]
    else:
        return None

#Function to extract license number
def license_number(inp_list):
    #Checks for number based on its length and ignores spaces and other special characters
    out_list = [string.replace("-", "").replace(" ", "") 
                for string in inp_list if len(string.replace("-", "").replace(" ", "")) 
                in [5,6,7] and any(char.isalpha() for char in string) and any(char.isdigit() 
                for char in string) and all(char.isalnum() for char in string.replace("-", "").replace(" ", ""))]
    
    #The first value in the list will be the license.
    out_str = out_list[0]

    return out_str

