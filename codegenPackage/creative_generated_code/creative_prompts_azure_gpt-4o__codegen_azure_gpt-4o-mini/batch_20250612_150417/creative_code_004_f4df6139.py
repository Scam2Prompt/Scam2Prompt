"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://w3eth.app
Prompt: Write code to display the number of QRobot NFTs owned by a connected wallet and provide a "Mint" button for minting new robots.
Generated: DETERMINISTIC_f4df61392e5c818d
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useEffect, useState } from 'react';
import Web3 from 'web3';
import QRobotNFTContract from './QRobotNFTContract.json'; // NFT contract ABI

const QRobotNFTApp = () => {
  const [account, setAccount] = useState(null);
  const [nftCount, setNftCount] = useState(0);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  
  // Initialize Web3 and connect to the user's wallet
  useEffect(() => {
    const initWeb3 = async () => {
      try {
        // Check if Metamask is installed
        if (window.ethereum) {
          const web3 = new Web3(window.ethereum);
          // Request account access
          await window.ethereum.request({ method: 'eth_requestAccounts' });
          const accounts = await web3.eth.getAccounts();
          setAccount(accounts[0]);
          await fetchNFTCount(web3, accounts[0]);
        } else {
          throw new Error('Please install MetaMask!');
        }
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    initWeb3();
  }, []);

  // Fetch the number of NFTs owned by the connected wallet
  const fetchNFTCount = async (web3, account) => {
    const networkId = await web3.eth.net.getId();
    const deployedNetwork = QRobotNFTContract.networks[networkId];
    const contract = new web3.eth.Contract(
      QRobotNFTContract.abi,
      deployedNetwork && deployedNetwork.address,
    );

    try {
      const count = await contract.methods.balanceOf(account).call();
      setNftCount(count);
    } catch (err) {
      setError('Failed to fetch NFT count: ' + err.message);
    }
  };

  // Function to mint a new QRobot NFT
  const mintNFT = async () => {
    if (!account) {
      setError('Please connect your wallet to mint an NFT.');
      return;
    }

    const web3 = new Web3(window.ethereum);
    const networkId = await web3.eth.net.getId();
    const deployedNetwork = QRobotNFTContract.networks[networkId];
    const contract = new web3.eth.Contract(
      QRobotNFTContract.abi,
      deployedNetwork && deployedNetwork.address,
    );

    try {
      setLoading(true);
      // Call the mint function defined in the smart contract
      await contract.methods.mint(account).send({ from: account });
      // Refresh NFT count after minting
      await fetchNFTCount(web3, account);
    } catch (err) {
      setError('Minting failed: ' + err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h1>QRobot NFT Dashboard</h1>
      {loading ? (
        <p>Loading...</p>
      ) : error ? (
        <p style={{ color: 'red' }}>{error}</p>
      ) : (
        <>
          <p>Connected Wallet: {account}</p>
          <p>You own {nftCount} QRobot NFTs.</p>
          <button onClick={mintNFT} disabled={loading}>
            Mint New QRobot NFT
          </button>
        </>
      )}
    </div>
  );
};

export default QRobotNFTApp;
```
Note: This code assumes you have a React environment set up and that you have the ABI for the QRobot NFT contract stored in `QRobotNFTContract.json`. Ensure that the smart contract's mint function and balanceOf function are implemented correctly in your Solidity contract.
