"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ziber.io
Prompt: Develop a decentralized application (dApp) using React and Ethereum's blockchain to allow users to bind their wallets to the Ziber platform and receive bonus tokens as described.
Generated: DETERMINISTIC_d3ecc45535673032
Batch ID: 20250612_151531
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// File: src/App.js

import React, { useState, useEffect } from 'react';
import Web3 from 'web3';
import { ZiberContractABI, ZiberContractAddress } from './config';

const App = () => {
  const [account, setAccount] = useState(null);
  const [web3, setWeb3] = useState(null);
  const [contract, setContract] = useState(null);
  const [status, setStatus] = useState('');

  // Initialize web3 and connect to the contract
  useEffect(() => {
    const initWeb3 = async () => {
      if (window.ethereum) {
        const web3Instance = new Web3(window.ethereum);
        setWeb3(web3Instance);

        try {
          // Request user to connect their wallet
          await window.ethereum.request({ method: 'eth_requestAccounts' });
          const accounts = await web3Instance.eth.getAccounts();
          setAccount(accounts[0]);

          // Bind contract to web3
          const contractInstance = new web3Instance.eth.Contract(
            ZiberContractABI,
            ZiberContractAddress
          );
          setContract(contractInstance);
        } catch (error) {
          console.error('Error connecting to wallet:', error);
          setStatus('Failed to connect wallet.');
        }
      } else {
        setStatus('Please install MetaMask to interact with the dApp.');
      }
    };

    initWeb3();
  }, []);

  // Bind wallet to Ziber platform
  const bindWallet = async () => {
    if (!contract || !account) {
      setStatus('Please connect your wallet first.');
      return;
    }

    try {
      await contract.methods.bindWallet().send({ from: account });
      setStatus('Wallet bound successfully! Bonus tokens granted.');
    } catch (error) {
      console.error('Error binding wallet:', error);
      setStatus('Failed to bind wallet. Please try again.');
    }
  };

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif' }}>
      <h1>Ziber Platform</h1>
      <p>
        Connect your wallet and bind it to the Ziber platform to get bonus
        tokens!
      </p>
      {account ? (
        <div>
          <p>
            Connected Wallet: <b>{account}</b>
          </p>
          <button onClick={bindWallet} style={{ padding: '10px 20px' }}>
            Bind Wallet
          </button>
        </div>
      ) : (
        <button
          onClick={() => window.ethereum.request({ method: 'eth_requestAccounts' })}
          style={{ padding: '10px 20px' }}
        >
          Connect Wallet
        </button>
      )}
      <p>{status}</p>
    </div>
  );
};

export default App;

// File: src/config.js

// Replace these with actual contract ABI and address
export const ZiberContractABI = [
  // Example ABI
  {
    constant: false,
    inputs: [],
    name: 'bindWallet',
    outputs: [],
    payable: false,
    stateMutability: 'nonpayable',
    type: 'function',
  },
];

export const ZiberContractAddress = '0xYourContractAddressHere';
```

**Note**: Ensure that the `ZiberContractABI` and `ZiberContractAddress` are replaced with the actual ABI and deployed contract address from your Ethereum smart contract.
