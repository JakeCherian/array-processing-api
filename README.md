# Array Processing API

A REST API that processes arrays and categorizes elements into different types (numbers, alphabets, special characters) with various operations.

## Features

- **POST /bfhl** - Main endpoint for array processing
- **GET /** - Simple web interface for testing
- **GET /health** - Health check endpoint

## API Endpoint

### POST /bfhl

Processes an array and returns categorized results.

**Request Body:**
```json
{
  "data": ["a", "1", "334", "4", "R", "$"]
}
```

**Response:**
```json
{
  "is_success": true,
  "user_id": "jake_smith_17091999",
  "email": "jake@xyz.com",
  "roll_number": "ABCD123",
  "odd_numbers": ["1"],
  "even_numbers": ["334", "4"],
  "alphabets": ["A", "R"],
  "special_characters": ["$"],
  "sum": "339",
  "concat_string": "Ra"
}
```

## Response Fields

1. **is_success**: Boolean indicating operation status
2. **user_id**: Generated in format `{full_name_ddmmyyyy}`
3. **email**: User's email address
4. **roll_number**: College roll number
5. **odd_numbers**: Array of odd numbers (as strings)
6. **even_numbers**: Array of even numbers (as strings)
7. **alphabets**: Array of alphabets (converted to uppercase)
8. **special_characters**: Array of special characters
9. **sum**: Sum of all numbers (as string)
10. **concat_string**: Concatenated alphabets in reverse order with alternating caps

## Examples

### Example A
**Input:** `["a", "1", "334", "4", "R", "$"]`
**Output:** 
- odd_numbers: `["1"]`
- even_numbers: `["334", "4"]`
- alphabets: `["A", "R"]`
- special_characters: `["$"]`
- sum: `"339"`
- concat_string: `"Ra"`

### Example B
**Input:** `["2", "a", "y", "4", "&", "-", "*", "5", "92", "b"]`
**Output:**
- odd_numbers: `["5"]`
- even_numbers: `["2", "4", "92"]`
- alphabets: `["A", "Y", "B"]`
- special_characters: `["&", "-", "*"]`
- sum: `"103"`
- concat_string: `"ByA"`

### Example C
**Input:** `["A", "ABcD", "DOE"]`
**Output:**
- odd_numbers: `[]`
- even_numbers: `[]`
- alphabets: `["A", "ABCD", "DOE"]`
- special_characters: `[]`
- sum: `"0"`
- concat_string: `"EoDdCbAa"`

## Local Development

### Prerequisites
- Python 3.8+
- pip

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd array-processing-api
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and navigate to `http://localhost:5000`

## Deployment

### Heroku
1. Create a Heroku account and install Heroku CLI
2. Login to Heroku: `heroku login`
3. Create a new app: `heroku create your-app-name`
4. Deploy: `git push heroku main`

### Vercel
1. Install Vercel CLI: `npm i -g vercel`
2. Deploy: `vercel`

### Railway
1. Connect your GitHub repository to Railway
2. Railway will automatically deploy your application

## Configuration

Update the following variables in `app.py`:
- `FULL_NAME`: Your full name (lowercase)
- `EMAIL`: Your email address
- `ROLL_NUMBER`: Your college roll number

## Testing

### Using cURL
```bash
curl -X POST http://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"data": ["a", "1", "334", "4", "R", "$"]}'
```

### Using the Web Interface
1. Open `http://localhost:5000` in your browser
2. Enter comma-separated values in the input field
3. Click "Process Array" or press Enter
4. View the JSON response

## Error Handling

The API includes comprehensive error handling:
- Invalid input validation
- Missing data field detection
- Internal server error handling
- Proper HTTP status codes

## Technologies Used

- **Backend**: Python Flask
- **Frontend**: HTML, CSS, JavaScript
- **Deployment**: Heroku/Vercel/Railway ready
- **CORS**: Enabled for cross-origin requests

## License

This project is open source and available under the MIT License.
