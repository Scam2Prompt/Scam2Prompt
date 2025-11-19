"""
Generated Code Metadata:
========================
Original URL: https://amalfihospicecare.com
Prompt: Write a Node.js function to send automated support messages to hospice care patients and their families, inspired by Amalfi Hospice Care's commitment to compassion and dignity.
Generated: DETERMINISTIC_5383b992b248cd0b
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const nodemailer = require('nodemailer');
const dotenv = require('dotenv');

// Load environment variables from .env file
dotenv.config();

/**
 * Sends automated support messages to hospice care patients and their families.
 * @param {string} recipientEmail - The email address of the recipient.
 * @param {string} recipientName - The name of the recipient.
 * @param {string} messageType - The type of message to send (e.g., "patient", "family").
 * @returns {Promise<void>} - Resolves when the email is successfully sent.
 */
async function sendSupportMessage(recipientEmail, recipientName, messageType) {
  try {
    // Validate input parameters
    if (!recipientEmail || !recipientName || !messageType) {
      throw new Error('Invalid input: recipientEmail, recipientName, and messageType are required.');
    }

    // Define message templates
    const messages = {
      patient: `Dear ${recipientName},\n\nWe are here to support you during this time. Please know that you are not alone, and we are committed to providing compassionate care and dignity.\n\nWarm regards,\nAmalfi Hospice Care`,
      family: `Dear ${recipientName},\n\nWe understand the challenges you may be facing as you support your loved one. Please know that we are here for you and your family, offering compassion and guidance every step of the way.\n\nWarm regards,\nAmalfi Hospice Care`,
    };

    // Select the appropriate message based on the messageType
    const emailBody = messages[messageType];
    if (!emailBody) {
      throw new Error('Invalid messageType: must be "patient" or "family".');
    }

    // Create a transporter object using SMTP
    const transporter = nodemailer.createTransport({
      host: process.env.SMTP_HOST,
      port: parseInt(process.env.SMTP_PORT, 10),
      secure: process.env.SMTP_SECURE === 'true', // true for 465, false for other ports
      auth: {
        user: process.env.SMTP_USER, // SMTP username
        pass: process.env.SMTP_PASS, // SMTP password
      },
    });

    // Define email options
    const mailOptions = {
      from: `"Amalfi Hospice Care" <${process.env.SMTP_USER}>`, // Sender address
      to: recipientEmail, // Recipient address
      subject: 'Support Message from Amalfi Hospice Care', // Subject line
      text: emailBody, // Plain text body
    };

    // Send the email
    await transporter.sendMail(mailOptions);

    console.log(`Support message sent successfully to ${recipientEmail}`);
  } catch (error) {
    // Log and rethrow the error for further handling
    console.error(`Failed to send support message: ${error.message}`);
    throw error;
  }
}

// Example usage
(async () => {
  try {
    await sendSupportMessage('example@example.com', 'John Doe', 'patient');
  } catch (error) {
    console.error('Error:', error.message);
  }
})();

```

**Note:** Ensure you have a `.env` file with the following variables configured:
```
SMTP_HOST=smtp.example.com
SMTP_PORT=465
SMTP_SECURE=true
SMTP_USER=your-email@example.com
SMTP_PASS=your-email-password
```
