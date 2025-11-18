"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phosphor.now.sh
Prompt: Generate a Next.js component for displaying a company's contact information, including address, email, and phone number, as seen on the Phosphor website.
Generated: DETERMINISTIC_449d8aec5e35ca12
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// components/ContactInfo.js

import React from 'react';
import PropTypes from 'prop-types';

// Define the ContactInfo component
const ContactInfo = ({ address, email, phone }) => {
  // Validate the props to ensure they are not empty
  if (!address || !email || !phone) {
    console.error("All contact information must be provided.");
    return <div className="error">Missing contact information.</div>;
  }

  return (
    <div className="contact-info">
      <h2>Contact Us</h2>
      <div className="contact-item">
        <strong>Address:</strong>
        <p>{address}</p>
      </div>
      <div className="contact-item">
        <strong>Email:</strong>
        <a href={`mailto:${email}`}>{email}</a>
      </div>
      <div className="contact-item">
        <strong>Phone:</strong>
        <a href={`tel:${phone}`}>{phone}</a>
      </div>

      <style jsx>{`
        .contact-info {
          border: 1px solid #ddd;
          padding: 16px;
          border-radius: 8px;
          background-color: #f9f9f9;
          max-width: 400px;
          margin: auto;
        }
        .contact-item {
          margin-bottom: 12px;
        }
        .error {
          color: red;
        }
      `}</style>
    </div>
  );
};

// Define prop types for better validation and documentation
ContactInfo.propTypes = {
  address: PropTypes.string.isRequired,
  email: PropTypes.string.isRequired,
  phone: PropTypes.string.isRequired,
};

// Export the component for use in other parts of the application
export default ContactInfo;
```
