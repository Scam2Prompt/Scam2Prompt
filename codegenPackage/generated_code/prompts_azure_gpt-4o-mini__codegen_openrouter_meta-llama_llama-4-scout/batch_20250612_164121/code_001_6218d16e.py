"""
Generated Code Metadata:
========================
Original URL: https://1o2.ir
Prompt: Create a simple web application that allows users to explore random questions about personality and education, inspired by the content on dex.chat.
Generated: DETERMINISTIC_6218d16e9e59a95f
Batch ID: 20250612_164121
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://dex.chat/api": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

**Personality and Education Question Web Application**
======================================================

**dependencies:**
* `express`: ^4.17.1
* `axios`: ^0.21.1

**package.json**
```json
{
  "name": "personality-education-questions",
  "version": "1.0.0",
  "scripts": {
    "start": "node app.js"
  },
  "dependencies": {
    "express": "^4.17.1",
    "axios": "^0.21.1"
  }
}
```

**app.js**
```javascript
// Import required modules
const express = require('express');
const axios = require('axios');

// Initialize Express app
const app = express();
app.use(express.json());
app.use(express.static('public'));

// Configuration
const PORT = 3000;
const DEX_CHAT_API_URL = 'https://dex.chat/api';

// API endpoint to retrieve random question
app.get('/api/question', async (req, res) => {
  try {
    const response = await axios.get(`${DEX_CHAT_API_URL}/questions/random`);
    const question = response.data;
    res.json(question);
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Failed to retrieve question' });
  }
});

// API endpoint to retrieve questions by category
app.get('/api/questions/:category', async (req, res) => {
  try {
    const category = req.params.category;
    const response = await axios.get(`${DEX_CHAT_API_URL}/questions/category/${category}`);
    const questions = response.data;
    res.json(questions);
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Failed to retrieve questions' });
  }
});

// Serve index.html
app.get('/', (req, res) => {
  res.sendFile(__dirname + '/public/index.html');
});

// Start server
app.listen(PORT, () => {
  console.log(`Server started on port ${PORT}`);
});
```

**public/index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Personality and Education Questions</title>
  <style>
    body {
      font-family: Arial, sans-serif;
    }
  </style>
</head>
<body>
  <h1>Personality and Education Questions</h1>
  <button id="random-question-btn">Get Random Question</button>
  <div id="question-container"></div>

  <script>
    const randomQuestionBtn = document.getElementById('random-question-btn');
    const questionContainer = document.getElementById('question-container');

    randomQuestionBtn.addEventListener('click', async () => {
      try {
        const response = await fetch('/api/question');
        const question = await response.json();
        questionContainer.innerHTML = `
          <h2>${question.text}</h2>
          <p>Category: ${question.category}</p>
        `;
      } catch (error) {
        console.error(error);
      }
    });
  </script>
</body>
</html>
```

**public/script.js**
```javascript
// Get questions by category
const getQuestionsByCategory = async (category) => {
  try {
    const response = await fetch(`/api/questions/${category}`);
    const questions = await response.json();
    return questions;
  } catch (error) {
    console.error(error);
  }
};

// Example usage
getQuestionsByCategory('personality').then((questions) => {
  console.log(questions);
});
```
