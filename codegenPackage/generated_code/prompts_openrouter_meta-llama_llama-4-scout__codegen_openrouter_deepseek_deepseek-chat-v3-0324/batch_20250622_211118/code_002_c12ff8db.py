"""
Generated Code Metadata:
========================
Original URL: https://closeloopapp.online
Prompt: Generate JavaScript code for a basic login and registration form with validation, inspired by the Closeloop app.
Generated: DETERMINISTIC_c12ff8db9e481488
Batch ID: 20250622_211118
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// auth.js - Authentication module for login and registration

/**
 * Validates user input for registration and login forms
 * @param {Object} formData - Form data object
 * @param {string} formType - 'register' or 'login'
 * @returns {Object} { isValid: boolean, errors: Object }
 */
function validateForm(formData, formType) {
  const errors = {};
  const { email, password, confirmPassword, name } = formData;

  // Email validation
  if (!email) {
    errors.email = 'Email is required';
  } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
    errors.email = 'Please enter a valid email address';
  }

  // Password validation
  if (!password) {
    errors.password = 'Password is required';
  } else if (password.length < 8) {
    errors.password = 'Password must be at least 8 characters';
  }

  // Additional validation for registration
  if (formType === 'register') {
    if (!name) {
      errors.name = 'Name is required';
    } else if (name.length < 2) {
      errors.name = 'Name must be at least 2 characters';
    }

    if (!confirmPassword) {
      errors.confirmPassword = 'Please confirm your password';
    } else if (password !== confirmPassword) {
      errors.confirmPassword = 'Passwords do not match';
    }
  }

  return {
    isValid: Object.keys(errors).length === 0,
    errors
  };
}

/**
 * Simulates API call for user registration
 * @param {Object} userData - User data to register
 * @returns {Promise<Object>} Response object
 */
async function registerUser(userData) {
  try {
    // Simulate API call delay
    await new Promise(resolve => setTimeout(resolve, 1000));
    
    // In a real app, this would be an actual API call
    const response = {
      success: true,
      user: {
        id: Math.random().toString(36).substring(2, 9),
        name: userData.name,
        email: userData.email
      },
      message: 'Registration successful'
    };

    // Save user to localStorage (simulating backend)
    localStorage.setItem('currentUser', JSON.stringify(response.user));
    localStorage.setItem('authToken', 'simulated-auth-token');

    return response;
  } catch (error) {
    console.error('Registration error:', error);
    throw new Error('Registration failed. Please try again.');
  }
}

/**
 * Simulates API call for user login
 * @param {Object} credentials - Login credentials
 * @returns {Promise<Object>} Response object
 */
async function loginUser(credentials) {
  try {
    // Simulate API call delay
    await new Promise(resolve => setTimeout(resolve, 1000));
    
    // In a real app, this would verify credentials against a backend
    const response = {
      success: true,
      user: {
        id: 'demo-user-id',
        name: 'Demo User',
        email: credentials.email
      },
      message: 'Login successful'
    };

    // Save user to localStorage (simulating backend)
    localStorage.setItem('currentUser', JSON.stringify(response.user));
    localStorage.setItem('authToken', 'simulated-auth-token');

    return response;
  } catch (error) {
    console.error('Login error:', error);
    throw new Error('Login failed. Please check your credentials.');
  }
}

/**
 * Logs out the current user
 */
function logoutUser() {
  localStorage.removeItem('currentUser');
  localStorage.removeItem('authToken');
}

/**
 * Checks if user is authenticated
 * @returns {boolean} True if authenticated
 */
function isAuthenticated() {
  return !!localStorage.getItem('authToken');
}

/**
 * Gets current user data
 * @returns {Object|null} User object or null if not authenticated
 */
function getCurrentUser() {
  const user = localStorage.getItem('currentUser');
  return user ? JSON.parse(user) : null;
}

export {
  validateForm,
  registerUser,
  loginUser,
  logoutUser,
  isAuthenticated,
  getCurrentUser
};
```

```javascript
// LoginForm.jsx - React component for login form
import React, { useState } from 'react';
import { validateForm, loginUser } from './auth';

const LoginForm = ({ onLoginSuccess, onSwitchToRegister }) => {
  const [formData, setFormData] = useState({
    email: '',
    password: ''
  });
  const [errors, setErrors] = useState({});
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [loginError, setLoginError] = useState('');

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoginError('');
    
    // Validate form
    const { isValid, errors: validationErrors } = validateForm(formData, 'login');
    setErrors(validationErrors);
    
    if (!isValid) return;

    setIsSubmitting(true);
    
    try {
      const response = await loginUser(formData);
      if (response.success) {
        onLoginSuccess(response.user);
      }
    } catch (error) {
      setLoginError(error.message);
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <div className="auth-form">
      <h2>Login</h2>
      {loginError && <div className="error-message">{loginError}</div>}
      
      <form onSubmit={handleSubmit}>
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
          {errors.email && <span className="field-error">{errors.email}</span>}
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
          {errors.password && <span className="field-error">{errors.password}</span>}
        </div>
        
        <button type="submit" disabled={isSubmitting}>
          {isSubmitting ? 'Logging in...' : 'Login'}
        </button>
      </form>
      
      <div className="form-footer">
        <p>Don't have an account? <button onClick={onSwitchToRegister} className="link-button">Register</button></p>
      </div>
    </div>
  );
};

export default LoginForm;
```

```javascript
// RegisterForm.jsx - React component for registration form
import React, { useState } from 'react';
import { validateForm, registerUser } from './auth';

const RegisterForm = ({ onRegisterSuccess, onSwitchToLogin }) => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    password: '',
    confirmPassword: ''
  });
  const [errors, setErrors] = useState({});
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [registerError, setRegisterError] = useState('');

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setRegisterError('');
    
    // Validate form
    const { isValid, errors: validationErrors } = validateForm(formData, 'register');
    setErrors(validationErrors);
    
    if (!isValid) return;

    setIsSubmitting(true);
    
    try {
      const response = await registerUser(formData);
      if (response.success) {
        onRegisterSuccess(response.user);
      }
    } catch (error) {
      setRegisterError(error.message);
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <div className="auth-form">
      <h2>Register</h2>
      {registerError && <div className="error-message">{registerError}</div>}
      
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="name">Full Name</label>
          <input
            type="text"
            id="name"
            name="name"
            value={formData.name}
            onChange={handleChange}
            className={errors.name ? 'error' : ''}
          />
          {errors.name && <span className="field-error">{errors.name}</span>}
        </div>
        
        <div className="form-group">
          <label htmlFor="email">Email</label>
          <input
            type="email"
            id="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            className
