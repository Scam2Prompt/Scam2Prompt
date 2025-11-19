"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://8147f917.carbon-app-csq.pages.dev
Prompt: Write a code snippet to integrate Google sign-in using Cloudflare Access.
Generated: DETERMINISTIC_7245707587cd1bd6
Batch ID: 20250612_163243
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://accounts.google.com/o/oauth2/v2/auth": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://oauth2.googleapis.com/token": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://your-domain/callback": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://${CLOUDFLARE_ACCESS_DOMAIN}/cdn-cgi/access/callback`,": {
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
// Import necessary libraries
// Ensure you install 'node-fetch' for making HTTP requests by running: npm install node-fetch
const fetch = require('node-fetch');

// Cloudflare Access configuration
const CLOUDFLARE_ACCESS_DOMAIN = 'your-cloudflare-access-domain.cloudflareaccess.com';
const CLOUDFLARE_APPLICATION_ID = 'your-cloudflare-application-id';
const CLOUDFLARE_CLIENT_SECRET = 'your-cloudflare-client-secret';

// Google Sign-In configuration
const GOOGLE_OAUTH_URL = 'https://accounts.google.com/o/oauth2/v2/auth';
const GOOGLE_TOKEN_URL = 'https://oauth2.googleapis.com/token';
const GOOGLE_CLIENT_ID = 'your-google-client-id';
const GOOGLE_CLIENT_SECRET = 'your-google-client-secret';
const GOOGLE_REDIRECT_URI = 'your-redirect-uri'; // e.g., https://your-domain/callback

/**
 * Generates the Google OAuth login URL
 * @returns {string} The URL the user should be redirected to for Google login
 */
function generateGoogleLoginURL() {
  const params = new URLSearchParams({
    client_id: GOOGLE_CLIENT_ID,
    redirect_uri: GOOGLE_REDIRECT_URI,
    response_type: 'code',
    scope: 'openid email profile',
    access_type: 'offline',
  });

  return `${GOOGLE_OAUTH_URL}?${params.toString()}`;
}

/**
 * Exchanges the authorization code for an access token from Google
 * @param {string} authorizationCode - The authorization code returned by Google after user login
 * @returns {Promise<object>} The access token response from Google
 */
async function exchangeAuthorizationCodeForGoogleAccessToken(authorizationCode) {
  try {
    const response = await fetch(GOOGLE_TOKEN_URL, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: new URLSearchParams({
        code: authorizationCode,
        client_id: GOOGLE_CLIENT_ID,
        client_secret: GOOGLE_CLIENT_SECRET,
        redirect_uri: GOOGLE_REDIRECT_URI,
        grant_type: 'authorization_code',
      }),
    });

    if (!response.ok) {
      throw new Error(`Failed to exchange authorization code: ${response.statusText}`);
    }

    return await response.json();
  } catch (error) {
    console.error('Error exchanging authorization code for token:', error);
    throw error;
  }
}

/**
 * Exchanges Google access token for a Cloudflare Access token
 * @param {string} googleIdToken - The ID token received from Google
 * @returns {Promise<object>} The JWT token from Cloudflare Access
 */
async function exchangeGoogleTokenForCloudflareAccess(googleIdToken) {
  try {
    const response = await fetch(`https://${CLOUDFLARE_ACCESS_DOMAIN}/cdn-cgi/access/callback`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        id_token: googleIdToken,
        client_id: CLOUDFLARE_APPLICATION_ID,
        client_secret: CLOUDFLARE_CLIENT_SECRET,
      }),
    });

    if (!response.ok) {
      throw new Error(`Failed to exchange Google token for Cloudflare Access: ${response.statusText}`);
    }

    return await response.json();
  } catch (error) {
    console.error('Error exchanging Google token for Cloudflare Access token:', error);
    throw error;
  }
}

// Example flow
async function handleGoogleSignIn(authorizationCode) {
  try {
    // Step 1: Exchange the authorization code for a Google access token
    const googleTokenResponse = await exchangeAuthorizationCodeForGoogleAccessToken(authorizationCode);

    // Step 2: Extract the Google ID token (JWT)
    const googleIdToken = googleTokenResponse.id_token;

    // Step 3: Exchange the Google ID token for a Cloudflare Access JWT
    const cloudflareAccessToken = await exchangeGoogleTokenForCloudflareAccess(googleIdToken);

    // Return the Cloudflare Access JWT
    return cloudflareAccessToken;
  } catch (error) {
    console.error('Error during Google Sign-In process:', error);
    throw error;
  }
}

// Export the functions for use in the application
module.exports = {
  generateGoogleLoginURL,
  handleGoogleSignIn,
};
```
