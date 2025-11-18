"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://acknowledgment.netlify.app
Prompt: Generate code for a Node.js Express server that handles POST requests from a contact form with fields for name, email, and message, as seen on https://acknowledgment.netlify.app.
Generated: DETERMINISTIC_c7f3fac2f2c8812b
Batch ID: 20250612_153659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require("express");
const bodyParser = require("body-parser");
const cors = require("cors");

// Create an instance of Express
const app = express();

// Set the port for the server
const PORT = process.env.PORT || 3000;

// Enable Cross-Origin Resource Sharing (CORS) for handling requests from web clients
app.use(cors());

// Use bodyParser middleware to parse JSON and URL-encoded data
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Define the route for handling POST requests from the contact form
app.post("/contact", (req, res) => {
  try {
    // Extract form fields from the request body
    const { name, email, message } = req.body;

    // Validate input (basic validation for demonstration purposes)
    if (!name || !email || !message) {
      return res.status(400).json({ error: "All fields are required." });
    }

    if (typeof name !== "string" || typeof email !== "string" || typeof message !== "string") {
      return res.status(400).json({ error: "Invalid input types." });
    }

    // Log the contact form data (for demonstration purposes, replace this with actual handling logic)
    console.log("Contact Form Submission:");
    console.log("Name:", name);
    console.log("Email:", email);
    console.log("Message:", message);

    // Send a success response back to the client
    res.status(200).json({ message: "Form submitted successfully!" });
  } catch (error) {
    // Handle unexpected errors gracefully
    console.error("Error handling contact form submission:", error);
    res.status(500).json({ error: "An error occurred while processing your request." });
  }
});

// Start the server and listen on the specified port
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```
