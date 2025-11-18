"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://earthmeta-aijko.pages.dev
Prompt: Suggest tools or frameworks for developing NFT trading functionalities in the EarthMeta Marketplace, focusing on the gamified UX/UI experience described on the site.
Generated: DETERMINISTIC_f10526e4e641ffb0
Batch ID: 20250612_154322
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:8545": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';
import { NFTMarketplaceContract } from './contracts/NFTMarketplaceContract'; // Import your NFT Marketplace Smart Contract

// Initialize Web3
const web3 = new Web3(Web3.givenProvider || 'http://localhost:8545');

// Main component for NFT Trading
const NFTMarketplace = () => {
  const [nfts, setNfts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Function to fetch NFTs from the blockchain
  const fetchNFTs = async () => {
    try {
      const nftCount = await NFTMarketplaceContract.methods.getNFTCount().call();
      const nftData = [];

      for (let i = 0; i < nftCount; i++) {
        const nft = await NFTMarketplaceContract.methods.getNFT(i).call();
        nftData.push(nft);
      }

      setNfts(nftData);
    } catch (err) {
      setError('Failed to fetch NFTs');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  // Use effect to fetch NFTs on component mount
  useEffect(() => {
    fetchNFTs();
  }, []);

  // Function to handle the purchase of an NFT
  const purchaseNFT = async (nftId) => {
    try {
      setLoading(true);
      const accounts = await web3.eth.getAccounts();
      await NFTMarketplaceContract.methods.purchaseNFT(nftId).send({ from: accounts[0] });
      // Refetch NFTs to update the UI after purchase
      fetchNFTs();
    } catch (err) {
      setError('Purchase failed. Please try again.');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  // Render the NFT Marketplace
  return (
    <div>
      <h1>EarthMeta NFT Marketplace</h1>
      {loading && <p>Loading NFTs...</p>}
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <div className="nft-grid">
        {nfts.map((nft) => (
          <div key={nft.id} className="nft-card">
            <img src={nft.imageUrl} alt={nft.name} />
            <h2>{nft.name}</h2>
            <p>{nft.description}</p>
            <p>Price: {web3.utils.fromWei(nft.price, 'ether')} ETH</p>
            <button onClick={() => purchaseNFT(nft.id)}>Purchase</button>
          </div>
        ))}
      </div>
    </div>
  );
};

// Export the component for use in the application
export default NFTMarketplace;

// Styles can be added according to your design for a gamified UX/UI experience
```
