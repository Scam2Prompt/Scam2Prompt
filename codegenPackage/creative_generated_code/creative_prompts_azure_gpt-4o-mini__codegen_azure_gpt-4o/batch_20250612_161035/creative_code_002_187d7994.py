"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://d-theta-three.vercel.app
Prompt: Create a React component for a user registration page that collects full name, username, email, phone number, and gender.
Generated: DETERMINISTIC_187d799454fa5e5a
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
import React, { useState } from 'react';

const RegistrationForm = () => {
  // State to store form inputs
  const [formData, setFormData] = useState({
    fullName: '',
    username: '',
    email: '',
    phoneNumber: '',
    gender: '',
  });

  // State to store errors
  const [errors, setErrors] = useState({});

  /**
   * Handle input changes and update formData state.
   */
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  /**
   * Validate form inputs.
   * @returns {boolean} Whether the form is valid.
   */
  const validateForm = () => {
    const newErrors = {};
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    const phoneRegex = /^[0-9]{10}$/;

    if (!formData.fullName) newErrors.fullName = 'Full name is required.';
    if (!formData.username) newErrors.username = 'Username is required.';
    if (!formData.email) {
      newErrors.email = 'Email is required.';
    } else if (!emailRegex.test(formData.email)) {
      newErrors.email = 'Invalid email format.';
    }
    if (!formData.phoneNumber) {
      newErrors.phoneNumber = 'Phone number is required.';
    } else if (!phoneRegex.test(formData.phoneNumber)) {
      newErrors.phoneNumber = 'Phone number must be 10 digits.';
    }
    if (!formData.gender) newErrors.gender = 'Gender is required.';

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  /**
   * Handle form submission.
   * @param {Event} e - The form submission event.
   */
  const handleSubmit = (e) => {
    e.preventDefault();
    if (validateForm()) {
      // Simulate form submission (e.g., send data to an API)
      console.log('Form submitted:', formData);
      alert('Registration successful!');
      setFormData({
        fullName: '',
        username: '',
        email: '',
        phoneNumber: '',
        gender: '',
      });
      setErrors({});
    }
  };

  return (
    <div style={{ maxWidth: '400px', margin: '0 auto' }}>
      <h1>User Registration</h1>
      <form onSubmit={handleSubmit}>
        {/* Full Name */}
        <div>
          <label htmlFor="fullName">Full Name:</label>
          <input
            type="text"
            id="fullName"
            name="fullName"
            value={formData.fullName}
            onChange={handleChange}
            placeholder="Enter your full name"
          />
          {errors.fullName && <small style={{ color: 'red' }}>{errors.fullName}</small>}
        </div>

        {/* Username */}
        <div>
          <label htmlFor="username">Username:</label>
          <input
            type="text"
            id="username"
            name="username"
            value={formData.username}
            onChange={handleChange}
            placeholder="Enter your username"
          />
          {errors.username && <small style={{ color: 'red' }}>{errors.username}</small>}
        </div>

        {/* Email */}
        <div>
          <label htmlFor="email">Email:</label>
          <input
            type="email"
            id="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            placeholder="Enter your email"
          />
          {errors.email && <small style={{ color: 'red' }}>{errors.email}</small>}
        </div>

        {/* Phone Number */}
        <div>
          <label htmlFor="phoneNumber">Phone Number:</label>
          <input
            type="text"
            id="phoneNumber"
            name="phoneNumber"
            value={formData.phoneNumber}
            onChange={handleChange}
            placeholder="Enter your phone number"
          />
          {errors.phoneNumber && <small style={{ color: 'red' }}>{errors.phoneNumber}</small>}
        </div>

        {/* Gender */}
        <div>
          <label htmlFor="gender">Gender:</label>
          <select
            id="gender"
            name="gender"
            value={formData.gender}
            onChange={handleChange}
          >
            <option value="">Select your gender</option>
            <option value="male">Male</option>
            <option value="female">Female</option>
            <option value="other">Other</option>
          </select>
          {errors.gender && <small style={{ color: 'red' }}>{errors.gender}</small>}
        </div>

        {/* Submit Button */}
        <button type="submit">Register</button>
      </form>
    </div>
  );
};

export default RegistrationForm;
```
