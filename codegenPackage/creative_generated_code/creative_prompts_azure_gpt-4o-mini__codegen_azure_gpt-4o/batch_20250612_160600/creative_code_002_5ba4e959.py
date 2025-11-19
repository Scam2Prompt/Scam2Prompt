"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://electrocoin.typeform.com
Prompt: Create a quiz using Typeform that collects user data while maintaining a branded design and interactive elements.
Generated: DETERMINISTIC_5ba4e95987918882
Batch ID: 20250612_160600
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.typeform.com/forms": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.typeform.com/themes/${quizConfig.themeId}`": {
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
// Required Dependencies: Make sure to install the 'axios' package before running this code.
// Run `npm install axios` to add axios for HTTP requests.

const axios = require('axios');

// Typeform API credentials
const TYPEFORM_API_URL = "https://api.typeform.com/forms";
const TYPEFORM_API_KEY = "your_typeform_api_key"; // Replace with your Typeform API key

/**
 * Creates a branded, interactive quiz form on Typeform.
 * @param {Object} quizConfig - Configuration for the quiz.
 * @param {string} quizConfig.title - Title of the quiz.
 * @param {string} quizConfig.themeId - ID of the theme for branded design.
 * @param {Array} quizConfig.questions - Questions for the quiz in the form of objects.
 */
async function createQuizForm(quizConfig) {
  try {
    // Validate input
    if (!quizConfig.title || !quizConfig.questions || quizConfig.questions.length === 0) {
      throw new Error("Invalid configuration: title and questions are required.");
    }

    // Prepare request body for Typeform API
    const formPayload = {
      title: quizConfig.title,
      theme: { href: `https://api.typeform.com/themes/${quizConfig.themeId}` }, // Branded design
      fields: quizConfig.questions.map((question) => ({
        title: question.title,
        type: question.type,
        properties: question.properties || {}, // Additional properties for the question
      })),
      settings: {
        is_public: true, // Make the form public
        is_trial: false,
        language: "en",
      },
    };

    // Send POST request to create the form
    const response = await axios.post(TYPEFORM_API_URL, formPayload, {
      headers: {
        Authorization: `Bearer ${TYPEFORM_API_KEY}`,
        "Content-Type": "application/json",
      },
    });

    // Handle response
    console.log("Quiz created successfully!", response.data);
    console.log("Form URL:", response.data._links.display);
  } catch (error) {
    // Error handling
    console.error("Failed to create quiz form:", error.message);
  }
}

// Example usage
const quizConfig = {
  title: "Interactive Quiz Example",
  themeId: "your_theme_id", // Replace with your branded theme ID from Typeform
  questions: [
    {
      title: "What is your name?",
      type: "short_text", // Short text field
    },
    {
      title: "What is your favorite programming language?",
      type: "multiple_choice", // Multiple choice
      properties: {
        choices: [
          { label: "JavaScript" },
          { label: "Python" },
          { label: "Java" },
          { label: "C++" },
        ],
      },
    },
    {
      title: "Rate your experience with coding.",
      type: "opinion_scale", // Opinion scale
      properties: {
        steps: 10,
        start_at_one: true,
      },
    },
  ],
};

// Create the quiz
createQuizForm(quizConfig);
```

**Note:** Replace `your_typeform_api_key` and `your_theme_id` with your actual Typeform API key and theme ID, respectively. Ensure you have appropriate permissions and the theme is already created in Typeform.
