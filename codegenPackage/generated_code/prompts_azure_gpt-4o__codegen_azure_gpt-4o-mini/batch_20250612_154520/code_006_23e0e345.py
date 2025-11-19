"""
Generated Code Metadata:
========================
Original URL: https://website-9v1.pages.dev
Prompt: Develop a front-end application using React.js that integrates with the $PLRT token and allows users to mint, buy, and sell PLR NFTs on the platform.
Generated: DETERMINISTIC_23e0e345be5b9762
Batch ID: 20250612_154520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries and components
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';
import { PLRTokenContract, PLRNFTContract } from './contracts'; // Import your contract instances

// Main App component
const App = () => {
  const [account, setAccount] = useState('');
  const [web3, setWeb3] = useState(null);
  const [nfts, setNfts] = useState([]);
  const [loading, setLoading] = useState(true);

  // Initialize Web3 and load user account
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
        } else {
          alert('Please install MetaMask to use this app.');
        }
      } catch (error) {
        console.error('Error initializing Web3:', error);
      }
    };

    initWeb3();
  }, []);

  // Fetch NFTs from the blockchain
  const fetchNFTs = async () => {
    setLoading(true);
    try {
      const nftData = await PLRNFTContract.methods.getAllNFTs().call();
      setNfts(nftData);
    } catch (error) {
      console.error('Error fetching NFTs:', error);
    } finally {
      setLoading(false);
    }
  };

  // Mint a new NFT
  const mintNFT = async (tokenURI) => {
    try {
      setLoading(true);
      await PLRNFTContract.methods.mintNFT(account, tokenURI).send({ from: account });
      alert('NFT minted successfully!');
      fetchNFTs(); // Refresh the NFT list
    } catch (error) {
      console.error('Error minting NFT:', error);
    } finally {
      setLoading(false);
    }
  };

  // Buy an NFT
  const buyNFT = async (nftId, price) => {
    try {
      setLoading(true);
      await PLRTokenContract.methods.approve(PLRNFTContract.options.address, price).send({ from: account });
      await PLRNFTContract.methods.buyNFT(nftId).send({ from: account });
      alert('NFT purchased successfully!');
      fetchNFTs(); // Refresh the NFT list
    } catch (error) {
      console.error('Error buying NFT:', error);
    } finally {
      setLoading(false);
    }
  };

  // Sell an NFT
  const sellNFT = async (nftId, price) => {
    try {
      setLoading(true);
      await PLRNFTContract.methods.sellNFT(nftId, price).send({ from: account });
      alert('NFT listed for sale successfully!');
      fetchNFTs(); // Refresh the NFT list
    } catch (error) {
      console.error('Error selling NFT:', error);
    } finally {
      setLoading(false);
    }
  };

  // Load NFTs on component mount
  useEffect(() => {
    if (web3) {
      fetchNFTs();
    }
  }, [web3]);

  return (
    <div>
      <h1>PLR NFT Marketplace</h1>
      <p>Connected Account: {account}</p>
      {loading ? (
        <p>Loading...</p>
      ) : (
        <div>
          <h2>Your NFTs</h2>
          <ul>
            {nfts.map((nft, index) => (
              <li key={index}>
                <p>NFT ID: {nft.id}</p>
                <p>Price: {nft.price} PLR</p>
                <button onClick={() => buyNFT(nft.id, nft.price)}>Buy</button>
                <button onClick={() => sellNFT(nft.id, nft.price)}>Sell</button>
              </li>
            ))}
          </ul>
          <h2>Mint New NFT</h2>
          <input type="text" placeholder="Token URI" id="tokenURI" />
          <button onClick={() => mintNFT(document.getElementById('tokenURI').value)}>Mint NFT</button>
        </div>
      )}
    </div>
  );
};

export default App;
```

### Note:
- Ensure you have the appropriate smart contract instances (`PLRTokenContract` and `PLRNFTContract`) set up in the `contracts.js` file.
- This code assumes that the smart contracts have the methods `getAllNFTs`, `mintNFT`, `buyNFT`, and `sellNFT` implemented.
- Make sure to handle the necessary imports and configurations for Web3 and your smart contracts.
