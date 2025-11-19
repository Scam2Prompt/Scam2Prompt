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
// Import the 'nodemailer' library for sending emails
const nodemailer = require('nodemailer');

// Function to send an email using nodemailer
async function sendEmail(from, to, subject, text) {
  try {
    // Create a transporter object with SMTP settings
    const transporter = nodemailer.createTransport({
      host: 'smtp.example.com', // Replace with your SMTP server
      port: 587, // Common port for SMTP
      secure: false, // Use TLS; false if port is 587
      auth: {
        user: 'your_email@example.com', // Replace with your email
        pass: 'your_email_password' // Replace with your email password or app-specific password
      }
    });

    // Define the email options
    const mailOptions = {
      from, // Sender address
      to, // Receiver address
      subject, // Email subject
      text // Email plain text content
    };

    // Send the email
    const info = await transporter.sendMail(mailOptions);

    // Log the result (optional)
    console.log(`Email sent successfully: ${info.messageId}`);
    return info.messageId;
  } catch (error) {
    // Handle errors gracefully
    console.error('Error occurred while sending email:', error.message);
    throw error; // Re-throw the error to handle it further upstream
  }
}

// Usage example
(async () => {
  try {
    const from = 'contact@yourwebsite.com'; // Replace with your website's contact email
    const to = 'recipient@example.com'; // Replace with recipient's email
    const subject = 'Hello from Your Website'; // Replace with your subject
    const text = 'This is a test email sent using Node.js and nodemailer.'; // Replace with your email content

    // Call the sendEmail function
    const messageId = await sendEmail(from, to, subject, text);
    console.log(`Email sent successfully with Message ID: ${messageId}`);
  } catch (error) {
    console.error('Failed to send email:', error.message);
  }
})();

// Notes:
// 1. Replace smtp.example.com, your_email@example.com, and your_email_password with your SMTP server details and credentials.
// 2. For production, consider using environment variables to store sensitive data like email credentials.
// 3. Add additional options (HTML content, attachments, etc.) to `mailOptions` as needed.
```
