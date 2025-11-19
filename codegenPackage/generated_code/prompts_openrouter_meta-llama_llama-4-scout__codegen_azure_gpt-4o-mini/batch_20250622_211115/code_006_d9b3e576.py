"""
Generated Code Metadata:
========================
Original URL: https://nft-good.web.app
Prompt: "Design a simple UI component for displaying NFT minting progress and details, similar to Magic Eden's Magic Box mint page."
Generated: DETERMINISTIC_d9b3e576a559e746
Batch ID: 20250622_211115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import './MintingProgress.css'; // Importing CSS for styling

/**
 * NFTMintingProgress Component
 * Displays the progress and details of the NFT minting process.
 * 
 * Props:
 * - totalSupply: Total number of NFTs to be minted
 * - mintedCount: Number of NFTs that have been minted
 * - isMinting: Boolean indicating if the minting process is ongoing
 * - onMintComplete: Callback function to be called when minting is complete
 */
const NFTMintingProgress = ({ totalSupply, mintedCount, isMinting, onMintComplete }) => {
    const [progress, setProgress] = useState(0);

    useEffect(() => {
        // Calculate the minting progress percentage
        if (totalSupply > 0) {
            setProgress((mintedCount / totalSupply) * 100);
        }

        // Call the onMintComplete callback if minting is complete
        if (mintedCount >= totalSupply && isMinting) {
            onMintComplete();
        }
    }, [mintedCount, totalSupply, isMinting, onMintComplete]);

    return (
        <div className="minting-progress-container">
            <h2>NFT Minting Progress</h2>
            <div className="progress-bar">
                <div className="progress" style={{ width: `${progress}%` }} />
            </div>
            <div className="progress-details">
                <p>{mintedCount} / {totalSupply} NFTs minted</p>
                {isMinting ? <p>Minting in progress...</p> : <p>Minting complete!</p>}
            </div>
        </div>
    );
};

// PropTypes for type checking
NFTMintingProgress.propTypes = {
    totalSupply: PropTypes.number.isRequired,
    mintedCount: PropTypes.number.isRequired,
    isMinting: PropTypes.bool.isRequired,
    onMintComplete: PropTypes.func.isRequired,
};

// Default props
NFTMintingProgress.defaultProps = {
    totalSupply: 0,
    mintedCount: 0,
    isMinting: false,
    onMintComplete: () => {},
};

export default NFTMintingProgress;
```

```css
/* MintingProgress.css */
.minting-progress-container {
    width: 100%;
    max-width: 600px;
    margin: 0 auto;
    text-align: center;
    border: 1px solid #ccc;
    border-radius: 8px;
    padding: 20px;
    background-color: #f9f9f9;
}

.progress-bar {
    width: 100%;
    height: 30px;
    background-color: #e0e0e0;
    border-radius: 5px;
    overflow: hidden;
    margin: 10px 0;
}

.progress {
    height: 100%;
    background-color: #76c7c0;
    transition: width 0.3s ease;
}

.progress-details {
    font-size: 16px;
}
```
