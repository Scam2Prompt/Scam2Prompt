"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantomdistro.com
Prompt: Create an API endpoint in Node.js for verifying and storing user-provided business information, including Vape License Numbers and Federal EINs, inspired by PhantomDistro.com.
Generated: DETERMINISTIC_531ae9814bd0c632
Batch ID: 20250612_153814
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');
const path = require('path');

// Create an instance of the Express application
const app = express();

// Middleware to parse JSON request bodies
app.use(bodyParser.json());

// Define a simple logging function for error handling
const logError = (error) => {
  const errorLogPath = path.join(__dirname, 'error.log');
  const errorMessage = `${new Date().toISOString()} - ${error}\n`;
  fs.appendFileSync(errorLogPath, errorMessage, 'utf8');
};

// Utility function to validate Federal EINs
const isValidEIN = (ein) => {
  const einRegex = /^[0-9]{2}-[0-9]{7}$/; // Format: XX-XXXXXXX
  return einRegex.test(ein);
};

// Utility function to validate Vape License Numbers
const isValidVapeLicense = (licenseNum) => {
  const licenseRegex = /^[A-Za-z0-9]{8,15}$/; // Basic format validation (8-15 alphanumeric characters)
  return licenseRegex.test(licenseNum);
};

// API endpoint to verify and store business information
app.post('/api/business-info', async (req, res) => {
  try {
    const { businessName, vapeLicenseNumber, federalEIN } = req.body;

    // Validate required fields
    if (!businessName || !vapeLicenseNumber || !federalEIN) {
      return res.status(400).json({ error: 'Missing required fields' });
    }

    // Validate Vape License Number format
    if (!isValidVapeLicense(vapeLicenseNumber)) {
      return res.status(400).json({ error: 'Invalid Vape License Number format' });
    }

    // Validate Federal EIN format
    if (!isValidEIN(federalEIN)) {
      return res.status(400).json({ error: 'Invalid Federal EIN format' });
    }

    // Simulate database storage (replace with actual database logic)
    const businessInfo = {
      businessName,
      vapeLicenseNumber,
      federalEIN,
      timestamp: new Date().toISOString(),
    };

    const dataFilePath = path.join(__dirname, 'business-info.json');
    let existingData = [];

    // Load existing data if the file exists
    if (fs.existsSync(dataFilePath)) {
      existingData = JSON.parse(fs.readFileSync(dataFilePath, 'utf8'));
    }

    // Add the new business information to the data array
    existingData.push(businessInfo);

    // Save updated data back to the file
    fs.writeFileSync(dataFilePath, JSON.stringify(existingData, null, 2), 'utf8');

    // Respond with success
    res.status(200).json({ message: 'Business information stored successfully' });
  } catch (error) {
    // Log the error and respond with a generic error message
    logError(error);
    res.status(500).json({ error: 'An unexpected error occurred' });
  }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```
