"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openai.cadn.net.cn
Prompt: Write a Node.js script using the OpenAI API to generate a haiku about artificial intelligence using the GPT-4o model, ensuring the response adheres to a JSON schema for structured output.
Generated: DETERMINISTIC_56261763180ec38a
Batch ID: 20250612_150135
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
// Import the necessary modules
const axios = require('axios');

// Configuration for the OpenAI API
const OPENAI_API_KEY = 'YOUR_OPENAI_API_KEY'; // Replace with your actual OpenAI API Key
const OPENAI_API_URL = 'https://api.openai.com/v1/chat/completions';

// Function to generate a haiku about artificial intelligence
async function generateHaiku() {
    // Define the prompt for the AI
    const prompt = 'Write a haiku about artificial intelligence.';

    // Prepare the request payload for the OpenAI API
    const requestBody = {
        model: 'gpt-4',
        messages: [{ role: 'user', content: prompt }],
        max_tokens: 60, // Limit the response length
        temperature: 0.7, // Control the creativity of the response
    };

    try {
        // Make a POST request to the OpenAI API
        const response = await axios.post(OPENAI_API_URL, requestBody, {
            headers: {
                'Authorization': `Bearer ${OPENAI_API_KEY}`,
                'Content-Type': 'application/json',
            },
        });

        // Extract the haiku from the response
        const haiku = response.data.choices[0].message.content.trim();

        // Structure the output according to JSON schema
        const output = {
            title: 'Haiku on Artificial Intelligence',
            author: 'OpenAI GPT-4',
            content: haiku,
            schema: {
                type: 'object',
                properties: {
                    title: { type: 'string' },
                    author: { type: 'string' },
                    content: { type: 'string' },
                },
                required: ['title', 'author', 'content'],
            },
        };

        // Log the structured output
        console.log(JSON.stringify(output, null, 2));
    } catch (error) {
        // Error handling for API call
        console.error('Error generating haiku:', error.response ? error.response.data : error.message);
    }
}

// Execute the haiku generation function
generateHaiku();
```

**Note:** Remember to replace `'YOUR_OPENAI_API_KEY'` with your actual OpenAI API key for the script to work.
