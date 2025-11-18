"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://krnas.com
Prompt: Provide code to check if a Gmail account has new emails using the Gmail API in Node.js.
Generated: DETERMINISTIC_5881cd6ab7023168
Batch ID: 20250612_151355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Load required libraries
const { google } = require('googleapis');
const { OAuth2 } = google.auth;

// Define constants for your application
const CLIENT_ID = 'YOUR_CLIENT_ID';
const CLIENT_SECRET = 'YOUR_CLIENT_SECRET';
const REDIRECT_URI = 'YOUR_REDIRECT_URI';
const REFRESH_TOKEN = 'YOUR_REFRESH_TOKEN';

// Initialize OAuth2 client
const oauth2Client = new OAuth2(
    CLIENT_ID,
    CLIENT_SECRET,
    REDIRECT_URI
);

// Set the refresh token
oauth2Client.setCredentials({ refresh_token: REFRESH_TOKEN });

// Create a function to check for new emails
async function checkForNewEmails() {
    try {
        // Create a Gmail instance
        const gmail = google.gmail({ version: 'v1', auth: oauth2Client });

        // Get the user's profile to retrieve the email address
        const profileResponse = await gmail.users.getProfile({ userId: 'me' });
        const userEmail = profileResponse.data.emailAddress;
        
        console.log(`Checking for new emails for: ${userEmail}`);

        // List the user's messages
        const messagesResponse = await gmail.users.messages.list({
            userId: 'me',
            q: 'is:unread', // Query for unread messages
        });

        const messages = messagesResponse.data.messages || [];
        
        if (messages.length > 0) {
            console.log(`You have ${messages.length} new email(s).`);
            return messages;
        } else {
            console.log('No new emails found.');
            return [];
        }
    } catch (error) {
        // Handle errors appropriately
        console.error('Error retrieving emails:', error.message);
        throw new Error('Failed to check for new emails');
    }
}

// Execute the function to check for new emails
checkForNewEmails().catch(err => console.error(err));
```

Make sure to replace `YOUR_CLIENT_ID`, `YOUR_CLIENT_SECRET`, `YOUR_REDIRECT_URI`, and `YOUR_REFRESH_TOKEN` with your actual credentials obtained from the Google Developer Console.
