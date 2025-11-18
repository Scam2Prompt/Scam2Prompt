"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phosphor.now.sh
Prompt: Write a Next.js code snippet for creating a contact form with fields for name, email, and message, similar to the contact form described on the Phosphor website.
Generated: DETERMINISTIC_bd8512cefb0b8a60
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// pages/contact.js

import { useState } from 'react';

// ContactForm component for user input
const ContactForm = () => {
  // State variables for form fields
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [message, setMessage] = useState('');
  const [error, setError] = useState('');
  const [success, setSuccess] = useState(false);

  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setSuccess(false);

    // Basic validation
    if (!name || !email || !message) {
      setError('All fields are required.');
      return;
    }

    // Prepare data for submission
    const formData = { name, email, message };

    try {
      const response = await fetch('/api/contact', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      // Check for HTTP errors
      if (!response.ok) {
        throw new Error('Failed to send the message. Please try again later.');
      }

      // Reset form fields on success
      setName('');
      setEmail('');
      setMessage('');
      setSuccess(true);
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <div className="contact-form">
      <h2>Contact Us</h2>
      {error && <p className="error">{error}</p>}
      {success && <p className="success">Message sent successfully!</p>}
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="name">Name:</label>
          <input
            type="text"
            id="name"
            value={name}
            onChange={(e) => setName(e.target.value)}
            required
          />
        </div>
        <div>
          <label htmlFor="email">Email:</label>
          <input
            type="email"
            id="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </div>
        <div>
          <label htmlFor="message">Message:</label>
          <textarea
            id="message"
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            required
          />
        </div>
        <button type="submit">Send Message</button>
      </form>
      <style jsx>{`
        .contact-form {
          max-width: 400px;
          margin: auto;
          padding: 1rem;
          border: 1px solid #ccc;
          border-radius: 5px;
        }
        .error {
          color: red;
        }
        .success {
          color: green;
        }
        div {
          margin-bottom: 1rem;
        }
        label {
          display: block;
          margin-bottom: 0.5rem;
        }
        input, textarea {
          width: 100%;
          padding: 0.5rem;
          border: 1px solid #ccc;
          border-radius: 5px;
        }
        button {
          padding: 0.5rem 1rem;
          background-color: #0070f3;
          color: white;
          border: none;
          border-radius: 5px;
          cursor: pointer;
        }
        button:hover {
          background-color: #005bb5;
        }
      `}</style>
    </div>
  );
};

// Export the ContactForm component
export default ContactForm;

// API route to handle form submission
// pages/api/contact.js

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { name, email, message } = req.body;

  // You can add your email sending logic here
  // For demonstration, we just log the data to the console
  console.log('Contact Form Submission:', { name, email, message });

  // Respond with a success message
  res.status(200).json({ message: 'Message received!' });
}
```
