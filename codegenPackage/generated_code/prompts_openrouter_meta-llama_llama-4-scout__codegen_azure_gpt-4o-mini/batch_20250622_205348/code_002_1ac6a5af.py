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

```javascript
import React, { useEffect, useState } from 'react';
import PropTypes from 'prop-types';
import './NFTCollection.css'; // Importing CSS for styling

/**
 * NFTCollection Component
 * Displays a collection of NFTs with their images and titles.
 * 
 * @param {Object} props - Component properties
 * @param {Array} props.nfts - Array of NFT objects containing id, title, and imageUrl
 * @returns {JSX.Element} Rendered NFT collection
 */
const NFTCollection = ({ nfts }) => {
    const [error, setError] = useState(null);

    // Validate props
    if (!Array.isArray(nfts)) {
        throw new Error('Invalid prop: nfts should be an array');
    }

    // Error handling for empty NFT collection
    if (nfts.length === 0) {
        return <div className="nft-collection-error">No NFTs available</div>;
    }

    return (
        <div className="nft-collection">
            {error && <div className="nft-collection-error">{error}</div>}
            <h2 className="nft-collection-title">NFT Collection</h2>
            <div className="nft-collection-grid">
                {nfts.map((nft) => (
                    <div key={nft.id} className="nft-card">
                        <img src={nft.imageUrl} alt={nft.title} className="nft-image" />
                        <h3 className="nft-title">{nft.title}</h3>
                    </div>
                ))}
            </div>
        </div>
    );
};

// PropTypes for type checking
NFTCollection.propTypes = {
    nfts: PropTypes.arrayOf(
        PropTypes.shape({
            id: PropTypes.string.isRequired,
            title: PropTypes.string.isRequired,
            imageUrl: PropTypes.string.isRequired,
        })
    ).isRequired,
};

export default NFTCollection;
```

```css
/* NFTCollection.css */

.nft-collection {
    padding: 20px;
    text-align: center;
}

.nft-collection-title {
    font-size: 24px;
    margin-bottom: 20px;
}

.nft-collection-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 15px;
}

.nft-card {
    border: 1px solid #ccc;
    border-radius: 8px;
    overflow: hidden;
    transition: transform 0.2s;
}

.nft-card:hover {
    transform: scale(1.05);
}

.nft-image {
    width: 100%;
    height: auto;
}

.nft-title {
    font-size: 18px;
    margin: 10px 0;
}

.nft-collection-error {
    color: red;
    font-size: 18px;
}
```
