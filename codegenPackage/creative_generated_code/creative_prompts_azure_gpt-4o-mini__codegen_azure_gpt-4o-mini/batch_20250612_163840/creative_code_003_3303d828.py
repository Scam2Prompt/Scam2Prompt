"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imetobkbn.com
Prompt: Can you provide a code example that demonstrates how to prompt users to enable JavaScript for better functionality on mobile sites like imetobkbn.com?
Generated: DETERMINISTIC_3303d82813167010
Batch ID: 20250612_163840
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
    <title>JavaScript Enable Prompt</title>
    <style>
        /* Basic styling for the prompt */
        #js-prompt {
            display: none; /* Hidden by default */
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-color: rgba(0, 0, 0, 0.7);
            color: white;
            text-align: center;
            padding: 50px;
            z-index: 1000;
        }

        #js-prompt h1 {
            font-size: 24px;
            margin-bottom: 20px;
        }

        #js-prompt p {
            font-size: 18px;
            margin-bottom: 30px;
        }

        #js-prompt button {
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
        }
    </style>
</head>
<body>

<div id="js-prompt">
    <h1>JavaScript Required</h1>
    <p>This site works best with JavaScript enabled. Please enable JavaScript in your browser settings.</p>
    <button onclick="closePrompt()">Close</button>
</div>

<script>
    // Function to check if JavaScript is enabled
    function checkJavaScriptEnabled() {
        // If JavaScript is enabled, we can remove the prompt
        document.getElementById('js-prompt').style.display = 'none';
    }

    // Function to close the prompt
    function closePrompt() {
        document.getElementById('js-prompt').style.display = 'none';
    }

    // Check if JavaScript is disabled
    window.onload = function() {
        // Show the prompt if JavaScript is not enabled
        document.getElementById('js-prompt').style.display = 'block';
    };

    // Call the function to confirm JavaScript is enabled
    checkJavaScriptEnabled();
</script>

<noscript>
    <!-- Fallback for browsers with JavaScript disabled -->
    <style>
        #js-prompt {
            display: block; /* Show the prompt when JavaScript is disabled */
        }
    </style>
</noscript>

</body>
</html>
```
