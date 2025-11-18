"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://matrica19.vercel.app
Prompt: Create a React component for a modal window that allows users to select a blockchain network (Solana, Ethereum, Polygon) and integrates with a login system, similar to the Matrica webpage.
Generated: DETERMINISTIC_493d8ad6c9cdc93d
Batch ID: 20250612_153400
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
import './Modal.css'; // Importing CSS for modal styling

/**
 * Modal component for selecting a blockchain network.
 * 
 * @param {Object} props - Component properties
 * @param {boolean} props.isOpen - Flag to control modal visibility
 * @param {function} props.onClose - Callback function to close the modal
 * @param {function} props.onNetworkSelect - Callback function when a network is selected
 */
const NetworkModal = ({ isOpen, onClose, onNetworkSelect }) => {
  // Local state to track the selected network
  const [selectedNetwork, setSelectedNetwork] = useState('');

  // List of available blockchain networks
  const networks = ['Solana', 'Ethereum', 'Polygon'];

  // Handles the network selection and calls the provided callback
  const handleNetworkSelect = (network) => {
    setSelectedNetwork(network);
    onNetworkSelect(network);
  };

  // Handles the modal close action
  const handleClose = () => {
    setSelectedNetwork('');
    onClose();
  };

  // Prevents background scrolling when modal is open
  if (!isOpen) return null;

  return (
    <div className="modal-overlay">
      <div className="modal-content">
        <h2>Select a Blockchain Network</h2>
        <div className="network-list">
          {networks.map((network) => (
            <button
              key={network}
              className={`network-button ${selectedNetwork === network ? 'selected' : ''}`}
              onClick={() => handleNetworkSelect(network)}
            >
              {network}
            </button>
          ))}
        </div>
        <button className="modal-close" onClick={handleClose}>
          Close
        </button>
      </div>
    </div>
  );
};

// Prop type validation
NetworkModal.propTypes = {
  isOpen: PropTypes.bool.isRequired,
  onClose: PropTypes.func.isRequired,
  onNetworkSelect: PropTypes.func.isRequired,
};

export default NetworkModal;
```

```css
/* Modal.css */
.modal-overlay {
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
  background-color: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
  width: 300px;
}

.network-list {
  margin: 20px 0;
}

.network-button {
  padding: 10px;
  margin: 5px 0;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.network-button.selected {
  background-color: #007bff;
  color: white;
}

.network-button:hover {
  background-color: #f0f0f0;
}

.modal-close {
  background-color: #dc3545;
  color: white;
  padding: 10px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
```
