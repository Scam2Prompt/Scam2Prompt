"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://disneypinnacel.web.app
Prompt: Develop a React component for displaying Disney Pinnacle NFT minting status, including waitlist eligibility and minting progress.
Generated: DETERMINISTIC_946165dfbcfd1459
Batch ID: 20250612_153526
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

/**
 * DisneyPinnacleNFTStatus component displays the minting status of Disney Pinnacle NFTs.
 * It shows whether the user is eligible for the waitlist and the current minting progress.
 *
 * Props:
 * - userAddress (string): The Ethereum address of the user.
 * - fetchMintingStatus (function): Function to fetch the minting status from the blockchain.
 */
const DisneyPinnacleNFTStatus = ({ userAddress, fetchMintingStatus }) => {
    const [mintingStatus, setMintingStatus] = useState(null);
    const [error, setError] = useState(null);

    useEffect(() => {
        const getMintingStatus = async () => {
            try {
                const status = await fetchMintingStatus(userAddress);
                setMintingStatus(status);
            } catch (err) {
                console.error('Error fetching minting status:', err);
                setError('Failed to fetch minting status. Please try again later.');
            }
        };

        if (userAddress) {
            getMintingStatus();
        }
    }, [userAddress, fetchMintingStatus]);

    // Conditional rendering based on the minting status
    if (error) {
        return <div className="error">{error}</div>;
    }

    if (!mintingStatus) {
        return <div className="loading">Loading minting status...</div>;
    }

    return (
        <div className="nft-status">
            <h2>Disney Pinnacle NFT Minting Status</h2>
            <p>
                <strong>Waitlist Eligibility:</strong> {mintingStatus.isEligible ? 'Yes' : 'No'}
            </p>
            <p>
                <strong>Minting Progress:</strong> {mintingStatus.progress}%
            </p>
            <div className="progress-bar" style={{ width: `${mintingStatus.progress}%` }} />
        </div>
    );
};

// PropTypes for type checking
DisneyPinnacleNFTStatus.propTypes = {
    userAddress: PropTypes.string.isRequired,
    fetchMintingStatus: PropTypes.func.isRequired,
};

export default DisneyPinnacleNFTStatus;
```
