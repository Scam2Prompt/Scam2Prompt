"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oraclememe-com.pages.dev
Prompt: Describe how to set up a Meme AI Generator using JavaScript that incorporates AI-powered suggestions for meme creation, similar to the features on Oracle Meme.
Generated: DETERMINISTIC_d60a346bb34e024d
Batch ID: 20250612_160940
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.openai.com/v1/completions": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://via.placeholder.com/500": {
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
/**
 * Meme AI Generator: JavaScript implementation for generating memes with AI-powered suggestions.
 * This script uses a combination of OpenAI API (for AI suggestions) and Canvas API for meme generation.
 * Note: Replace placeholder API keys and ensure required dependencies are installed.
 */

// Import required modules. Ensure you have installed 'node-fetch' for API calls (npm install node-fetch).
const fetch = require('node-fetch');

// Configuration for OpenAI API
const OPENAI_API_KEY = 'your_openai_api_key'; // Replace with your actual OpenAI API key
const OPENAI_API_URL = 'https://api.openai.com/v1/completions';

// HTML structure for web page (front-end integration)
const memeHTMLTemplate = `
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Meme AI Generator</title>
  <style>
    body { font-family: Arial, sans-serif; text-align: center; }
    canvas { border: 1px solid #000; margin-top: 20px; }
  </style>
</head>
<body>
  <h1>Meme AI Generator</h1>
  <input type="text" id="memePrompt" placeholder="Enter meme prompt" style="width: 300px;">
  <button id="generateMemeBtn">Generate Meme</button>
  <canvas id="memeCanvas" width="500" height="500"></canvas>
  <script src="memeGenerator.js"></script>
</body>
</html>
`;

// Save the above template as index.html, and the following script as memeGenerator.js

// JavaScript for front-end interactivity
(async function () {
  // Select DOM elements
  const memePromptInput = document.getElementById('memePrompt');
  const generateMemeBtn = document.getElementById('generateMemeBtn');
  const memeCanvas = document.getElementById('memeCanvas');
  const ctx = memeCanvas.getContext('2d');

  // Function to call OpenAI API for suggestions
  async function getAISuggestions(prompt) {
    const response = await fetch(OPENAI_API_URL, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${OPENAI_API_KEY}`
      },
      body: JSON.stringify({
        model: 'text-davinci-003', // Specify the model
        prompt: `Generate a funny meme idea based on: "${prompt}"`,
        max_tokens: 50, // Limit the response length
        temperature: 0.7 // Control randomness
      })
    });

    if (!response.ok) {
      throw new Error(`AI API Error: ${response.statusText}`);
    }

    const data = await response.json();
    return data.choices[0].text.trim(); // Extract AI suggestion
  }

  // Function to generate meme
  async function generateMeme() {
    const prompt = memePromptInput.value;
    if (!prompt) {
      alert('Please enter a meme prompt.');
      return;
    }

    try {
      // Get AI suggestion
      const suggestion = await getAISuggestions(prompt);

      // Clear canvas and draw meme
      ctx.clearRect(0, 0, memeCanvas.width, memeCanvas.height);
      ctx.fillStyle = '#fff';
      ctx.fillRect(0, 0, memeCanvas.width, memeCanvas.height);

      // Load a random meme image (for simplicity, using a static image URL)
      const img = new Image();
      img.src = 'https://via.placeholder.com/500'; // Replace with dynamic image source
      img.onload = () => {
        ctx.drawImage(img, 0, 0, memeCanvas.width, memeCanvas.height);

        // Add text suggestions
        ctx.fillStyle = '#000';
        ctx.font = '20px Arial';
        ctx.textAlign = 'center';
        ctx.fillText(suggestion, memeCanvas.width / 2, memeCanvas.height - 50);
      };
    } catch (error) {
      console.error('Error generating meme:', error);
      alert('Failed to generate meme. Please try again.');
    }
  }

  // Attach event listener to button
  generateMemeBtn.addEventListener('click', generateMeme);
})();
```

**Instructions for setup:**
1. Replace the `OPENAI_API_KEY` placeholder with your actual OpenAI API key.
2. Save the HTML template as `index.html` and the JavaScript code as `memeGenerator.js`.
3. Run a local server (e.g., using `http-server` or any other static file server) to host the files.
4. Ensure `node-fetch` is installed if you are executing the backend logic in Node.js for API calls.
