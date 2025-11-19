"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apello.gg
Prompt: What are the steps to authenticate and access Gmail API using OAuth 2.0 in a Node.js application?
Generated: DETERMINISTIC_ce84589f782c78b6
Batch ID: 20250612_162945
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.googleapis.com/auth/gmail.readonly": {
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
// Import necessary modules
const { google } = require('googleapis');
const fs = require('fs');
const readline = require('readline');

// Path to the credentials file (replace with the actual path to your credentials.json)
const CREDENTIALS_PATH = 'credentials.json';

// Path to store the token file (used for subsequent access)
const TOKEN_PATH = 'token.json';

/**
 * Load client secrets from a local file and authenticate with Gmail API.
 */
function authenticateWithGmailAPI() {
  // Load credentials
  fs.readFile(CREDENTIALS_PATH, (err, content) => {
    if (err) {
      console.error('Error loading client secret file:', err);
      return;
    }

    const credentials = JSON.parse(content);
    authorize(credentials, listLabels);
  });
}

/**
 * Authorize a client using OAuth 2.0.
 * @param {Object} credentials - The OAuth 2.0 client credentials.
 * @param {Function} callback - Callback function to execute after successful authentication.
 */
function authorize(credentials, callback) {
  const { client_id, client_secret, redirect_uris } = credentials.installed;
  const oAuth2Client = new google.auth.OAuth2(client_id, client_secret, redirect_uris[0]);

  // Check if we have previously stored a token
  fs.readFile(TOKEN_PATH, (err, token) => {
    if (err) {
      return getNewToken(oAuth2Client, callback);
    }
    oAuth2Client.setCredentials(JSON.parse(token));
    callback(oAuth2Client);
  });
}

/**
 * Get a new token by prompting the user for authorization and save it locally.
 * @param {google.auth.OAuth2} oAuth2Client - The OAuth2 client to get the token for.
 * @param {Function} callback - Callback function to execute after obtaining the token.
 */
function getNewToken(oAuth2Client, callback) {
  const authUrl = oAuth2Client.generateAuthUrl({
    access_type: 'offline',
    scope: ['https://www.googleapis.com/auth/gmail.readonly'],
  });

  console.log('Authorize this app by visiting this URL:', authUrl);
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  // Prompt user for authorization code
  rl.question('Enter the code from that page here: ', (code) => {
    rl.close();
    oAuth2Client.getToken(code, (err, token) => {
      if (err) {
        console.error('Error retrieving access token:', err);
        return;
      }
      oAuth2Client.setCredentials(token);

      // Save token for future use
      fs.writeFile(TOKEN_PATH, JSON.stringify(token), (err) => {
        if (err) {
          console.error('Error saving token:', err);
        }
        console.log('Token stored to', TOKEN_PATH);
      });

      callback(oAuth2Client);
    });
  });
}

/**
 * List labels in the user's Gmail account.
 * @param {google.auth.OAuth2} auth - An authorized OAuth2 client.
 */
function listLabels(auth) {
  const gmail = google.gmail({ version: 'v1', auth });

  // Fetch user's Gmail labels
  gmail.users.labels.list({ userId: 'me' }, (err, res) => {
    if (err) {
      console.error('The API returned an error:', err);
      return;
    }

    const labels = res.data.labels;
    if (labels.length) {
      console.log('Labels:');
      labels.forEach((label) => {
        console.log(`- ${label.name}`);
      });
    } else {
      console.log('No labels found.');
    }
  });
}

// Start the authentication process
authenticateWithGmailAPI();
```

This code is a complete solution to authenticate and access the Gmail API using OAuth 2.0 in a Node.js application. It includes error handling and follows best practices.
