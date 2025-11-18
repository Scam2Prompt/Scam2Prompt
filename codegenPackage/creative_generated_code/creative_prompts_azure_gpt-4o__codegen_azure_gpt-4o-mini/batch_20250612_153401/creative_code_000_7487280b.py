"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-jessepollak-ebv.pages.dev
Prompt: Write code to integrate a "Connect Wallet" feature for a decentralized application, inspired by Jesse Pollak's work on Coinbase Wallet and Base. Include best practices for security and user experience.
Generated: DETERMINISTIC_7487280b5037cd0a
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';
import { Modal, Button } from 'react-bootstrap'; // Assuming using React Bootstrap for modal

// ConnectWallet Component
const ConnectWallet = ({ onConnect }) => {
  const [showModal, setShowModal] = useState(false);
  const [error, setError] = useState(null);
  const [accounts, setAccounts] = useState([]);

  // Initialize Web3
  const web3 = new Web3(window.ethereum);

  // Function to handle wallet connection
  const connectWallet = async () => {
    try {
      // Request account access
      const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
      setAccounts(accounts);
      setError(null);
      onConnect(accounts[0]); // Pass the connected account to the parent component
      setShowModal(false); // Close the modal on successful connection
    } catch (err) {
      // Handle errors
      console.error('Error connecting to wallet:', err);
      setError('Failed to connect wallet. Please try again.');
    }
  };

  // Effect to handle Ethereum account changes
  useEffect(() => {
    const handleAccountChange = (accounts) => {
      if (accounts.length > 0) {
        setAccounts(accounts);
        onConnect(accounts[0]); // Update the connected account
      }
    };

    // Listen for account changes
    window.ethereum.on('accountsChanged', handleAccountChange);

    // Clean up the listener on component unmount
    return () => {
      window.ethereum.removeListener('accountsChanged', handleAccountChange);
    };
  }, [onConnect]);

  return (
    <>
      <Button variant="primary" onClick={() => setShowModal(true)}>
        Connect Wallet
      </Button>

      <Modal show={showModal} onHide={() => setShowModal(false)}>
        <Modal.Header closeButton>
          <Modal.Title>Connect Your Wallet</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          {error && <div className="alert alert-danger">{error}</div>}
          <p>Please select a wallet to connect:</p>
          <Button onClick={connectWallet}>Connect MetaMask</Button>
        </Modal.Body>
      </Modal>
    </>
  );
};

export default ConnectWallet;
```

### Notes
- This code uses React and Web3.js for connecting to an Ethereum wallet (e.g., MetaMask).
- It includes a modal for user interaction and handles errors gracefully.
- The connected wallet address is communicated back to the parent component using the `onConnect` callback. 
- The error handling provides feedback to the user if the connection fails.
