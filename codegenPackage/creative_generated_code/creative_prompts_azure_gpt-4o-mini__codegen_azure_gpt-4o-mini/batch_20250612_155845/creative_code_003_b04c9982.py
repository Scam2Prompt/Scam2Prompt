"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://auth.krevetka.cc
Prompt: Develop a user interface in React that incorporates the login and registration features of the krevétka VPN, focusing on error handling for incorrect email and password entries.
Generated: DETERMINISTIC_b04c9982ec775694
Batch ID: 20250612_155845
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and components
import React, { useState } from 'react';
import PropTypes from 'prop-types';

// Define the Login and Registration component
const AuthForm = ({ onLogin, onRegister }) => {
  // State variables for email, password, and error messages
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  // Handle input changes
  const handleChange = (e) => {
    const { name, value } = e.target;
    if (name === 'email') setEmail(value);
    if (name === 'password') setPassword(value);
  };

  // Validate email format
  const validateEmail = (email) => {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
  };

  // Handle form submission for login
  const handleLogin = async (e) => {
    e.preventDefault();
    if (!validateEmail(email)) {
      setError('Invalid email format.');
      return;
    }

    // Clear previous errors
    setError('');
    try {
      await onLogin({ email, password });
    } catch (err) {
      setError(err.message || 'Login failed. Please try again.');
    }
  };

  // Handle form submission for registration
  const handleRegister = async (e) => {
    e.preventDefault();
    if (!validateEmail(email)) {
      setError('Invalid email format.');
      return;
    }

    // Clear previous errors
    setError('');
    try {
      await onRegister({ email, password });
    } catch (err) {
      setError(err.message || 'Registration failed. Please try again.');
    }
  };

  return (
    <div className="auth-container">
      <h2>Login / Register</h2>
      {error && <div className="error-message">{error}</div>}
      <form>
        <div>
          <label htmlFor="email">Email:</label>
          <input
            type="email"
            id="email"
            name="email"
            value={email}
            onChange={handleChange}
            required
          />
        </div>
        <div>
          <label htmlFor="password">Password:</label>
          <input
            type="password"
            id="password"
            name="password"
            value={password}
            onChange={handleChange}
            required
          />
        </div>
        <button type="submit" onClick={handleLogin}>Login</button>
        <button type="button" onClick={handleRegister}>Register</button>
      </form>
    </div>
  );
};

// PropTypes for type checking
AuthForm.propTypes = {
  onLogin: PropTypes.func.isRequired,
  onRegister: PropTypes.func.isRequired,
};

// Export the component
export default AuthForm;
```
