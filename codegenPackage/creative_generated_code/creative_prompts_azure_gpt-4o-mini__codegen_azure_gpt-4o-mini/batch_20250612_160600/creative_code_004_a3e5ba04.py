"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://originprotocol.typeform.com
Prompt: Create a Typeform quiz that gathers deeper insights by asking follow-up questions based on previous answers. Include design customization tips.
Generated: DETERMINISTIC_a3e5ba04407182cb
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
// Import required libraries
const express = require('express');
const bodyParser = require('body-parser');
const axios = require('axios');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware to parse JSON request bodies
app.use(bodyParser.json());

// Define Typeform API credentials
const TYPEFORM_API_URL = 'https://api.typeform.com/forms';
const TYPEFORM_API_KEY = 'YOUR_TYPEFORM_API_KEY'; // Replace with your Typeform API key

// Define a function to create a Typeform quiz
async function createTypeformQuiz(questions) {
    try {
        const response = await axios.post(TYPEFORM_API_URL, {
            title: "Insight Gathering Quiz",
            fields: questions,
        }, {
            headers: {
                Authorization: `Bearer ${TYPEFORM_API_KEY}`,
                'Content-Type': 'application/json',
            },
        });
        return response.data;
    } catch (error) {
        console.error("Error creating Typeform quiz:", error);
        throw new Error('Unable to create Typeform quiz.');
    }
}

// Sample questions for the quiz
const questions = [
    {
        type: 'multiple_choice',
        question: 'What is your favorite programming language?',
        choices: ['JavaScript', 'Python', 'Java', 'C#'],
        required: true,
    },
    {
        type: 'short_text',
        question: 'Why do you prefer this language?',
        required: true,
        ref: 'follow_up_why_prefer',
    },
    {
        type: 'multiple_choice',
        question: 'What type of applications do you develop?',
        choices: ['Web', 'Mobile', 'Desktop'],
        required: true,
        ref: 'follow_up_app_type',
    },
    {
        type: 'short_text',
        question: 'What challenges do you face while developing?',
        required: false,
        ref: 'follow_up_challenges',
    },
];

// Endpoint to create the Typeform quiz
app.post('/create-quiz', async (req, res) => {
    try {
        const quizData = await createTypeformQuiz(questions);
        res.status(201).json({ message: 'Quiz created successfully!', quiz: quizData });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
```

### Design Customization Tips:
1. **Branding**: Use your brand's colors and logo in the Typeform settings to ensure brand consistency.
2. **Question Logic**: Utilize Typeform's logic jumps to direct respondents to relevant follow-up questions based on their previous answers.
3. **Imagery**: Incorporate images or GIFs to make the quiz visually engaging.
4. **Responsive Design**: Ensure the quiz is mobile-friendly by testing it on various devices.
5. **User Experience**: Keep questions concise and use clear language to enhance user engagement.
