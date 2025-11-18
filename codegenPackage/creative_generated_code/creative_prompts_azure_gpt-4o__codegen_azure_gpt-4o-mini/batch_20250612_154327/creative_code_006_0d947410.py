"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stakewise.pages.dev
Prompt: Generate a guide for setting up a Node.js application to interact with Stakewise staking services.
Generated: DETERMINISTIC_0d94741068f8e9fb
Batch ID: 20250612_154327
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://nodejs.org/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:3000/api/staking/YOUR_STAKING_ADDRESS": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:${PORT}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.stakewise.io/v1": {
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
// Import necessary modules
const express = require('express'); // Web framework for Node.js
const axios = require('axios'); // Promise-based HTTP client for the browser and Node.js
const morgan = require('morgan'); // HTTP request logger middleware
const cors = require('cors'); // Package to enable CORS

// Create an Express application
const app = express();
const PORT = process.env.PORT || 3000; // Set the port for the application

// Middleware setup
app.use(cors()); // Enable CORS for all routes
app.use(express.json()); // Parse JSON request bodies
app.use(morgan('dev')); // Log requests to the console

// Base URL for Stakewise API
const STAKEWISE_API_URL = 'https://api.stakewise.io/v1';

// Function to get staking information
async function getStakingInfo(stakingAddress) {
    try {
        const response = await axios.get(`${STAKEWISE_API_URL}/staking/${stakingAddress}`);
        return response.data; // Return response data
    } catch (error) {
        console.error('Error fetching staking information:', error.message);
        throw new Error('Could not fetch staking information.'); // Throw a generic error
    }
}

// Route to fetch staking info by address
app.get('/api/staking/:address', async (req, res) => {
    const stakingAddress = req.params.address;
    
    try {
        const stakingInfo = await getStakingInfo(stakingAddress);
        res.status(200).json(stakingInfo); // Send response back to client
    } catch (error) {
        res.status(500).json({ error: error.message }); // Send error response
    }
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`); // Log server start message
});

// Handle uncaught exceptions and unhandled promise rejections
process.on('uncaughtException', (error) => {
    console.error('Uncaught Exception:', error.message);
    process.exit(1); // Exit the process with failure
});

process.on('unhandledRejection', (reason, promise) => {
    console.error('Unhandled Rejection at:', promise, 'reason:', reason);
    process.exit(1); // Exit the process with failure
});
```

### Instructions for Running the Application

1. **Install Node.js**: Ensure Node.js is installed on your machine. You can download it from [nodejs.org](https://nodejs.org/).

2. **Create a new project directory**: 
   ```bash
   mkdir stakewise-app
   cd stakewise-app
   ```

3. **Initialize a new Node.js project**: 
   ```bash
   npm init -y
   ```

4. **Install dependencies**: 
   ```bash
   npm install express axios morgan cors
   ```

5. **Create a new file named `app.js`**: 
   ```bash
   touch app.js
   ```

6. **Copy the provided code** into `app.js`.

7. **Run the application**: 
   ```bash
   node app.js
   ```

8. **Test the API**: You can use Postman or cURL to test the endpoint:
   ```
   GET http://localhost:3000/api/staking/YOUR_STAKING_ADDRESS
   ```

9. **Replace `YOUR_STAKING_ADDRESS`** with the actual address you wish to query.
