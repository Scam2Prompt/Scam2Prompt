"""
Generated Code Metadata:
========================
Original URL: https://jellybabiesnft.web.app
Prompt: Write a React component that displays the total claimed $Jelly tokens and percentage of claimed tokens, based on the "Total Claimed" and "% of Claimed" stats shown on the Jelly Babies NFT webpage.
Generated: DETERMINISTIC_8c2c68d7b6872660
Batch ID: 20250612_142645
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

/**
 * TokenStats component displays the total claimed $Jelly tokens
 * and the percentage of claimed tokens.
 *
 * @param {Object} props - Component properties
 * @param {number} props.totalClaimed - Total claimed $Jelly tokens
 * @param {number} props.totalSupply - Total supply of $Jelly tokens
 * @returns {JSX.Element} Rendered component
 */
const TokenStats = ({ totalClaimed, totalSupply }) => {
    const [claimedPercentage, setClaimedPercentage] = useState(0);

    useEffect(() => {
        // Calculate the percentage of claimed tokens
        if (totalSupply > 0) {
            const percentage = (totalClaimed / totalSupply) * 100;
            setClaimedPercentage(percentage.toFixed(2)); // Keep two decimal places
        } else {
            setClaimedPercentage(0); // Avoid division by zero
        }
    }, [totalClaimed, totalSupply]);

    return (
        <div className="token-stats">
            <h2>Token Statistics</h2>
            <p>
                <strong>Total Claimed:</strong> {totalClaimed} $Jelly
            </p>
            <p>
                <strong>Percentage of Claimed:</strong> {claimedPercentage}%
            </p>
        </div>
    );
};

// PropTypes for type checking
TokenStats.propTypes = {
    totalClaimed: PropTypes.number.isRequired,
    totalSupply: PropTypes.number.isRequired,
};

// Default props for safety
TokenStats.defaultProps = {
    totalClaimed: 0,
    totalSupply: 0,
};

export default TokenStats;
```
