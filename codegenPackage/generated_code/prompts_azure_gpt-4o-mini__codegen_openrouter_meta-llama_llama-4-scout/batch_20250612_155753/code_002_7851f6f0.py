"""
Generated Code Metadata:
========================
Original URL: https://hrtsforstrky.carrd.co
Prompt: Write a JavaScript function to validate user input for a follow request form on a Carrd site, ensuring it checks for negative energy keywords.
Generated: DETERMINISTIC_7851f6f0e83eccd8
Batch ID: 20250612_155753
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates user input for a follow request form, checking for negative energy keywords.
 *
 * @param {string} username - The username of the user submitting the request.
 * @param {string} message - The message accompanying the follow request.
 * @returns {object} An object containing a boolean indicating validity and an array of error messages.
 */
function validateFollowRequest(username, message) {
  // Define negative energy keywords to check for
  const negativeKeywords = ['hate', 'stupid', 'bad', 'awful', 'terrible'];

  // Initialize error messages array
  const errorMessages = [];

  // Check if username is provided and not empty
  if (!username || username.trim() === '') {
    errorMessages.push('Username is required');
  }

  // Check if message is provided and not empty
  if (!message || message.trim() === '') {
    errorMessages.push('Message is required');
  } else {
    // Check for negative energy keywords in the message
    const hasNegativeKeyword = negativeKeywords.some((keyword) => {
      return message.toLowerCase().includes(keyword);
    });

    if (hasNegativeKeyword) {
      errorMessages.push('Message contains negative energy keywords');
    }
  }

  // Return validity and error messages
  return {
    isValid: errorMessages.length === 0,
    errorMessages,
  };
}

// Example usage:
function handleFollowRequest() {
  try {
    const username = document.getElementById('username').value;
    const message = document.getElementById('message').value;

    const { isValid, errorMessages } = validateFollowRequest(username, message);

    if (!isValid) {
      // Display error messages to user
      const errorList = document.getElementById('error-list');
      errorList.innerHTML = '';
      errorMessages.forEach((error) => {
        const errorItem = document.createElement('li');
        errorItem.textContent = error;
        errorList.appendChild(errorItem);
      });
    } else {
      // Submit the follow request
      console.log('Submitting follow request...');
      // Add submission logic here
    }
  } catch (error) {
    console.error('Error handling follow request:', error);
  }
}
```
