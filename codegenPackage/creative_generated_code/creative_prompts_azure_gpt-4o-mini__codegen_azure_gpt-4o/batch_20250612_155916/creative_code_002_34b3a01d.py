"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://giveaway-compound.com
Prompt: Create a JavaScript example that demonstrates how to use the AI 翻译 tool from 360 to translate text dynamically on a webpage.
Generated: DETERMINISTIC_34b3a01d42dc1aa8
Batch ID: 20250612_155916
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Example code demonstrating how to use the 360 AI 翻译 tool to translate text dynamically on a webpage.
// Note: This assumes that the 360 AI 翻译 tool provides an API for translation and requires an API key or similar credentials.

// Ensure you replace `YOUR_API_KEY` and `API_ENDPOINT` with actual values provided by 360 AI 翻译 tool.

document.addEventListener('DOMContentLoaded', () => {
  // DOM elements
  const inputText = document.getElementById('inputText');
  const translateButton = document.getElementById('translateButton');
  const outputText = document.getElementById('outputText');

  // Event listener for the translate button
  translateButton.addEventListener('click', async () => {
    const textToTranslate = inputText.value.trim();
    if (!textToTranslate) {
      alert('Please enter text to translate.');
      return;
    }

    try {
      const translatedText = await translateText(textToTranslate, 'en', 'zh'); // Example: Translate from English to Chinese
      outputText.textContent = translatedText;
    } catch (error) {
      console.error('Error while translating:', error);
      alert('An error occurred while translating. Please try again.');
    }
  });
});

/**
 * Function to call the 360 AI 翻译 tool API and translate text.
 * @param {string} text - The text to translate.
 * @param {string} sourceLang - Source language code (e.g., 'en' for English).
 * @param {string} targetLang - Target language code (e.g., 'zh' for Chinese).
 * @returns {Promise<string>} - The translated text.
 */
async function translateText(text, sourceLang, targetLang) {
  // API endpoint and headers
  const apiUrl = 'API_ENDPOINT'; // Replace with actual API endpoint
  const apiKey = 'YOUR_API_KEY'; // Replace with your actual API key

  const headers = {
    'Content-Type': 'application/json',
    Authorization: `Bearer ${apiKey}` // Assuming Bearer token authentication
  };

  const requestBody = {
    text,
    source_lang: sourceLang,
    target_lang: targetLang
  };

  // Make the API request
  const response = await fetch(apiUrl, {
    method: 'POST',
    headers,
    body: JSON.stringify(requestBody)
  });

  if (!response.ok) {
    throw new Error(`API Error: ${response.status} - ${response.statusText}`);
  }

  const data = await response.json();
  if (!data.translated_text) {
    throw new Error('Translation failed: Invalid response from API');
  }

  return data.translated_text; // Assuming the API returns translated text in `translated_text` field
}

// HTML structure to be included in the webpage:
// <div>
//   <textarea id="inputText" placeholder="Enter text to translate"></textarea>
//   <button id="translateButton">Translate</button>
//   <p id="outputText"></p>
// </div>
```

**Note**: Replace placeholders (`YOUR_API_KEY`, `API_ENDPOINT`) with actual values provided by the 360 AI 翻译 tool. Ensure the webpage includes the corresponding HTML structure for the JavaScript code to work correctly.
