"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://matrica15.vercel.app
Prompt: Create a React component for a login modal that includes options for Solana, Ethereum, and Polygon networks, inspired by the Matrica website design.
Generated: DETERMINISTIC_66c792a5119dc635
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useState } from 'react';
import PropTypes from 'prop-types';
import './LoginModal.css'; // Ensure to create a CSS file for styling

const LoginModal = ({ isOpen, onClose }) => {
  const [selectedNetwork, setSelectedNetwork] = useState('');
  const [error, setError] = useState('');

  // Handle network selection
  const handleNetworkSelection = (network) => {
    setSelectedNetwork(network);
    setError('');
  };

  // Handle login action
  const handleLogin = async () => {
    if (!selectedNetwork) {
      setError('Please select a network to log in.');
      return;
    }

    try {
      // Placeholder for login logic (e.g., connecting to the selected network)
      console.log(`Logging in with ${selectedNetwork} network...`);
      // Add your login logic here (e.g., web3 provider connection)
      // await loginWithNetwork(selectedNetwork);
      onClose(); // Close modal on successful login
    } catch (err) {
      setError('Login failed. Please try again.'); // Error handling
      console.error('Login error:', err);
    }
  };

  // Render the modal
  return (
    isOpen && (
      <div className="login-modal">
        <div className="modal-content">
          <button className="close-button" onClick={onClose}>
            &times;
          </button>
          <h2>Login</h2>
          <div className="network-selection">
            <h3>Select Network</h3>
            <button 
              className={`network-button ${selectedNetwork === 'Solana' ? 'active' : ''}`} 
              onClick={() => handleNetworkSelection('Solana')}
            >
              Solana
            </button>
            <button 
              className={`network-button ${selectedNetwork === 'Ethereum' ? 'active' : ''}`} 
              onClick={() => handleNetworkSelection('Ethereum')}
            >
              Ethereum
            </button>
            <button 
              className={`network-button ${selectedNetwork === 'Polygon' ? 'active' : ''}`} 
              onClick={() => handleNetworkSelection('Polygon')}
            >
              Polygon
            </button>
          </div>
          {error && <p className="error-message">{error}</p>}
          <button className="login-button" onClick={handleLogin}>
            Login
          </button>
        </div>
      </div>
    )
  );
};

// PropTypes for type checking
LoginModal.propTypes = {
  isOpen: PropTypes.bool.isRequired,
  onClose: PropTypes.func.isRequired,
};

export default LoginModal;
```

```css
/* LoginModal.css */
.login-modal {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-content {
  background: #fff;
  padding: 20px;
  border-radius: 8px;
  width: 300px;
  text-align: center;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.close-button {
  position: absolute;
  top: 10px;
  right: 15px;
  border: none;
  background: transparent;
  cursor: pointer;
}

.network-selection {
  margin: 20px 0;
}

.network-button {
  margin: 5px;
  padding: 10px 15px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  background-color: #e0e0e0;
  transition: background-color 0.3s;
}

.network-button.active {
  background-color: #007bff;
  color: white;
}

.error-message {
  color: red;
}

.login-button {
  padding: 10px 15px;
  border: none;
  border-radius: 5px;
  background-color: #28a745;
  color: white;
  cursor: pointer;
  transition: background-color 0.3s;
}

.login-button:hover {
  background-color: #218838;
}
```
