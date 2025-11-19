"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://origineth.com
Prompt: Create a JavaScript function that checks for unread emails in a Gmail inbox using the Gmail API.
Generated: DETERMINISTIC_22cf7cbe21367a47
Batch ID: 20250612_161246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to check for unread emails in a Gmail inbox using the Gmail API.
 * @returns {Promise<number>} - Returns the count of unread emails.
 */
async function getUnreadEmailCount() {
  try {
    // Load the Google API client library
    await gapi.client.load('gmail', 'v1');

    // Get the authenticated user's email messages
    const response = await gapi.client.gmail.users.messages.list({
      userId: 'me', // 'me' refers to the authenticated user
      q: 'is:unread', // Query to search for unread emails
    });

    // Check if the response contains messages
    if (response.result.messages && response.result.messages.length > 0) {
      return response.result.messages.length; // Return the count of unread emails
    } else {
      return 0; // No unread emails found
    }
  } catch (error) {
    // Log the error for debugging
    console.error('Error fetching unread emails:', error);

    // Throw a meaningful error for the caller to handle
    throw new Error('Failed to retrieve unread email count. Please ensure the Gmail API is properly authenticated and configured.');
  }
}

// Example usage:
// getUnreadEmailCount()
//   .then((count) => console.log(`Unread emails: ${count}`))
//   .catch((error) => console.error(error));
```

### Notes:
1. This code assumes that the Google API client (`gapi`) has been loaded and authenticated prior to calling this function.
2. Configuration and authentication for the Gmail API should be handled separately (e.g., obtaining OAuth tokens, enabling the API in Google Cloud console, etc.).
3. Replace `'me'` with a specific user's email if you want to query a different user's inbox.
