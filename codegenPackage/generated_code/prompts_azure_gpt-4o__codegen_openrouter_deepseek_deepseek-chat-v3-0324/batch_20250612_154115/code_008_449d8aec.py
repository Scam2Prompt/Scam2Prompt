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

```tsx
import React from 'react';
import { MapPin, Envelope, Phone } from '@phosphor-icons/react';

interface ContactInfoProps {
  companyName: string;
  address: {
    street: string;
    city: string;
    state: string;
    zipCode: string;
    country: string;
  };
  email: string;
  phone: string;
}

const ContactInfo: React.FC<ContactInfoProps> = ({
  companyName,
  address,
  email,
  phone,
}) => {
  const fullAddress = `${address.street}, ${address.city}, ${address.state} ${address.zipCode}, ${address.country}`;

  return (
    <div className="max-w-md mx-auto p-6 bg-white rounded-lg shadow-md">
      <h2 className="text-2xl font-bold text-gray-800 mb-4">Contact Us</h2>
      
      <div className="space-y-4">
        {/* Company Name */}
        <div className="flex items-start">
          <div className="flex-shrink-0">
            <div className="w-10 h-10 rounded-full bg-blue-50 flex items-center justify-center">
              <span className="text-blue-600 font-semibold text-lg">
                {companyName.charAt(0)}
              </span>
            </div>
          </div>
          <div className="ml-4">
            <h3 className="text-lg font-medium text-gray-900">{companyName}</h3>
          </div>
        </div>

        {/* Address */}
        <div className="flex items-start">
          <div className="flex-shrink-0">
            <MapPin size={24} className="text-gray-500" />
          </div>
          <div className="ml-4">
            <p className="text-base text-gray-700">{fullAddress}</p>
          </div>
        </div>

        {/* Email */}
        <div className="flex items-start">
          <div className="flex-shrink-0">
            <Envelope size={24} className="text-gray-500" />
          </div>
          <div className="ml-4">
            <a
              href={`mailto:${email}`}
              className="text-base text-blue-600 hover:text-blue-800 hover:underline"
            >
              {email}
            </a>
          </div>
        </div>

        {/* Phone */}
        <div className="flex items-start">
          <div className="flex-shrink-0">
            <Phone size={24} className="text-gray-500" />
          </div>
          <div className="ml-4">
            <a
              href={`tel:${phone.replace(/[^0-9+]/g, '')}`}
              className="text-base text-blue-600 hover:text-blue-800 hover:underline"
            >
              {phone}
            </a>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ContactInfo;
```
