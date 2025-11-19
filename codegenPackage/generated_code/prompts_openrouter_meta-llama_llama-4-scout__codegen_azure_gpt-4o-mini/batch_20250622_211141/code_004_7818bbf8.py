"""
Generated Code Metadata:
========================
Original URL: https://nft-spark.com
Prompt: Develop a basic dapp that allows users to buy, sell, and trade NFTs using MetaMask for wallet integration.
Generated: DETERMINISTIC_7818bbf8dd08af5c
Batch ID: 20250622_211141
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import React, { useEffect, useState } from 'react';
import Web3 from 'web3';
import { ethers } from 'ethers';
import NFTContract from './NFTContract.json'; // Import your NFT contract ABI

// Define the main App component
const App = () => {
  const [account, setAccount] = useState('');
  const [nfts, setNfts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [provider, setProvider] = useState(null);
  const [contract, setContract] = useState(null);

  // Initialize Web3 and load the user's account
  useEffect(() => {
    const init = async () => {
      if (window.ethereum) {
        const web3 = new Web3(window.ethereum);
        setProvider(web3);
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        const accounts = await web3.eth.getAccounts();
        setAccount(accounts[0]);
        const nftContract = new web3.eth.Contract(NFTContract.abi, NFTContract.networks[5777].address); // Replace with your network ID
        setContract(nftContract);
        loadNFTs(nftContract);
      } else {
        alert('Please install MetaMask to use this DApp');
      }
    };
    init();
  }, []);

  // Load NFTs from the contract
  const loadNFTs = async (contract) => {
    try {
      const totalSupply = await contract.methods.totalSupply().call();
      const nftsArray = [];
      for (let i = 0; i < totalSupply; i++) {
        const nft = await contract.methods.nfts(i).call();
        nftsArray.push(nft);
      }
      setNfts(nftsArray);
      setLoading(false);
    } catch (error) {
      console.error('Error loading NFTs:', error);
    }
  };

  // Function to buy an NFT
  const buyNFT = async (nftId) => {
    try {
      const price = await contract.methods.getPrice(nftId).call();
      await contract.methods.buyNFT(nftId).send({ from: account, value: price });
      loadNFTs(contract); // Reload NFTs after purchase
    } catch (error) {
      console.error('Error buying NFT:', error);
    }
  };

  // Function to sell an NFT
  const sellNFT = async (nftId, price) => {
    try {
      await contract.methods.sellNFT(nftId, price).send({ from: account });
      loadNFTs(contract); // Reload NFTs after selling
    } catch (error) {
      console.error('Error selling NFT:', error);
    }
  };

  // Render the component
  return (
    <div>
      <h1>NFT Marketplace</h1>
      <p>Connected account: {account}</p>
      {loading ? (
        <p>Loading NFTs...</p>
      ) : (
        <div>
          {nfts.map((nft, index) => (
            <div key={index}>
              <h2>{nft.name}</h2>
              <p>Price: {nft.price} ETH</p>
              <button onClick={() => buyNFT(nft.id)}>Buy</button>
              <button onClick={() => sellNFT(nft.id, nft.price)}>Sell</button>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default App;
```

### Notes:
- Ensure you have the appropriate NFT contract ABI and address in `NFTContract.json`.
- Replace the network ID in the contract instantiation with the correct one for your deployment.
- This code assumes that the NFT contract has methods like `totalSupply`, `nfts`, `getPrice`, `buyNFT`, and `sellNFT`. Adjust the method names according to your contract's implementation.
