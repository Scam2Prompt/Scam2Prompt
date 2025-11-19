"""
Generated Code Metadata:
========================
Original URL: https://phosphor.now.sh
Prompt: Write a Next.js code snippet for creating a contact form with fields for name, email, and message, similar to the contact form described on the Phosphor website.
Generated: DETERMINISTIC_bd8512cefb0b8a60
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// components/ContactForm.js
import React, { useState } from 'react';
import axios from 'axios';

/**
 * Contact form component
 * 
 * @returns {JSX.Element} Contact form JSX element
 */
const ContactForm = () => {
  // Form state
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [message, setMessage] = useState('');
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(null);

  // Handle form submission
  const handleSubmit = async (event) => {
    event.preventDefault();
    setIsSubmitting(true);
    setError(null);
    setSuccess(null);

    try {
      // Send form data to API endpoint
      const response = await axios.post('/api/contact', {
        name,
        email,
        message,
      });

      // Check if the response was successful
      if (response.status === 200) {
        setSuccess('Message sent successfully!');
        setName('');
        setEmail('');
        setMessage('');
      } else {
        setError('Failed to send message. Please try again.');
      }
    } catch (error) {
      setError('Failed to send message. Please try again.');
      console.error(error);
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Name:
        <input
          type="text"
          value={name}
          onChange={(event) => setName(event.target.value)}
          required
        />
      </label>
      <br />
      <label>
        Email:
        <input
          type="email"
          value={email}
          onChange={(event) => setEmail(event.target.value)}
          required
        />
      </label>
      <br />
      <label>
        Message:
        <textarea
          value={message}
          onChange={(event) => setMessage(event.target.value)}
          required
        />
      </label>
      <br />
      <button type="submit" disabled={isSubmitting}>
        {isSubmitting ? 'Submitting...' : 'Send Message'}
      </button>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {success && <p style={{ color: 'green' }}>{success}</p>}
    </form>
  );
};

export default ContactForm;
```

```jsx
// pages/index.js
import ContactForm from '../components/ContactForm';

const HomePage = () => {
  return (
    <div>
      <h1>Contact Us</h1>
      <ContactForm />
    </div>
  );
};

export default HomePage;
```

```javascript
// pages/api/contact.js
import nodemailer from 'nodemailer';

const contactHandler = async (req, res) => {
  // Check if the request method is POST
  if (req.method !== 'POST') {
    return res.status(405).json({ message: 'Method not allowed' });
  }

  // Check if the form data is present
  if (!req.body.name || !req.body.email || !req.body.message) {
    return res.status(400).json({ message: 'Please fill all fields' });
  }

  try {
    // Send email using nodemailer
    const transporter = nodemailer.createTransport({
      host: process.env.EMAIL_HOST,
      port: process.env.EMAIL_PORT,
      auth: {
        user: process.env.EMAIL_USER,
        pass: process.env.EMAIL_PASSWORD,
      },
    });

    const mailOptions = {
      from: req.body.email,
      to: process.env.RECEIVER_EMAIL,
      subject: 'New message from contact form',
      text: `
        Name: ${req.body.name}
        Email: ${req.body.email}
        Message: ${req.body.message}
      `,
    };

    await transporter.sendMail(mailOptions);
    res.status(200).json({ message: 'Message sent successfully' });
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Failed to send message' });
  }
};

export default contactHandler;
```

```makefile
# .env
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USER=your-email@gmail.com
EMAIL_PASSWORD=your-email-password
RECEIVER_EMAIL=receiver-email@gmail.com
```
