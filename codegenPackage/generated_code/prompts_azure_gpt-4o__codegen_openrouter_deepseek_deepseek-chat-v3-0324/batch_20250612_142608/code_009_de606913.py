"""
Generated Code Metadata:
========================
Original URL: https://wap.xushuishiwu.cn
Prompt: Create a tutorial for integrating MetaMask wallet functionality into a React application, including token management and transaction execution, based on the "MetaMask钱包和imToken钱包" comparison section.
Generated: DETERMINISTIC_de606913a51e70f6
Batch ID: 20250612_142608
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
import detectEthereumProvider from '@metamask/detect-provider';

// Token contract ABI (simplified ERC20 interface)
const ERC20_ABI = [
  {
    "constant": true,
    "inputs": [{ "name": "_owner", "type": "address" }],
    "name": "balanceOf",
    "outputs": [{ "name": "balance", "type": "uint256" }],
    "type": "function"
  },
  {
    "constant": false,
    "inputs": [
      { "name": "_to", "type": "address" },
      { "name": "_value", "type": "uint256" }
    ],
    "name": "transfer",
    "outputs": [{ "name": "success", "type": "bool" }],
    "type": "function"
  }
];

const MetaMaskIntegration = () => {
  const [web3, setWeb3] = useState(null);
  const [account, setAccount] = useState('');
  const [balance, setBalance] = useState('0');
  const [tokenBalance, setTokenBalance] = useState('0');
  const [tokenAddress, setTokenAddress] = useState('');
  const [recipient, setRecipient] = useState('');
  const [amount, setAmount] = useState('0');
  const [network, setNetwork] = useState('');
  const [error, setError] = useState('');

  // Initialize Web3 and MetaMask connection
  const initWeb3 = async () => {
    try {
      const provider = await detectEthereumProvider();
      
      if (provider) {
        const web3Instance = new Web3(provider);
        setWeb3(web3Instance);
        
        // Request account access
        const accounts = await provider.request({ method: 'eth_requestAccounts' });
        setAccount(accounts[0]);
        
        // Get network ID
        const chainId = await provider.request({ method: 'eth_chainId' });
        setNetwork(getNetworkName(chainId));
        
        // Set up event listeners
        provider.on('accountsChanged', (accounts) => {
          setAccount(accounts[0] || '');
        });
        
        provider.on('chainChanged', (chainId) => {
          window.location.reload();
        });
        
        // Get initial balance
        getEthBalance(web3Instance, accounts[0]);
      } else {
        setError('Please install MetaMask!');
      }
    } catch (err) {
      setError(`Error connecting to MetaMask: ${err.message}`);
    }
  };

  // Get ETH balance
  const getEthBalance = async (web3Instance, account) => {
    try {
      const balance = await web3Instance.eth.getBalance(account);
      setBalance(web3Instance.utils.fromWei(balance, 'ether'));
    } catch (err) {
      setError(`Error fetching balance: ${err.message}`);
    }
  };

  // Get token balance
  const getTokenBalance = async () => {
    if (!web3 || !tokenAddress || !account) return;
    
    try {
      const tokenContract = new web3.eth.Contract(ERC20_ABI, tokenAddress);
      const balance = await tokenContract.methods.balanceOf(account).call();
      setTokenBalance(web3.utils.fromWei(balance, 'ether'));
    } catch (err) {
      setError(`Error fetching token balance: ${err.message}`);
    }
  };

  // Send ETH transaction
  const sendTransaction = async () => {
    if (!web3 || !recipient || !amount) return;
    
    try {
      const tx = {
        from: account,
        to: recipient,
        value: web3.utils.toWei(amount, 'ether')
      };
      
      const txHash = await web3.eth.sendTransaction(tx);
      console.log('Transaction successful:', txHash);
      getEthBalance(web3, account);
    } catch (err) {
      setError(`Transaction failed: ${err.message}`);
    }
  };

  // Send token transaction
  const sendTokenTransaction = async () => {
    if (!web3 || !tokenAddress || !recipient || !amount) return;
    
    try {
      const tokenContract = new web3.eth.Contract(ERC20_ABI, tokenAddress);
      const tx = tokenContract.methods.transfer(
        recipient,
        web3.utils.toWei(amount, 'ether')
      ).send({ from: account });
      
      const txHash = await tx;
      console.log('Token transfer successful:', txHash);
      getTokenBalance();
    } catch (err) {
      setError(`Token transfer failed: ${err.message}`);
    }
  };

  // Helper function to get network name
  const getNetworkName = (chainId) => {
    switch (chainId) {
      case '0x1': return 'Ethereum Mainnet';
      case '0x3': return 'Ropsten Testnet';
      case '0x4': return 'Rinkeby Testnet';
      case '0x5': return 'Goerli Testnet';
      case '0x2a': return 'Kovan Testnet';
      default: return 'Unknown Network';
    }
  };

  // Check if MetaMask is installed on component mount
  useEffect(() => {
    initWeb3();
    return () => {
      if (window.ethereum) {
        window.ethereum.removeAllListeners();
      }
    };
  }, []);

  // Update token balance when token address changes
  useEffect(() => {
    getTokenBalance();
  }, [tokenAddress, account]);

  return (
    <div className="metamask-integration">
      <h1>MetaMask Wallet Integration</h1>
      
      {error && <div className="error">{error}</div>}
      
      <div className="wallet-info">
        <h2>Wallet Information</h2>
        <p>Network: {network}</p>
        <p>Account: {account || 'Not connected'}</p>
        <p>ETH Balance: {balance}</p>
        
        <button onClick={initWeb3}>
          {account ? 'Refresh Connection' : 'Connect to MetaMask'}
        </button>
      </div>
      
      <div className="token-management">
        <h2>Token Management</h2>
        <div>
          <label>Token Contract Address:</label>
          <input
            type="text"
            value={tokenAddress}
            onChange={(e) => setTokenAddress(e.target.value)}
            placeholder="0x..."
          />
          <button onClick={getTokenBalance}>Get Balance</button>
          <p>Token Balance: {tokenBalance}</p>
        </div>
      </div>
      
      <div className="transaction-section">
        <h2>Transactions</h2>
        
        <div className="eth-transaction">
          <h3>Send ETH</h3>
          <label>Recipient Address:</label>
          <input
            type="text"
            value={recipient}
            onChange={(e) => setRecipient(e.target.value)}
            placeholder="0x..."
          />
          <label>Amount (ETH):</label>
          <input
            type="number"
            value={amount}
            onChange={(e) => setAmount(e.target.value)}
            placeholder="0.1"
          />
          <button onClick={sendTransaction}>Send ETH</button>
        </div>
        
        <div className="token-transaction">
          <h3>Send Token</h3>
          <label>Recipient Address:</label>
          <input
            type="text"
            value={recipient}
            onChange={(e) => setRecipient(e.target.value)}
            placeholder="0x..."
          />
          <label>Amount (Tokens):</label>
          <input
            type="number"
            value={amount}
            onChange={(e) => setAmount(e.target.value)}
            placeholder="10"
          />
          <button onClick={sendTokenTransaction}>Send Tokens</button>
        </div>
      </div>
    </div>
  );
};

export default MetaMaskIntegration;
```
