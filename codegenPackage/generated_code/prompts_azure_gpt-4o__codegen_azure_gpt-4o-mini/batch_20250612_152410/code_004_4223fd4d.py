"""
Generated Code Metadata:
========================
Original URL: https://btcetfcoinn.pages.dev
Prompt: Develop a DApp interface for buying and staking BTCETF tokens, including wallet connection functionality and presale purchase options using ETH, BNB, or USDT.
Generated: DETERMINISTIC_4223fd4d49045619
Batch ID: 20250612_152410
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
import { ethers } from 'ethers';
import './App.css'; // Import your CSS for styling

// Define the contract ABI and address
const CONTRACT_ABI = [ /* ABI goes here */ ];
const CONTRACT_ADDRESS = '0xYourContractAddressHere';

const App = () => {
  const [account, setAccount] = useState(null);
  const [web3, setWeb3] = useState(null);
  const [amount, setAmount] = useState('');
  const [tokenType, setTokenType] = useState('ETH'); // Default to ETH
  const [error, setError] = useState('');

  // Initialize Web3 and connect to wallet
  useEffect(() => {
    const initWeb3 = async () => {
      if (window.ethereum) {
        const web3Instance = new Web3(window.ethereum);
        setWeb3(web3Instance);
        try {
          // Request account access
          const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
          setAccount(accounts[0]);
        } catch (err) {
          setError('User denied account access');
        }
      } else {
        setError('Please install MetaMask!');
      }
    };
    initWeb3();
  }, []);

  // Function to handle token purchase
  const buyTokens = async () => {
    if (!amount || isNaN(amount) || amount <= 0) {
      setError('Please enter a valid amount');
      return;
    }

    try {
      const provider = new ethers.providers.Web3Provider(window.ethereum);
      const signer = provider.getSigner();
      const contract = new ethers.Contract(CONTRACT_ADDRESS, CONTRACT_ABI, signer);

      let tx;
      if (tokenType === 'ETH') {
        tx = await contract.buyWithETH({ value: ethers.utils.parseEther(amount) });
      } else if (tokenType === 'BNB') {
        tx = await contract.buyWithBNB({ value: ethers.utils.parseEther(amount) });
      } else if (tokenType === 'USDT') {
        const usdtContract = new ethers.Contract('0xYourUSDTContractAddress', USDT_ABI, signer);
        const amountInWei = ethers.utils.parseUnits(amount, 6); // Assuming USDT has 6 decimals
        await usdtContract.approve(CONTRACT_ADDRESS, amountInWei);
        tx = await contract.buyWithUSDT(amountInWei);
      }

      await tx.wait();
      alert('Tokens purchased successfully!');
    } catch (err) {
      setError('Transaction failed: ' + err.message);
    }
  };

  return (
    <div className="App">
      <h1>BTCETF Token Purchase</h1>
      {error && <p className="error">{error}</p>}
      <div>
        <label>
          Amount:
          <input
            type="number"
            value={amount}
            onChange={(e) => setAmount(e.target.value)}
            placeholder="Enter amount"
          />
        </label>
      </div>
      <div>
        <label>
          Token Type:
          <select value={tokenType} onChange={(e) => setTokenType(e.target.value)}>
            <option value="ETH">ETH</option>
            <option value="BNB">BNB</option>
            <option value="USDT">USDT</option>
          </select>
        </label>
      </div>
      <button onClick={buyTokens}>Buy Tokens</button>
    </div>
  );
};

export default App;
```

**Note:** Replace `/* ABI goes here */`, `0xYourContractAddressHere`, and `0xYourUSDTContractAddress` with the actual ABI and contract addresses. Also, ensure you have the appropriate USDT ABI defined in your code.
