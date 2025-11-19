"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apello.gg
Prompt: Write a script that retrieves Gmail messages using the Google API client library for JavaScript.
Generated: DETERMINISTIC_240defdfe52e9738
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the required libraries
const { google } = require('googleapis');
const OAuth2 = google.auth.OAuth2;

// Set up OAuth2 client with client ID and secret
const CLIENT_ID = 'YOUR_CLIENT_ID';
const CLIENT_SECRET = 'YOUR_CLIENT_SECRET';
const REDIRECT_URI = 'YOUR_REDIRECT_URI';

// Create an OAuth2 client instance
const oauth2Client = new OAuth2(
    CLIENT_ID,
    CLIENT_SECRET,
    REDIRECT_URI
);

// Set the access token for authorization
oauth2Client.setCredentials({
    refresh_token: 'YOUR_REFRESH_TOKEN' // Obtain this token after user authentication
});

// Create a Gmail API client
const gmail = google.gmail({ version: 'v1', auth: oauth2Client });

/**
 * Function to retrieve Gmail messages
 * @param {string} userId - The user's email address. 'me' refers to the authenticated user.
 * @returns {Promise<void>} - A promise that resolves when messages are retrieved.
 */
async function listMessages(userId = 'me') {
    try {
        // Retrieve the list of messages from the user's Gmail
        const response = await gmail.users.messages.list({
            userId: userId,
            maxResults: 10, // Limit the number of messages retrieved
            q: 'is:unread'  // Optional: filter for unread messages
        });

        const messages = response.data.messages || [];

        if (messages.length) {
            console.log('Messages:');
            // Loop through the messages and log their IDs
            messages.forEach((message) => {
                console.log(`- Message ID: ${message.id}`);
            });
        } else {
            console.log('No unread messages found.');
        }
    } catch (error) {
        console.error('The API returned an error: ' + error);
    }
}

// Call the function to list messages
listMessages();
```

**Note:** 
- Replace `YOUR_CLIENT_ID`, `YOUR_CLIENT_SECRET`, `YOUR_REDIRECT_URI`, and `YOUR_REFRESH_TOKEN` with your actual credentials.
- Make sure to initialize the Google API client and obtain the necessary tokens through the OAuth2 flow before running this script.
