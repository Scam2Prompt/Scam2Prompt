"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openai.cadn.net.cn
Prompt: How can I use the OpenAI API to generate a haiku about AI using Node.js?
Generated: DETERMINISTIC_51f16a3a43fb66ca
Batch ID: 20250612_160232
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.openai.com/v1/chat/completions": {
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
// Importing the required modules
const axios = require('axios');

// Constants for the OpenAI API
const API_URL = 'https://api.openai.com/v1/chat/completions';
const API_KEY = 'YOUR_API_KEY_HERE'; // Replace with your OpenAI API key

/**
 * Generates a haiku about AI using the OpenAI API.
 * 
 * @returns {Promise<string>} The generated haiku.
 * @throws {Error} If there is an error in the API call or response.
 */
async function generateHaiku() {
    // Setting up the request payload for OpenAI API
    const requestBody = {
        model: 'gpt-3.5-turbo',
        messages: [
            {
                role: 'user',
                content: 'Write a haiku about artificial intelligence.'
            }
        ],
        max_tokens: 50, // Adjust the token limit as needed to ensure a haiku format
        temperature: 0.7 // Adjust the temperature for creativity
    };

    try {
        // Making the API call
        const response = await axios.post(API_URL, requestBody, {
            headers: {
                'Authorization': `Bearer ${API_KEY}`,
                'Content-Type': 'application/json'
            }
        });

        // Extracting the haiku from the response
        const haiku = response.data.choices[0].message.content.trim();
        return haiku;
    } catch (error) {
        // Error handling for API call failures
        console.error('Error generating haiku:', error.message);
        throw new Error('Failed to generate haiku. Please try again later.');
    }
}

// Main function to execute the haiku generation
(async () => {
    try {
        const haiku = await generateHaiku();
        console.log('Generated Haiku:\n', haiku);
    } catch (error) {
        console.error(error.message);
    }
})();
```
Make sure to replace `'YOUR_API_KEY_HERE'` with your actual OpenAI API key before running the code.
