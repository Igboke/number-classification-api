# Stage One HNG-Internship Number Classification API

A RESTful API built with Flask to classify numbers based on mathematical properties (prime, perfect, Armstrong, etc.) and retrieve fun facts from the Numbers API.

## Features

- **Mathematical Classification**:
  - Check if a number is **prime**, **perfect**, or an **Armstrong number**.
  - Calculate the sum of its digits.
  - Determine parity (even/odd).
- **Fun Fact Integration**: Fetch interesting trivia about the number from [Numbers API](http://numbersapi.com).
- **Error Handling**: Validate input and return descriptive error messages.
- **CORS Support**: Configured to handle cross-origin requests.

## API Specification

### Endpoint
`GET /api/classify-number`

### Parameters
| Parameter | Type   | Description               |
|-----------|--------|---------------------------|
| `number`  | Integer| The number to classify.   |

### Responses

**200 OK**  
Successful response with number properties:

```json
{
  "number": 371,
  "is_prime": false,
  "is_perfect": false,
  "properties": ["armstrong", "odd"],
  "digit_sum": 11,
  "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

**400 Bad Request**
Invalid input (e.g., non-integer value):

```json
{
  "number": "alphabet",
  "error": true
}
```

## Getting Started

**Prerequisites**

- Python 3.8+
- pip

### Installation

1. Clone the repository:

```bash
git clone https://github.com/Igboke/number-classification-api.git
cd number-classification-api
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

### Local Development

1. Start Flask development server:

```bash
flask run --host=0.0.0.0 --port=5000
```

2. Test with curl

```bash
curl "http://localhost:5000/api/classify-number?number=371"
```

### Deployment

### Testing

Validate functionality with sample requests:

```bash
# Valid request
curl "https://number-classification-api-1n0u.onrender.com/api/classify-number?number=16"

# Invalid request
curl "https://number-classification-api-1n0u.onrender.com/api/classify-number?number=abg"
```

### Contributing

- Fork the repository

- Create feature branch (git checkout -b feature/improvement)

- Commit changes (git commit -m 'Add new feature')

- Push to branch (git push origin feature/improvement)

- Open Pull Request
