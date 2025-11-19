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
 * Function to validate user input for a follow request form.
 * Ensures the input does not contain negative energy keywords.
 * 
 * @param {string} userInput - The text input from the user.
 * @returns {Object} - An object containing validation status and a message.
 */
function validateFollowRequest(userInput) {
  // List of negative energy keywords to check for
  const negativeKeywords = [
    "hate",
    "anger",
    "jealousy",
    "resentment",
    "negativity",
    "toxic",
    "hostility",
    "rage",
    "bitterness",
    "malice"
  ];

  // Ensure input is a string and not empty
  if (typeof userInput !== "string" || userInput.trim() === "") {
    return {
      isValid: false,
      message: "Input cannot be empty and must be a valid string."
    };
  }

  // Normalize input to lowercase for case-insensitive comparison
  const normalizedInput = userInput.toLowerCase();

  // Check for negative keywords in the input
  const foundKeywords = negativeKeywords.filter(keyword => normalizedInput.includes(keyword));

  if (foundKeywords.length > 0) {
    return {
      isValid: false,
      message: `Input contains negative energy keywords: ${foundKeywords.join(", ")}. Please revise your message.`
    };
  }

  // If no negative keywords are found, input is valid
  return {
    isValid: true,
    message: "Input is valid and free of negative energy keywords."
  };
}

// Example usage:
// const result = validateFollowRequest("I feel a lot of anger and resentment.");
// console.log(result);
```
