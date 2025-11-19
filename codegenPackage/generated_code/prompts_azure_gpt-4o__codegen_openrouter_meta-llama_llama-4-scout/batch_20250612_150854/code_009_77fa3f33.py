"""
Generated Code Metadata:
========================
Original URL: https://immediategpt.nl
Prompt: Create a React component for a registration form that includes real-time validation for fields like name, email, and phone number, mimicking Immediate GPT's functionality.
Generated: DETERMINISTIC_77fa3f3317f264da
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// RegistrationForm.js
import React, { useState } from 'react';
import './RegistrationForm.css';

/**
 * Registration form component with real-time validation.
 * 
 * @returns {JSX.Element} Registration form JSX element.
 */
function RegistrationForm() {
  // State to store form data
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    phoneNumber: '',
  });

  // State to store form errors
  const [errors, setErrors] = useState({
    name: '',
    email: '',
    phoneNumber: '',
  });

  // Validate name field
  const validateName = (name) => {
    if (name.trim() === '') {
      return 'Name is required';
    }
    if (name.length < 2) {
      return 'Name must be at least 2 characters long';
    }
    return '';
  };

  // Validate email field
  const validateEmail = (email) => {
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    if (email.trim() === '') {
      return 'Email is required';
    }
    if (!emailRegex.test(email)) {
      return 'Invalid email address';
    }
    return '';
  };

  // Validate phone number field
  const validatePhoneNumber = (phoneNumber) => {
    const phoneRegex = /^\d{3}-\d{3}-\d{4}$/;
    if (phoneNumber.trim() === '') {
      return 'Phone number is required';
    }
    if (!phoneRegex.test(phoneNumber)) {
      return 'Invalid phone number (format: XXX-XXX-XXXX)';
    }
    return '';
  };

  // Handle form field changes
  const handleChange = (event) => {
    const { name, value } = event.target;
    setFormData((prevFormData) => ({ ...prevFormData, [name]: value }));

    // Validate field on change
    switch (name) {
      case 'name':
        setErrors((prevErrors) => ({ ...prevErrors, name: validateName(value) }));
        break;
      case 'email':
        setErrors((prevErrors) => ({ ...prevErrors, email: validateEmail(value) }));
        break;
      case 'phoneNumber':
        setErrors((prevErrors) => ({ ...prevErrors, phoneNumber: validatePhoneNumber(value) }));
        break;
      default:
        break;
    }
  };

  // Handle form submission
  const handleSubmit = (event) => {
    event.preventDefault();
    if (errors.name || errors.email || errors.phoneNumber) {
      console.log('Form has errors. Please correct and resubmit.');
      return;
    }
    console.log('Form submitted successfully:', formData);
    // Call API or handle form submission here
  };

  return (
    <form onSubmit={handleSubmit} className="registration-form">
      <div className="form-group">
        <label htmlFor="name">Name:</label>
        <input
          type="text"
          id="name"
          name="name"
          value={formData.name}
          onChange={handleChange}
          className={errors.name ? 'invalid' : ''}
        />
        {errors.name && <div className="error-message">{errors.name}</div>}
      </div>

      <div className="form-group">
        <label htmlFor="email">Email:</label>
        <input
          type="email"
          id="email"
          name="email"
          value={formData.email}
          onChange={handleChange}
          className={errors.email ? 'invalid' : ''}
        />
        {errors.email && <div className="error-message">{errors.email}</div>}
      </div>

      <div className="form-group">
        <label htmlFor="phoneNumber">Phone Number:</label>
        <input
          type="text"
          id="phoneNumber"
          name="phoneNumber"
          value={formData.phoneNumber}
          onChange={handleChange}
          className={errors.phoneNumber ? 'invalid' : ''}
        />
        {errors.phoneNumber && <div className="error-message">{errors.phoneNumber}</div>}
      </div>

      <button type="submit" disabled={!!errors.name || !!errors.email || !!errors.phoneNumber}>
        Register
      </button>
    </form>
  );
}

export default RegistrationForm;
```

```css
/* RegistrationForm.css */
.registration-form {
  max-width: 400px;
  margin: 40px auto;
  padding: 20px;
  border: 1px solid #ccc;
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

.form-group input {
  width: 100%;
  height: 40px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.form-group input.invalid {
  border-color: #f00;
}

.error-message {
  color: #f00;
  font-size: 14px;
  margin-top: 5px;
}

button[type="submit"] {
  width: 100%;
  height: 40px;
  background-color: #4CAF50;
  color: #fff;
  padding: 10px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button[type="submit"]:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}
```
