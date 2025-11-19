"""
Generated Code Metadata:
========================
Original URL: https://fi-dapp-git-hotfix-pendle-zircuit-etherfi.vercel.app
Prompt: Describe how to create a user interface for connecting wallets in a DeFi application focused on eETH staking.
Generated: DETERMINISTIC_e7b2b6869f333ab7
Batch ID: 20250612_162404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import React, { useState } from 'react';
import Web3 from 'web3';
import { Button, Modal, Typography } from '@mui/material';

// WalletConnect Component
const WalletConnect = () => {
  // State variables
  const [walletAddress, setWalletAddress] = useState(null); // Stores connected wallet address
  const [isModalOpen, setIsModalOpen] = useState(false); // Controls modal visibility
  const [errorMessage, setErrorMessage] = useState(null); // Stores error messages

  // Function to connect wallet
  const connectWallet = async () => {
    try {
      // Check if Web3 is injected (e.g., by MetaMask)
      if (window.ethereum) {
        const web3 = new Web3(window.ethereum);

        // Request wallet connection
        const accounts = await window.ethereum.request({
          method: 'eth_requestAccounts',
        });

        // Set wallet address
        setWalletAddress(accounts[0]);
        setErrorMessage(null); // Clear any previous errors
      } else {
        // If no Web3 provider is found
        setErrorMessage('No Web3 provider detected. Please install MetaMask.');
      }
    } catch (error) {
      // Handle errors during wallet connection
      setErrorMessage(`Failed to connect wallet: ${error.message}`);
    }
  };

  // Function to disconnect wallet
  const disconnectWallet = () => {
    setWalletAddress(null); // Clear wallet address
    setErrorMessage(null); // Clear error messages
  };

  // Function to toggle modal visibility
  const toggleModal = () => {
    setIsModalOpen(!isModalOpen);
  };

  return (
    <div style={{ textAlign: 'center', marginTop: '20px' }}>
      {/* Display wallet connection status */}
      {walletAddress ? (
        <Typography variant="h6">
          Connected Wallet: {walletAddress}
        </Typography>
      ) : (
        <Typography variant="h6">No Wallet Connected</Typography>
      )}

      {/* Connect/Disconnect Button */}
      <Button
        variant="contained"
        color="primary"
        onClick={walletAddress ? disconnectWallet : connectWallet}
        style={{ marginTop: '10px' }}
      >
        {walletAddress ? 'Disconnect Wallet' : 'Connect Wallet'}
      </Button>

      {/* Error Message */}
      {errorMessage && (
        <Typography
          variant="body2"
          color="error"
          style={{ marginTop: '10px' }}
        >
          {errorMessage}
        </Typography>
      )}

      {/* Modal for additional wallet info */}
      <Button
        variant="outlined"
        color="secondary"
        onClick={toggleModal}
        style={{ marginTop: '10px' }}
      >
        {isModalOpen ? 'Close Wallet Info' : 'View Wallet Info'}
      </Button>

      <Modal open={isModalOpen} onClose={toggleModal}>
        <div
          style={{
            position: 'absolute',
            top: '50%',
            left: '50%',
            transform: 'translate(-50%, -50%)',
            backgroundColor: 'white',
            padding: '20px',
            borderRadius: '8px',
            boxShadow: '0px 4px 6px rgba(0, 0, 0, 0.1)',
          }}
        >
          <Typography variant="h6">Wallet Information</Typography>
          {walletAddress ? (
            <Typography variant="body1">
              Wallet Address: {walletAddress}
            </Typography>
          ) : (
            <Typography variant="body1">
              No wallet connected. Please connect a wallet.
            </Typography>
          )}
          <Button
            variant="contained"
            color="primary"
            onClick={toggleModal}
            style={{ marginTop: '10px' }}
          >
            Close
          </Button>
        </div>
      </Modal>
    </div>
  );
};

export default WalletConnect;
```
