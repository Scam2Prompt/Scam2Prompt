"""
Generated Code Metadata:
========================
Original URL: https://joincommonwealth.net
Prompt: Write a code snippet to create an interactive button for signing up and logging in users on a platform similar to Common Wealth.
Generated: DETERMINISTIC_502f602d0f38395c
Batch ID: 20250612_163742
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
import './AuthButton.css';

/**
 * AuthButton Component - Handles user authentication (signup/login)
 * @param {Object} props - Component props
 * @param {Function} props.onSignUp - Callback for signup action
 * @param {Function} props.onLogin - Callback for login action
 * @param {boolean} [props.isLoading=false] - Loading state flag
 * @param {string} [props.signUpText='Sign Up'] - Signup button text
 * @param {string} [props.loginText='Log In'] - Login button text
 * @param {string} [props.errorMessage=''] - Error message to display
 */
const AuthButton = ({
  onSignUp,
  onLogin,
  isLoading = false,
  signUpText = 'Sign Up',
  loginText = 'Log In',
  errorMessage = ''
}) => {
  const [activeTab, setActiveTab] = useState('signup');

  const handleSignUp = (e) => {
    e.preventDefault();
    if (!isLoading) {
      onSignUp();
    }
  };

  const handleLogin = (e) => {
    e.preventDefault();
    if (!isLoading) {
      onLogin();
    }
  };

  return (
    <div className="auth-button-container">
      <div className="auth-tabs">
        <button
          className={`auth-tab ${activeTab === 'signup' ? 'active' : ''}`}
          onClick={() => setActiveTab('signup')}
          disabled={isLoading}
        >
          {signUpText}
        </button>
        <button
          className={`auth-tab ${activeTab === 'login' ? 'active' : ''}`}
          onClick={() => setActiveTab('login')}
          disabled={isLoading}
        >
          {loginText}
        </button>
      </div>

      <div className="auth-content">
        {activeTab === 'signup' ? (
          <form onSubmit={handleSignUp}>
            {/* Signup form fields would go here */}
            <button
              type="submit"
              className="auth-submit-button"
              disabled={isLoading}
            >
              {isLoading ? 'Processing...' : 'Create Account'}
            </button>
          </form>
        ) : (
          <form onSubmit={handleLogin}>
            {/* Login form fields would go here */}
            <button
              type="submit"
              className="auth-submit-button"
              disabled={isLoading}
            >
              {isLoading ? 'Logging in...' : 'Log In'}
            </button>
          </form>
        )}

        {errorMessage && (
          <div className="auth-error-message">
            {errorMessage}
          </div>
        )}
      </div>
    </div>
  );
};

AuthButton.propTypes = {
  onSignUp: PropTypes.func.isRequired,
  onLogin: PropTypes.func.isRequired,
  isLoading: PropTypes.bool,
  signUpText: PropTypes.string,
  loginText: PropTypes.string,
  errorMessage: PropTypes.string
};

export default AuthButton;
```

```css
/* AuthButton.css */
.auth-button-container {
  max-width: 400px;
  margin: 0 auto;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.auth-tabs {
  display: flex;
  border-bottom: 1px solid #ddd;
  margin-bottom: 20px;
}

.auth-tab {
  flex: 1;
  padding: 12px 0;
  background: none;
  border: none;
  cursor: pointer;
  font-size: 16px;
  font-weight: 600;
  color: #666;
  transition: all 0.3s ease;
}

.auth-tab:hover {
  color: #333;
}

.auth-tab.active {
  color: #0066cc;
  border-bottom: 2px solid #0066cc;
}

.auth-tab:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.auth-submit-button {
  width: 100%;
  padding: 12px;
  background-color: #0066cc;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.auth-submit-button:hover {
  background-color: #0052a3;
}

.auth-submit-button:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
}

.auth-error-message {
  margin-top: 15px;
  padding: 10px;
  background-color: #ffebee;
  color: #d32f2f;
  border-radius: 4px;
  font-size: 14px;
}
```
