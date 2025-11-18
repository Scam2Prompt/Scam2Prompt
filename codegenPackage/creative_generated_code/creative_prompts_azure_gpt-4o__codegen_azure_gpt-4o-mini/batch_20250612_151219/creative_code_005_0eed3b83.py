"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://npcs.pages.dev
Prompt: Create a guide for integrating the generaitiv AI API into a web application to generate NPC-related images based on user input.
Generated: DETERMINISTIC_0eed3b8349466a2e
Batch ID: 20250612_151219
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://api.generativeai.com/v1/generate-image": {
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
  "http://localhost:3000/generate-npc-image`": {
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
// Import necessary libraries
const express = require('express');
const axios = require('axios');
const bodyParser = require('body-parser');

// Initialize the Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware to parse JSON bodies
app.use(bodyParser.json());

// Replace with your actual generative AI API URL and key
const GENERATIVE_AI_API_URL = 'https://api.generativeai.com/v1/generate-image';
const API_KEY = 'YOUR_API_KEY_HERE';

// Function to generate NPC-related images based on user input
async function generateImage(npcDescription) {
    try {
        const response = await axios.post(GENERATIVE_AI_API_URL, {
            description: npcDescription,
        }, {
            headers: {
                'Authorization': `Bearer ${API_KEY}`,
                'Content-Type': 'application/json',
            }
        });

        // Check for successful response
        if (response.status === 200) {
            return response.data.imageUrl; // Assuming the API returns the URL of the generated image
        } else {
            throw new Error(`Failed to generate image: ${response.statusText}`);
        }
    } catch (error) {
        console.error('Error generating NPC image:', error);
        throw new Error('Image generation failed. Please try again later.');
    }
}

// API endpoint to handle image generation requests
app.post('/generate-npc-image', async (req, res) => {
    const { description } = req.body;

    // Validate input
    if (!description || typeof description !== 'string') {
        return res.status(400).json({ error: 'Invalid input: description is required and must be a string.' });
    }

    try {
        const imageUrl = await generateImage(description);
        res.status(200).json({ imageUrl });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
```

### Instructions to Set Up and Run the Application:
1. Ensure you have Node.js and npm installed on your machine.
2. Create a new directory for your project and navigate into it.
3. Run `npm init -y` to create a new `package.json` file.
4. Install the required dependencies by running:
   ```bash
   npm install express axios body-parser
   ```
5. Replace `YOUR_API_KEY_HERE` with your actual API key for the generative AI service.
6. Save the provided code in a file named `app.js`.
7. Start the application by running:
   ```bash
   node app.js
   ```
8. Use a tool like Postman or cURL to send a POST request to `http://localhost:3000/generate-npc-image` with a JSON body containing the `description`.

### Example JSON Body:
```json
{
    "description": "A tall, mysterious wizard with a long beard and a staff."
}
```
