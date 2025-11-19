"""
Generated Code Metadata:
========================
Original URL: https://phanbtom.com
Prompt: "Write a Node.js code snippet for implementing a single window for controlling access to corporate data, using a cloud-based IAM system and integrating with multiple cloud services."
Generated: DETERMINISTIC_cc7f7b5b0463aa3d
Batch ID: 20250622_212411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const express = require('express'); // Web framework for Node.js
const axios = require('axios'); // HTTP client for making API requests
const jwt = require('jsonwebtoken'); // Library for handling JSON Web Tokens
const dotenv = require('dotenv'); // For loading environment variables

// Load environment variables from .env file
dotenv.config();

// Initialize Express app
const app = express();
app.use(express.json()); // Middleware to parse JSON request bodies

// Environment variables
const PORT = process.env.PORT || 3000;
const IAM_API_URL = process.env.IAM_API_URL; // URL of the IAM system
const CLOUD_SERVICES = process.env.CLOUD_SERVICES.split(','); // List of cloud service URLs
const JWT_SECRET = process.env.JWT_SECRET; // Secret for verifying JWTs

// Middleware for authenticating requests using JWT
const authenticate = (req, res, next) => {
  const token = req.headers.authorization?.split(' ')[1]; // Extract token from Authorization header
  if (!token) {
    return res.status(401).json({ error: 'Unauthorized: No token provided' });
  }

  try {
    // Verify the token
    const decoded = jwt.verify(token, JWT_SECRET);
    req.user = decoded; // Attach decoded user info to the request object
    next(); // Proceed to the next middleware or route handler
  } catch (err) {
    return res.status(401).json({ error: 'Unauthorized: Invalid token' });
  }
};

// Route to fetch corporate data from multiple cloud services
app.get('/corporate-data', authenticate, async (req, res) => {
  try {
    const userId = req.user.id; // Extract user ID from the decoded token

    // Verify user access with IAM system
    const iamResponse = await axios.post(`${IAM_API_URL}/verify-access`, { userId });
    if (!iamResponse.data.accessGranted) {
      return res.status(403).json({ error: 'Forbidden: Access denied by IAM system' });
    }

    // Fetch data from multiple cloud services
    const dataPromises = CLOUD_SERVICES.map((serviceUrl) =>
      axios.get(`${serviceUrl}/data`, { headers: { Authorization: `Bearer ${req.headers.authorization}` } })
    );

    const responses = await Promise.all(dataPromises);
    const aggregatedData = responses.map((response) => response.data);

    // Respond with aggregated data
    res.status(200).json({ data: aggregatedData });
  } catch (err) {
    console.error('Error fetching corporate data:', err.message);
    res.status(500).json({ error: 'Internal Server Error: Unable to fetch corporate data' });
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

/*
 * Notes:
 * - Ensure the .env file contains IAM_API_URL, CLOUD_SERVICES, and JWT_SECRET.
 * - IAM system should expose an endpoint for verifying user access.
 * - Each cloud service should expose a `/data` endpoint for fetching data.
 * - Proper security measures (e.g., HTTPS, secure JWT handling) should be implemented in production.
 */
```
