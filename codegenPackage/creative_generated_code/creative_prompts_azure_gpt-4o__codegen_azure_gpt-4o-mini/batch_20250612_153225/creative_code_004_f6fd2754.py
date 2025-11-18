"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fannie.ai
Prompt: Write code to customize the user interface of the Fannie AI chatbot tool using JavaScript.
Generated: DETERMINISTIC_f6fd2754d2504f5a
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Fannie AI Chatbot UI Customization Script
// This script customizes the user interface of the Fannie AI chatbot tool.

(function() {
    // Check if the Fannie AI chatbot element is present on the page
    const chatbotContainer = document.getElementById('fannie-ai-chatbot');

    if (!chatbotContainer) {
        console.error("Fannie AI Chatbot element not found. Ensure that the chatbot is included on the page.");
        return;
    }

    // Function to customize the chatbot styles
    function customizeChatbotStyles() {
        try {
            // Set overall styles for the chatbot container
            chatbotContainer.style.backgroundColor = '#f9f9f9';
            chatbotContainer.style.borderRadius = '10px';
            chatbotContainer.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.1)';
            chatbotContainer.style.padding = '20px';

            // Customize the header
            const header = chatbotContainer.querySelector('.chatbot-header');
            if (header) {
                header.style.backgroundColor = '#6200ea';
                header.style.color = '#ffffff';
                header.style.padding = '10px';
                header.style.borderRadius = '10px 10px 0 0';
                header.innerHTML = '<h2 style="margin: 0;">Fannie AI Chatbot</h2>';
            } else {
                console.warn("Header element not found.");
            }

            // Customize message bubble styles
            const messageBubbles = chatbotContainer.querySelectorAll('.chatbot-message');
            messageBubbles.forEach(bubble => {
                bubble.style.borderRadius = '15px';
                bubble.style.padding = '10px';
                bubble.style.margin = '5px 0';
                bubble.style.maxWidth = '70%';
            });

            // Customize input field
            const inputField = chatbotContainer.querySelector('.chatbot-input');
            if (inputField) {
                inputField.style.borderRadius = '25px';
                inputField.style.border = '1px solid #6200ea';
                inputField.style.padding = '10px';
                inputField.style.width = '80%';
                inputField.style.marginRight = '5px';
            } else {
                console.warn("Input field element not found.");
            }

            // Customize send button
            const sendButton = chatbotContainer.querySelector('.chatbot-send');
            if (sendButton) {
                sendButton.style.backgroundColor = '#6200ea';
                sendButton.style.color = '#ffffff';
                sendButton.style.border = 'none';
                sendButton.style.borderRadius = '25px';
                sendButton.style.padding = '10px 15px';
                sendButton.style.cursor = 'pointer';

                // Add hover effect
                sendButton.addEventListener('mouseover', () => {
                    sendButton.style.backgroundColor = '#3700b3';
                });

                sendButton.addEventListener('mouseout', () => {
                    sendButton.style.backgroundColor = '#6200ea';
                });
            } else {
                console.warn("Send button element not found.");
            }
        } catch (error) {
            console.error("Error customizing chatbot styles:", error);
        }
    }

    // Initialize customization
    customizeChatbotStyles();
})();
```
