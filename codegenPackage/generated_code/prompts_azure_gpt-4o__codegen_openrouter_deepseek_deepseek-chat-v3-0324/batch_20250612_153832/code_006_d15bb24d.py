"""
Generated Code Metadata:
========================
Original URL: https://opensea-clone-ten.vercel.app
Prompt: Create a React component to dynamically render NFT collections and their stats, inspired by the OpenSea clone interface.
Generated: DETERMINISTIC_d15bb24dff84d003
Batch ID: 20250612_153832
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import PropTypes from 'prop-types';
import { ethers } from 'ethers';

// Utility function to format large numbers
const formatNumber = (num) => {
  if (num >= 1000000) {
    return (num / 1000000).toFixed(1) + 'M';
  }
  if (num >= 1000) {
    return (num / 1000).toFixed(1) + 'K';
  }
  return num.toString();
};

// NFT Collection Card Component
const NFTCard = ({ collection }) => {
  return (
    <div className="nft-card">
      <div className="nft-card-image-container">
        <img 
          src={collection.image_url || '/placeholder.png'} 
          alt={collection.name} 
          onError={(e) => { e.target.src = '/placeholder.png'; }}
        />
      </div>
      <div className="nft-card-info">
        <h3>{collection.name || 'Unnamed Collection'}</h3>
        <div className="nft-stats">
          <div className="stat">
            <span className="stat-label">Floor</span>
            <span className="stat-value">
              {collection.floor_price ? 
                `${ethers.utils.formatEther(collection.floor_price)} ETH` : 
                '--'}
            </span>
          </div>
          <div className="stat">
            <span className="stat-label">Volume</span>
            <span className="stat-value">
              {collection.total_volume ? 
                `${formatNumber(collection.total_volume)} ETH` : 
                '--'}
            </span>
          </div>
          <div className="stat">
            <span className="stat-label">Owners</span>
            <span className="stat-value">
              {collection.num_owners ? 
                formatNumber(collection.num_owners) : 
                '--'}
            </span>
          </div>
        </div>
      </div>
    </div>
  );
};

NFTCard.propTypes = {
  collection: PropTypes.shape({
    name: PropTypes.string,
    image_url: PropTypes.string,
    floor_price: PropTypes.string,
    total_volume: PropTypes.number,
    num_owners: PropTypes.number,
  }).isRequired,
};

// Main NFT Collections Component
const NFTCollections = ({ apiUrl, itemsPerPage = 20 }) => {
  const [collections, setCollections] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [page, setPage] = useState(1);

  useEffect(() => {
    const fetchCollections = async () => {
      try {
        setLoading(true);
        const response = await axios.get(
          `${apiUrl}?limit=${itemsPerPage}&offset=${(page - 1) * itemsPerPage}`
        );
        setCollections(response.data.collections || []);
        setError(null);
      } catch (err) {
        console.error('Error fetching NFT collections:', err);
        setError('Failed to load collections. Please try again later.');
        setCollections([]);
      } finally {
        setLoading(false);
      }
    };

    fetchCollections();
  }, [apiUrl, page, itemsPerPage]);

  const handlePrevPage = () => {
    if (page > 1) setPage(page - 1);
  };

  const handleNextPage = () => {
    setPage(page + 1);
  };

  return (
    <div className="nft-collections-container">
      <h2>NFT Collections</h2>
      
      {error && <div className="error-message">{error}</div>}
      
      {loading ? (
        <div className="loading-spinner">Loading...</div>
      ) : (
        <>
          <div className="nft-collections-grid">
            {collections.map((collection) => (
              <NFTCard key={collection.slug || collection.name} collection={collection} />
            ))}
          </div>
          
          <div className="pagination-controls">
            <button 
              onClick={handlePrevPage} 
              disabled={page === 1}
            >
              Previous
            </button>
            <span className="page-number">Page {page}</span>
            <button 
              onClick={handleNextPage} 
              disabled={collections.length < itemsPerPage}
            >
              Next
            </button>
          </div>
        </>
      )}
    </div>
  );
};

NFTCollections.propTypes = {
  apiUrl: PropTypes.string.isRequired,
  itemsPerPage: PropTypes.number,
};

export default NFTCollections;
```

```css
/* NFT Collections Styles */
.nft-collections-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  font-family: 'Inter', sans-serif;
}

.nft-collections-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 20px;
  margin: 20px 0;
}

.nft-card {
  border: 1px solid #e1e1e1;
  border-radius: 8px;
  overflow: hidden;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.nft-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
}

.nft-card-image-container {
  width: 100%;
  height: 200px;
  overflow: hidden;
}

.nft-card-image-container img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.nft-card-info {
  padding: 15px;
}

.nft-card-info h3 {
  margin: 0 0 10px 0;
  font-size: 16px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.nft-stats {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 10px;
}

.stat {
  display: flex;
  flex-direction: column;
}

.stat-label {
  font-size: 12px;
  color: #666;
}

.stat-value {
  font-size: 14px;
  font-weight: 600;
}

.pagination-controls {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 20px;
  margin-top: 30px;
}

.pagination-controls button {
  padding: 8px 16px;
  background-color: #3182ce;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.pagination-controls button:disabled {
  background-color: #a0aec0;
  cursor: not-allowed;
}

.loading-spinner {
  text-align: center;
  padding: 40px;
  font-size: 18px;
}

.error-message {
  color: #e53e3e;
  background-color: #fed7d7;
  padding: 10px;
  border-radius: 4px;
  margin-bottom: 20px;
  text-align: center;
}
```
