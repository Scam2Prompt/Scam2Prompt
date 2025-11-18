"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chajianxw.com
Prompt: Suggest Chrome extensions for grammar checking and paraphrasing, such as "AI Grammar Checker & Paraphraser – LanguageTool," and write code to integrate its API into a web application.
Generated: DETERMINISTIC_5b10952ab7be1a14
Batch ID: 20250612_155000
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://api.languagetool.org/v2/check": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:3000/api/check`": {
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
// Importing necessary libraries
const express = require('express');
const axios = require('axios');

// Initialize Express application
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware to parse JSON requests
app.use(express.json());

// API endpoint to check grammar and paraphrase text
app.post('/api/check', async (req, res) => {
    const { text } = req.body;

    // Validate request body
    if (!text) {
        return res.status(400).json({ error: 'Text is required' });
    }

    // Define LanguageTool API endpoint
    const apiUrl = 'https://api.languagetool.org/v2/check';

    try {
        // Make request to LanguageTool API
        const response = await axios.post(apiUrl, null, {
            params: {
                text: text,
                language: 'en-US' // Specify the language
            }
        });

        // Return the response from LanguageTool
        return res.status(200).json(response.data);
    } catch (error) {
        // Error handling
        console.error('Error calling LanguageTool API:', error.message);
        return res.status(500).json({ error: 'An error occurred while checking grammar' });
    }
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
```

### Instructions for Running the Code
1. Ensure you have Node.js installed on your machine.
2. Create a directory for the project and navigate into it.
3. Initialize a new Node.js project with `npm init -y`.
4. Install the necessary dependencies: `npm install express axios`.
5. Save the above code to a file named `server.js`.
6. Run the server with `node server.js`.
7. Use a tool like Postman or cURL to send a POST request to `http://localhost:3000/api/check` with a JSON body containing the text to check. 

### Example JSON body for the POST request:
```json
{
    "text": "This is an exmple of text to check."
}
```

### Suggested Chrome Extensions
1. **Grammarly** - A popular grammar, punctuation, and style checker.
2. **ProWritingAid** - Comprehensive writing tool and grammar checker.
3. **LanguageTool** - Multi-language grammar and style checker that integrates well with various applications.
4. **Ginger** - Grammar and spell checker with paraphrasing capabilities.
