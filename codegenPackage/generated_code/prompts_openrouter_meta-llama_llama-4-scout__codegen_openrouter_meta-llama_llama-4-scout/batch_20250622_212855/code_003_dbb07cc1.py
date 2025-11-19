"""
Generated Code Metadata:
========================
Original URL: https://teslax.in
Prompt: Design a basic backend API using Node.js and Express to handle form submissions similar to the one on teslax.in, including validation and sending emails.
Generated: DETERMINISTIC_dbb07cc17d72efcf
Batch ID: 20250622_212855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**dependencies:**

*   express: ^4.17.1
*   nodemailer: ^6.7.2
*   joi: ^17.6.0
*   dotenv: ^16.0.3

**index.js**
```javascript
// Import required modules
require('dotenv').config();
const express = require('express');
const Joi = require('joi');
const nodemailer = require('nodemailer');

// Initialize Express app
const app = express();
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Define validation schema
const validationSchema = Joi.object({
    name: Joi.string().required().min(2).max(50),
    email: Joi.string().required().email(),
    phone: Joi.string().required().min(10).max(15),
    message: Joi.string().required().min(10).max(200),
});

// Define email transporter
const transporter = nodemailer.createTransport({
    host: process.env.EMAIL_HOST,
    port: process.env.EMAIL_PORT,
    secure: process.env.EMAIL_SECURE === 'true',
    auth: {
        user: process.env.EMAIL_USER,
        pass: process.env.EMAIL_PASSWORD,
    },
});

// API endpoint to handle form submissions
app.post('/submit', async (req, res) => {
    try {
        // Validate incoming request data
        const { error } = validationSchema.validate(req.body);
        if (error) {
            return res.status(400).json({ message: error.details[0].message });
        }

        // Extract validated data
        const { name, email, phone, message } = req.body;

        // Prepare email message
        const mailOptions = {
            from: email,
            to: process.env.RECEIVER_EMAIL,
            subject: 'New Form Submission',
            text: `
                Name: ${name}
                Email: ${email}
                Phone: ${phone}
                Message: ${message}
            `,
        };

        // Send email using transporter
        await transporter.sendMail(mailOptions);

        // Return success response
        res.json({ message: 'Form submitted successfully!' });
    } catch (error) {
        console.error(error);
        res.status(500).json({ message: 'Internal Server Error' });
    }
});

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server listening on port ${PORT}`);
});
```

**.env**
```makefile
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_SECURE=false
EMAIL_USER=your-email@gmail.com
EMAIL_PASSWORD=your-email-password
RECEIVER_EMAIL=receiver-email@example.com
```

**package.json**
```json
{
  "name": "tesla-form-backend",
  "version": "1.0.0",
  "scripts": {
    "start": "node index.js"
  },
  "dependencies": {
    "dotenv": "^16.0.3",
    "express": "^4.17.1",
    "joi": "^17.6.0",
    "nodemailer": "^6.7.2"
  }
}
```
