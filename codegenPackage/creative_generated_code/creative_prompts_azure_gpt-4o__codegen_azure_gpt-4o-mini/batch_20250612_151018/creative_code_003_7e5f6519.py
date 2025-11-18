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
// Import necessary packages
const express = require('express');
const nodemailer = require('nodemailer');
const bodyParser = require('body-parser');
const crypto = require('crypto');

// Create an instance of the Express app
const app = express();

// Middleware to parse JSON bodies
app.use(bodyParser.json());

// Configuration for the email transporter
const transporter = nodemailer.createTransport({
    service: 'Gmail', // Use your email service provider
    auth: {
        user: process.env.EMAIL_USER, // Your email address
        pass: process.env.EMAIL_PASS, // Your email password or app-specific password
    },
});

// Endpoint to send login code
app.post('/send-login-code', async (req, res) => {
    const { email } = req.body;

    // Validate request body
    if (!email) {
        return res.status(400).json({ error: 'Email is required.' });
    }

    // Generate a six-digit code for authentication
    const code = Math.floor(100000 + Math.random() * 900000).toString();

    // Setup email data
    const mailOptions = {
        from: process.env.EMAIL_USER,
        to: email,
        subject: 'Your Login Code',
        text: `Your login code is: ${code}`,
    };

    try {
        // Send the email
        await transporter.sendMail(mailOptions);
        // Ideally, you would store `code` in a secure session store or database associated with the email
        // Here, we just return the code for demonstration purposes (do not do this in production)
        return res.status(200).json({ message: 'Login code sent successfully.', code });
    } catch (error) {
        console.error('Error sending email:', error);
        return res.status(500).json({ error: 'Failed to send login code. Please try again later.' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

### .env
```plaintext
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_app_specific_password
```

### Dependencies (package.json)
```json
{
  "name": "email-auth",
  "version": "1.0.0",
  "description": "A simple email-based login code authentication.",
  "main": "index.js",
  "scripts": {
    "start": "node index.js"
  },
  "dependencies": {
    "express": "^4.17.1",
    "nodemailer": "^6.4.18",
    "body-parser": "^1.19.0"
  }
}
```

### Usage
1. Ensure you have Node.js installed.
2. Set up your environment variables in a `.env` file.
3. Install dependencies: `npm install`
4. Start the server: `npm start`
5. Send a POST request to `/send-login-code` with the email in the body.
