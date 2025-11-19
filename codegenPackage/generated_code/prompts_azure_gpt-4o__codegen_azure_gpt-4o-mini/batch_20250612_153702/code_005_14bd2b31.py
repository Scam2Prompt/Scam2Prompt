"""
Generated Code Metadata:
========================
Original URL: https://solana-nft-fraction-frontend.vercel.app
Prompt: Provide code to integrate a "Cancel" button in a Solana NFT fractionalizer frontend that resets all input fields for NFT creation.
Generated: DETERMINISTIC_14bd2b313172dddc
Batch ID: 20250612_153702
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState } from 'react';

// Functional component for NFT fractionalizer
const NftFractionalizer = () => {
    // State to manage input fields
    const [nftName, setNftName] = useState('');
    const [nftDescription, setNftDescription] = useState('');
    const [nftAmount, setNftAmount] = useState('');

    // Handler for input changes
    const handleInputChange = (e) => {
        const { name, value } = e.target;
        switch (name) {
            case 'nftName':
                setNftName(value);
                break;
            case 'nftDescription':
                setNftDescription(value);
                break;
            case 'nftAmount':
                setNftAmount(value);
                break;
            default:
                break;
        }
    };

    // Handler for the Cancel button
    const handleCancel = () => {
        // Reset all input fields to their initial state
        setNftName('');
        setNftDescription('');
        setNftAmount('');
    };

    // Render the component
    return (
        <div>
            <h1>NFT Fractionalizer</h1>
            <form>
                <div>
                    <label htmlFor="nftName">NFT Name:</label>
                    <input
                        type="text"
                        id="nftName"
                        name="nftName"
                        value={nftName}
                        onChange={handleInputChange}
                        required
                    />
                </div>
                <div>
                    <label htmlFor="nftDescription">NFT Description:</label>
                    <textarea
                        id="nftDescription"
                        name="nftDescription"
                        value={nftDescription}
                        onChange={handleInputChange}
                        required
                    />
                </div>
                <div>
                    <label htmlFor="nftAmount">Amount of NFTs:</label>
                    <input
                        type="number"
                        id="nftAmount"
                        name="nftAmount"
                        value={nftAmount}
                        onChange={handleInputChange}
                        required
                    />
                </div>
                <button type="button" onClick={handleCancel}>
                    Cancel
                </button>
                <button type="submit">Create NFT</button>
            </form>
        </div>
    );
};

export default NftFractionalizer;
```
