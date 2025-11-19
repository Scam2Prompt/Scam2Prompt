"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poligon.store
Prompt: Write a code snippet in JavaScript that interacts with the Мамбa API to send messages to users based on specific interests and preferences.
Generated: DETERMINISTIC_c1205cace8cb76bd
Batch ID: 20250612_162753
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.mamba.ru/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Constants for API endpoint and access token
const API_BASE_URL = 'https://api.mamba.ru/v1'; // Mamba API base URL
const ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN_HERE'; // Replace with your actual access token

/**
 * Sends a message to a user based on their interests and preferences.
 * 
 * @param {string} userId - The ID of the user to whom the message will be sent.
 * @param {string} message - The message content to send.
 * @returns {Promise<void>} - A promise that resolves when the message is sent.
 * @throws {Error} - Throws an error if the API call fails or returns an error.
 */
async function sendMessageToUser(userId, message) {
    if (!userId || !message) {
        throw new Error('User ID and message content are required.');
    }

    const url = `${API_BASE_URL}/messages/send`;
    const payload = {
        user_id: userId,
        message: message,
    };

    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${ACCESS_TOKEN}`,
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(payload),
        });
        
        // Check if the response status indicates success
        if (!response.ok) {
            const errorDetails = await response.json();
            throw new Error(`Failed to send message: ${errorDetails.message}`);
        }

        console.log(`Message sent successfully to user ${userId}`);

    } catch (error) {
        console.error('Error while sending message:', error.message);
        throw error; // Re-throw the error for further handling if needed
    }
}

/**
 * Example usage: Sending a message to a user with specified interests.
 * 
 * Replace 'USER_ID' and 'Your message here' with actual values.
 */
(async () => {
    const userId = 'USER_ID'; // Replace with the actual user ID
    const message = 'Your message here'; // Replace with the message you want to send

    try {
        await sendMessageToUser(userId, message);
    } catch (error) {
        console.error('An error occurred:', error.message);
    }
})();
```
