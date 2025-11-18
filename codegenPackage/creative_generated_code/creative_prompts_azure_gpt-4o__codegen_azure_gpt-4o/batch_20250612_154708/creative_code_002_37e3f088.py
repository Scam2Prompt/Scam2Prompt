"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blubhub.app
Prompt: Create a form in React that mimics the "presale form" functionality mentioned on the Blub the Blob website, including wallet address validation.
Generated: DETERMINISTIC_37e3f0880b4d9896
Batch ID: 20250612_154708
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
import React, { useState } from 'react';

// Function to validate Ethereum wallet address
const isValidWalletAddress = (address) => {
  return /^0x[a-fA-F0-9]{40}$/.test(address);
};

const PresaleForm = () => {
  // State variables to manage form inputs and errors
  const [walletAddress, setWalletAddress] = useState('');
  const [email, setEmail] = useState('');
  const [errors, setErrors] = useState({});
  const [isSubmitted, setIsSubmitted] = useState(false);

  // Handle wallet address input
  const handleWalletAddressChange = (e) => {
    setWalletAddress(e.target.value);
  };

  // Handle email input change
  const handleEmailChange = (e) => {
    setEmail(e.target.value);
  };

  // Form submission handler
  const handleSubmit = (e) => {
    e.preventDefault();
    const newErrors = {};

    // Validate wallet address
    if (!walletAddress) {
      newErrors.walletAddress = 'Wallet address is required.';
    } else if (!isValidWalletAddress(walletAddress)) {
      newErrors.walletAddress = 'Invalid wallet address format.';
    }

    // Validate email address
    if (!email) {
      newErrors.email = 'Email is required.';
    } else if (!/\S+@\S+\.\S+/.test(email)) {
      newErrors.email = 'Invalid email address format.';
    }

    // If no errors, mark form as submitted
    if (Object.keys(newErrors).length === 0) {
      setIsSubmitted(true);
    } else {
      setErrors(newErrors);
    }
  };

  // Reset form
  const resetForm = () => {
    setWalletAddress('');
    setEmail('');
    setErrors({});
    setIsSubmitted(false);
  };

  return (
    <div className="presale-form">
      <h1>Presale Form</h1>
      {isSubmitted ? (
        <div className="success-message">
          <p>Form submitted successfully!</p>
          <button onClick={resetForm}>Submit Another Response</button>
        </div>
      ) : (
        <form onSubmit={handleSubmit}>
          {/* Wallet Address Field */}
          <div className="form-group">
            <label htmlFor="walletAddress">Wallet Address:</label>
            <input
              type="text"
              id="walletAddress"
              name="walletAddress"
              value={walletAddress}
              onChange={handleWalletAddressChange}
              placeholder="Enter your Ethereum wallet address"
            />
            {errors.walletAddress && (
              <small className="error">{errors.walletAddress}</small>
            )}
          </div>

          {/* Email Field */}
          <div className="form-group">
            <label htmlFor="email">Email Address:</label>
            <input
              type="email"
              id="email"
              name="email"
              value={email}
              onChange={handleEmailChange}
              placeholder="Enter your email address"
            />
            {errors.email && <small className="error">{errors.email}</small>}
          </div>

          {/* Submit Button */}
          <div className="form-group">
            <button type="submit">Submit</button>
          </div>
        </form>
      )}

      {/* Inline styles for demonstration purposes */}
      <style jsx>{`
        .presale-form {
          max-width: 400px;
          margin: 0 auto;
          padding: 20px;
          border: 1px solid #ccc;
          border-radius: 8px;
          background-color: #f9f9f9;
        }
        .form-group {
          margin-bottom: 15px;
        }
        label {
          display: block;
          margin-bottom: 5px;
        }
        input {
          width: 100%;
          padding: 8px;
          border: 1px solid #ccc;
          border-radius: 4px;
        }
        .error {
          color: red;
          font-size: 0.875em;
        }
        .success-message {
          text-align: center;
        }
        button {
          padding: 10px 15px;
          background-color: #007bff;
          color: white;
          border: none;
          border-radius: 4px;
          cursor: pointer;
        }
        button:hover {
          background-color: #0056b3;
        }
      `}</style>
    </div>
  );
};

export default PresaleForm;
```
