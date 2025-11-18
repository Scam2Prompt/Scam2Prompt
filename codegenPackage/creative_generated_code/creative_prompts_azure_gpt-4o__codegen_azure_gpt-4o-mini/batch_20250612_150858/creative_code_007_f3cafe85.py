"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://disneyglobalse.web.app
Prompt: Develop a React component for displaying Disney-themed NFTs, including support for mp4 and webm previews.
Generated: DETERMINISTIC_f3cafe8509820487
Batch ID: 20250612_150858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useEffect, useState } from 'react';
import PropTypes from 'prop-types';
import './DisneyNFTDisplay.css'; // Assuming you have some styles defined

/**
 * DisneyNFTDisplay is a React component that displays Disney-themed NFTs
 * with support for mp4 and webm previews.
 *
 * Props:
 * - nftData: Array of NFT objects [{ id, title, imageUrl, videoUrl, videoType }]
 * - loading: Boolean indicating loading state
 * - error: Error message to display when fetching data fails
 */
const DisneyNFTDisplay = ({ nftData, loading, error }) => {
    const [visibleNfts, setVisibleNfts] = useState([]);

    useEffect(() => {
        if (!loading && nftData) {
            setVisibleNfts(nftData);
        }
    }, [loading, nftData]);

    // Error fallback for user feedback
    if (error) {
        return <div className="error-message">{error}</div>;
    }

    // Show loading state
    if (loading) {
        return <div className="loading-message">Loading NFTs...</div>;
    }

    return (
        <div className="nft-grid">
            {visibleNfts.map((nft) => (
                <div key={nft.id} className="nft-card">
                    <h3 className="nft-title">{nft.title}</h3>
                    <img src={nft.imageUrl} alt={nft.title} className="nft-image" />
                    {nft.videoUrl && (
                        <video
                            className="nft-video"
                            controls
                            preload="metadata"
                        >
                            <source src={nft.videoUrl} type={nft.videoType} />
                            Your browser does not support the video tag.
                        </video>
                    )}
                </div>
            ))}
        </div>
    );
};

// PropTypes for type-checking
DisneyNFTDisplay.propTypes = {
    nftData: PropTypes.arrayOf(
        PropTypes.shape({
            id: PropTypes.string.isRequired,
            title: PropTypes.string.isRequired,
            imageUrl: PropTypes.string.isRequired,
            videoUrl: PropTypes.string,
            videoType: PropTypes.oneOf(['video/mp4', 'video/webm']),
        })
    ).isRequired,
    loading: PropTypes.bool.isRequired,
    error: PropTypes.string,
};

// Default props
DisneyNFTDisplay.defaultProps = {
    error: null,
};

export default DisneyNFTDisplay;
```

```css
/* DisneyNFTDisplay.css */
.nft-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 16px;
}

.nft-card {
    border: 1px solid #ccc;
    border-radius: 8px;
    padding: 16px;
    text-align: center;
    background-color: #fff;
    transition: box-shadow 0.3s;
}

.nft-card:hover {
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
}

.nft-title {
    font-size: 1.2em;
    margin-bottom: 8px;
}

.nft-image {
    max-width: 100%;
    border-radius: 4px;
}

.nft-video {
    max-width: 100%;
    border-radius: 4px;
}

.loading-message {
    text-align: center;
    font-size: 1.5em;
}

.error-message {
    color: red;
    text-align: center;
    font-size: 1.5em;
}
```
