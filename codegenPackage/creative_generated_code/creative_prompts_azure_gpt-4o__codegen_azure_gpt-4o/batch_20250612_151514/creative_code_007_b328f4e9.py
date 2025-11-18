"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coastalboatrentals.co.za
Prompt: Write a Node.js API endpoint to retrieve detailed information about a specific boat, such as "Celebrity 170," including its features like foam flotation and Yamaha outboard motor.
Generated: DETERMINISTIC_b328f4e91a2dec62
Batch ID: 20250612_151514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require('express'); // Express framework for API creation
const bodyParser = require('body-parser'); // Middleware for parsing JSON requests

// Initialize the app
const app = express();
app.use(bodyParser.json()); // Enable JSON parsing

// Mock database of boats
const boats = [
  {
    id: 1,
    name: "Celebrity 170",
    features: ["Foam flotation", "Yamaha outboard motor", "Comfortable seating", "GPS navigation"],
  },
  {
    id: 2,
    name: "Speedster 200X",
    features: ["Turbo engine", "Hydraulic steering", "Bluetooth sound system"],
  },
  {
    id: 3,
    name: "Ocean Cruiser 500",
    features: ["Satellite radio", "Deep hull design", "Automatic bilge pump"],
  },
];

// API endpoint to retrieve detailed information about a specific boat
/**
 * Route: GET /api/boats/:name
 * Description: Retrieves detailed information about a specific boat.
 * Request Params: 
 *   - name (string): The name of the boat to search for.
 * Response:
 *   - 200: Returns the boat details in JSON format.
 *   - 404: If the boat is not found, returns an error message.
 */
app.get('/api/boats/:name', (req, res) => {
  try {
    const boatName = req.params.name; // Extract the boat name from the route parameters

    // Find the boat in the mock database
    const boat = boats.find((b) => b.name.toLowerCase() === boatName.toLowerCase());

    if (!boat) {
      // If the boat is not found, return a 404 error
      return res.status(404).json({
        error: `Boat with name "${boatName}" not found.`,
      });
    }

    // If the boat is found, return its details
    res.status(200).json({
      message: "Boat details retrieved successfully.",
      boat,
    });
  } catch (error) {
    // Generic error handling
    console.error("Error occurred while retrieving the boat details:", error);
    res.status(500).json({
      error: "An internal server error occurred. Please try again later.",
    });
  }
});

// Start the server
const PORT = process.env.PORT || 3000; // Use environment variable PORT or default to 3000
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```
