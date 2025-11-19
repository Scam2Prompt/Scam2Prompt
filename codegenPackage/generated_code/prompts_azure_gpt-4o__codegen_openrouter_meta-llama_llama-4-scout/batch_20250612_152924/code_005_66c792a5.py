"""
Generated Code Metadata:
========================
Original URL: https://matrica15.vercel.app
Prompt: Create a React component for a login modal that includes options for Solana, Ethereum, and Polygon networks, inspired by the Matrica website design.
Generated: DETERMINISTIC_66c792a5119dc635
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// LoginModal.js
import React, { useState } from 'react';
import './LoginModal.css';

/**
 * LoginModal component props
 * @typedef {Object} LoginModalProps
 * @property {function} onClose - callback function to close the modal
 */

/**
 * LoginModal component
 * @param {LoginModalProps} props
 * @returns {JSX.Element}
 */
function LoginModal(props) {
  const { onClose } = props;
  const [selectedNetwork, setSelectedNetwork] = useState(null);

  const networks = [
    {
      id: 1,
      name: 'Solana',
      icon: 'solana-logo.png',
    },
    {
      id: 2,
      name: 'Ethereum',
      icon: 'ethereum-logo.png',
    },
    {
      id: 3,
      name: 'Polygon',
      icon: 'polygon-logo.png',
    },
  ];

  const handleNetworkSelect = (network) => {
    setSelectedNetwork(network);
  };

  const handleLogin = () => {
    if (!selectedNetwork) {
      alert('Please select a network');
      return;
    }
    // Add login logic here
    console.log(`Login with ${selectedNetwork.name}`);
  };

  return (
    <div className="login-modal">
      <div className="modal-header">
        <h2>Login</h2>
        <button className="close-button" onClick={onClose}>
          <svg
            width="24"
            height="24"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="2"
            strokeLinecap="round"
            strokeLinejoin="round"
          >
            <line x1="18" y1="6" x2="6" y2="18" />
            <line x1="6" y1="6" x2="18" y2="18" />
          </svg>
        </button>
      </div>
      <div className="modal-content">
        <p>Select a network to login</p>
        <div className="network-options">
          {networks.map((network) => (
            <div
              key={network.id}
              className={`network-option ${
                selectedNetwork === network ? 'selected' : ''
              }`}
              onClick={() => handleNetworkSelect(network)}
            >
              <img src={network.icon} alt={network.name} />
              <span>{network.name}</span>
            </div>
          ))}
        </div>
        <button className="login-button" onClick={handleLogin}>
          Login
        </button>
      </div>
    </div>
  );
}

export default LoginModal;
```

```css
/* LoginModal.css */
.login-modal {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: #fff;
  padding: 24px;
  border-radius: 16px;
  box-shadow: 0 0 16px rgba(0, 0, 0, 0.2);
  width: 400px;
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
}

.close-button {
  background-color: transparent;
  border: none;
  cursor: pointer;
}

.close-button svg {
  width: 24px;
  height: 24px;
}

.modal-content {
  text-align: center;
}

.network-options {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  margin-bottom: 16px;
}

.network-option {
  margin: 8px;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 8px;
  cursor: pointer;
}

.network-option.selected {
  border-color: #337ab7;
}

.network-option img {
  width: 24px;
  height: 24px;
  margin-right: 8px;
}

.login-button {
  background-color: #337ab7;
  color: #fff;
  border: none;
  padding: 8px 16px;
  border-radius: 8px;
  cursor: pointer;
}

.login-button:hover {
  background-color: #23527c;
}
```
