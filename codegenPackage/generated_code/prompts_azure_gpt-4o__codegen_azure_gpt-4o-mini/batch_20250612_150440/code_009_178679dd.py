"""
Generated Code Metadata:
========================
Original URL: https://arbitrum-svd.vercel.app
Prompt: Create a front-end interface using React and Web3.js for users to mint, stake, and withdraw "FREE SHAVACADOO" tokens.
Generated: DETERMINISTIC_178679dd2a2388c6
Batch ID: 20250612_150440
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
import { Contract } from 'web3-eth-contract';
import TokenABI from './TokenABI.json'; // Import the ABI of the token contract

// Define the contract address (replace with your actual contract address)
const TOKEN_CONTRACT_ADDRESS = '0xYourTokenContractAddress';

const App = () => {
  // State variables
  const [account, setAccount] = useState('');
  const [web3, setWeb3] = useState(null);
  const [contract, setContract] = useState(null);
  const [amount, setAmount] = useState(0);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  // Initialize Web3 and contract
  useEffect(() => {
    const initWeb3 = async () => {
      try {
        // Check if MetaMask is installed
        if (window.ethereum) {
          const web3Instance = new Web3(window.ethereum);
          await window.ethereum.request({ method: 'eth_requestAccounts' });
          const accounts = await web3Instance.eth.getAccounts();
          setAccount(accounts[0]);
          setWeb3(web3Instance);
          const tokenContract = new web3Instance.eth.Contract(TokenABI, TOKEN_CONTRACT_ADDRESS);
          setContract(tokenContract);
        } else {
          setError('Please install MetaMask to use this app.');
        }
      } catch (err) {
        setError('Failed to connect to Web3: ' + err.message);
      }
    };

    initWeb3();
  }, []);

  // Function to mint tokens
  const mintTokens = async () => {
    if (!contract) return;
    setLoading(true);
    setError('');
    try {
      await contract.methods.mint(account, amount).send({ from: account });
      alert('Tokens minted successfully!');
    } catch (err) {
      setError('Minting failed: ' + err.message);
    } finally {
      setLoading(false);
    }
  };

  // Function to stake tokens
  const stakeTokens = async () => {
    if (!contract) return;
    setLoading(true);
    setError('');
    try {
      await contract.methods.stake(amount).send({ from: account });
      alert('Tokens staked successfully!');
    } catch (err) {
      setError('Staking failed: ' + err.message);
    } finally {
      setLoading(false);
    }
  };

  // Function to withdraw tokens
  const withdrawTokens = async () => {
    if (!contract) return;
    setLoading(true);
    setError('');
    try {
      await contract.methods.withdraw(amount).send({ from: account });
      alert('Tokens withdrawn successfully!');
    } catch (err) {
      setError('Withdrawal failed: ' + err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h1>FREE SHAVACADOO Token Interface</h1>
      <p>Connected Account: {account}</p>
      <input
        type="number"
        value={amount}
        onChange={(e) => setAmount(e.target.value)}
        placeholder="Amount"
      />
      <div>
        <button onClick={mintTokens} disabled={loading}>
          Mint Tokens
        </button>
        <button onClick={stakeTokens} disabled={loading}>
          Stake Tokens
        </button>
        <button onClick={withdrawTokens} disabled={loading}>
          Withdraw Tokens
        </button>
      </div>
      {loading && <p>Loading...</p>}
      {error && <p style={{ color: 'red' }}>{error}</p>}
    </div>
  );
};

export default App;
```

**Note:** Ensure you replace `0xYourTokenContractAddress` with the actual address of your token contract and provide the correct ABI in `TokenABI.json`.
