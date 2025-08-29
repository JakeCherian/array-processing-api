from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import re
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)

# Configuration
FULL_NAME = "jacob_cherian_m"  # Replace with your actual name
EMAIL = "jacob@xyz.com"    # Replace with your actual email
ROLL_NUMBER = "ABCD123"   # Replace with your actual roll number

def get_user_id():
    """Generate user_id in format: full_name_ddmmyyyy"""
    today = datetime.now()
    return f"{FULL_NAME}_{today.strftime('%d%m%Y')}"

def process_array(data):
    """Process the input array and return categorized results"""
    if not isinstance(data, list):
        return None, "Input must be an array"
    
    odd_numbers = []
    even_numbers = []
    alphabets = []
    special_characters = []
    sum_numbers = 0
    all_alphabets = []
    
    for item in data:
        item_str = str(item).strip()
        
        # Check if it's a number
        if item_str.isdigit():
            num = int(item_str)
            sum_numbers += num
            if num % 2 == 0:
                even_numbers.append(item_str)
            else:
                odd_numbers.append(item_str)
        # Check if it's an alphabet (single character or word with only letters)
        elif item_str.isalpha():
            alphabets.append(item_str.upper())
            all_alphabets.extend(list(item_str.upper()))
        # Check if it's a special character
        elif len(item_str) == 1 and not item_str.isalnum():
            special_characters.append(item_str)
        # For multi-character strings that aren't purely alphabetic
        else:
            # Check each character in the string
            for char in item_str:
                if char.isdigit():
                    num = int(char)
                    sum_numbers += num
                    if num % 2 == 0:
                        even_numbers.append(char)
                    else:
                        odd_numbers.append(char)
                elif char.isalpha():
                    alphabets.append(char.upper())
                    all_alphabets.append(char.upper())
                elif not char.isalnum():
                    special_characters.append(char)
    
    # Create concatenated string with alternating caps in reverse order
    concat_string = ""
    for i, char in enumerate(reversed(all_alphabets)):
        if i % 2 == 0:
            concat_string += char.upper()
        else:
            concat_string += char.lower()
    
    return {
        "odd_numbers": odd_numbers,
        "even_numbers": even_numbers,
        "alphabets": alphabets,
        "special_characters": special_characters,
        "sum": str(sum_numbers),
        "concat_string": concat_string
    }, None

@app.route('/')
def index():
    """Serve the frontend"""
    return render_template('index.html')

@app.route('/bfhl', methods=['POST'])
def bfhl():
    """Main API endpoint for processing arrays"""
    try:
        # Get JSON data from request
        request_data = request.get_json()
        
        if not request_data or 'data' not in request_data:
            return jsonify({
                "is_success": False,
                "error": "Missing 'data' field in request"
            }), 400
        
        # Process the array
        result, error = process_array(request_data['data'])
        
        if error:
            return jsonify({
                "is_success": False,
                "error": error
            }), 400
        
        # Prepare response
        response = {
            "is_success": True,
            "user_id": get_user_id(),
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            **result
        }
        
        return jsonify(response), 200
        
    except Exception as e:
        return jsonify({
            "is_success": False,
            "error": f"Internal server error: {str(e)}"
        }), 500

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "message": "API is running successfully"
    }), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port, debug=False)
