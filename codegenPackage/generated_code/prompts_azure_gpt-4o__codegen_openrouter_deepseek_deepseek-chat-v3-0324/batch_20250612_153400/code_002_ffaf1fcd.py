"""
Generated Code Metadata:
========================
Original URL: https://presales-friend.pages.dev
Prompt: Develop a registration form for a PWA, ensuring that users who register within a specified timeframe (e.g., 48 hours) are flagged for inclusion in a special event or feature.
Generated: DETERMINISTIC_ffaf1fcd343e05b6
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// RegistrationForm.js
import React, { useState, useEffect } from 'react';
import { registerUser } from './apiService';
import './RegistrationForm.css';

const RegistrationForm = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    password: '',
    confirmPassword: ''
  });
  const [errors, setErrors] = useState({});
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [registrationSuccess, setRegistrationSuccess] = useState(false);
  const [isEligibleForEvent, setIsEligibleForEvent] = useState(false);

  // Event eligibility window (48 hours from now)
  const eventEligibilityWindow = 48 * 60 * 60 * 1000; // 48 hours in milliseconds
  const eventStartTime = new Date().getTime();

  useEffect(() => {
    // Check if current time is within eligibility window
    const checkEligibility = () => {
      const currentTime = new Date().getTime();
      setIsEligibleForEvent(currentTime - eventStartTime <= eventEligibilityWindow);
    };

    checkEligibility();
  }, [eventStartTime, eventEligibilityWindow]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value
    });
  };

  const validateForm = () => {
    const newErrors = {};
    if (!formData.name.trim()) newErrors.name = 'Name is required';
    if (!formData.email.trim()) {
      newErrors.email = 'Email is required';
    } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.email)) {
      newErrors.email = 'Email is invalid';
    }
    if (!formData.password) {
      newErrors.password = 'Password is required';
    } else if (formData.password.length < 8) {
      newErrors.password = 'Password must be at least 8 characters';
    }
    if (formData.password !== formData.confirmPassword) {
      newErrors.confirmPassword = 'Passwords do not match';
    }
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!validateForm()) return;

    setIsSubmitting(true);
    try {
      const userData = {
        ...formData,
        registrationTime: new Date().toISOString(),
        isEligibleForEvent
      };

      await registerUser(userData);
      setRegistrationSuccess(true);
    } catch (error) {
      console.error('Registration error:', error);
      setErrors({ submit: error.message || 'Registration failed. Please try again.' });
    } finally {
      setIsSubmitting(false);
    }
  };

  if (registrationSuccess) {
    return (
      <div className="success-message">
        <h2>Registration Successful!</h2>
        {isEligibleForEvent && (
          <p className="event-notice">
            Congratulations! You're eligible for our special event.
          </p>
        )}
        <p>Welcome to our platform!</p>
      </div>
    );
  }

  return (
    <div className="registration-form">
      <h2>Register</h2>
      {isEligibleForEvent && (
        <div className="event-banner">
          Register now to participate in our special event!
        </div>
      )}
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="name">Name</label>
          <input
            type="text"
            id="name"
            name="name"
            value={formData.name}
            onChange={handleChange}
            className={errors.name ? 'error' : ''}
          />
          {errors.name && <span className="error-message">{errors.name}</span>}
        </div>
        <div className="form-group">
          <label htmlFor="email">Email</label>
          <input
            type="email"
            id="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            className={errors.email ? 'error' : ''}
          />
          {errors.email && <span className="error-message">{errors.email}</span>}
        </div>
        <div className="form-group">
          <label htmlFor="password">Password</label>
          <input
            type="password"
            id="password"
            name="password"
            value={formData.password}
            onChange={handleChange}
            className={errors.password ? 'error' : ''}
          />
          {errors.password && <span className="error-message">{errors.password}</span>}
        </div>
        <div className="form-group">
          <label htmlFor="confirmPassword">Confirm Password</label>
          <input
            type="password"
            id="confirmPassword"
            name="confirmPassword"
            value={formData.confirmPassword}
            onChange={handleChange}
            className={errors.confirmPassword ? 'error' : ''}
          />
          {errors.confirmPassword && (
            <span className="error-message">{errors.confirmPassword}</span>
          )}
        </div>
        {errors.submit && <div className="submit-error">{errors.submit}</div>}
        <button type="submit" disabled={isSubmitting} className="submit-btn">
          {isSubmitting ? 'Registering...' : 'Register'}
        </button>
      </form>
    </div>
  );
};

export default RegistrationForm;
```

```javascript
// apiService.js
export const registerUser = async (userData) => {
  const response = await fetch('/api/register', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(userData),
  });

  if (!response.ok) {
    const errorData = await response.json();
    throw new Error(errorData.message || 'Registration failed');
  }

  return response.json();
};
```

```css
/* RegistrationForm.css */
.registration-form {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.event-banner {
  background-color: #ffeb3b;
  padding: 10px;
  border-radius: 4px;
  margin-bottom: 20px;
  text-align: center;
  font-weight: bold;
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
  font-weight: 500;
}

input {
  width: 100%;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
  box-sizing: border-box;
}

input.error {
  border-color: #f44336;
}

.error-message {
  color: #f44336;
  font-size: 0.8em;
  margin-top: 5px;
  display: block;
}

.submit-error {
  color: #f44336;
  margin-bottom: 15px;
  text-align: center;
}

.submit-btn {
  width: 100%;
  padding: 10px;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1em;
}

.submit-btn:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
}

.success-message {
  text-align: center;
  padding: 20px;
}

.event-notice {
  color: #ff9800;
  font-weight: bold;
  margin: 15px 0;
}
```

```javascript
// server.js (example backend implementation)
const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
app.use(bodyParser.json());
app.use(cors());

const users = [];

app.post('/api/register', (req, res) => {
  try {
    const { name, email, password, registrationTime, isEligibleForEvent } = req.body;
    
    // Validate required fields
    if (!name || !email || !password) {
      return res.status(400).json({ message: 'Missing required fields' });
    }

    // Check if email already exists
    if (users.some(user => user.email === email)) {
      return res.status(409).json({ message: 'Email already registered' });
    }

    // Store user data
    const user = {
      id: Date.now().toString(),
      name,
      email,
      password, // Note: In production, hash the password before storing
      registrationTime,
      isEligibleForEvent
    };

    users.push(user);
    res.status(201).json({ message: 'User registered successfully', user });
  } catch (error) {
    console.error('Registration error:', error);
    res.status(500).json({ message: 'Internal server error
