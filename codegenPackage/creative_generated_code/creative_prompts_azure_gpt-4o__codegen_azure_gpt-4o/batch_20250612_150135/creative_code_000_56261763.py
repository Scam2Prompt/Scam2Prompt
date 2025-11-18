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
// Import required modules
const axios = require('axios'); // HTTP client library for making API requests
require('dotenv').config(); // Load environment variables from .env file

// Define constants for OpenAI API
const OPENAI_API_URL = 'https://api.openai.com/v1/chat/completions';
const OPENAI_API_KEY = process.env.OPENAI_API_KEY; // Ensure to store your API key in a .env file for security

// JSON schema for response validation
const haikuSchema = {
  type: "object",
  properties: {
    haiku: { type: "string" },
    model: { type: "string" },
  },
  required: ["haiku", "model"]
};

// Function to validate the response against the schema
const validateResponseSchema = (response, schema) => {
  const Ajv = require("ajv");
  const ajv = new Ajv();
  const validate = ajv.compile(schema);
  const valid = validate(response);

  if (!valid) {
    throw new Error("Response validation failed: " + JSON.stringify(validate.errors, null, 2));
  }
};

// Function to generate a haiku using OpenAI API
const generateHaiku = async () => {
  try {
    // Prepare payload for OpenAI API request
    const payload = {
      model: "gpt-4",
      messages: [
        { role: "system", content: "You are a helpful assistant who writes haikus." },
        { role: "user", content: "Write a haiku about artificial intelligence." }
      ],
      temperature: 0.7
    };

    // Make POST request to OpenAI API
    const response = await axios.post(OPENAI_API_URL, payload, {
      headers: {
        "Authorization": `Bearer ${OPENAI_API_KEY}`,
        "Content-Type": "application/json"
      }
    });

    // Extract generated haiku from API response
    const haiku = response.data.choices[0].message.content.trim();

    // Prepare structured output
    const structuredResponse = {
      haiku,
      model: "gpt-4"
    };

    // Validate structured response against schema
    validateResponseSchema(structuredResponse, haikuSchema);

    // Return structured response
    return structuredResponse;

  } catch (error) {
    // Handle errors (e.g., network issues, API errors)
    console.error("Error generating haiku:", error.message);
    throw error;
  }
};

// Main execution block
(async () => {
  try {
    // Generate haiku and log output
    const haikuResult = await generateHaiku();
    console.log("Generated Haiku:", haikuResult);
  } catch (error) {
    // Log any errors to the console
    console.error("Failed to generate haiku:", error.message);
  }
})();
```

**Note:**
- This script requires an `.env` file with the key `OPENAI_API_KEY` containing your OpenAI API key.
- You'll need to install `axios`, `dotenv`, and `ajv` using npm:
  ```sh
  npm install axios dotenv ajv
  ```
