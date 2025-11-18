"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-demo.vercel.app
Prompt: Build a React component to save network changes and display selected networks and their associated assets and NFTs, based on the design of https://metamask-demo.vercel.app.
Generated: DETERMINISTIC_ff9a82cad2f901e3
Batch ID: 20250612_150052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import axios from 'axios';

/**
 * NetworkAssets component to display selected networks and their associated assets and NFTs.
 *
 * @param {Object} props - Component properties
 * @param {string[]} props.networks - List of available networks
 * @returns {JSX.Element} The rendered component
 */
const NetworkAssets = ({ networks }) => {
    const [selectedNetwork, setSelectedNetwork] = useState('');
    const [assets, setAssets] = useState([]);
    const [error, setError] = useState(null);

    /**
     * Handles network selection change.
     * @param {Event} event - The change event from the select input
     */
    const handleNetworkChange = (event) => {
        setSelectedNetwork(event.target.value);
    };

    /**
     * Fetches assets and NFTs based on the selected network.
     */
    const fetchAssets = async () => {
        if (!selectedNetwork) return;

        try {
            const response = await axios.get(`/api/assets?network=${selectedNetwork}`);
            setAssets(response.data);
        } catch (err) {
            console.error("Error fetching assets:", err);
            setError("Failed to fetch assets. Please try again later.");
        }
    };

    // Fetch assets whenever the selected network changes
    useEffect(() => {
        fetchAssets();
    }, [selectedNetwork]);

    return (
        <div className="network-assets-container">
            <h1>Network Assets</h1>
            
            <div className="network-selector">
                <label htmlFor="network-select">Select Network:</label>
                <select id="network-select" value={selectedNetwork} onChange={handleNetworkChange}>
                    <option value="">--Choose a Network--</option>
                    {networks.map((network) => (
                        <option key={network} value={network}>
                            {network}
                        </option>
                    ))}
                </select>
            </div>

            {error && <div className="error-message">{error}</div>}

            <div className="assets-list">
                <h2>Assets and NFTs</h2>
                {assets.length === 0 ? (
                    <p>No assets or NFTs found for the selected network.</p>
                ) : (
                    <ul>
                        {assets.map((asset) => (
                            <li key={asset.id}>
                                <strong>{asset.name}</strong>: {asset.description}
                            </li>
                        ))}
                    </ul>
                )}
            </div>
        </div>
    );
};

NetworkAssets.propTypes = {
    networks: PropTypes.arrayOf(PropTypes.string).isRequired,
};

export default NetworkAssets;
```
