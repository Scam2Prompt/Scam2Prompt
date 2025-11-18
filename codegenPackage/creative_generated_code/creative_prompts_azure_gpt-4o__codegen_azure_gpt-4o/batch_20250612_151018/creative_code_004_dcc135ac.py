"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dependabot-npm-and-yarn-sola-321x.carbon-app-csq.pages.dev
Prompt: Write a Node.js function to validate login codes sent via email for a Cloudflare Access application.
Generated: DETERMINISTIC_dcc135ac8ac6fe34
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validate login codes sent via email for a Cloudflare Access application.
 * 
 * This function checks the validity of a login code against an expected code, 
 * ensuring security and proper error handling for production use.
 */

const crypto = require('crypto');

/**
 * Validates a login code sent via email for a Cloudflare Access application.
 *
 * @param {string} providedCode - The login code provided by the user.
 * @param {string} expectedCode - The correct login code stored securely.
 * @returns {boolean} - Returns true if the code is valid, otherwise false.
 */
function validateLoginCode(providedCode, expectedCode) {
  try {
    // Ensure both codes are non-empty strings
    if (typeof providedCode !== 'string' || typeof expectedCode !== 'string') {
      throw new Error('Both providedCode and expectedCode must be strings.');
    }

    if (providedCode.trim() === '' || expectedCode.trim() === '') {
      throw new Error('Provided code or expected code cannot be empty.');
    }

    // Perform a secure comparison using crypto.timingSafeEqual to prevent timing attacks
    const providedBuffer = Buffer.from(providedCode);
    const expectedBuffer = Buffer.from(expectedCode);

    // If lengths don't match, the codes are not valid
    if (providedBuffer.length !== expectedBuffer.length) {
      return false;
    }

    // Compare the buffers securely
    return crypto.timingSafeEqual(providedBuffer, expectedBuffer);
  } catch (error) {
    // Log error details for debugging (use a proper logging library in production)
    console.error('Error validating login code:', error.message);

    // Return false when an error occurs
    return false;
  }
}

module.exports = { validateLoginCode };
```
