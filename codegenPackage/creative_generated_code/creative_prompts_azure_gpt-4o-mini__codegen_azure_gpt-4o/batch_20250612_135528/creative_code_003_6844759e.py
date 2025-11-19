"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://questsmisten.space
Prompt: What libraries can help manage user data privacy in a JavaScript application?
Generated: DETERMINISTIC_6844759e0cadc409
Batch ID: 20250612_135528
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
// `crypto-js` for encryption, `dotenv` for environment variable management,
// and `cookies` for secure cookie handling

const CryptoJS = require("crypto-js");
require("dotenv").config();
const Cookies = require("cookies");

// Environment variables should include `ENCRYPTION_SECRET` for key management
const encryptionSecret = process.env.ENCRYPTION_SECRET;

if (!encryptionSecret) {
  throw new Error("ENCRYPTION_SECRET is not defined in environment variables.");
}

/**
 * Encrypts sensitive user data using AES encryption.
 * @param {string} data - The data to be encrypted.
 * @returns {string} - Encrypted data.
 */
function encryptData(data) {
  try {
    return CryptoJS.AES.encrypt(data, encryptionSecret).toString();
  } catch (error) {
    console.error("Error encrypting data:", error);
    throw new Error("Failed to encrypt data.");
  }
}

/**
 * Decrypts sensitive user data.
 * @param {string} encryptedData - The encrypted data to be decrypted.
 * @returns {string} - Decrypted data.
 */
function decryptData(encryptedData) {
  try {
    const bytes = CryptoJS.AES.decrypt(encryptedData, encryptionSecret);
    return bytes.toString(CryptoJS.enc.Utf8);
  } catch (error) {
    console.error("Error decrypting data:", error);
    throw new Error("Failed to decrypt data.");
  }
}

/**
 * Sets a secure cookie for the user.
 * @param {object} req - The HTTP request object.
 * @param {object} res - The HTTP response object.
 * @param {string} cookieName - The name of the cookie.
 * @param {string} cookieValue - The value of the cookie.
 */
function setSecureCookie(req, res, cookieName, cookieValue) {
  try {
    const cookies = new Cookies(req, res);
    cookies.set(cookieName, cookieValue, {
      httpOnly: true, // Protect against XSS
      secure: true, // Require HTTPS
      sameSite: "Strict", // Prevent CSRF
    });
  } catch (error) {
    console.error("Error setting secure cookie:", error);
    throw new Error("Failed to set secure cookie.");
  }
}

/**
 * Retrieves a secure cookie value.
 * @param {object} req - The HTTP request object.
 * @param {object} res - The HTTP response object.
 * @param {string} cookieName - The name of the cookie.
 * @returns {string|null} - The value of the cookie or null if not found.
 */
function getSecureCookie(req, res, cookieName) {
  try {
    const cookies = new Cookies(req, res);
    return cookies.get(cookieName);
  } catch (error) {
    console.error("Error retrieving cookie:", error);
    throw new Error("Failed to retrieve cookie value.");
  }
}

// Example Usage

// Encrypt and Decrypt Example
const sensitiveInfo = "user-password-123";
const encrypted = encryptData(sensitiveInfo);
console.log("Encrypted Data:", encrypted);

const decrypted = decryptData(encrypted);
console.log("Decrypted Data:", decrypted);

// Cookie Example
// Assume `req` and `res` are available from an HTTP server
// setSecureCookie(req, res, "sessionToken", encrypted);
// const sessionToken = getSecureCookie(req, res, "sessionToken");
// console.log("Session Token:", sessionToken);
```

**Dependencies:**  
Ensure to install the required libraries using npm:
```bash
npm install crypto-js dotenv cookies
```
