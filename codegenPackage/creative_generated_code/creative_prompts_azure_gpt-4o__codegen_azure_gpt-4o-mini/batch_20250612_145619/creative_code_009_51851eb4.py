"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethfjw.com
Prompt: Create a React component that integrates ETH pledging functionality with a user-friendly interface using ethers.js.
Generated: DETERMINISTIC_51851eb42a47e500
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and hooks
import React, { useState, useEffect } from 'react';
import { ethers } from 'ethers';

// Define the Pledge component
const Pledge = () => {
  // State variables to manage the pledge amount and user feedback
  const [amount, setAmount] = useState('');
  const [message, setMessage] = useState('');
  const [provider, setProvider] = useState(null);
  const [signer, setSigner] = useState(null);

  // Initialize ethers.js provider and signer
  useEffect(() => {
    const initProvider = async () => {
      try {
        // Check if MetaMask is installed
        if (window.ethereum) {
          const newProvider = new ethers.providers.Web3Provider(window.ethereum);
          const newSigner = newProvider.getSigner();
          setProvider(newProvider);
          setSigner(newSigner);
        } else {
          setMessage('Please install MetaMask to use this feature.');
        }
      } catch (error) {
        console.error("Error initializing provider:", error);
        setMessage('Failed to initialize wallet. Please check console for details.');
      }
    };
    initProvider();
  }, []);

  // Function to handle the pledge action
  const handlePledge = async (event) => {
    event.preventDefault();
    setMessage(''); // Reset message

    // Validating input amount
    if (!amount || isNaN(amount) || parseFloat(amount) <= 0) {
      setMessage('Please enter a valid pledge amount.');
      return;
    }
    
    // Convert amount to ethers
    const pledgeAmount = ethers.utils.parseEther(amount);
    
    // Add your contract address and ABI here
    const contractAddress = 'YOUR_CONTRACT_ADDRESS'; 
    const contractABI = [
      // Your contract ABI goes here
    ];
    
    try {
      // Create a new instance of the contract
      const contract = new ethers.Contract(contractAddress, contractABI, signer);
      
      // Call the pledge function on the contract
      const transaction = await contract.pledge({ value: pledgeAmount });
      setMessage('Transaction pending...');
      
      // Wait for the transaction to be confirmed
      await transaction.wait();
      setMessage('Pledge successful! Thank you for your contribution.');
    } catch (error) {
      console.error("Error during pledge transaction:", error);
      setMessage('Transaction failed. Please check console for details.');
    }
  };

  return (
    <div>
      <h1>Pledge ETH</h1>
      <form onSubmit={handlePledge}>
        <div>
          <label htmlFor="amount">Amount (ETH):</label>
          <input
            type="text"
            id="amount"
            value={amount}
            onChange={(e) => setAmount(e.target.value)}
            placeholder="Enter amount to pledge"
          />
        </div>
        <button type="submit">Pledge</button>
      </form>
      {message && <p>{message}</p>}
    </div>
  );
};

export default Pledge;
```
