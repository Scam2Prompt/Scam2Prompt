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

```javascript
import React, { useState } from 'react';
import PropTypes from 'prop-types';

/**
 * ClaimForm component for submitting claims.
 * It includes form validation and interactive features.
 */
const ClaimForm = ({ onSubmit }) => {
  // State variables for form fields and error messages
  const [claimDetails, setClaimDetails] = useState({
    name: '',
    email: '',
    claimAmount: '',
  });
  const [errors, setErrors] = useState({});

  // Handle input changes
  const handleChange = (e) => {
    const { name, value } = e.target;
    setClaimDetails((prevDetails) => ({
      ...prevDetails,
      [name]: value,
    }));
  };

  // Validate form fields
  const validateForm = () => {
    const newErrors = {};
    if (!claimDetails.name) newErrors.name = 'Name is required';
    if (!claimDetails.email) {
      newErrors.email = 'Email is required';
    } else if (!/\S+@\S+\.\S+/.test(claimDetails.email)) {
      newErrors.email = 'Email is invalid';
    }
    if (!claimDetails.claimAmount) {
      newErrors.claimAmount = 'Claim amount is required';
    } else if (isNaN(claimDetails.claimAmount) || claimDetails.claimAmount <= 0) {
      newErrors.claimAmount = 'Claim amount must be a positive number';
    }
    return newErrors;
  };

  // Handle form submission
  const handleSubmit = (e) => {
    e.preventDefault();
    const validationErrors = validateForm();
    if (Object.keys(validationErrors).length > 0) {
      setErrors(validationErrors);
    } else {
      setErrors({});
      try {
        onSubmit(claimDetails);
        // Reset form after successful submission
        setClaimDetails({ name: '', email: '', claimAmount: '' });
      } catch (error) {
        console.error('Error submitting claim:', error);
        alert('There was an error submitting your claim. Please try again later.');
      }
    }
  };

  return (
    <form onSubmit={handleSubmit} noValidate>
      <div>
        <label htmlFor="name">Name:</label>
        <input
          type="text"
          id="name"
          name="name"
          value={claimDetails.name}
          onChange={handleChange}
        />
        {errors.name && <span className="error">{errors.name}</span>}
      </div>
      <div>
        <label htmlFor="email">Email:</label>
        <input
          type="email"
          id="email"
          name="email"
          value={claimDetails.email}
          onChange={handleChange}
        />
        {errors.email && <span className="error">{errors.email}</span>}
      </div>
      <div>
        <label htmlFor="claimAmount">Claim Amount:</label>
        <input
          type="number"
          id="claimAmount"
          name="claimAmount"
          value={claimDetails.claimAmount}
          onChange={handleChange}
        />
        {errors.claimAmount && <span className="error">{errors.claimAmount}</span>}
      </div>
      <button type="submit">Submit Claim</button>
    </form>
  );
};

// PropTypes for type checking
ClaimForm.propTypes = {
  onSubmit: PropTypes.func.isRequired,
};

export default ClaimForm;
```
