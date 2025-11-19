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

```javascript
import React, { useState } from 'react';
import PropTypes from 'prop-types';
import axios from 'axios';
import './ContactForm.css'; // Assuming you have some basic styles

const ContactForm = ({ apiEndpoint }) => {
  // State variables for form fields and error handling
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

    try {
      // Send the form data to the email service
      const response = await axios.post(apiEndpoint, {
        name,
        email,
        message,
      });

      // Check for successful response
      if (response.status === 200) {
        setSuccess(true);
        // Clear the form fields
        setName('');
        setEmail('');
        setMessage('');
      } else {
        setError('Failed to send message. Please try again later.');
      }
    } catch (err) {
      // Handle errors from the API
      setError('An error occurred while sending your message. Please try again later.');
      console.error('Error sending message:', err);
    }
  };

  return (
    <div className="contact-form">
      <h2>Contact Us</h2>
      {error && <div className="error">{error}</div>}
      {success && <div className="success">Message sent successfully!</div>}
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="name">Name:</label>
          <input
            type="text"
            id="name"
            value={name}
            onChange={(e) => setName(e.target.value)}
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="email">Email:</label>
          <input
            type="email"
            id="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </div>
        <div className="form-group">
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
    </div>
  );
};

// PropTypes for type checking
ContactForm.propTypes = {
  apiEndpoint: PropTypes.string.isRequired,
};

export default ContactForm;
```

```css
/* ContactForm.css */
.contact-form {
  max-width: 400px;
  margin: auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #f9f9f9;
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
}

input, textarea {
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

button {
  padding: 10px 15px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}

.error {
  color: red;
  margin-bottom: 15px;
}

.success {
  color: green;
  margin-bottom: 15px;
}
```
