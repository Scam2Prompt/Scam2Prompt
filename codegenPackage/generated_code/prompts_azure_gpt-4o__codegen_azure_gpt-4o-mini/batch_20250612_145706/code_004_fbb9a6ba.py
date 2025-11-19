"""
Generated Code Metadata:
========================
Original URL: https://secureweb3.pages.dev
Prompt: Write code to create a user-friendly interface for connecting wallets and managing web3 interactions, inspired by SecureWeb3's design principles.
Generated: DETERMINISTIC_fbb9a6baa8a141f6
Batch ID: 20250612_145706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';
import { Button, Modal, Input, notification } from 'antd';
import 'antd/dist/antd.css'; // Import Ant Design styles

// Initialize Web3
const web3 = new Web3(window.ethereum);

// Main App Component
const App = () => {
  const [account, setAccount] = useState(null);
  const [isModalVisible, setIsModalVisible] = useState(false);
  const [transactionHash, setTransactionHash] = useState('');

  // Function to connect wallet
  const connectWallet = async () => {
    try {
      // Request account access
      const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
      setAccount(accounts[0]);
      notification.success({ message: 'Wallet connected successfully!' });
    } catch (error) {
      console.error('Error connecting wallet:', error);
      notification.error({ message: 'Failed to connect wallet. Please try again.' });
    }
  };

  // Function to send a transaction
  const sendTransaction = async () => {
    if (!account) {
      notification.warning({ message: 'Please connect your wallet first.' });
      return;
    }

    const transactionParameters = {
      to: '0xRecipientAddressHere', // Replace with recipient address
      from: account,
      value: web3.utils.toHex(web3.utils.toWei('0.01', 'ether')), // Sending 0.01 ETH
    };

    try {
      const txHash = await window.ethereum.request({
        method: 'eth_sendTransaction',
        params: [transactionParameters],
      });
      setTransactionHash(txHash);
      notification.success({ message: 'Transaction sent successfully!', description: `Transaction Hash: ${txHash}` });
    } catch (error) {
      console.error('Transaction error:', error);
      notification.error({ message: 'Transaction failed. Please try again.' });
    }
  };

  // Function to handle modal visibility
  const handleModal = () => {
    setIsModalVisible(!isModalVisible);
  };

  return (
    <div style={{ padding: '20px' }}>
      <h1>SecureWeb3 Wallet Connector</h1>
      <Button type="primary" onClick={connectWallet}>
        Connect Wallet
      </Button>
      {account && (
        <div style={{ marginTop: '20px' }}>
          <h2>Connected Account: {account}</h2>
          <Button type="default" onClick={handleModal}>
            Send Transaction
          </Button>
        </div>
      )}
      <Modal
        title="Send Transaction"
        visible={isModalVisible}
        onCancel={handleModal}
        footer={[
          <Button key="back" onClick={handleModal}>
            Cancel
          </Button>,
          <Button key="submit" type="primary" onClick={sendTransaction}>
            Send
          </Button>,
        ]}
      >
        <Input placeholder="Recipient Address" style={{ marginBottom: '10px' }} />
        <Input placeholder="Amount (ETH)" />
      </Modal>
      {transactionHash && (
        <div style={{ marginTop: '20px' }}>
          <h3>Last Transaction Hash:</h3>
          <p>{transactionHash}</p>
        </div>
      )}
    </div>
  );
};

export default App;
```
