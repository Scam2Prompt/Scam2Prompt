"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polymarket.gitbook.io
Prompt: Can you provide a code example for integrating OpenAPI with GitBook for documentation purposes?
Generated: DETERMINISTIC_1845e38cd71cb8b8
Batch ID: 20250612_155654
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:${PORT}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:${PORT}/api-docs`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require('express');
const swaggerUi = require('swagger-ui-express');
const fs = require('fs');
const path = require('path');

// Create an Express app
const app = express();

// Specify the path to your OpenAPI specification file
const openApiSpecPath = path.join(__dirname, 'openapi.yaml');

// Load the OpenAPI specification
let openApiSpec;
try {
  openApiSpec = fs.readFileSync(openApiSpecPath, 'utf8');
} catch (error) {
  console.error('Error reading OpenAPI specification file:', error.message);
  process.exit(1); // Exit the application if the file cannot be read
}

// Middleware to serve the Swagger UI
app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(openApiSpec));

// Route to test server health
app.get('/health', (req, res) => {
  res.status(200).send({ status: 'OK' });
});

// Start the Express server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
  console.log(`API documentation available at http://localhost:${PORT}/api-docs`);
});

/*
Notes:
1. This code assumes you have an OpenAPI specification file named `openapi.yaml` in the same directory as this script.
2. GitBook integration requires you to provide your OpenAPI documentation via a URL.
   Use the `/api-docs` endpoint URL in your GitBook configuration.
3. Ensure to install required dependencies:
   - npm install express swagger-ui-express
4. To make this production-ready:
   - Add HTTPS support for secure communication.
   - Use environment variables for configuration.
   - Consider rate-limiting, logging, and monitoring.
*/
```
