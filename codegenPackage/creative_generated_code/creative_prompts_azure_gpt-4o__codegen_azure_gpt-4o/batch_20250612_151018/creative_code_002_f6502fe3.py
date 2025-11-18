"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dependabot-npm-and-yarn-sola-321x.carbon-app-csq.pages.dev
Prompt: Generate a script using JavaScript to send login codes via email for a Cloudflare Access-based authentication system.
Generated: DETERMINISTIC_f6502fe36b9ee285
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const nodemailer = require('nodemailer');
const crypto = require('crypto');

// Configuration for email transport
// Replace these placeholder values with your actual email credentials
const emailConfig = {
  host: "smtp.example.com", // SMTP server
  port: 587,               // SMTP port (often 587 for TLS)
  secure: false,           // Use TLS (false because we're specifying port 587)
  auth: {
    user: "your_email@example.com", // Sender email address
    pass: "your_email_password"     // Sender email password
  }
};

// Create a reusable SMTP transport object
const transporter = nodemailer.createTransport(emailConfig);

/**
 * Generates a random login code.
 * @return {string} A random, secure code string.
 */
function generateLoginCode() {
  // Generate a random 6-digit numeric code
  return crypto.randomInt(100000, 999999).toString();
}

/**
 * Sends a login code via email.
 * @param {string} recipientEmail - The recipient's email address.
 * @param {string} loginCode - The login code to send.
 * @return {Promise<void>} Resolves when the email is successfully sent.
 */
async function sendLoginCode(recipientEmail, loginCode) {
  // Email content configuration
  const mailOptions = {
    from: '"Cloudflare Access Auth" <your_email@example.com>', // Sender (From)
    to: recipientEmail, // Recipient (To)
    subject: "Your Cloudflare Access Login Code", // Email Subject
    text: `Your login code is: ${loginCode}`, // Plain-text content
    html: `<p>Your login code is: <strong>${loginCode}</strong></p>` // HTML content
  };

  try {
    // Send the email and await the result
    await transporter.sendMail(mailOptions);
    console.log(`Login code sent to ${recipientEmail}.`);
  } catch (err) {
    // Log the error and rethrow it
    console.error(`Failed to send email to ${recipientEmail}:`, err.message);
    throw new Error("Error sending login code email.");
  }
}

/**
 * Main function to initiate login code sending process.
 * Replace the recipientEmail with the actual email address you want to send the code to.
 */
async function main() {
  const recipientEmail = "recipient@example.com"; // Replace with actual recipient email
  const loginCode = generateLoginCode(); // Generate a random login code

  console.log(`Generated login code: ${loginCode}`);
  
  try {
    // Send the login code via email
    await sendLoginCode(recipientEmail, loginCode);
    console.log("Login code successfully sent.");
  } catch (err) {
    console.error("An error occurred while sending the login code:", err.message);
  }
}

// Execute the main function
main();
```
