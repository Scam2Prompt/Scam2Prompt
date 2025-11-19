"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fannie.ai
Prompt: What are the steps to enable JavaScript for using the Fannie AI chatbot?
Generated: DETERMINISTIC_4794ffba61ca661c
Batch ID: 20250612_162050
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
    <title>Enable JavaScript for Fannie AI Chatbot</title>
    <style>
        /* Basic styling to guide users */
        .js-disabled {
            display: none;
            color: red;
            font-size: 1.2em;
        }

        .js-enabled {
            display: none;
            color: green;
            font-size: 1.2em;
        }
    </style>
    <script>
        // Check if JavaScript is enabled in the user's browser
        document.addEventListener('DOMContentLoaded', () => {
            // Hide the "JavaScript Disabled" message and show the "JavaScript Enabled" message
            const jsDisabledElement = document.getElementById('js-disabled-message');
            const jsEnabledElement = document.getElementById('js-enabled-message');

            if (jsDisabledElement && jsEnabledElement) {
                jsDisabledElement.style.display = 'none'; // Hide "disabled" message
                jsEnabledElement.style.display = 'block'; // Show "enabled" message
            }
        });
    </script>
</head>
<body>
    <!-- Message displayed when JavaScript is disabled -->
    <noscript>
        <p id="js-disabled-message" class="js-disabled">
            JavaScript is disabled in your browser. Please enable JavaScript to use the Fannie AI chatbot.
        </p>
    </noscript>

    <!-- Message displayed when JavaScript is enabled -->
    <p id="js-enabled-message" class="js-enabled">
        JavaScript is enabled! You can now use the Fannie AI chatbot.
    </p>

    <!-- Placeholder for the chatbot integration -->
    <div id="chatbot-container">
        <!-- Fannie AI Chatbot will be loaded here dynamically -->
    </div>

    <script>
        // Example code to initialize the Fannie AI chatbot after confirming JavaScript is enabled
        function initializeChatbot() {
            try {
                const chatbotContainer = document.getElementById('chatbot-container');
                if (!chatbotContainer) {
                    throw new Error('Chatbot container not found!');
                }

                // Simulate loading the chatbot (replace this with actual API or SDK initialization)
                const chatbotElement = document.createElement('div');
                chatbotElement.textContent = 'Fannie AI Chatbot is now active!';
                chatbotElement.style.border = '1px solid #ccc';
                chatbotElement.style.padding = '10px';
                chatbotElement.style.marginTop = '20px';

                chatbotContainer.appendChild(chatbotElement);
            } catch (error) {
                console.error('Error initializing chatbot:', error.message);
                alert('Failed to load Fannie AI chatbot. Please try again later.');
            }
        }

        // Initialize the chatbot
        initializeChatbot();
    </script>
</body>
</html>
```
