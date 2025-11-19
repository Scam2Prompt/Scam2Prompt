"""
Generated Code Metadata:
========================
Original URL: https://globalarbitrageinvest.com
Prompt: Develop a React component for a login form that includes Metamask integration, "Remember Me" functionality, and password recovery options, inspired by the Global Arbitrage Investments website.
Generated: DETERMINISTIC_334ad1cbf2720488
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
import React, { useState, useEffect } from 'react';
import { ethers } from 'ethers';
import './LoginForm.css';

const LoginForm = ({ onLoginSuccess }) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [rememberMe, setRememberMe] = useState(false);
  const [isMetamaskInstalled, setIsMetamaskInstalled] = useState(false);
  const [isConnecting, setIsConnecting] = useState(false);
  const [error, setError] = useState('');
  const [showRecovery, setShowRecovery] = useState(false);
  const [recoveryEmail, setRecoveryEmail] = useState('');

  // Check if Metamask is installed on component mount
  useEffect(() => {
    if (typeof window.ethereum !== 'undefined') {
      setIsMetamaskInstalled(true);
    }
  }, []);

  const handleEmailChange = (e) => {
    setEmail(e.target.value);
    setError('');
  };

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
    setError('');
  };

  const handleRememberMeChange = (e) => {
    setRememberMe(e.target.checked);
  };

  const handleRecoveryEmailChange = (e) => {
    setRecoveryEmail(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');

    if (!email || !password) {
      setError('Please fill in all fields');
      return;
    }

    try {
      // Simulate login API call
      // In a real app, you would call your backend here
      await new Promise(resolve => setTimeout(resolve, 1000));
      onLoginSuccess({ email, rememberMe });
    } catch (err) {
      setError('Invalid email or password');
    }
  };

  const handleMetamaskLogin = async () => {
    if (!isMetamaskInstalled) {
      setError('Metamask is not installed');
      return;
    }

    setIsConnecting(true);
    setError('');

    try {
      const provider = new ethers.providers.Web3Provider(window.ethereum);
      await provider.send("eth_requestAccounts", []);
      const signer = provider.getSigner();
      const address = await signer.getAddress();

      // In a real app, you would verify the signature with your backend
      onLoginSuccess({ walletAddress: address, rememberMe });
    } catch (err) {
      setError('Failed to connect with Metamask');
    } finally {
      setIsConnecting(false);
    }
  };

  const handleRecoverySubmit = (e) => {
    e.preventDefault();
    if (!recoveryEmail) {
      setError('Please enter your email');
      return;
    }

    // Simulate recovery email sent
    setError('');
    setShowRecovery(false);
    alert(`Password recovery instructions sent to ${recoveryEmail}`);
  };

  return (
    <div className="login-container">
      <h2>Login to Your Account</h2>
      
      {error && <div className="error-message">{error}</div>}

      {!showRecovery ? (
        <>
          <form onSubmit={handleSubmit}>
            <div className="form-group">
              <label htmlFor="email">Email</label>
              <input
                type="email"
                id="email"
                value={email}
                onChange={handleEmailChange}
                placeholder="Enter your email"
                required
              />
            </div>

            <div className="form-group">
              <label htmlFor="password">Password</label>
              <input
                type="password"
                id="password"
                value={password}
                onChange={handlePasswordChange}
                placeholder="Enter your password"
                required
              />
            </div>

            <div className="form-options">
              <div className="remember-me">
                <input
                  type="checkbox"
                  id="rememberMe"
                  checked={rememberMe}
                  onChange={handleRememberMeChange}
                />
                <label htmlFor="rememberMe">Remember Me</label>
              </div>

              <button
                type="button"
                className="recovery-link"
                onClick={() => setShowRecovery(true)}
              >
                Forgot Password?
              </button>
            </div>

            <button type="submit" className="login-button">
              Login
            </button>
          </form>

          {isMetamaskInstalled && (
            <button
              className="metamask-button"
              onClick={handleMetamaskLogin}
              disabled={isConnecting}
            >
              {isConnecting ? 'Connecting...' : 'Login with Metamask'}
            </button>
          )}
        </>
      ) : (
        <form onSubmit={handleRecoverySubmit} className="recovery-form">
          <h3>Password Recovery</h3>
          <p>Enter your email to receive password reset instructions</p>

          <div className="form-group">
            <label htmlFor="recoveryEmail">Email</label>
            <input
              type="email"
              id="recoveryEmail"
              value={recoveryEmail}
              onChange={handleRecoveryEmailChange}
              placeholder="Enter your email"
              required
            />
          </div>

          <div className="recovery-buttons">
            <button type="submit" className="recovery-submit">
              Send Recovery Email
            </button>
            <button
              type="button"
              className="recovery-cancel"
              onClick={() => setShowRecovery(false)}
            >
              Back to Login
            </button>
          </div>
        </form>
      )}
    </div>
  );
};

export default LoginForm;
```

```css
/* LoginForm.css */
.login-container {
  max-width: 400px;
  margin: 0 auto;
  padding: 2rem;
  background: #fff;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.login-container h2 {
  text-align: center;
  margin-bottom: 1.5rem;
  color: #2c3e50;
}

.error-message {
  color: #e74c3c;
  background-color: #fadbd8;
  padding: 0.75rem;
  border-radius: 4px;
  margin-bottom: 1rem;
  text-align: center;
}

.form-group {
  margin-bottom: 1rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  color: #2c3e50;
  font-weight: 500;
}

.form-group input {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 1rem;
}

.form-options {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 1rem 0;
}

.remember-me {
  display: flex;
  align-items: center;
}

.remember-me input {
  margin-right: 0.5rem;
}

.recovery-link {
  background: none;
  border: none;
  color: #3498db;
  cursor: pointer;
  font-size: 0.9rem;
  padding: 0;
}

.recovery-link:hover {
  text-decoration: underline;
}

.login-button {
  width: 100%;
  padding: 0.75rem;
  background-color: #3498db;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 1rem;
  cursor: pointer;
  margin-bottom: 1rem;
}

.login-button:hover {
  background-color: #2980b9;
}

.metamask-button {
  width: 100%;
  padding: 0.75rem;
  background-color: #f6851b;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 1rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
}

.metamask-button:hover {
  background-color: #e2761b;
}

.metamask-button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

.recovery-form {
  margin-top: 1rem;
}

.recovery-form h3 {
  text-align: center;
  margin-bottom: 1rem;
}

.recovery-form p {
  text-align: center;
  margin-bottom: 1.5rem;
  color: #7f8c8d;
}

.recovery-buttons {
  display: flex;
  gap: 1rem;
}

.recovery-submit {
  flex: 1;
  padding: 0.75rem;
  background-color: #3498db;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 1rem;
  cursor: pointer;
}

.recovery-submit:hover {
  background-color: #2980b9;
}

.recovery
