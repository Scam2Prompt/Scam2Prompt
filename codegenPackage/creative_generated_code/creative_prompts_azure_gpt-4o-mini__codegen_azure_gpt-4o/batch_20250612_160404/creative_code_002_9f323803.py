"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.iaci.org
Prompt: Create a RESTful API endpoint in Node.js that allows users to submit testimonials for a business association like IACI, including fields for member name, organization, and testimonial text.
Generated: DETERMINISTIC_9f32380394deab95
Batch ID: 20250612_160404
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
const bodyParser = require('body-parser');
const { v4: uuidv4 } = require('uuid'); // For generating unique IDs

// Initialize the app
const app = express();
const PORT = 3000;

// Middleware
app.use(bodyParser.json()); // Parse JSON body

// In-memory storage for testimonials (replace with a database in production)
const testimonials = [];

/**
 * POST /api/testimonials
 * Endpoint to submit a testimonial
 * Expects a JSON body with:
 * - memberName (string): Name of the member submitting the testimonial
 * - organization (string): Name of the organization
 * - testimonialText (string): Testimonial content
 */
app.post('/api/testimonials', (req, res) => {
  try {
    // Extract data from the request body
    const { memberName, organization, testimonialText } = req.body;

    // Validate input
    if (!memberName || typeof memberName !== 'string') {
      return res.status(400).json({ error: 'Invalid memberName. It must be a non-empty string.' });
    }
    if (!organization || typeof organization !== 'string') {
      return res.status(400).json({ error: 'Invalid organization. It must be a non-empty string.' });
    }
    if (!testimonialText || typeof testimonialText !== 'string') {
      return res.status(400).json({ error: 'Invalid testimonialText. It must be a non-empty string.' });
    }

    // Create a new testimonial entry
    const newTestimonial = {
      id: uuidv4(), // Generate a unique ID
      memberName,
      organization,
      testimonialText,
      submittedAt: new Date().toISOString(), // Timestamp of submission
    };

    // Store the testimonial
    testimonials.push(newTestimonial);

    // Respond with the created testimonial
    res.status(201).json({
      message: 'Testimonial successfully submitted.',
      testimonial: newTestimonial,
    });
  } catch (error) {
    // Handle unexpected errors
    console.error('Error submitting testimonial:', error);
    res.status(500).json({ error: 'An unexpected error occurred. Please try again later.' });
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});

```

### Instructions:
1. Save the code in a file called `app.js`.
2. Install required dependencies using:
   ```bash
   npm install express body-parser uuid
   ```
3. Start the server with:
   ```bash
   node app.js
   ```
4. Test the API using tools like Postman or `curl`. Example request body:
   ```json
   {
     "memberName": "John Doe",
     "organization": "IACI",
     "testimonialText": "The association has helped us grow tremendously!"
   }
   ```
