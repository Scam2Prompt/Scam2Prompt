"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://be-solana-methods-v1.docs-62t.pages.dev
Prompt: Generate a full web-based documentation for a smart contract using Código's CIDL, including all exposed methods and input parameters.
Generated: DETERMINISTIC_b1d0b8fe37e7e304
Batch ID: 20250612_163305
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:3000/api/docs`.": {
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
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');
const path = require('path');

// Initialize the Express application
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware to parse JSON request bodies
app.use(bodyParser.json());

// Function to load CIDL file and parse methods
const loadCIDL = (cidlPath) => {
    try {
        const data = fs.readFileSync(cidlPath, 'utf8');
        return JSON.parse(data); // Assuming CIDL is in JSON format
    } catch (error) {
        console.error("Error reading CIDL file:", error);
        throw new Error("Failed to load CIDL file");
    }
};

// Endpoint to get smart contract documentation
app.get('/api/docs', (req, res) => {
    const cidlPath = path.join(__dirname, 'contract.cidl');
    try {
        const contractData = loadCIDL(cidlPath);
        res.json(contractData); // Send contract data as JSON response
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
```

**contract.cidl** (Example CIDL file content)
```json
{
    "contractName": "MySmartContract",
    "methods": [
        {
            "name": "createUser",
            "description": "Creates a new user in the system.",
            "parameters": [
                {
                    "name": "username",
                    "type": "string",
                    "required": true
                },
                {
                    "name": "email",
                    "type": "string",
                    "required": true
                }
            ]
        },
        {
            "name": "getUser",
            "description": "Retrieves user information based on the username.",
            "parameters": [
                {
                    "name": "username",
                    "type": "string",
                    "required": true
                }
            ]
        }
    ]
}
```

### Instructions to Run:
1. Save the JavaScript code in a file named `server.js`.
2. Save the CIDL example in a file named `contract.cidl` in the same directory.
3. Ensure Node.js is installed on your machine.
4. Run `npm init -y` to create a package.json file.
5. Run `npm install express body-parser`.
6. Execute `node server.js` to start the server.
7. Access the documentation at `http://localhost:3000/api/docs`.
