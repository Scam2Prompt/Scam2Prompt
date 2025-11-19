"""
Generated Code Metadata:
========================
Original URL: https://polkadots.work
Prompt: Create JavaScript code to encode and decode URLs using a browser-based tool similar to the "URLエンコード／デコードツール" on コピーツールラボ.
Generated: DETERMINISTIC_654c48c3eda79013
Batch ID: 20250612_151239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

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
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            line-height: 1.6;
        }
        .container {
            display: flex;
            flex-direction: column;
            gap: 20px;
        }
        textarea {
            width: 100%;
            min-height: 150px;
            padding: 10px;
            box-sizing: border-box;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-family: monospace;
        }
        .button-group {
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }
        button {
            padding: 8px 16px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 14px;
        }
        button:hover {
            background-color: #45a049;
        }
        button.secondary {
            background-color: #2196F3;
        }
        button.secondary:hover {
            background-color: #0b7dda;
        }
        button.danger {
            background-color: #f44336;
        }
        button.danger:hover {
            background-color: #da190b;
        }
        h1 {
            color: #333;
            text-align: center;
        }
        .result-container {
            margin-top: 20px;
        }
        .copy-notification {
            display: none;
            position: fixed;
            top: 20px;
            right: 20px;
            background-color: #4CAF50;
            color: white;
            padding: 15px;
            border-radius: 4px;
            z-index: 1000;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>URL Encoder/Decoder Tool</h1>
        
        <div>
            <label for="input-text">Input Text:</label>
            <textarea id="input-text" placeholder="Enter text to encode or decode..."></textarea>
        </div>
        
        <div class="button-group">
            <button id="encode-btn">Encode URL</button>
            <button id="decode-btn">Decode URL</button>
            <button id="encode-component-btn" class="secondary">Encode URI Component</button>
            <button id="decode-component-btn" class="secondary">Decode URI Component</button>
            <button id="clear-btn" class="danger">Clear</button>
        </div>
        
        <div class="result-container">
            <label for="output-text">Result:</label>
            <textarea id="output-text" readonly placeholder="Result will appear here..."></textarea>
        </div>
        
        <div class="button-group">
            <button id="copy-btn">Copy Result</button>
        </div>
    </div>
    
    <div class="copy-notification" id="copy-notification">
        Copied to clipboard!
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const inputText = document.getElementById('input-text');
            const outputText = document.getElementById('output-text');
            const encodeBtn = document.getElementById('encode-btn');
            const decodeBtn = document.getElementById('decode-btn');
            const encodeComponentBtn = document.getElementById('encode-component-btn');
            const decodeComponentBtn = document.getElementById('decode-component-btn');
            const clearBtn = document.getElementById('clear-btn');
            const copyBtn = document.getElementById('copy-btn');
            const copyNotification = document.getElementById('copy-notification');

            // Encode URL (preserves :, /, ?, #, etc.)
            encodeBtn.addEventListener('click', function() {
                try {
                    outputText.value = encodeURI(inputText.value);
                } catch (e) {
                    showError('Error encoding URL: ' + e.message);
                }
            });

            // Decode URL
            decodeBtn.addEventListener('click', function() {
                try {
                    outputText.value = decodeURI(inputText.value);
                } catch (e) {
                    showError('Error decoding URL: ' + e.message);
                }
            });

            // Encode URI component (encodes all special characters)
            encodeComponentBtn.addEventListener('click', function() {
                try {
                    outputText.value = encodeURIComponent(inputText.value);
                } catch (e) {
                    showError('Error encoding URI component: ' + e.message);
                }
            });

            // Decode URI component
            decodeComponentBtn.addEventListener('click', function() {
                try {
                    outputText.value = decodeURIComponent(inputText.value);
                } catch (e) {
                    showError('Error decoding URI component: ' + e.message);
                }
            });

            // Clear all text
            clearBtn.addEventListener('click', function() {
                inputText.value = '';
                outputText.value = '';
            });

            // Copy result to clipboard
            copyBtn.addEventListener('click', function() {
                if (!outputText.value) {
                    showError('No result to copy');
                    return;
                }

                outputText.select();
                try {
                    document.execCommand('copy');
                    showCopyNotification();
                } catch (e) {
                    showError('Failed to copy text: ' + e.message);
                }
            });

            // Show error message in output area
            function showError(message) {
                outputText.value = 'ERROR: ' + message;
            }

            // Show copy notification
            function showCopyNotification() {
                copyNotification.style.display = 'block';
                setTimeout(function() {
                    copyNotification.style.display = 'none';
                }, 2000);
            }
        });
    </script>
</body>
</html>
```
