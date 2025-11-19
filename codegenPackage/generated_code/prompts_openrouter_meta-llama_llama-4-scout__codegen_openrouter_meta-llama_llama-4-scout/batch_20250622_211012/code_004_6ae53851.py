"""
Generated Code Metadata:
========================
Original URL: https://acknowledgment.netlify.app
Prompt: Design a basic contact page UI component using React, including fields for name, email, and message, and integration with an email service.
Generated: DETERMINISTIC_6ae53851dc79e8a1
Batch ID: 20250622_211012
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// ContactForm.js
import React, { useState } from 'react';
import axios from 'axios';

/**
 * Contact form component
 * 
 * @returns {JSX.Element} Contact form JSX element
 */
function ContactForm() {
  // State to store form data
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [message, setMessage] = useState('');
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(null);

  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      // Validate form data
      if (!name || !email || !message) {
        setError('Please fill out all fields.');
        return;
      }

      // Send email using email service
      const response = await axios.post('/api/send-email', {
        name,
        email,
        message,
      });

      // Handle successful email send
      if (response.status === 200) {
        setSuccess('Email sent successfully!');
        setName('');
        setEmail('');
        setMessage('');
      } else {
        setError('Error sending email. Please try again.');
      }
    } catch (error) {
      setError('Error sending email. Please try again.');
      console.error(error);
    }
  };

  return (
    <div className="contact-form">
      <h2>Contact Us</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="name">Name:</label>
          <input
            type="text"
            id="name"
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
        </div>
        <div className="form-group">
          <label htmlFor="email">Email:</label>
          <input
            type="email"
            id="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
        </div>
        <div className="form-group">
          <label htmlFor="message">Message:</label>
          <textarea
            id="message"
            value={message}
            onChange={(e) => setMessage(e.target.value)}
          />
        </div>
        {error && <p className="error">{error}</p>}
        {success && <p className="success">{success}</p>}
        <button type="submit">Send Email</button>
      </form>
    </div>
  );
}

export default ContactForm;
```

```jsx
// App.js
import React from 'react';
import ContactForm from './ContactForm';

function App() {
  return (
    <div className="app">
      <ContactForm />
    </div>
  );
}

export default App;
```

```javascript
// server.js
const express = require('express');
const nodemailer = require('nodemailer');
const app = express();
app.use(express.json());

// Email service configuration
const transporter = nodemailer.createTransport({
  host: 'smtp.gmail.com',
  port: 587,
  secure: false, // or 'STARTTLS'
  auth: {
    user: 'your-email@gmail.com',
    pass: 'your-password',
  },
});

// API endpoint to send email
app.post('/api/send-email', (req, res) => {
  const { name, email, message } = req.body;

  const mailOptions = {
    from: email,
    to: 'your-email@gmail.com',
    subject: `Contact Form Submission from ${name}`,
    text: message,
  };

  transporter.sendMail(mailOptions, (error, info) => {
    if (error) {
      console.error(error);
      res.status(500).send({ message: 'Error sending email' });
    } else {
      console.log(`Email sent: ${info.response}`);
      res.send({ message: 'Email sent successfully' });
    }
  });
});

const port = 3001;
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
```

```css
/* styles.css */
.contact-form {
  max-width: 500px;
  margin: 40px auto;
  padding: 20px;
  background-color: #f9f9f9;
  border: 1px solid #ccc;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.form-group {
  margin-bottom: 20px;
}

.form-group label {
  display: block;
  margin-bottom: 10px;
}

.form-group input,
.form-group textarea {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.error {
  color: #f00;
  font-size: 14px;
  margin-bottom: 20px;
}

.success {
  color: #0f0;
  font-size: 14px;
  margin-bottom: 20px;
}
```
