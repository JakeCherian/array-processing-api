# API Documentation

## Array Processing API

This document provides detailed information about the Array Processing API endpoints.

## Base URL

- **Local Development**: `http://localhost:5001`
- **Production**: `https://your-deployed-url.com`

## Endpoints

### 1. POST /bfhl

The main endpoint for processing arrays and categorizing elements.

#### Request

**Method**: `POST`  
**Content-Type**: `application/json`

**Request Body**:
```json
{
  "data": ["a", "1", "334", "4", "R", "$"]
}
```

**Parameters**:
- `data` (array, required): Array of strings to be processed

#### Response

**Success Response (200 OK)**:
```json
{
  "is_success": true,
  "user_id": "jake_smith_29082025",
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

**Error Response (400 Bad Request)**:
```json
{
  "is_success": false,
  "error": "Missing 'data' field in request"
}
```

**Error Response (500 Internal Server Error)**:
```json
{
  "is_success": false,
  "error": "Internal server error: [error details]"
}
```

#### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `is_success` | boolean | Indicates if the operation was successful |
| `user_id` | string | Generated in format `{full_name_ddmmyyyy}` |
| `email` | string | User's email address |
| `roll_number` | string | College roll number |
| `odd_numbers` | array | Array of odd numbers (as strings) |
| `even_numbers` | array | Array of even numbers (as strings) |
| `alphabets` | array | Array of alphabets (converted to uppercase) |
| `special_characters` | array | Array of special characters |
| `sum` | string | Sum of all numbers (as string) |
| `concat_string` | string | Concatenated alphabets in reverse order with alternating caps |

### 2. GET /

Serves the web interface for testing the API.

**Method**: `GET`  
**Response**: HTML page with a simple interface for testing the API.

### 3. GET /health

Health check endpoint to verify API status.

**Method**: `GET`

**Response (200 OK)**:
```json
{
  "status": "healthy",
  "message": "API is running successfully"
}
```

## Processing Logic

### Number Processing
- **Single digits**: Treated as individual numbers
- **Multi-digit numbers**: Treated as single numbers
- **Even/Odd classification**: Based on mathematical rules
- **Sum calculation**: All numeric values are summed

### Alphabet Processing
- **Single characters**: Converted to uppercase
- **Multi-character strings**: If purely alphabetic, converted to uppercase
- **Mixed strings**: Each character is processed individually
- **Concatenation**: All alphabets are collected, reversed, and formatted with alternating caps

### Special Character Processing
- **Single characters**: Non-alphanumeric characters
- **Classification**: Characters that are not numbers or letters

## Examples

### Example 1: Mixed Data
**Input**: `["a", "1", "334", "4", "R", "$"]`

**Processing**:
- Numbers: `1` (odd), `334` (even), `4` (even) → Sum: 339
- Alphabets: `a` → `A`, `R` → `R`
- Special characters: `$`

**Output**:
```json
{
  "odd_numbers": ["1"],
  "even_numbers": ["334", "4"],
  "alphabets": ["A", "R"],
  "special_characters": ["$"],
  "sum": "339",
  "concat_string": "Ra"
}
```

### Example 2: Complex Strings
**Input**: `["A", "ABcD", "DOE"]`

**Processing**:
- Numbers: None
- Alphabets: `A`, `ABcD` → `ABCD`, `DOE`
- Special characters: None

**Output**:
```json
{
  "odd_numbers": [],
  "even_numbers": [],
  "alphabets": ["A", "ABCD", "DOE"],
  "special_characters": [],
  "sum": "0",
  "concat_string": "EoDdCbAa"
}
```

## Error Handling

### Validation Errors
- **Missing data field**: Returns 400 with error message
- **Invalid data type**: Returns 400 with error message
- **Empty array**: Returns 200 with empty results

### Server Errors
- **Internal errors**: Returns 500 with error details
- **Database errors**: Returns 500 (if applicable)
- **Network errors**: Returns appropriate HTTP status codes

## Rate Limiting

Currently, no rate limiting is implemented. For production use, consider implementing rate limiting to prevent abuse.

## CORS

Cross-Origin Resource Sharing (CORS) is enabled for all origins to allow web-based testing.

## Security Considerations

1. **Input Validation**: All inputs are validated before processing
2. **Error Handling**: Sensitive information is not exposed in error messages
3. **HTTPS**: Use HTTPS in production for secure communication
4. **Authentication**: No authentication required for this API

## Testing

### Using cURL
```bash
# Test the main endpoint
curl -X POST http://localhost:5001/bfhl \
  -H "Content-Type: application/json" \
  -d '{"data": ["a", "1", "334", "4", "R", "$"]}'

# Test health endpoint
curl http://localhost:5001/health
```

### Using Python
```python
import requests

# Test the main endpoint
response = requests.post(
    'http://localhost:5001/bfhl',
    json={'data': ['a', '1', '334', '4', 'R', '$']},
    headers={'Content-Type': 'application/json'}
)

print(response.json())
```

### Using JavaScript
```javascript
// Test the main endpoint
fetch('http://localhost:5001/bfhl', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        data: ['a', '1', '334', '4', 'R', '$']
    })
})
.then(response => response.json())
.then(data => console.log(data));
```

## Versioning

Current version: 1.0.0

## Support

For issues or questions:
1. Check the error messages in the API response
2. Review the processing logic documentation
3. Test with the provided examples
4. Check the server logs for detailed error information
