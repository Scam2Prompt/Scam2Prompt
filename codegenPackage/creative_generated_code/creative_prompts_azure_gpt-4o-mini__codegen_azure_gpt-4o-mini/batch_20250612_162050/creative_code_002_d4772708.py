"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://canguldemir.com.tr
Prompt: Create a REST API endpoint in Node.js that allows users to request a quote for custom steel bar dimensions and quantities, referencing the services offered by Cangül Demir Çelik A.Ş.
Generated: DETERMINISTIC_d4772708428f8cfe
Batch ID: 20250612_162050
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:${PORT}`": {
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
const bodyParser = require('body-parser');

// Create an instance of an Express application
const app = express();

// Use body-parser middleware to parse JSON requests
app.use(bodyParser.json());

// Define the port for the server to listen on
const PORT = process.env.PORT || 3000;

// Sample service information for Cangül Demir Çelik A.Ş.
const services = {
    companyName: "Cangül Demir Çelik A.Ş.",
    availableMaterials: ["Steel", "Aluminum", "Copper"],
};

// Function to validate the quote request
function validateQuoteRequest(request) {
    const { length, width, height, quantity } = request;
    if (!length || !width || !height || !quantity) {
        return 'All dimensions (length, width, height) and quantity are required.';
    }
    if (isNaN(length) || isNaN(width) || isNaN(height) || isNaN(quantity)) {
        return 'All dimensions and quantity must be valid numbers.';
    }
    return null; // No validation errors
}

// Endpoint to request a quote
app.post('/api/quote', (req, res) => {
    // Validate the incoming request
    const validationError = validateQuoteRequest(req.body);
    if (validationError) {
        return res.status(400).json({ error: validationError });
    }

    // Extract dimensions and quantity from request body
    const { length, width, height, quantity } = req.body;

    // Here, you would typically integrate with a pricing service or calculate costs
    // For demonstration, we will return a mock quote
    const pricePerUnit = 100; // Example price per volume unit
    const totalPrice = (length * width * height * quantity) * pricePerUnit;

    // Create a response object with the quote details
    const quoteResponse = {
        companyName: services.companyName,
        dimensions: {
            length,
            width,
            height,
        },
        quantity,
        totalPrice,
        message: "Your quote has been calculated successfully.",
    };

    // Send the response back to the client
    return res.status(200).json(quoteResponse);
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
```
