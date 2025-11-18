"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fannie.ai
Prompt: Write code to handle errors when initializing the Fannie AI chatbot tool on a webpage.
Generated: DETERMINISTIC_47c587ae3f0ae6a5
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to initialize the Fannie AI chatbot tool
function initializeFannieAIChatbot() {
    try {
        // Check if the Fannie AI script is already loaded
        if (typeof FannieAI === 'undefined') {
            throw new Error("Fannie AI script is not loaded. Please ensure the script is included in your HTML.");
        }
        
        // Initialize the chatbot with necessary configurations
        const chatbotConfig = {
            apiKey: 'YOUR_API_KEY', // Replace with your actual API key
            containerId: 'chatbot-container', // The ID of the HTML element where the chatbot will be rendered
            theme: 'default', // Customize the theme if needed
            language: 'en' // Set the preferred language
        };

        // Creating an instance of the chatbot
        const chatbotInstance = new FannieAI.Chatbot(chatbotConfig);

        // Render the chatbot in the specified container
        chatbotInstance.render();

        console.log("Fannie AI Chatbot initialized successfully.");
        
    } catch (error) {
        // Handle errors during initialization
        console.error("Error initializing Fannie AI chatbot:", error.message);
        
        // Optionally, display an error message to the user
        displayErrorMessage("Failed to initialize the chatbot. Please try again later.");
    }
}

// Function to display error messages to the user
function displayErrorMessage(message) {
    const errorContainer = document.getElementById('error-container');
    if (errorContainer) {
        errorContainer.innerText = message;
        errorContainer.style.color = 'red'; // Style the error message
    } else {
        console.warn("Error container not found. Unable to display error message.");
    }
}

// Call the function to initialize the chatbot when the window loads
window.onload = function() {
    initializeFannieAIChatbot();
};
```

Make sure to replace `'YOUR_API_KEY'` with the actual API key and ensure that the HTML contains elements with the IDs `'chatbot-container'` and `'error-container'` for the chatbot and error messages, respectively.
