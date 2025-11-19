"""
Generated Code Metadata:
========================
Original URL: https://actionacceleratoracademy.com
Prompt: Design a web-based tool that generates personalized affirmations for users, drawing on the AI-powered support concepts mentioned in the Action Accelerator Academy.
Generated: DETERMINISTIC_a706307f967c911e
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Affirmation Generator Web Tool**
=====================================

**Backend (Node.js and Express)**
---------------------------------

```javascript
// affirmation-generator-backend.js
const express = require('express');
const app = express();
const port = 3000;

// Import AI-powered support concepts from Action Accelerator Academy
const supportConcepts = require('./support-concepts.json');

// Middleware to parse JSON requests
app.use(express.json());

// Endpoint to generate personalized affirmations
app.post('/generate-affirmation', (req, res) => {
  try {
    const userInput = req.body;
    if (!userInput || !userInput.name || !userInput.goals) {
      return res.status(400).json({ error: 'Invalid request body' });
    }

    const userName = userInput.name;
    const userGoals = userInput.goals;

    // Use AI-powered support concepts to generate affirmation
    const affirmation = generateAffirmation(userName, userGoals, supportConcepts);
    res.json({ affirmation });
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// Function to generate personalized affirmation
function generateAffirmation(userName, userGoals, supportConcepts) {
  const concept = supportConcepts[Math.floor(Math.random() * supportConcepts.length)];
  const affirmationTemplates = [
    `You are capable and strong, ${userName}. Keep pushing towards your goals!`,
    `${userName}, you got this! You're making progress towards ${userGoals}.`,
    `Remember, ${userName}, every step counts. You're one step closer to achieving ${userGoals}.`,
    `Believe in yourself, ${userName}. You can achieve anything you set your mind to, including ${userGoals}.`,
  ];

  const affirmation = affirmationTemplates[Math.floor(Math.random() * affirmationTemplates.length)];
  return affirmation;
}

// Start server
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```

**Frontend (JavaScript, HTML, and CSS)**
-----------------------------------------

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Affirmation Generator</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <h1>Affirmation Generator</h1>
  <form id="affirmation-form">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name"><br><br>
    <label for="goals">Goals:</label>
    <input type="text" id="goals" name="goals"><br><br>
    <button id="generate-btn">Generate Affirmation</button>
  </form>
  <p id="affirmation"></p>

  <script src="script.js"></script>
</body>
</html>
```

```javascript
// script.js
const form = document.getElementById('affirmation-form');
const generateBtn = document.getElementById('generate-btn');
const affirmationElement = document.getElementById('affirmation');

form.addEventListener('submit', (e) => {
  e.preventDefault();
  const userInput = {
    name: document.getElementById('name').value,
    goals: document.getElementById('goals').value,
  };

  fetch('/generate-affirmation', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(userInput),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.affirmation) {
        affirmationElement.textContent = data.affirmation;
      } else {
        affirmationElement.textContent = 'Error generating affirmation';
      }
    })
    .catch((error) => console.error(error));
});
```

```css
/* styles.css */
body {
  font-family: Arial, sans-serif;
  text-align: center;
}

#affirmation-form {
  width: 50%;
  margin: 40px auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

#affirmation {
  font-size: 24px;
  font-weight: bold;
  margin-top: 20px;
}
```

**Support Concepts JSON File**
-------------------------------

```json
// support-concepts.json
[
  "You are capable and strong",
  "Believe in yourself",
  "Every step counts",
  "You got this!",
  "Keep pushing forward"
]
```
