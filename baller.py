

import json


def validate_json(font_data, color_data, case_data):
    """
    Validates JSON data from font, color, and case checkers.


    Args:
        font_data: JSON data from font_report.json.
        color_data: JSON data from color_report.json.
        case_data: JSON data from case_report.json.


    Returns:
        True if all validations pass, False otherwise.
    """


    valid = True


    # Validate font_report.json
    if font_data["issuesFound"] != 0:
        print(f"Validation failed: font_report.json issuesFound is {font_data['issuesFound']}, expected 0.")
        valid = False


    # Validate color_report.json
    if color_data["issuesFound"] != 0:
        print(f"Validation failed: color_report.json issuesFound is {color_data['issuesFound']}, expected 0.")
        valid = False


    # Validate case_report.json
    for item in case_data:
        if item["is_valid"] != True:
            print(f"Validation failed: case_report.json component '{item['component']}' is_valid is {item['is_valid']}, expected True.")
            valid = False
            break


    return valid


def main():
    try:
        with open('prototype/api/compliance_report/font_report.json', 'r') as f:
            font_data = json.load(f)


        with open('prototype/api/compliance_report/color_report.json', 'r') as f:
            color_data = json.load(f)


        with open('prototype/api/compliance_report/case_report.json', 'r') as f:
            case_data = json.load(f)


        if validate_json(font_data, color_data, case_data):
            print("All JSON validations passed. 🔥🔥🔥")
            return("All JSON validations passed. 🔥🔥🔥")
        else:
            exit(1) # Indicate validation failure.
            

    except FileNotFoundError as e:
        return(f"Error: File not found - {e}")
        exit(1)
    except json.JSONDecodeError as e:
        return (f"Error: Invalid JSON format - {e}")
        exit(1)


if __name__ == "__main__":
    main()





