"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fannie.ai
Prompt: Generate JavaScript code to log user interactions with the Fannie AI chatbot for analytics purposes.
Generated: DETERMINISTIC_449b1278558fd936
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Logs user interactions with the Fannie AI chatbot for analytics purposes.
 * The log includes the user's message, the chatbot's response, and a timestamp.
 */

// Create a logging function for analytics
function logUserInteraction(userMessage, botResponse) {
  try {
    // Validate inputs
    if (typeof userMessage !== 'string' || typeof botResponse !== 'string') {
      throw new Error('Invalid input: Both userMessage and botResponse must be strings.');
    }

    // Prepare log object
    const interactionLog = {
      timestamp: new Date().toISOString(), // ISO format timestamp
      userMessage: userMessage.trim(),    // Trim whitespace from user message
      botResponse: botResponse.trim()     // Trim whitespace from bot response
    };

    // Send log to server or save locally (example API endpoint used here)
    fetch('/api/interaction-log', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(interactionLog)
    })
      .then(response => {
        if (!response.ok) {
          throw new Error(`Failed to log interaction: ${response.statusText}`);
        }
        // Log success in the console for debugging
        console.log('User interaction logged successfully:', interactionLog);
      })
      .catch(error => {
        // Handle network or server errors
        console.error('Error logging user interaction:', error.message);
      });

  } catch (error) {
    // Handle validation or unexpected errors
    console.error('Error in logUserInteraction function:', error.message);
  }
}

// Example usage of the logging function
const userMessage = "Hi, how can you help me?";
const botResponse = "Hello! I can assist you with your questions about Fannie AI.";
logUserInteraction(userMessage, botResponse);
```
