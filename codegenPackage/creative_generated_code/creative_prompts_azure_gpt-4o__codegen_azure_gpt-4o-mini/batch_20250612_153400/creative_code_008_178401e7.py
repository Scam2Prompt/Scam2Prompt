"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://matrica19.vercel.app
Prompt: Develop a user interface component for network selection (Solana, Ethereum, Polygon) with real-time stats display, similar to the Matrica platform.
Generated: DETERMINISTIC_178401e72adc37ea
Batch ID: 20250612_153400
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
import './NetworkSelector.css'; // Import your CSS for styling

// Mock function to fetch network stats
const fetchNetworkStats = async (network) => {
  // Replace with actual API calls
  const stats = {
    Solana: { transactions: 1200, status: 'Active' },
    Ethereum: { transactions: 800, status: 'Active' },
    Polygon: { transactions: 600, status: 'Active' },
  };
  return stats[network] || { transactions: 0, status: 'Unknown' };
};

const NetworkSelector = ({ defaultNetwork }) => {
  // State to hold selected network and stats
  const [selectedNetwork, setSelectedNetwork] = useState(defaultNetwork);
  const [networkStats, setNetworkStats] = useState({ transactions: 0, status: 'Unknown' });

  // Function to handle network change
  const handleNetworkChange = async (event) => {
    const network = event.target.value;
    setSelectedNetwork(network);
    await updateNetworkStats(network);
  };

  // Function to update network stats
  const updateNetworkStats = async (network) => {
    try {
      const stats = await fetchNetworkStats(network);
      setNetworkStats(stats);
    } catch (error) {
      console.error('Error fetching network stats:', error);
      setNetworkStats({ transactions: 0, status: 'Error fetching stats' });
    }
  };

  // Effect to fetch stats when component mounts or network changes
  useEffect(() => {
    updateNetworkStats(selectedNetwork);
  }, [selectedNetwork]);

  return (
    <div className="network-selector">
      <select value={selectedNetwork} onChange={handleNetworkChange}>
        <option value="Solana">Solana</option>
        <option value="Ethereum">Ethereum</option>
        <option value="Polygon">Polygon</option>
      </select>
      <div className="network-stats">
        <h3>Network Stats:</h3>
        <p>Transactions: {networkStats.transactions}</p>
        <p>Status: {networkStats.status}</p>
      </div>
    </div>
  );
};

// Prop types for the component
NetworkSelector.propTypes = {
  defaultNetwork: PropTypes.oneOf(['Solana', 'Ethereum', 'Polygon']).isRequired,
};

// Export the component
export default NetworkSelector;
```

```css
/* NetworkSelector.css */

.network-selector {
  font-family: Arial, sans-serif;
  padding: 20px;
  background-color: #f9f9f9;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.network-selector select {
  margin-bottom: 15px;
  padding: 5px;
  font-size: 16px;
}

.network-stats {
  margin-top: 10px;
  padding: 10px;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 5px;
}
```
