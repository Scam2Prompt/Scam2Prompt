"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phi-f1z.pages.dev
Prompt: Write code to implement a feature in a dApp that lets users showcase their Phi Cred NFTs in various formats, such as text, images, or videos.
Generated: DETERMINISTIC_34249019d9293edd
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import { getNFTs } from './api'; // Function to fetch NFTs from the backend
import './NFTGallery.css'; // CSS for styling the gallery

// NFTGallery component to showcase Phi Cred NFTs
const NFTGallery = ({ userAddress }) => {
    const [nfts, setNFTs] = useState([]); // State to hold the user's NFTs
    const [error, setError] = useState(null); // State to handle errors

    // Fetch NFTs when the component mounts or userAddress changes
    useEffect(() => {
        const fetchNFTs = async () => {
            try {
                const fetchedNFTs = await getNFTs(userAddress); // Fetch NFTs
                setNFTs(fetchedNFTs); // Update state with fetched NFTs
            } catch (err) {
                console.error('Error fetching NFTs:', err); // Log error
                setError('Failed to fetch NFTs. Please try again later.'); // Update error state
            }
        };

        if (userAddress) {
            fetchNFTs(); // Call fetch function if userAddress is valid
        }
    }, [userAddress]);

    // Render error message if there's an error
    if (error) {
        return <div className="error">{error}</div>;
    }

    // Render the NFT gallery
    return (
        <div className="nft-gallery">
            <h2>Your Phi Cred NFTs</h2>
            {nfts.length === 0 ? (
                <p>No NFTs to display.</p> // Message when no NFTs are available
            ) : (
                <div className="nft-grid">
                    {nfts.map((nft) => (
                        <div key={nft.id} className="nft-card">
                            <h3>{nft.name}</h3>
                            {nft.mediaType === 'image' && (
                                <img src={nft.uri} alt={nft.name} className="nft-image" />
                            )}
                            {nft.mediaType === 'video' && (
                                <video controls className="nft-video">
                                    <source src={nft.uri} type="video/mp4" />
                                    Your browser does not support the video tag.
                                </video>
                            )}
                            {nft.mediaType === 'text' && (
                                <p>{nft.description}</p>
                            )}
                        </div>
                    ))}
                </div>
            )}
        </div>
    );
};

// PropTypes for type checking
NFTGallery.propTypes = {
    userAddress: PropTypes.string.isRequired,
};

export default NFTGallery;
```

```css
/* NFTGallery.css */
.nft-gallery {
    padding: 20px;
}

.nft-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 16px;
}

.nft-card {
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 10px;
    text-align: center;
    background-color: #fff;
    transition: transform 0.2s;
}

.nft-card:hover {
    transform: scale(1.05);
}

.nft-image {
    width: 100%;
    height: auto;
    border-radius: 5px;
}

.nft-video {
    width: 100%;
    border-radius: 5px;
}

.error {
    color: red;
    font-weight: bold;
}
```
