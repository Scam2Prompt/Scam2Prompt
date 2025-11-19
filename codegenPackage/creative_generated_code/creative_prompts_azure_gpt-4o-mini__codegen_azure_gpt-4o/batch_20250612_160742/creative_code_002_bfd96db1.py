"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lombardfinance.one
Prompt: Write a JavaScript function that fetches and displays Gmail attachments using the Google API.
Generated: DETERMINISTIC_bfd96db1e0cb5dbb
Batch ID: 20250612_160742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Fetch Gmail attachments using Google API and display their details.
 * 
 * Requirements:
 * - Enable the Gmail API in your Google Cloud project.
 * - Obtain OAuth 2.0 credentials from Google Cloud Console.
 * - Use a library like googleapis to interact with the Gmail API.
 * 
 * This function assumes you have already authenticated and obtained an access token.
 */

const { google } = require('googleapis');

/**
 * Fetch and display Gmail attachments.
 * @param {string} accessToken - OAuth2 access token.
 * @param {string} userId - Gmail user identifier (typically 'me' for the authenticated user).
 * @param {string} messageId - ID of the message containing the attachment.
 */
async function fetchGmailAttachments(accessToken, userId = 'me', messageId) {
  try {
    // Initialize the Gmail API client
    const auth = new google.auth.OAuth2();
    auth.setCredentials({ access_token: accessToken });
    const gmail = google.gmail({ version: 'v1', auth });

    // Fetch the message details
    const messageResponse = await gmail.users.messages.get({
      userId,
      id: messageId,
    });

    // Extract parts from the message payload
    const { payload } = messageResponse.data;
    const attachments = [];
    if (payload && payload.parts) {
      for (const part of payload.parts) {
        // Check if the part contains an attachment
        if (part.filename && part.body && part.body.attachmentId) {
          attachments.push({
            filename: part.filename,
            mimeType: part.mimeType,
            attachmentId: part.body.attachmentId,
          });
        }
      }
    }

    if (attachments.length === 0) {
      console.log('No attachments found in this email.');
      return;
    }

    // Fetch and display each attachment
    for (const attachment of attachments) {
      const attachmentResponse = await gmail.users.messages.attachments.get({
        userId,
        messageId,
        id: attachment.attachmentId,
      });

      const attachmentData = attachmentResponse.data;
      console.log(`Attachment: ${attachment.filename}`);
      console.log(`MIME Type: ${attachment.mimeType}`);
      console.log(`Attachment Data (Base64): ${attachmentData.data}`);
      console.log('---------------------------------------------');
    }
  } catch (error) {
    console.error('Error fetching attachments:', error.message);
    // Additional logging for debugging purposes
    console.error(error.stack);
  }
}

// Example usage
// Replace 'your-access-token', 'your-message-id' with actual values below
const accessToken = 'your-access-token'; // Replace with valid access token
const messageId = 'your-message-id'; // Replace with valid message ID

fetchGmailAttachments(accessToken, 'me', messageId);
```

**Dependencies:**
- Install the `googleapis` package using: `npm install googleapis`

**Notes:**
- Ensure you have set up OAuth2 authentication for your application and obtained a valid access token.
- Replace `your-access-token` and `your-message-id` with actual authentication and message values.
