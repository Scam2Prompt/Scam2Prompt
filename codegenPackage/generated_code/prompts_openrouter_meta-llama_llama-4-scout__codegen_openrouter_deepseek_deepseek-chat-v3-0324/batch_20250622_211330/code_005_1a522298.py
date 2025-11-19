"""
Generated Code Metadata:
========================
Original URL: https://dispensenode.co
Prompt: Design a UI component for a dApp that integrates with Dispense Node's NFT feature, allowing users to view their collection of digital works.
Generated: DETERMINISTIC_1a522298ad52b949
Batch ID: 20250622_211330
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState, useEffect } from 'react';
import { ethers } from 'ethers';
import './NFTGallery.css';

/**
 * NFTGallery Component
 * 
 * A UI component for displaying a user's NFT collection from Dispense Node.
 * 
 * Props:
 * - provider: Ethereum provider (e.g., from Web3Modal, ethers.js)
 * - contractAddress: Dispense Node NFT contract address
 * - contractABI: Dispense Node NFT contract ABI
 * - walletAddress: User's wallet address
 */
const NFTGallery = ({ provider, contractAddress, contractABI, walletAddress }) => {
  const [nfts, setNfts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (!provider || !contractAddress || !contractABI || !walletAddress) {
      setError('Missing required props');
      setLoading(false);
      return;
    }

    const fetchNFTs = async () => {
      try {
        const contract = new ethers.Contract(contractAddress, contractABI, provider);
        const balance = await contract.balanceOf(walletAddress);

        const nftPromises = [];
        for (let i = 0; i < balance.toNumber(); i++) {
          const tokenId = await contract.tokenOfOwnerByIndex(walletAddress, i);
          const tokenURI = await contract.tokenURI(tokenId);
          nftPromises.push(
            fetch(tokenURI)
              .then(res => res.json())
              .then(metadata => ({
                id: tokenId.toString(),
                name: metadata.name || 'Untitled',
                description: metadata.description || '',
                image: metadata.image || '',
                external_url: metadata.external_url || '',
                attributes: metadata.attributes || []
              }))
          );
        }

        const nftData = await Promise.all(nftPromises);
        setNfts(nftData);
      } catch (err) {
        console.error('Error fetching NFTs:', err);
        setError('Failed to load NFTs. Please try again.');
      } finally {
        setLoading(false);
      }
    };

    fetchNFTs();
  }, [provider, contractAddress, contractABI, walletAddress]);

  if (loading) {
    return <div className="loading">Loading your NFT collection...</div>;
  }

  if (error) {
    return <div className="error">{error}</div>;
  }

  if (nfts.length === 0) {
    return <div className="empty">No NFTs found in your collection.</div>;
  }

  return (
    <div className="nft-gallery">
      <h2>Your NFT Collection</h2>
      <div className="nft-grid">
        {nfts.map((nft) => (
          <div key={nft.id} className="nft-card">
            <img 
              src={nft.image} 
              alt={nft.name} 
              className="nft-image"
              onError={(e) => {
                e.target.onerror = null;
                e.target.src = 'fallback-image-url.png';
              }}
            />
            <div className="nft-details">
              <h3>{nft.name}</h3>
              <p>{nft.description}</p>
              {nft.external_url && (
                <a href={nft.external_url} target="_blank" rel="noopener noreferrer">
                  View External Link
                </a>
              )}
              {nft.attributes.length > 0 && (
                <div className="nft-attributes">
                  {nft.attributes.map((attr, index) => (
                    <div key={index} className="attribute">
                      <strong>{attr.trait_type}:</strong> {attr.value}
                    </div>
                  ))}
                </div>
              )}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default NFTGallery;
```

```css
/* NFTGallery.css */
.nft-gallery {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.nft-gallery h2 {
  text-align: center;
  margin-bottom: 30px;
  color: #333;
}

.nft-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
}

.nft-card {
  border: 1px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
  transition: transform 0.2s;
}

.nft-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
}

.nft-image {
  width: 100%;
  height: 300px;
  object-fit: cover;
}

.nft-details {
  padding: 15px;
}

.nft-details h3 {
  margin: 0 0 10px 0;
  font-size: 1.2rem;
}

.nft-details p {
  margin: 0 0 10px 0;
  color: #666;
}

.nft-details a {
  display: inline-block;
  margin-bottom: 10px;
  color: #1e88e5;
  text-decoration: none;
}

.nft-details a:hover {
  text-decoration: underline;
}

.nft-attributes {
  margin-top: 10px;
}

.attribute {
  margin-bottom: 5px;
}

.loading, .error, .empty {
  text-align: center;
  padding: 40px;
  font-size: 1.2rem;
}

.error {
  color: #f44336;
}

.empty {
  color: #666;
}
```
