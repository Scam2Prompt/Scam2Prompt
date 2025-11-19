"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hrtsforstrky.carrd.co
Prompt: Write a JavaScript function to validate user input for a follow request form on a Carrd site, ensuring it checks for negative energy keywords.
Generated: DETERMINISTIC_7851f6f0e83eccd8
Batch ID: 20250612_155753
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to validate user input for a follow request form.
 * Checks for negative energy keywords to ensure positivity in user messages.
 *
 * @param {string} userInput - The text provided by the user in the form.
 * @returns {object} - Result object containing validity status and error message (if any).
 */
function validateFollowRequest(userInput) {
  // List of negative energy keywords
  const negativeKeywords = [
    "hate",
    "anger",
    "jealousy",
    "resentment",
    "negativity",
    "hostility",
    "toxic",
  ];

  // Trim whitespace from user input for better validation
  const trimmedInput = userInput.trim();

  // Error handling: Check if input is empty
  if (!trimmedInput) {
    return {
      isValid: false,
      errorMessage: "Input cannot be empty. Please provide a positive message.",
    };
  }

  // Validate against negative keywords
  for (const keyword of negativeKeywords) {
    if (trimmedInput.toLowerCase().includes(keyword)) {
      return {
        isValid: false,
        errorMessage: `Your message contains negative energy. Please avoid using words like "${keyword}".`,
      };
    }
  }

  // If no issues found, return valid status
  return {
    isValid: true,
    errorMessage: null,
  };
}

// Example usage:
// const result = validateFollowRequest("I really dislike this platform!");
// console.log(result);
```
