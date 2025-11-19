"""
Generated Code Metadata:
========================
Original URL: https://phosphor.now.sh
Prompt: Generate a Next.js component for displaying a company's contact information, including address, email, and phone number, as seen on the Phosphor website.
Generated: DETERMINISTIC_449d8aec5e35ca12
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// components/ContactInfo.js

import React from 'react';
import PropTypes from 'prop-types';

/**
 * ContactInfo component displays the company's contact information.
 *
 * @param {Object} props - The component props.
 * @param {string} props.address - The company's address.
 * @param {string} props.email - The company's email address.
 * @param {string} props.phone - The company's phone number.
 * @returns {JSX.Element} The rendered contact information.
 */
const ContactInfo = ({ address, email, phone }) => {
  // Validate props
  if (!address || !email || !phone) {
    console.error('ContactInfo: Missing required props');
    return null; // Return null if required props are missing
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
          border: 1px solid #ccc;
          padding: 20px;
          border-radius: 5px;
          background-color: #f9f9f9;
        }
        .contact-item {
          margin-bottom: 10px;
        }
        strong {
          display: inline-block;
          margin-right: 5px;
        }
      `}</style>
    </div>
  );
};

// Prop types validation
ContactInfo.propTypes = {
  address: PropTypes.string.isRequired,
  email: PropTypes.string.isRequired,
  phone: PropTypes.string.isRequired,
};

export default ContactInfo;
```

```javascript
// pages/index.js

import React from 'react';
import ContactInfo from '../components/ContactInfo';

const HomePage = () => {
  const companyInfo = {
    address: '1234 Phosphor St, Suite 100, City, State, 12345',
    email: 'contact@phosphor.com',
    phone: '+1 (234) 567-8900',
  };

  return (
    <div>
      <h1>Welcome to Phosphor</h1>
      <ContactInfo 
        address={companyInfo.address} 
        email={companyInfo.email} 
        phone={companyInfo.phone} 
      />
    </div>
  );
};

export default HomePage;
```
