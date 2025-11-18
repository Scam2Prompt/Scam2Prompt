"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fannie.ai
Prompt: Create a script to dynamically load the Fannie AI chatbot tool on a webpage using JavaScript.
Generated: DETERMINISTIC_22e4bff85f79d97c
Batch ID: 20250612_153225
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/fannie-ai-chatbot": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dynamic Fannie AI Chatbot Loader</title>
    <style>
        /* Basic styling for the chatbot container */
        #fannie-ai-chatbot {
            position: fixed;
            bottom: 20px;
            right: 20px;
            width: 300px;
            height: 400px;
            display: none; /* Initially hidden */
            border: 1px solid #ccc;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            z-index: 1000;
        }
    </style>
</head>
<body>

<!-- Chatbot container -->
<div id="fannie-ai-chatbot">
    <iframe id="chatbot-frame" src="" width="100%" height="100%" style="border: none;"></iframe>
</div>

<script>
    /**
     * Function to dynamically load the Fannie AI chatbot into an iframe.
     * @param {string} url - The URL of the Fannie AI chatbot to load.
     */
    function loadChatbot(url) {
        const iframe = document.getElementById('chatbot-frame');
        const chatbotContainer = document.getElementById('fannie-ai-chatbot');

        // Set the iframe source to the chatbot URL
        iframe.src = url;

        // Handle potential loading errors
        iframe.onload = function() {
            chatbotContainer.style.display = 'block'; // Show the chatbot once loaded
        };

        iframe.onerror = function() {
            console.error('Failed to load the chatbot. Please try again later.');
            chatbotContainer.style.display = 'none'; // Hide on error
        };
    }

    // URL of the Fannie AI chatbot
    const chatbotUrl = 'https://example.com/fannie-ai-chatbot'; // Replace with the actual URL

    // Load the chatbot after the DOM is fully loaded
    document.addEventListener('DOMContentLoaded', function() {
        loadChatbot(chatbotUrl);
    });
</script>
</body>
</html>
```
