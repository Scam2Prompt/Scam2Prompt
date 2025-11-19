"""
Generated Code Metadata:
========================
Original URL: https://collectiblemarkethub.com
Prompt: "Design a simple NFT marketplace using JavaScript and React, inspired by the Collectible Market Hub, with a focus on easy-to-use minting and trading features."
Generated: DETERMINISTIC_66869776cfde1c5e
Batch ID: 20250622_204816
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://ipfs.io/ipfs/${Math.random": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// NFTMarketplace.js
import React, { useState, useEffect } from 'react';
import { ethers } from 'ethers';
import NFTMarketplaceABI from './contracts/NFTMarketplace.json';
import NFTABI from './contracts/NFT.json';

// Contract addresses (replace with your actual deployed contract addresses)
const NFT_MARKETPLACE_ADDRESS = '0x123...';
const NFT_CONTRACT_ADDRESS = '0x456...';

const NFTMarketplace = () => {
  const [provider, setProvider] = useState(null);
  const [account, setAccount] = useState(null);
  const [nftMarketplace, setNftMarketplace] = useState(null);
  const [nftContract, setNftContract] = useState(null);
  const [nfts, setNfts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [formData, setFormData] = useState({
    name: '',
    description: '',
    price: '',
    file: null
  });

  // Initialize provider and contracts
  useEffect(() => {
    const init = async () => {
      try {
        // Check if MetaMask is installed
        if (window.ethereum) {
          const provider = new ethers.providers.Web3Provider(window.ethereum);
          setProvider(provider);

          // Get accounts
          const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
          setAccount(accounts[0]);

          // Initialize contracts
          const signer = provider.getSigner();
          const nftMarketplace = new ethers.Contract(
            NFT_MARKETPLACE_ADDRESS,
            NFTMarketplaceABI.abi,
            signer
          );
          const nftContract = new ethers.Contract(
            NFT_CONTRACT_ADDRESS,
            NFTABI.abi,
            signer
          );
          setNftMarketplace(nftMarketplace);
          setNftContract(nftContract);

          // Load NFTs
          await loadNFTs(nftMarketplace, nftContract);
        } else {
          alert('Please install MetaMask to use this marketplace!');
        }
      } catch (error) {
        console.error('Initialization error:', error);
      } finally {
        setLoading(false);
      }
    };
    init();
  }, []);

  // Load NFTs from marketplace
  const loadNFTs = async (marketplace, nft) => {
    try {
      const items = await marketplace.fetchMarketItems();
      const nfts = await Promise.all(items.map(async item => {
        const tokenUri = await nft.tokenURI(item.tokenId);
        const response = await fetch(tokenUri);
        const metadata = await response.json();
        return {
          price: ethers.utils.formatUnits(item.price.toString(), 'ether'),
          tokenId: item.tokenId.toNumber(),
          seller: item.seller,
          owner: item.owner,
          image: metadata.image,
          name: metadata.name,
          description: metadata.description
        };
      }));
      setNfts(nfts);
    } catch (error) {
      console.error('Error loading NFTs:', error);
    }
  };

  // Handle form input changes
  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  // Handle file upload
  const handleFileChange = (e) => {
    setFormData({
      ...formData,
      file: e.target.files[0]
    });
  };

  // Mint and list NFT
  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      if (!formData.name || !formData.description || !formData.price || !formData.file) {
        alert('Please fill all fields');
        return;
      }

      // Upload image to IPFS (simplified - in production use actual IPFS client)
      const imageUrl = `https://ipfs.io/ipfs/${Math.random().toString(36).substring(2)}`;

      // Create metadata
      const metadata = {
        name: formData.name,
        description: formData.description,
        image: imageUrl
      };

      // Mint NFT
      const price = ethers.utils.parseUnits(formData.price, 'ether');
      const transaction = await nftMarketplace.createToken(
        JSON.stringify(metadata),
        price
      );
      await transaction.wait();

      // Reload NFTs
      await loadNFTs(nftMarketplace, nftContract);

      // Reset form
      setFormData({
        name: '',
        description: '',
        price: '',
        file: null
      });
    } catch (error) {
      console.error('Error minting NFT:', error);
      alert('Failed to mint NFT');
    }
  };

  // Buy NFT
  const buyNFT = async (nft) => {
    try {
      const price = ethers.utils.parseUnits(nft.price, 'ether');
      const transaction = await nftMarketplace.createMarketSale(
        NFT_CONTRACT_ADDRESS,
        nft.tokenId,
        { value: price }
      );
      await transaction.wait();
      await loadNFTs(nftMarketplace, nftContract);
    } catch (error) {
      console.error('Error buying NFT:', error);
      alert('Failed to buy NFT');
    }
  };

  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <div className="marketplace">
      <header>
        <h1>NFT Marketplace</h1>
        <p>Connected account: {account}</p>
      </header>

      <div className="content">
        <div className="mint-form">
          <h2>Mint NFT</h2>
          <form onSubmit={handleSubmit}>
            <input
              type="text"
              name="name"
              placeholder="NFT Name"
              value={formData.name}
              onChange={handleChange}
              required
            />
            <textarea
              name="description"
              placeholder="NFT Description"
              value={formData.description}
              onChange={handleChange}
              required
            />
            <input
              type="number"
              name="price"
              placeholder="Price in ETH"
              value={formData.price}
              onChange={handleChange}
              required
              min="0"
              step="0.01"
            />
            <input
              type="file"
              name="file"
              onChange={handleFileChange}
              required
            />
            <button type="submit">Mint & List</button>
          </form>
        </div>

        <div className="nft-list">
          <h2>Available NFTs</h2>
          {nfts.length > 0 ? (
            <div className="nft-grid">
              {nfts.map((nft, i) => (
                <div key={i} className="nft-card">
                  <img src={nft.image} alt={nft.name} />
                  <div className="nft-info">
                    <h3>{nft.name}</h3>
                    <p>{nft.description}</p>
                    <p>Price: {nft.price} ETH</p>
                    <button onClick={() => buyNFT(nft)}>Buy</button>
                  </div>
                </div>
              ))}
            </div>
          ) : (
            <p>No NFTs available</p>
          )}
        </div>
      </div>
    </div>
  );
};

export default NFTMarketplace;
```

```javascript
// contracts/NFTMarketplace.json
{
  "abi": [
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "_nftContract",
          "type": "address"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "constructor"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": true,
          "internalType": "uint256",
          "name": "itemId",
          "type": "uint256"
        },
        {
          "indexed": true,
          "internalType": "address",
          "name": "nftContract",
          "type": "address"
        },
        {
          "indexed": true,
          "internalType": "uint256",
          "name": "tokenId",
          "type": "uint256"
        },
        {
          "indexed": false,
          "internalType": "address",
          "name": "seller",
          "type": "address"
        },
        {
          "indexed": false,
          "internalType": "address",
          "name": "owner",
          "type": "address"
        },
        {
          "indexed": false,
          "internalType": "uint256",
          "name": "price",
          "type": "uint256"
        }
      ],
      "name": "MarketItemCreated",
      "type": "event"
    },
    {
      "inputs": [
        {
          "internalType": "string",
          "name": "tokenURI",
          "type": "string"
        },
        {
          "internalType": "uint256",
          "name": "price",
          "type": "uint256"
        }
      ],
      "name": "createToken",
      "outputs": [
        {
