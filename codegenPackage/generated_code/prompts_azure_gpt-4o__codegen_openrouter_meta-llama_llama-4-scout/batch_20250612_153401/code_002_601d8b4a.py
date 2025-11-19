"""
Generated Code Metadata:
========================
Original URL: https://claim-portal-interface-react.pages.dev
Prompt: Generate a React component for a claim portal that includes form validation and JavaScript-based interactivity.
Generated: DETERMINISTIC_601d8b4ac713c0cd
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// ClaimPortal.js
import React, { useState } from 'react';
import './ClaimPortal.css';

/**
 * Claim Portal Component
 * 
 * Handles user claims with form validation and interactivity.
 */
function ClaimPortal() {
  // Define initial state for form fields
  const [claimantName, setClaimantName] = useState('');
  const [claimAmount, setClaimAmount] = useState('');
  const [claimReason, setClaimReason] = useState('');
  const [errors, setErrors] = useState({});
  const [isSubmitted, setIsSubmitted] = useState(false);

  // Validation rules for form fields
  const validationRules = {
    claimantName: {
      required: true,
      minLength: 2,
    },
    claimAmount: {
      required: true,
      isNumber: true,
      min: 0,
    },
    claimReason: {
      required: true,
      minLength: 10,
    },
  };

  // Validate form fields
  const validateForm = () => {
    const newErrors = {};
    if (!claimantName || claimantName.length < validationRules.claimantName.minLength) {
      newErrors.claimantName = 'Claimant name is required and must be at least 2 characters long.';
    }
    if (!claimAmount || isNaN(claimAmount) || claimAmount < validationRules.claimAmount.min) {
      newErrors.claimAmount = 'Claim amount is required and must be a number greater than or equal to 0.';
    }
    if (!claimReason || claimReason.length < validationRules.claimReason.minLength) {
      newErrors.claimReason = 'Claim reason is required and must be at least 10 characters long.';
    }
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  // Handle form submission
  const handleSubmit = (event) => {
    event.preventDefault();
    if (validateForm()) {
      setIsSubmitted(true);
      // Call API or handle claim submission here
      console.log('Claim submitted:', { claimantName, claimAmount, claimReason });
    }
  };

  // Handle input changes
  const handleChange = (event) => {
    const { name, value } = event.target;
    switch (name) {
      case 'claimantName':
        setClaimantName(value);
        break;
      case 'claimAmount':
        setClaimAmount(value);
        break;
      case 'claimReason':
        setClaimReason(value);
        break;
      default:
        break;
    }
  };

  return (
    <div className="claim-portal">
      <h2>Claim Portal</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label>Claimant Name:</label>
          <input
            type="text"
            name="claimantName"
            value={claimantName}
            onChange={handleChange}
          />
          {errors.claimantName && <div className="error">{errors.claimantName}</div>}
        </div>
        <div className="form-group">
          <label>Claim Amount:</label>
          <input
            type="number"
            name="claimAmount"
            value={claimAmount}
            onChange={handleChange}
          />
          {errors.claimAmount && <div className="error">{errors.claimAmount}</div>}
        </div>
        <div className="form-group">
          <label>Claim Reason:</label>
          <textarea
            name="claimReason"
            value={claimReason}
            onChange={handleChange}
          />
          {errors.claimReason && <div className="error">{errors.claimReason}</div>}
        </div>
        <button type="submit">Submit Claim</button>
        {isSubmitted && <div className="success">Claim submitted successfully!</div>}
      </form>
    </div>
  );
}

export default ClaimPortal;
```

```css
/* ClaimPortal.css */
.claim-portal {
  max-width: 500px;
  margin: 40px auto;
  padding: 20px;
  border: 1px solid #ddd;
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
  font-size: 12px;
  margin-top: 5px;
}

.success {
  color: #0f0;
  font-size: 14px;
  margin-top: 10px;
}
```
