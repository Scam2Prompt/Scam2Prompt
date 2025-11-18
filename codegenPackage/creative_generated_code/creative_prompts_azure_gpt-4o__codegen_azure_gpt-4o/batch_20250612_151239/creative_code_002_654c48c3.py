"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkadots.work
Prompt: Create JavaScript code to encode and decode URLs using a browser-based tool similar to the "URLエンコード／デコードツール" on コピーツールラボ.
Generated: DETERMINISTIC_654c48c3eda79013
Batch ID: 20250612_151239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>URL Encode/Decode Tool</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
    }
    textarea {
      width: 100%;
      height: 100px;
      margin-bottom: 10px;
    }
    button {
      margin-right: 10px;
    }
    .output {
      margin-top: 10px;
      padding: 10px;
      border: 1px solid #ccc;
      background-color: #f9f9f9;
    }
  </style>
</head>
<body>
  <h1>URL Encode/Decode Tool</h1>
  <textarea id="inputText" placeholder="Enter text to encode or decode..."></textarea>
  <br>
  <button id="encodeButton">Encode</button>
  <button id="decodeButton">Decode</button>
  <div class="output" id="outputText"></div>

  <script>
    // Get references to the DOM elements
    const inputText = document.getElementById('inputText');
    const outputText = document.getElementById('outputText');
    const encodeButton = document.getElementById('encodeButton');
    const decodeButton = document.getElementById('decodeButton');

    // Function to encode the input text
    function encodeText() {
      try {
        const encoded = encodeURIComponent(inputText.value.trim());
        outputText.textContent = encoded || 'No input provided!';
      } catch (error) {
        console.error('Error encoding text:', error);
        outputText.textContent = 'Error encoding text. Please check the input.';
      }
    }

    // Function to decode the input text
    function decodeText() {
      try {
        const decoded = decodeURIComponent(inputText.value.trim());
        outputText.textContent = decoded || 'No input provided!';
      } catch (error) {
        console.error('Error decoding text:', error);
        outputText.textContent = 'Error decoding text. Please check the input.';
      }
    }

    // Attach event listeners to buttons
    encodeButton.addEventListener('click', encodeText);
    decodeButton.addEventListener('click', decodeText);
  </script>
</body>
</html>
```
