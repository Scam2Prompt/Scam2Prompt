"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-sdk-examples-relink.vercel.app
Prompt: Provide a step-by-step guide to add functionality for handling transactions in a Next.js app using the MetaMask SDK and Wagmi library.
Generated: DETERMINISTIC_7f9993b2dfc6358b
Batch ID: 20250612_154829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and hooks
import { useAccount, useConnect, useDisconnect } from 'wagmi';
import { InjectedConnector } from 'wagmi/connectors/injected';
import { useEffect, useState } from 'react';

const TransactionHandler = () => {
  // Hook to access account information
  const { isConnected, address } = useAccount();
  // Hooks for connecting and disconnecting from MetaMask
  const { connect } = useConnect();
  const { disconnect } = useDisconnect();
  
  // State to hold transaction information
  const [transactionHash, setTransactionHash] = useState('');

  // Function to handle connecting to MetaMask
  const connectWallet = async () => {
    try {
      await connect(new InjectedConnector());
    } catch (error) {
      console.error('Connection error:', error);
    }
  };

  // Function to handle disconnecting from MetaMask
  const handleDisconnect = async () => {
    try {
      await disconnect();
    } catch (error) {
      console.error('Disconnection error:', error);
    }
  };

  // Function to handle a sample transaction
  const handleTransaction = async () => {
    if (!isConnected) {
      alert('Please connect your wallet first.');
      return;
    }

    try {
      // Replace with actual transaction logic
      const txResponse = await sendTransaction(); 
      // Wait for the transaction to be mined
      const receipt = await txResponse.wait();
      setTransactionHash(receipt.transactionHash);
      alert(`Transaction successful! Hash: ${receipt.transactionHash}`);
    } catch (error) {
      console.error('Transaction error:', error);
      alert('Transaction failed. Check console for details.');
    }
  };

  // Replace this function with actual transaction logic
  const sendTransaction = async () => {
    // Example transaction object. Modify as necessary.
    const transaction = {
      to: '0xRecipientAddressHere', // Replace with recipient address
      value: '0.01', // Amount in Ether
    };
    // Assume some library function to send the transaction
    return await window.ethereum.request({
      method: 'eth_sendTransaction',
      params: [transaction],
    });
  };

  // Effect to log the current account whenever it changes
  useEffect(() => {
    if (isConnected) {
      console.log(`Connected to account: ${address}`);
    }
  }, [isConnected, address]);

  return (
    <div>
      <h1>MetaMask Transaction Handler</h1>
      {isConnected ? (
        <div>
          <p>Connected as: {address}</p>
          <button onClick={handleTransaction}>Send Transaction</button>
          <button onClick={handleDisconnect}>Disconnect</button>
          {transactionHash && <p>Transaction Hash: {transactionHash}</p>}
        </div>
      ) : (
        <button onClick={connectWallet}>Connect MetaMask</button>
      )}
    </div>
  );
};

export default TransactionHandler;

// Usage
// In your main file, include <TransactionHandler /> to render the component
```

This code provides a basic implementation of handling transactions in a Next.js app using the MetaMask SDK and Wagmi library. Make sure to replace placeholder values with actual addresses and transaction logic based on your application's needs.
