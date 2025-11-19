"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fijimaths.com
Prompt: Design an API endpoint in Node.js that retrieves the competition rules and forms for the Fiji Mathematics Association's events.
Generated: DETERMINISTIC_a567bf83afa462b4
Batch ID: 20250612_161235
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
// Import necessary modules
const express = require('express');
const fs = require('fs');
const path = require('path');

// Initialize Express app
const app = express();

// Set up a port for the server
const PORT = process.env.PORT || 3000;

// Define the route to fetch competition rules and forms
app.get('/api/competition-details', async (req, res) => {
    try {
        // Define paths to the rules and forms files (replace with actual file paths)
        const rulesFilePath = path.join(__dirname, 'data', 'competition_rules.json');
        const formsFilePath = path.join(__dirname, 'data', 'competition_forms.json');

        // Read the competition rules file
        const rulesData = await fs.promises.readFile(rulesFilePath, 'utf8');
        
        // Read the competition forms file
        const formsData = await fs.promises.readFile(formsFilePath, 'utf8');

        // Parse JSON data
        const competitionRules = JSON.parse(rulesData);
        const competitionForms = JSON.parse(formsData);

        // Send the combined response
        res.status(200).json({
            success: true,
            message: "Competition rules and forms retrieved successfully.",
            data: {
                rules: competitionRules,
                forms: competitionForms
            }
        });
    } catch (error) {
        // Handle errors such as file not found or JSON parsing issues
        console.error('Error retrieving competition details:', error.message);
        
        res.status(500).json({
            success: false,
            message: 'Failed to retrieve competition details. Please try again later.',
            error: error.message
        });
    }
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});

// Export the app for testing or further development (optional)
module.exports = app;
```
