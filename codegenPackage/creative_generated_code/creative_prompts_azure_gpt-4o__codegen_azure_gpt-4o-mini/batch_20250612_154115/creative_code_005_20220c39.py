"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phosphor.now.sh
Prompt: Write a function in JavaScript to send form data via email, using the contact email provided on the Phosphor website.
Generated: DETERMINISTIC_20220c3961e9a0f1
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing necessary libraries
const nodemailer = require('nodemailer');

// Function to send form data via email
/**
 * Sends an email with the provided form data.
 * 
 * @param {Object} formData - The form data to be sent in the email.
 * @param {string} contactEmail - The email address to send the form data to.
 * @returns {Promise<void>} - A promise that resolves when the email is sent.
 * @throws {Error} - Throws an error if the email fails to send.
 */
async function sendFormDataViaEmail(formData, contactEmail) {
    // Validate email format
    if (!validateEmail(contactEmail)) {
        throw new Error('Invalid email format.');
    }

    // Create a transporter object using SMTP
    const transporter = nodemailer.createTransport({
        service: 'gmail', // Example using Gmail
        auth: {
            user: process.env.EMAIL_USER, // Your email address
            pass: process.env.EMAIL_PASS, // Your email password
        },
    });

    // Email content
    const mailOptions = {
        from: process.env.EMAIL_USER,
        to: contactEmail,
        subject: 'New Form Submission',
        text: JSON.stringify(formData, null, 2), // Sending form data as a string
    };

    try {
        // Send the email
        await transporter.sendMail(mailOptions);
        console.log('Email sent successfully');
    } catch (error) {
        console.error('Error sending email:', error);
        throw new Error('Failed to send email. Please try again later.');
    }
}

/**
 * Validates the email format using a regular expression.
 * 
 * @param {string} email - The email address to validate.
 * @returns {boolean} - Returns true if the email format is valid, otherwise false.
 */
function validateEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

// Example usage
const formData = {
    name: 'John Doe',
    email: 'john.doe@example.com',
    message: 'Hello, I would like more information about your services.',
};

const contactEmail = 'contact@phosphor.com'; // Contact email from Phosphor website

sendFormDataViaEmail(formData, contactEmail)
    .then(() => {
        console.log('Form data sent successfully.');
    })
    .catch((error) => {
        console.error('Error:', error.message);
    });
```

**Note**: Make sure to set your environment variables (`EMAIL_USER` and `EMAIL_PASS`) with your email credentials before running the code.
