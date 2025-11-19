"""
Generated Code Metadata:
========================
Original URL: https://nft.stoneinno.com
Prompt: "Design a UI component for an NFT marketplace that showcases popular and new NFTs, including image, video, and audio elements."
Generated: DETERMINISTIC_b8eae50cca551ca3
Batch ID: 20250622_204554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import './NFTShowcase.css'; // Import CSS for styling

/**
 * NFTShowcase Component
 * Displays popular and new NFTs with support for image, video, and audio elements.
 * @param {Array} nfts - Array of NFT objects containing metadata.
 */
const NFTShowcase = ({ nfts }) => {
  const [popularNFTs, setPopularNFTs] = useState([]);
  const [newNFTs, setNewNFTs] = useState([]);

  // Fetch and categorize NFTs into popular and new
  useEffect(() => {
    if (nfts && nfts.length > 0) {
      const popular = nfts.filter((nft) => nft.isPopular);
      const newItems = nfts.filter((nft) => nft.isNew);
      setPopularNFTs(popular);
      setNewNFTs(newItems);
    }
  }, [nfts]);

  /**
   * Render NFT card based on its type (image, video, audio).
   * @param {Object} nft - NFT object containing metadata.
   */
  const renderNFTCard = (nft) => {
    return (
      <div className="nft-card" key={nft.id}>
        <h3 className="nft-title">{nft.title}</h3>
<<<<<<< HEAD
        {nft.type === 'image' && <img src={nft.url} alt={nft.title} className="nft-media" />}
        {nft.type === 'video' && (
          <video controls className="nft-media">
            <source src={nft.url} type="video/mp4" />
            Your browser does not support the video tag.
          </video>
        )}
        {nft.type === 'audio' && (
          <audio controls className="nft-media">
            <source src={nft.url} type="audio/mpeg" />
            Your browser does not support the audio tag.
          </audio>
        )}
=======
        <div className="nft-media">
          {nft.type === 'image' && <img src={nft.url} alt={nft.title} />}
          {nft.type === 'video' && (
            <video controls>
              <source src={nft.url} type="video/mp4" />
              Your browser does not support the video tag.
            </video>
          )}
          {nft.type === 'audio' && (
            <audio controls>
              <source src={nft.url} type="audio/mpeg" />
              Your browser does not support the audio tag.
            </audio>
          )}
        </div>
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
        <p className="nft-description">{nft.description}</p>
      </div>
    );
  };

  return (
    <div className="nft-showcase">
      <section className="popular-nfts">
        <h2>Popular NFTs</h2>
        <div className="nft-grid">
          {popularNFTs.length > 0 ? (
            popularNFTs.map((nft) => renderNFTCard(nft))
          ) : (
            <p>No popular NFTs available.</p>
          )}
        </div>
      </section>
      <section className="new-nfts">
        <h2>New NFTs</h2>
        <div className="nft-grid">
          {newNFTs.length > 0 ? (
            newNFTs.map((nft) => renderNFTCard(nft))
          ) : (
            <p>No new NFTs available.</p>
          )}
        </div>
      </section>
    </div>
  );
};

// PropTypes for type checking
NFTShowcase.propTypes = {
  nfts: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.string.isRequired,
      title: PropTypes.string.isRequired,
      description: PropTypes.string,
      url: PropTypes.string.isRequired,
      type: PropTypes.oneOf(['image', 'video', 'audio']).isRequired,
      isPopular: PropTypes.bool,
      isNew: PropTypes.bool,
    })
  ).isRequired,
};

// Default props
NFTShowcase.defaultProps = {
  nfts: [],
};

export default NFTShowcase;

/* NFTShowcase.css */
<<<<<<< HEAD
/* Basic styling for the NFT Showcase component */
=======
/* Basic styling for the NFT showcase component */
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
.nft-showcase {
  padding: 20px;
  font-family: Arial, sans-serif;
}

.nft-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.nft-card {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 15px;
  width: 300px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.nft-title {
  font-size: 18px;
  margin-bottom: 10px;
}

<<<<<<< HEAD
.nft-media {
  width: 100%;
  border-radius: 8px;
  margin-bottom: 10px;
}

.nft-description {
=======
.nft-media img,
.nft-media video,
.nft-media audio {
  width: 100%;
  border-radius: 8px;
}

.nft-description {
  margin-top: 10px;
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
  font-size: 14px;
  color: #555;
}
```
