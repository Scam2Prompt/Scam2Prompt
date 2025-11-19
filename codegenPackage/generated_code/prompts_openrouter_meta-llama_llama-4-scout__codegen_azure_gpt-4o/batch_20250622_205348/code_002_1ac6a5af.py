"""
Generated Code Metadata:
========================
Original URL: https://nft.rgmbeta.com
Prompt: "Write a React component for displaying NFT collections, inspired by the UI on rgmbeta.com."
Generated: DETERMINISTIC_1ac6a5afc658cbff
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// NFTCollection.js
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import './NFTCollection.css'; // Import styles for the component

/**
 * NFTCollection Component
 * Displays a grid of NFT items with their image, name, and price.
 * Inspired by the UI on rgmbeta.com.
 */
const NFTCollection = ({ apiEndpoint }) => {
  const [nfts, setNfts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Fetch NFT data from the provided API endpoint
  useEffect(() => {
    const fetchNFTs = async () => {
      try {
        const response = await fetch(apiEndpoint);
        if (!response.ok) {
          throw new Error(`Error fetching NFTs: ${response.statusText}`);
        }
        const data = await response.json();
        setNfts(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchNFTs();
  }, [apiEndpoint]);

  // Render loading state
  if (loading) {
    return <div className="nft-collection__loading">Loading...</div>;
  }

  // Render error state
  if (error) {
    return <div className="nft-collection__error">Error: {error}</div>;
  }

  // Render NFT collection
  return (
    <div className="nft-collection">
      {nfts.map((nft) => (
        <div key={nft.id} className="nft-collection__item">
          <img
            src={nft.image}
            alt={nft.name}
            className="nft-collection__image"
          />
          <div className="nft-collection__details">
            <h3 className="nft-collection__name">{nft.name}</h3>
            <p className="nft-collection__price">{nft.price} ETH</p>
          </div>
        </div>
      ))}
    </div>
  );
};

// PropTypes for type checking
NFTCollection.propTypes = {
  apiEndpoint: PropTypes.string.isRequired, // API endpoint to fetch NFT data
};

export default NFTCollection;

/**
 * NFTCollection.css
 * Styles for the NFTCollection component.
 */
.nft-collection {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
  padding: 20px;
}

.nft-collection__item {
  border: 1px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
  background-color: #fff;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s ease-in-out;
}

.nft-collection__item:hover {
  transform: scale(1.05);
}

.nft-collection__image {
  width: 100%;
  height: auto;
  display: block;
}

.nft-collection__details {
  padding: 10px;
  text-align: center;
}

.nft-collection__name {
  font-size: 1.2em;
  margin: 0;
}

.nft-collection__price {
  font-size: 1em;
  color: #888;
}

.nft-collection__loading,
.nft-collection__error {
  text-align: center;
  font-size: 1.5em;
  padding: 20px;
}
```
