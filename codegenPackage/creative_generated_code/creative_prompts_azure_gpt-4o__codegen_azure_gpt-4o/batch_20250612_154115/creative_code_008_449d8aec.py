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

// A reusable Next.js functional component for displaying company contact information
const ContactInfo = ({ companyName, address, email, phoneNumber }) => {
  // Render the contact information in a clear and accessible layout
  return (
    <div className="contact-info">
      {/* Company name */}
      <h2 className="company-name">{companyName}</h2>
      
      {/* Address */}
      <div className="address">
        <h3>Address:</h3>
        <p>{address}</p>
      </div>
      
      {/* Email */}
      <div className="email">
        <h3>Email:</h3>
        <p>
          <a href={`mailto:${email}`} className="email-link">
            {email}
          </a>
        </p>
      </div>
      
      {/* Phone number */}
      <div className="phone-number">
        <h3>Phone:</h3>
        <p>
          <a href={`tel:${phoneNumber}`} className="phone-link">
            {phoneNumber}
          </a>
        </p>
      </div>

      {/* Optional styling */}
      <style jsx>{`
        .contact-info {
          border: 1px solid #ccc;
          border-radius: 8px;
          padding: 16px;
          max-width: 400px;
          margin: 0 auto;
          font-family: Arial, sans-serif;
        }

        .company-name {
          font-size: 24px;
          margin-bottom: 16px;
        }

        h3 {
          margin: 8px 0;
          font-size: 18px;
        }

        p {
          margin: 4px 0;
          font-size: 16px;
        }

        .email-link,
        .phone-link {
          text-decoration: none;
          color: #0070f3;
        }

        .email-link:hover,
        .phone-link:hover {
          text-decoration: underline;
        }
      `}</style>
    </div>
  );
};

export default ContactInfo;

// Usage Example:
// Import this component in a Next.js page or another component and pass the necessary props:
// <ContactInfo 
//   companyName="Phosphor Inc." 
//   address="123 Main Street, San Francisco, CA, USA" 
//   email="contact@phosphor.com" 
//   phoneNumber="+1 (123) 456-7890" 
// />
```
