"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starplumbingelectrical.com
Prompt: Develop a RESTful API endpoint in Node.js that allows users to request plumbing inspections and maintenance services, ensuring it includes location-based filtering for Graham, TX.
Generated: DETERMINISTIC_b48054194a6ae3a6
Batch ID: 20250612_164035
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
/**
 * RESTful API endpoint for requesting plumbing inspections and maintenance services.
 * This API includes location-based filtering for Graham, TX.
 * 
 * Author: [Your Name]
 * Date: [Today's Date]
 */

const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const PORT = 3000;

// Middleware to parse incoming JSON requests
app.use(bodyParser.json());

// Mock database for plumbing services (Replace with actual database in production)
const plumbingRequests = [];

// Predefined location filter: Graham, TX
const SERVICE_LOCATION = 'Graham, TX';

/**
 * POST /api/request-service
 * Endpoint to request plumbing inspections and maintenance services.
 * Validates location to ensure requests are for Graham, TX.
 *
 * Request Body:
 * {
 *   "name": "string",        // Name of the requester
 *   "email": "string",       // Email of the requester
 *   "phone": "string",       // Phone number of the requester
 *   "location": "string",    // Location of the service request
 *   "serviceType": "string"  // Type of service requested (e.g., inspection, maintenance)
 * }
 *
 * Response:
 * 201 Created - Successfully created service request.
 * 400 Bad Request - Invalid location or missing required fields.
 * 500 Internal Server Error - Server-side error.
 */
app.post('/api/request-service', (req, res) => {
  try {
    const { name, email, phone, location, serviceType } = req.body;

    // Validate required fields
    if (!name || !email || !phone || !location || !serviceType) {
      return res.status(400).json({ error: 'All fields are required.' });
    }

    // Location-based filtering: Only allow requests from Graham, TX
    if (location !== SERVICE_LOCATION) {
      return res.status(400).json({ error: 'Service is only available in Graham, TX.' });
    }

    // Create service request
    const newRequest = {
      id: plumbingRequests.length + 1, // Simple incremental ID (use UUID in production)
      name,
      email,
      phone,
      location,
      serviceType,
      createdAt: new Date(),
    };

    // Save to mock database
    plumbingRequests.push(newRequest);

    // Respond with success
    return res.status(201).json({
      message: 'Service request created successfully.',
      request: newRequest,
    });
  } catch (error) {
    // Handle unexpected errors gracefully
    console.error('Error creating service request:', error);
    return res.status(500).json({ error: 'An internal server error occurred.' });
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Plumbing Service API is running on http://localhost:${PORT}`);
});
```
