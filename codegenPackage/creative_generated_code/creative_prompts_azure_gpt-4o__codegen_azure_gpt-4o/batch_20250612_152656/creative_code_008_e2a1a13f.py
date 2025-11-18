"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gaimin.pages.dev
Prompt: Write code for a Terms of Use and Privacy Policy agreement popup that appears when a user connects their wallet, similar to the Gaimin-Portal implementation.
Generated: DETERMINISTIC_e2a1a13f32cbd842
Batch ID: 20250612_152656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary dependencies
import React, { useState } from 'react';
import Modal from 'react-modal'; // Modal package for popup
import PropTypes from 'prop-types'; // PropTypes for type checking

// Custom styles for the modal popup
const modalStyles = {
  overlay: {
    backgroundColor: 'rgba(0, 0, 0, 0.5)',
  },
  content: {
    top: '50%',
    left: '50%',
    right: 'auto',
    bottom: 'auto',
    marginRight: '-50%',
    transform: 'translate(-50%, -50%)',
    padding: '20px',
    borderRadius: '8px',
    width: '90%',
    maxWidth: '500px',
  },
};

// TermsOfUseAndPrivacyPolicy Component
const TermsOfUseAndPrivacyPolicy = ({ onAccept, onReject }) => {
  const [isOpen, setIsOpen] = useState(true); // State to track modal visibility

  // Close the modal
  const closeModal = () => {
    setIsOpen(false);
  };

  // Handle acceptance
  const handleAccept = () => {
    closeModal();
    onAccept(); // Callback function for acceptance
  };

  // Handle rejection
  const handleReject = () => {
    closeModal();
    onReject(); // Callback function for rejection
  };

  return (
    <Modal isOpen={isOpen} onRequestClose={closeModal} style={modalStyles}>
      <h2>Terms of Use & Privacy Policy</h2>
      <p>
        By connecting your wallet, you agree to our Terms of Use and Privacy
        Policy. Please review the details carefully before proceeding.
      </p>
      <div style={{ display: 'flex', justifyContent: 'space-between', marginTop: '20px' }}>
        <button
          onClick={handleReject}
          style={{
            padding: '10px 20px',
            border: 'none',
            background: '#e74c3c',
            color: '#fff',
            borderRadius: '4px',
            cursor: 'pointer',
          }}
        >
          Decline
        </button>
        <button
          onClick={handleAccept}
          style={{
            padding: '10px 20px',
            border: 'none',
            background: '#2ecc71',
            color: '#fff',
            borderRadius: '4px',
            cursor: 'pointer',
          }}
        >
          Accept
        </button>
      </div>
    </Modal>
  );
};

// PropTypes validation
TermsOfUseAndPrivacyPolicy.propTypes = {
  onAccept: PropTypes.func.isRequired, // Callback for acceptance
  onReject: PropTypes.func.isRequired, // Callback for rejection
};

// Example Parent Component
const WalletConnection = () => {
  const handleAccept = () => {
    console.log('User accepted terms');
    // Perform wallet connection logic here
  };

  const handleReject = () => {
    console.log('User rejected terms');
    // Handle rejection logic here (e.g., disabling wallet connection)
  };

  return (
    <div>
      <h1>Connect Your Wallet</h1>
      <TermsOfUseAndPrivacyPolicy onAccept={handleAccept} onReject={handleReject} />
      {/* The rest of the wallet connection UI */}
    </div>
  );
};

export default WalletConnection;
```
