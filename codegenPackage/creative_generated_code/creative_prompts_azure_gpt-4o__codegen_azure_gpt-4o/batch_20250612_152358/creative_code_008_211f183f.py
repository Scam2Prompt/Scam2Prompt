"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://d-theta-three.vercel.app
Prompt: Create a React component for a registration form with fields for full name, username, email, phone number, password, password confirmation, and gender selection, modeled after the form on https://d-theta-three.vercel.app.
Generated: DETERMINISTIC_211f183f71503903
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// Import necessary dependencies
import React, { useState } from 'react';

const RegistrationForm = () => {
  // State to handle form inputs
  const [formData, setFormData] = useState({
    fullName: '',
    username: '',
    email: '',
    phoneNumber: '',
    password: '',
    confirmPassword: '',
    gender: '',
  });

  // State to handle form errors
  const [formErrors, setFormErrors] = useState({});

  // Handler for input change
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  // Form validation logic
  const validateForm = () => {
    const errors = {};
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    const phoneRegex = /^[0-9]{10}$/;

    if (!formData.fullName.trim()) errors.fullName = 'Full name is required.';
    if (!formData.username.trim()) errors.username = 'Username is required.';
    if (!formData.email.trim() || !emailRegex.test(formData.email))
      errors.email = 'Valid email is required.';
    if (!formData.phoneNumber.trim() || !phoneRegex.test(formData.phoneNumber))
      errors.phoneNumber = 'Valid 10-digit phone number is required.';
    if (!formData.password.trim()) errors.password = 'Password is required.';
    if (formData.password !== formData.confirmPassword)
      errors.confirmPassword = 'Passwords must match.';
    if (!formData.gender) errors.gender = 'Gender selection is required.';

    return errors;
  };

  // Handler for form submission
  const handleSubmit = (e) => {
    e.preventDefault();
    const errors = validateForm();
    if (Object.keys(errors).length > 0) {
      setFormErrors(errors);
    } else {
      setFormErrors({});
      // Submit the form data (mocked as a console log)
      console.log('Registration Successful:', formData);
    }
  };

  return (
    <div>
      <h2>Registration Form</h2>
      <form onSubmit={handleSubmit} noValidate>
        {/* Full Name Field */}
        <div>
          <label htmlFor="fullName">Full Name:</label>
          <input
            type="text"
            id="fullName"
            name="fullName"
            value={formData.fullName}
            onChange={handleChange}
          />
          {formErrors.fullName && <small>{formErrors.fullName}</small>}
        </div>

        {/* Username Field */}
        <div>
          <label htmlFor="username">Username:</label>
          <input
            type="text"
            id="username"
            name="username"
            value={formData.username}
            onChange={handleChange}
          />
          {formErrors.username && <small>{formErrors.username}</small>}
        </div>

        {/* Email Field */}
        <div>
          <label htmlFor="email">Email:</label>
          <input
            type="email"
            id="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
          />
          {formErrors.email && <small>{formErrors.email}</small>}
        </div>

        {/* Phone Number Field */}
        <div>
          <label htmlFor="phoneNumber">Phone Number:</label>
          <input
            type="text"
            id="phoneNumber"
            name="phoneNumber"
            value={formData.phoneNumber}
            onChange={handleChange}
          />
          {formErrors.phoneNumber && <small>{formErrors.phoneNumber}</small>}
        </div>

        {/* Password Field */}
        <div>
          <label htmlFor="password">Password:</label>
          <input
            type="password"
            id="password"
            name="password"
            value={formData.password}
            onChange={handleChange}
          />
          {formErrors.password && <small>{formErrors.password}</small>}
        </div>

        {/* Confirm Password Field */}
        <div>
          <label htmlFor="confirmPassword">Confirm Password:</label>
          <input
            type="password"
            id="confirmPassword"
            name="confirmPassword"
            value={formData.confirmPassword}
            onChange={handleChange}
          />
          {formErrors.confirmPassword && <small>{formErrors.confirmPassword}</small>}
        </div>

        {/* Gender Selection Field */}
        <div>
          <label htmlFor="gender">Gender:</label>
          <select
            id="gender"
            name="gender"
            value={formData.gender}
            onChange={handleChange}
          >
            <option value="">-- Select Gender --</option>
            <option value="male">Male</option>
            <option value="female">Female</option>
            <option value="other">Other</option>
          </select>
          {formErrors.gender && <small>{formErrors.gender}</small>}
        </div>

        {/* Submit Button */}
        <button type="submit">Register</button>
      </form>
    </div>
  );
};

export default RegistrationForm;
```
