"""
Generated Code Metadata:
========================
Original URL: https://80759891.carbon-app-csq.pages.dev
Prompt: Write code to send login codes via email for user authentication, as described in the Cloudflare Access "carbon-app" setup.
Generated: DETERMINISTIC_3e82be21f0f508c3
Batch ID: 20250612_150927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Email Login Code Sender**
==========================

**Overview**
------------

This code sends login codes via email for user authentication, as described in the Cloudflare Access "carbon-app" setup.

**Requirements**
---------------

* Node.js 14+
* `nodemailer` package for sending emails

**Code**
------
```javascript
// Import required packages
const nodemailer = require('nodemailer');
const crypto = require('crypto');

// Configuration
const config = {
  // Email service configuration
  emailService: {
    host: 'smtp.gmail.com',
    port: 587,
    secure: false, // or 'STARTTLS'
    auth: {
      user: 'your-email@gmail.com',
      pass: 'your-email-password',
    },
  },
  // Login code expiration time (in minutes)
  loginCodeExpirationTime: 15,
};

// Generate a random login code
function generateLoginCode() {
  return crypto.randomBytes(6).toString('hex').toUpperCase();
}

// Send login code via email
async function sendLoginCode(email, loginCode) {
  try {
    // Create a nodemailer transporter
    const transporter = nodemailer.createTransport(config.emailService);

    // Define the email message
    const mailOptions = {
      from: config.emailService.auth.user,
      to: email,
      subject: 'Login Code for Cloudflare Access',
      text: `Your login code is: ${loginCode}`,
    };

    // Send the email
    await transporter.sendMail(mailOptions);
    console.log(`Login code sent to ${email}`);
  } catch (error) {
    console.error(`Error sending login code: ${error.message}`);
    throw error;
  }
}

// Verify login code
function verifyLoginCode(loginCode, expectedLoginCode, expirationTime) {
  // Check if the login code is valid
  if (loginCode !== expectedLoginCode) {
    return false;
  }

  // Check if the login code has expired
  const expirationDate = new Date();
  expirationDate.setMinutes(expirationDate.getMinutes() - expirationTime);
  const loginCodeGeneratedAt = new Date();
  // Assuming loginCodeGeneratedAt is stored somewhere
  // For demonstration purposes, it's assumed to be now
  loginCodeGeneratedAt.setMinutes(loginCodeGeneratedAt.getMinutes() - 5);
  if (loginCodeGeneratedAt < expirationDate) {
    return false;
  }

  return true;
}

// Example usage
async function main() {
  const email = 'user@example.com';
  const loginCode = generateLoginCode();
  await sendLoginCode(email, loginCode);

  // Verify login code
  const isValid = verifyLoginCode(loginCode, loginCode, config.loginCodeExpirationTime);
  console.log(`Is login code valid? ${isValid}`);
}

main().catch((error) => {
  console.error(`Error: ${error.message}`);
  process.exit(1);
});
```
**package.json**
```json
{
  "name": "email-login-code-sender",
  "version": "1.0.0",
  "scripts": {
    "start": "node index.js"
  },
  "dependencies": {
    "nodemailer": "^6.7.2"
  }
}
```
