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

```javascript
// pages/contact.js

import { useState } from 'react';

// ContactForm component for handling user input
const ContactForm = () => {
  // State variables for form fields and submission status
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [message, setMessage] = useState('');
  const [status, setStatus] = useState('');

  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault(); // Prevent default form submission behavior

    // Basic validation
    if (!name || !email || !message) {
      setStatus('Please fill in all fields.');
      return;
    }

    // Prepare data for submission
    const formData = { name, email, message };

    try {
      // Send form data to the server
      const response = await fetch('/api/contact', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      // Check for successful response
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      // Clear form fields and update status
      setName('');
      setEmail('');
      setMessage('');
      setStatus('Message sent successfully!');
    } catch (error) {
      // Handle errors during submission
      setStatus(`Error: ${error.message}`);
    }
  };

  return (
    <div>
      <h1>Contact Us</h1>
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
      {status && <p>{status}</p>} {/* Display submission status */}
    </div>
  );
};

export default ContactForm;

// pages/api/contact.js

// API route for handling contact form submissions
export default async function handler(req, res) {
  if (req.method === 'POST') {
    const { name, email, message } = req.body;

    // Basic validation
    if (!name || !email || !message) {
      return res.status(400).json({ error: 'All fields are required.' });
    }

    // Here you would typically send the data to a database or an email service
    // For demonstration, we will just log it to the console
    console.log('Contact Form Submission:', { name, email, message });

    // Respond with success
    return res.status(200).json({ message: 'Message received!' });
  } else {
    // Handle any other HTTP method
    res.setHeader('Allow', ['POST']);
    return res.status(405).end(`Method ${req.method} Not Allowed`);
  }
}
```
