"""
Generated Code Metadata:
========================
Original URL: https://penpie.io
Prompt: Design a UI component to display the details of various liquidity pools on Penpie, including pool name, APY, TVL, and maturity date.
Generated: DETERMINISTIC_552149ecf3454afc
Batch ID: 20250622_211120
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
import './LiquidityPoolDetails.css'; // Importing CSS for styling

/**
 * LiquidityPoolDetails component displays the details of various liquidity pools.
 * 
 * @param {Object} props - Component properties
 * @param {Array} props.pools - Array of liquidity pool objects
 * @returns {JSX.Element} Rendered component
 */
const LiquidityPoolDetails = ({ pools }) => {
    const [error, setError] = useState(null);

    // Validate the pools prop
    if (!Array.isArray(pools)) {
        setError('Invalid data format for pools');
        return <div className="error">Error: {error}</div>;
    }

    return (
        <div className="liquidity-pool-details">
            <h2>Liquidity Pool Details</h2>
            {error && <div className="error">Error: {error}</div>}
            <table>
                <thead>
                    <tr>
                        <th>Pool Name</th>
                        <th>APY (%)</th>
                        <th>TVL ($)</th>
                        <th>Maturity Date</th>
                    </tr>
                </thead>
                <tbody>
                    {pools.length > 0 ? (
                        pools.map((pool, index) => (
                            <tr key={index}>
                                <td>{pool.name}</td>
                                <td>{pool.apy.toFixed(2)}</td>
                                <td>{pool.tvl.toLocaleString()}</td>
                                <td>{new Date(pool.maturityDate).toLocaleDateString()}</td>
                            </tr>
                        ))
                    ) : (
                        <tr>
                            <td colSpan="4">No liquidity pools available</td>
                        </tr>
                    )}
                </tbody>
            </table>
        </div>
    );
};

// PropTypes for type checking
LiquidityPoolDetails.propTypes = {
    pools: PropTypes.arrayOf(
        PropTypes.shape({
            name: PropTypes.string.isRequired,
            apy: PropTypes.number.isRequired,
            tvl: PropTypes.number.isRequired,
            maturityDate: PropTypes.string.isRequired,
        })
    ).isRequired,
};

export default LiquidityPoolDetails;
```

```css
/* LiquidityPoolDetails.css */

.liquidity-pool-details {
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
    background-color: #f9f9f9;
}

h2 {
    margin-bottom: 20px;
}

table {
    width: 100%;
    border-collapse: collapse;
}

th, td {
    padding: 10px;
    text-align: left;
    border-bottom: 1px solid #ddd;
}

th {
    background-color: #f2f2f2;
}

.error {
    color: red;
    margin-bottom: 10px;
}
```
