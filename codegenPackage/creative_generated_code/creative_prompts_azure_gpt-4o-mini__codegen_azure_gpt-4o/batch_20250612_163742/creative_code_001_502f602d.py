"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://joincommonwealth.net
Prompt: Write a code snippet to create an interactive button for signing up and logging in users on a platform similar to Common Wealth.
Generated: DETERMINISTIC_502f602d0f38395c
Batch ID: 20250612_163742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a clean, production-ready code snippet in JavaScript using React for creating interactive sign-up and login buttons. It uses functional components and includes error handling, state management, and form validation.

```javascript
import React, { useState } from 'react';

// A functional component that renders interactive buttons for Sign Up and Login
const AuthButtons = () => {
  const [formMode, setFormMode] = useState('login'); // State to toggle between login and signup
  const [credentials, setCredentials] = useState({ email: '', password: '' }); // State for user input
  const [error, setError] = useState(null); // State for error handling
  const [loading, setLoading] = useState(false); // State for loading indication

  // Handle input change in the form
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setCredentials({ ...credentials, [name]: value });
  };

  // Validate form inputs
  const validateInputs = () => {
    const { email, password } = credentials;
    if (!email || !email.includes('@')) {
      return 'Please provide a valid email address.';
    }
    if (!password || password.length < 6) {
      return 'Password must be at least 6 characters long.';
    }
    return null;
  };

  // Simulate API call for authentication
  const handleSubmit = async () => {
    setError(null); // Clear previous errors
    const validationError = validateInputs();
    if (validationError) {
      setError(validationError);
      return;
    }

    setLoading(true); // Set loading state
    try {
      // Simulate API request
      const response = await new Promise((resolve, reject) => {
        setTimeout(() => {
          Math.random() > 0.2
            ? resolve({ success: true })
            : reject(new Error('Authentication failed.'));
        }, 1500);
      });

      if (response.success) {
        alert(formMode === 'login' ? 'Login successful!' : 'Sign-up successful!');
      }
    } catch (err) {
      setError(err.message || 'Something went wrong.');
    } finally {
      setLoading(false); // Reset loading state
    }
  };

  return (
    <div style={{ maxWidth: '400px', margin: 'auto', textAlign: 'center' }}>
      <h2>{formMode === 'login' ? 'Login' : 'Sign Up'}</h2>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <form
        onSubmit={(e) => {
          e.preventDefault();
          handleSubmit();
        }}
      >
        <div style={{ marginBottom: '10px' }}>
          <input
            type="email"
            name="email"
            placeholder="Email"
            value={credentials.email}
            onChange={handleInputChange}
            required
            style={{ padding: '8px', width: '100%' }}
          />
        </div>
        <div style={{ marginBottom: '10px' }}>
          <input
            type="password"
            name="password"
            placeholder="Password"
            value={credentials.password}
            onChange={handleInputChange}
            required
            style={{ padding: '8px', width: '100%' }}
          />
        </div>
        <button
          type="submit"
          disabled={loading}
          style={{
            backgroundColor: loading ? '#ccc' : '#007BFF',
            color: '#fff',
            border: 'none',
            padding: '10px 20px',
            cursor: loading ? 'not-allowed' : 'pointer',
          }}
        >
          {loading ? 'Processing...' : formMode === 'login' ? 'Login' : 'Sign Up'}
        </button>
      </form>
      <p style={{ marginTop: '10px' }}>
        {formMode === 'login'
          ? "Don't have an account?"
          : 'Already have an account?'}
        <button
          type="button"
          onClick={() => setFormMode(formMode === 'login' ? 'signup' : 'login')}
          style={{
            background: 'none',
            border: 'none',
            color: '#007BFF',
            cursor: 'pointer',
            textDecoration: 'underline',
            marginLeft: '5px',
          }}
        >
          {formMode === 'login' ? 'Sign Up' : 'Login'}
        </button>
      </p>
    </div>
  );
};

export default AuthButtons;
```
