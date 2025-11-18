"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://status.ttec.smartteam.chat
Prompt: Create a function in JavaScript that subscribes a user to TTEC STC Cluster Status updates by submitting their email and displays a confirmation message upon success.
Generated: DETERMINISTIC_f58f69a834f255d0
Batch ID: 20250612_154742
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/subscribe": {
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
/**
 * Subscribes a user to TTEC STC Cluster Status updates.
 * 
 * @param {string} email - The email address of the user to subscribe.
 * @returns {Promise<void>} - A promise that resolves when the subscription is successful.
 */
async function subscribeToClusterStatus(email) {
    // Validate the email format using a regular expression
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailPattern.test(email)) {
        throw new Error('Invalid email format.');
    }

    try {
        // Send a POST request to the subscription API
        const response = await fetch('https://api.example.com/subscribe', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ email }),
        });

        // Check if the response is successful
        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(`Subscription failed: ${errorData.message}`);
        }

        // Display a confirmation message upon success
        console.log('Subscription successful! You will receive updates at ' + email);
    } catch (error) {
        // Handle errors gracefully
        console.error('An error occurred while subscribing:', error.message);
        alert('Failed to subscribe. Please try again later.');
    }
}

// Example Usage
const emailInput = document.getElementById('email');  // Assuming there's an input with ID 'email'
const subscribeButton = document.getElementById('subscribe');  // Assuming there's a button with ID 'subscribe'

subscribeButton.addEventListener('click', async () => {
    const email = emailInput.value.trim();
    try {
        await subscribeToClusterStatus(email);
    } catch (error) {
        alert(error.message);
    }
});
```
