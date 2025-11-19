"""
Generated Code Metadata:
========================
Original URL: https://krnas.com
Prompt: Write a function in JavaScript to authenticate a user via OAuth2 for Gmail API access.
Generated: DETERMINISTIC_1c2e897ad7c2df8c
Batch ID: 20250612_151355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
const { google } = require('googleapis');
const fs = require('fs').promises;
const path = require('path');

/**
 * Authenticates with Gmail API using OAuth2
 * @param {Object} credentials - OAuth2 client credentials
 * @param {string} credentials.client_id - Google OAuth2 client ID
 * @param {string} credentials.client_secret - Google OAuth2 client secret
 * @param {string} credentials.redirect_uris - Google OAuth2 redirect URIs
 * @param {string} tokenPath - Path to store/read the OAuth2 token
 * @param {string[]} scopes - Array of Gmail API scopes
 * @returns {Promise<google.auth.OAuth2>} Authenticated OAuth2 client
 */
async function authenticateGmail(credentials, tokenPath, scopes) {
    try {
        const { client_secret, client_id, redirect_uris } = credentials;
        const oAuth2Client = new google.auth.OAuth2(
            client_id,
            client_secret,
            redirect_uris[0]
        );

        // Check if we have previously stored a token
        try {
            const token = await fs.readFile(tokenPath);
            oAuth2Client.setCredentials(JSON.parse(token));
            return oAuth2Client;
        } catch (err) {
            return getNewToken(oAuth2Client, tokenPath, scopes);
        }
    } catch (error) {
        console.error('Error during authentication:', error);
        throw error;
    }
}

/**
 * Gets new token after prompting for user authorization
 * @param {google.auth.OAuth2} oAuth2Client - The OAuth2 client
 * @param {string} tokenPath - Path to store the OAuth2 token
 * @param {string[]} scopes - Array of Gmail API scopes
 * @returns {Promise<google.auth.OAuth2>} Authenticated OAuth2 client
 */
async function getNewToken(oAuth2Client, tokenPath, scopes) {
    try {
        const authUrl = oAuth2Client.generateAuthUrl({
            access_type: 'offline',
            scope: scopes,
        });

        console.log('Authorize this app by visiting this URL:', authUrl);
        
        // In a real application, you would redirect the user to authUrl
        // and handle the callback with the authorization code
        // For CLI purposes, we'll simulate it here
        const readline = require('readline').createInterface({
            input: process.stdin,
            output: process.stdout,
        });

        return new Promise((resolve, reject) => {
            readline.question('Enter the code from that page here: ', async (code) => {
                readline.close();
                try {
                    const { tokens } = await oAuth2Client.getToken(code);
                    oAuth2Client.setCredentials(tokens);
                    
                    // Store the token to disk for later program executions
                    await fs.writeFile(tokenPath, JSON.stringify(tokens));
                    console.log('Token stored to', tokenPath);
                    
                    resolve(oAuth2Client);
                } catch (error) {
                    reject(error);
                }
            });
        });
    } catch (error) {
        console.error('Error getting new token:', error);
        throw error;
    }
}

module.exports = { authenticateGmail };
```
