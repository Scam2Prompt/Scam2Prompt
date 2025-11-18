"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dependabot-npm-and-yarn-sola.carbon-app-csq.pages.dev
Prompt: Write code to send an email-based login code for authentication in a web app that uses Dependabot for npm and Yarn dependency updates.
Generated: DETERMINISTIC_7e5f6519e7caeb04
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
const nodemailer = require('nodemailer'); // For sending emails
const crypto = require('crypto'); // For generating secure random codes
const dotenv = require('dotenv'); // For managing environment variables

// Load environment variables from .env file
dotenv.config();

// Validate required environment variables
if (!process.env.SMTP_HOST || !process.env.SMTP_PORT || !process.env.SMTP_USER || !process.env.SMTP_PASS || !process.env.EMAIL_FROM) {
  throw new Error("Missing required environment variables for SMTP configuration.");
}

// Function to generate a random authentication code
const generateAuthCode = () => {
  return crypto.randomBytes(3).toString('hex').toUpperCase(); // Generates a 6-character hexadecimal code
};

// Configure the SMTP transporter
const transporter = nodemailer.createTransport({
  host: process.env.SMTP_HOST,
  port: parseInt(process.env.SMTP_PORT, 10),
  secure: process.env.SMTP_PORT === "465", // Use TLS if port is 465
  auth: {
    user: process.env.SMTP_USER,
    pass: process.env.SMTP_PASS
  }
});

// Function to send the email with the authentication code
const sendLoginCodeEmail = async (recipientEmail) => {
  try {
    // Validate recipient email
    if (!recipientEmail || !recipientEmail.includes('@')) {
      throw new Error("Invalid recipient email address.");
    }

    const authCode = generateAuthCode(); // Generate the login code

    // Email content
    const mailOptions = {
      from: process.env.EMAIL_FROM, // Sender address
      to: recipientEmail, // Recipient address
      subject: "Your Login Code", // Email subject
      text: `Your login code is: ${authCode}\n\nThis code will expire in 10 minutes.`, // Plain text body
      html: `<p>Your login code is: <strong>${authCode}</strong></p><p>This code will expire in 10 minutes.</p>` // HTML body
    };

    // Send the email
    await transporter.sendMail(mailOptions);

    console.log(`Authentication email sent successfully to ${recipientEmail}. Code: ${authCode}`);

    // Return the code for further processing (e.g., storing it for verification)
    return authCode;
  } catch (error) {
    console.error("Error sending email:", error.message);
    throw error; // Re-throw the error for handling upstream
  }
};

// Example usage
(async () => {
  try {
    const recipientEmail = "user@example.com"; // Replace with the actual recipient's email
    const loginCode = await sendLoginCodeEmail(recipientEmail);
    console.log(`Generated Login Code for ${recipientEmail}:`, loginCode);
  } catch (error) {
    console.error("Failed to send login code email:", error.message);
  }
})();
```

**Dependency Note:** Ensure the following npm packages are installed:
```bash
npm install nodemailer crypto dotenv
```

**Environment Configuration (`.env` file):**
```plaintext
SMTP_HOST=your-smtp-host
SMTP_PORT=your-smtp-port
SMTP_USER=your-smtp-username
SMTP_PASS=your-smtp-password
EMAIL_FROM=your-email-address
```
