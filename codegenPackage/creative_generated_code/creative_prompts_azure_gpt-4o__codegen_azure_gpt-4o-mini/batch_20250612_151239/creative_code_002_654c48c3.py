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
    <title>URL Encoder/Decoder Tool</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            padding: 20px;
            max-width: 600px;
            margin: auto;
            background-color: #f4f4f4;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        input, textarea, button {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            background-color: #28a745;
            color: white;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: #218838;
        }
    </style>
</head>
<body>

    <h1>URL Encoder/Decoder Tool</h1>
    <label for="inputText">Enter URL:</label>
    <textarea id="inputText" rows="4" placeholder="Type or paste your URL here..."></textarea>
    
    <button id="encodeBtn">Encode URL</button>
    <button id="decodeBtn">Decode URL</button>
    
    <h2>Result:</h2>
    <textarea id="outputText" rows="4" readonly></textarea>

    <script>
        /**
         * Encodes a given URL by replacing special characters with their UTF-8 encoded equivalents.
         * @param {string} url - The URL to encode.
         * @returns {string} - The encoded URL.
         */
        function encodeUrl(url) {
            try {
                return encodeURIComponent(url);
            } catch (error) {
                console.error('Error encoding URL:', error);
                return 'Encoding error. Please check your input.';
            }
        }

        /**
         * Decodes a given encoded URL back to its original format.
         * @param {string} encodedUrl - The encoded URL to decode.
         * @returns {string} - The decoded URL.
         */
        function decodeUrl(encodedUrl) {
            try {
                return decodeURIComponent(encodedUrl);
            } catch (error) {
                console.error('Error decoding URL:', error);
                return 'Decoding error. Please check your input.';
            }
        }

        // Get references to DOM elements
        const inputText = document.getElementById('inputText');
        const outputText = document.getElementById('outputText');
        const encodeBtn = document.getElementById('encodeBtn');
        const decodeBtn = document.getElementById('decodeBtn');

        // Event listener for the encode button
        encodeBtn.addEventListener('click', () => {
            const input = inputText.value.trim();
            if (input) {
                const result = encodeUrl(input);
                outputText.value = result;
            } else {
                outputText.value = 'Please enter a URL to encode.';
            }
        });

        // Event listener for the decode button
        decodeBtn.addEventListener('click', () => {
            const input = inputText.value.trim();
            if (input) {
                const result = decodeUrl(input);
                outputText.value = result;
            } else {
                outputText.value = 'Please enter an encoded URL to decode.';
            }
        });
    </script>

</body>
</html>
```
