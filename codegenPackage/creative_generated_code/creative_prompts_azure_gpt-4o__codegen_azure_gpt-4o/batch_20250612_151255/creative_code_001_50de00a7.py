"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appparax.pages.dev
Prompt: Generate code to integrate a wallet connection feature into a Web3 app, referencing ParaX's NFT staking pool and P2P contract functionality.
Generated: DETERMINISTIC_50de00a7e9f7c926
Batch ID: 20250612_151255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries and modules
import { useState, useEffect } from 'react';
import Web3 from 'web3'; // Web3.js library to interact with Ethereum blockchain
import ParaXABI from './ParaXABI.json'; // ABI for the ParaX NFT staking pool and P2P contract

// Wallet Connection Feature
export default function WalletConnection() {
  // State variables for wallet address and connection status
  const [walletAddress, setWalletAddress] = useState('');
  const [isConnected, setIsConnected] = useState(false);
  const [web3, setWeb3] = useState(null);
  const [contractInstance, setContractInstance] = useState(null);

  // ParaX Contract address — replace with actual deployed address
  const contractAddress = '0xYourParaXContractAddressHere';

  // Function to connect wallet
  const connectWallet = async () => {
    try {
      // Detect if MetaMask is installed
      if (!window.ethereum) {
        alert('MetaMask not found. Please install MetaMask to proceed.');
        return;
      }

      // Request wallet connection
      const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
      const connectedAccount = accounts[0];

      // Initialize Web3 instance
      const web3Instance = new Web3(window.ethereum);

      // Set state variables
      setWeb3(web3Instance);
      setWalletAddress(connectedAccount);
      setIsConnected(true);

      // Initialize the ParaX contract instance
      const contract = new web3Instance.eth.Contract(ParaXABI, contractAddress);
      setContractInstance(contract);

      console.log('Wallet connected:', connectedAccount);
    } catch (error) {
      console.error('Error connecting wallet:', error);
      alert('Failed to connect wallet. Please try again.');
    }
  };

  // Function to disconnect wallet
  const disconnectWallet = () => {
    setWalletAddress('');
    setIsConnected(false);
    setWeb3(null);
    setContractInstance(null);
    console.log('Wallet disconnected');
  };

  // Function to interact with ParaX NFT staking pool
  const stakeNFT = async (tokenId) => {
    try {
      if (!isConnected || !contractInstance) {
        alert('Please connect your wallet first.');
        return;
      }

      // Call the stake function of the contract
      await contractInstance.methods.stake(tokenId).send({ from: walletAddress });

      alert(`NFT with token ID ${tokenId} staked successfully.`);
    } catch (error) {
      console.error('Error staking NFT:', error);
      alert('Failed to stake NFT. Please check the console for details.');
    }
  };

  // Function to interact with ParaX P2P contract functionality
  const executeP2PTransaction = async (peerAddress, amount) => {
    try {
      if (!isConnected || !contractInstance) {
        alert('Please connect your wallet first.');
        return;
      }

      // Call the P2P transaction function of the contract
      await contractInstance.methods.p2pTransaction(peerAddress, amount).send({ from: walletAddress });

      alert(`P2P transaction of ${amount} completed successfully with ${peerAddress}.`);
    } catch (error) {
      console.error('Error executing P2P transaction:', error);
      alert('Failed to execute P2P transaction. Please check the console for details.');
    }
  };

  // Monitor wallet connection status
  useEffect(() => {
    const checkConnection = async () => {
      try {
        if (window.ethereum && window.ethereum.selectedAddress) {
          const web3Instance = new Web3(window.ethereum);
          const connectedAccount = window.ethereum.selectedAddress;

          setWeb3(web3Instance);
          setWalletAddress(connectedAccount);
          setIsConnected(true);

          // Initialize the ParaX contract instance
          const contract = new web3Instance.eth.Contract(ParaXABI, contractAddress);
          setContractInstance(contract);

          console.log('Wallet reconnected:', connectedAccount);
        }
      } catch (error) {
        console.error('Error checking wallet connection:', error);
      }
    };

    checkConnection();
  }, []);

  return (
    <div>
      <h1>Web3 Wallet Connection</h1>

      {isConnected ? (
        <div>
          <p>Connected Wallet Address: {walletAddress}</p>
          <button onClick={disconnectWallet}>Disconnect Wallet</button>
          {/* Example buttons to trigger contract interactions */}
          <button onClick={() => stakeNFT(1)}>Stake NFT (Token ID: 1)</button>
          <button onClick={() => executeP2PTransaction('0xPeerAddressHere', 10)}>Execute P2P Transaction</button>
        </div>
      ) : (
        <button onClick={connectWallet}>Connect Wallet</button>
      )}
    </div>
  );
}
```
