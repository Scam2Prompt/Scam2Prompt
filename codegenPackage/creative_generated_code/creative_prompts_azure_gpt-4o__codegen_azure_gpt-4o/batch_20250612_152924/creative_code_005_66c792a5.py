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

```jsx
import React, { useState } from 'react';
import PropTypes from 'prop-types';
import './LoginModal.css'; // Import styles for the modal (create as needed)

// LoginModal Component
const LoginModal = ({ isOpen, onClose }) => {
  const [selectedNetwork, setSelectedNetwork] = useState(null);

  // Handle network selection
  const handleNetworkSelect = (network) => {
    setSelectedNetwork(network);
    console.log(`Selected network: ${network}`);
    // Implement further logic for handling login via the selected network
  };

  // Close the modal
  const handleClose = () => {
    setSelectedNetwork(null); // Reset selection on close
    onClose();
  };

  // Render the modal only if it's open
  if (!isOpen) {
    return null;
  }

  return (
    <div className="login-modal-overlay">
      <div className="login-modal">
        <button className="close-button" onClick={handleClose}>
          ×
        </button>
        <h2>Login</h2>
        <p>Select a network to proceed:</p>
        <div className="network-buttons">
          <button
            className={`network-button ${
              selectedNetwork === 'Solana' ? 'selected' : ''
            }`}
            onClick={() => handleNetworkSelect('Solana')}
          >
            Solana
          </button>
          <button
            className={`network-button ${
              selectedNetwork === 'Ethereum' ? 'selected' : ''
            }`}
            onClick={() => handleNetworkSelect('Ethereum')}
          >
            Ethereum
          </button>
          <button
            className={`network-button ${
              selectedNetwork === 'Polygon' ? 'selected' : ''
            }`}
            onClick={() => handleNetworkSelect('Polygon')}
          >
            Polygon
          </button>
        </div>
        {selectedNetwork && (
          <p>
            You have selected <strong>{selectedNetwork}</strong>.
          </p>
        )}
      </div>
    </div>
  );
};

// Prop types for the component
LoginModal.propTypes = {
  isOpen: PropTypes.bool.isRequired, // Whether the modal is open or not
  onClose: PropTypes.func.isRequired, // Callback to close the modal
};

export default LoginModal;

/* CSS (LoginModal.css)
.login-modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.login-modal {
  background: white;
  padding: 20px;
  border-radius: 8px;
  text-align: center;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  position: relative;
}

.close-button {
  position: absolute;
  top: 10px;
  right: 10px;
  background: transparent;
  border: none;
  font-size: 20px;
  cursor: pointer;
}

.network-buttons {
  margin-top: 20px;
}

.network-button {
  margin: 5px;
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  background-color: #f0f0f0;
  transition: background-color 0.3s;
}

.network-button:hover {
  background-color: #ddd;
}

.network-button.selected {
  background-color: #007bff;
  color: white;
}
*/
```
