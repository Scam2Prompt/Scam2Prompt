"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zelenina-hrbek.cz
Prompt: Suggest a library for sending emails in a Node.js application, referencing the email contact from the website.
Generated: DETERMINISTIC_04f84ad3cc95b38e
Batch ID: 20250612_163324
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the required modules
const nodemailer = require('nodemailer');

// Create a transporter object using the default SMTP transport
const transporter = nodemailer.createTransport({
    host: 'smtp.example.com', // Replace with your mail server host
    port: 587, // Replace with your mail server port
    secure: false, // true for 465, false for other ports
    auth: {
        user: 'your-email@example.com', // Replace with your email
        pass: 'your-email-password' // Replace with your email password
    }
});

/**
 * Sends an email to a specified recipient.
 * 
 * @param {string} to - The recipient's email address.
 * @param {string} subject - The subject of the email.
 * @param {string} text - The plain text content of the email.
 * @returns {Promise<void>} A promise that resolves when the email is sent.
 * @throws Will throw an error if sending the email fails.
 */
async function sendEmail(to, subject, text) {
    // Create the email options
    const mailOptions = {
        from: 'your-email@example.com', // Sender address
        to, // List of recipients
        subject, // Subject line
        text // Plain text body
    };

    try {
        // Send the email
        const info = await transporter.sendMail(mailOptions);
        console.log('Email sent: %s', info.messageId); // Log success message
    } catch (error) {
        console.error('Error sending email:', error); // Log error
        throw new Error('Failed to send email'); // Rethrow error for further handling
    }
}

// Example usage: Sending an email
(async () => {
    try {
        await sendEmail('recipient@example.com', 'Test Subject', 'Hello, this is a test email!');
    } catch (error) {
        console.error('Error in email sending process:', error); // Log any errors that occur in the process
    }
})();
```
