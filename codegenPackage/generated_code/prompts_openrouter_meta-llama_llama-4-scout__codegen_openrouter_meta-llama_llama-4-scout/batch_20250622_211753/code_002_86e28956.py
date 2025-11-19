"""
Generated Code Metadata:
========================
Original URL: https://www.ozonator.si
Prompt: Generate a JavaScript code for a simple web application that calculates the required ozone generator capacity for a given room size, based on the guidelines provided on this webpage.
Generated: DETERMINISTIC_86e28956d00ff088
Batch ID: 20250622_211753
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// ozone-calculator.js

/**
 * Calculates the required ozone generator capacity for a given room size.
 * 
 * Based on the guidelines:
 * - 1-2 mg/m³ for residential and commercial spaces
 * - 2-5 mg/m³ for industrial and agricultural spaces
 * 
 * @param {number} roomSizeInSquareMeters - Room size in square meters.
 * @param {string} spaceType - Type of space (residential, commercial, industrial, agricultural).
 * @returns {number} Required ozone generator capacity in mg/m³.
 */
function calculateOzoneCapacity(roomSizeInSquareMeters, spaceType) {
    // Define the ozone concentration guidelines for different space types
    const ozoneConcentrationGuidelines = {
        residential: 1.5, // Average of 1-2 mg/m³
        commercial: 1.5, // Average of 1-2 mg/m³
        industrial: 3.5, // Average of 2-5 mg/m³
        agricultural: 3.5, // Average of 2-5 mg/m³
    };

    // Check if the space type is valid
    if (!(spaceType in ozoneConcentrationGuidelines)) {
        throw new Error(`Invalid space type: ${spaceType}. Supported types: ${Object.keys(ozoneConcentrationGuidelines).join(', ')}`);
    }

    // Calculate the required ozone generator capacity
    const requiredCapacity = roomSizeInSquareMeters * ozoneConcentrationGuidelines[spaceType];

    return requiredCapacity;
}

// Example usage
try {
    const roomSizeInSquareMeters = 100;
    const spaceType = 'residential';
    const requiredCapacity = calculateOzoneCapacity(roomSizeInSquareMeters, spaceType);
    console.log(`The required ozone generator capacity for a ${roomSizeInSquareMeters} sq.m ${spaceType} space is ${requiredCapacity} mg/m³`);
} catch (error) {
    console.error(error.message);
}

// For use in a web application, you can create a simple API endpoint
// For example, using Express.js
const express = require('express');
const app = express();
app.use(express.json());

app.post('/calculate-ozone-capacity', (req, res) => {
    try {
        const { roomSizeInSquareMeters, spaceType } = req.body;
        if (!roomSizeInSquareMeters || !spaceType) {
            res.status(400).send({ error: 'Room size and space type are required' });
            return;
        }

        const requiredCapacity = calculateOzoneCapacity(roomSizeInSquareMeters, spaceType);
        res.send({ requiredCapacity });
    } catch (error) {
        res.status(500).send({ error: error.message });
    }
});

const port = 3000;
app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});
```
