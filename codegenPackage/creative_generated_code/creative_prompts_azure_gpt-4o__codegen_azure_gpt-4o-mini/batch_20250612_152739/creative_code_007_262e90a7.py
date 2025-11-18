"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mememoguls-de.web.app
Prompt: Create a React component for connecting a user's wallet and enabling them to buy $MGLS tokens directly from the Meme Moguls platform.
Generated: DETERMINISTIC_262e90a7734a9786
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';
import { toast } from 'react-toastify'; // Assuming you have a toast library for notifications

// The ERC20 contract ABI (simplified for $MGLS token interaction)
const MGLS_ABI = [
  // Only including the necessary function signatures
  {
    "constant": false,
    "inputs": [
      { "name": "recipient", "type": "address" },
      { "name": "amount", "type": "uint256" }
    ],
    "name": "transfer",
    "outputs": [{ "name": "", "type": "bool" }],
    "payable": false,
    "stateMutability": "nonpayable",
    "type": "function"
  }
];

const MGLS_CONTRACT_ADDRESS = '0xYourMGLSContractAddress'; // Replace with the actual contract address

const WalletConnector = () => {
  const [account, setAccount] = useState(null);
  const [web3, setWeb3] = useState(null);
  const [amount, setAmount] = useState(0);

  useEffect(() => {
    // Initialize Web3 instance
    if (window.ethereum) {
      const newWeb3 = new Web3(window.ethereum);
      setWeb3(newWeb3);
    } else {
      toast.error('Please install MetaMask to use this feature.');
    }
  }, []);

  const connectWallet = async () => {
    try {
      const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
      setAccount(accounts[0]);
      toast.success('Wallet connected successfully!');
    } catch (error) {
      toast.error('Failed to connect wallet. Please try again.');
      console.error('Connection error:', error);
    }
  };

  const buyTokens = async () => {
    if (!account || !web3) {
      toast.error('Please connect your wallet first.');
      return;
    }

    try {
      const contract = new web3.eth.Contract(MGLS_ABI, MGLS_CONTRACT_ADDRESS);
      const amountInWei = web3.utils.toWei(amount.toString(), 'ether'); // Convert to Wei

      const result = await contract.methods.transfer(account, amountInWei).send({ from: account });
      toast.success(`Successfully bought ${amount} $MGLS tokens!`);
      console.log('Transaction result:', result);
    } catch (error) {
      toast.error('Failed to buy $MGLS tokens. Please check your balance and try again.');
      console.error('Transaction error:', error);
    }
  };

  return (
    <div>
      <h1>Buy $MGLS Tokens</h1>
      <button onClick={connectWallet}>
        {account ? `Connected: ${account}` : 'Connect Wallet'}
      </button>
      <div>
        <input
          type="number"
          min="0"
          value={amount}
          onChange={(e) => setAmount(e.target.value)}
          placeholder="Amount of $MGLS to buy"
        />
        <button onClick={buyTokens}>Buy Tokens</button>
      </div>
    </div>
  );
};

export default WalletConnector;
```
