"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-coolcoinwtf.pages.dev
Prompt: Create a web interface for connecting a wallet and claiming $COOL tokens, ensuring it integrates with the Coolman Universe NFT Checker tool.
Generated: DETERMINISTIC_6ddee3c09f4a57a3
Batch ID: 20250612_153526
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
import './App.css';

// Configure the contract address and ABI for the $COOL token
const contractAddress = '0xYourContractAddress'; // Replace with the actual contract address
const contractABI = [ /* Your contract ABI here */ ];

const App = () => {
  // State variables
  const [account, setAccount] = useState('');
  const [web3, setWeb3] = useState(null);
  const [contract, setContract] = useState(null);
  const [isConnected, setIsConnected] = useState(false);
  const [message, setMessage] = useState('');

  // Initialize Web3 and contract
  useEffect(() => {
    const initWeb3 = async () => {
      if (window.ethereum) {
        const web3Instance = new Web3(window.ethereum);
        setWeb3(web3Instance);

        // Request account access if needed
        try {
          await window.ethereum.enable();
          const accounts = await web3Instance.eth.getAccounts();
          setAccount(accounts[0]);
          setIsConnected(true);
        } catch (error) {
          console.error("User denied account access");
          setMessage('Failed to connect wallet. Please try again.');
        }

        // Initialize the contract
        const contractInstance = new web3Instance.eth.Contract(contractABI, contractAddress);
        setContract(contractInstance);
      } else {
        console.error('Please install MetaMask!');
        setMessage('MetaMask is not installed. Please install it to use this feature.');
      }
    };

    initWeb3();
  }, []);

  // Function to claim $COOL tokens
  const claimTokens = async () => {
    if (!contract || !account) {
      setMessage('Wallet not connected or contract not initialized.');
      return;
    }

    try {
      // Call the contract's claim function
      const response = await contract.methods.claim().send({ from: account });
      console.log('Tokens claimed successfully:', response);
      setMessage('Successfully claimed $COOL tokens!');
    } catch (error) {
      console.error('Error claiming tokens:', error);
      setMessage('Error claiming tokens. Please try again.');
    }
  };

  return (
    <div className="App">
      <h1>Claim $COOL Tokens</h1>
      {isConnected ? (
        <div>
          <p>Connected account: {account}</p>
          <button onClick={claimTokens}>Claim Tokens</button>
        </div>
      ) : (
        <button onClick={() => window.ethereum && window.ethereum.enable()}>Connect Wallet</button>
      )}
      {message && <p>{message}</p>}
    </div>
  );
};

export default App;
```

### App.css
```css
.App {
  text-align: center;
  margin-top: 50px;
}

button {
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
  margin: 10px;
}

p {
  font-size: 18px;
}
```

### Instructions:
1. Replace `0xYourContractAddress` with the actual Ethereum contract address for the $COOL token.
2. Replace the comment `/* Your contract ABI here */` with the actual ABI of the smart contract.
3. Ensure you have React and Web3.js installed in your project by running:
   ```bash
   npm install react web3
   ```
4. You can use this code as part of a larger React application. Make sure to handle additional scenarios based on your requirements.
