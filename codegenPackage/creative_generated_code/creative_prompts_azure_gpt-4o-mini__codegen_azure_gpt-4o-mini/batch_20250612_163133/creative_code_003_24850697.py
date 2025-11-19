"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defiiway.com
Prompt: Provide an example of how to change the network for a cryptocurrency in three clicks using Defiway.Bridge.
Generated: DETERMINISTIC_24850697e0594834
Batch ID: 20250612_163133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useState } from 'react';
import { DefiwayBridge } from 'defiway-sdk'; // Hypothetical SDK for Defiway.Bridge

// Define the main application component
const NetworkSwitcher = () => {
    // State to hold selected network and loading status
    const [selectedNetwork, setSelectedNetwork] = useState('');
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null); // To capture any errors during the network switch

    // Function to handle network change
    const changeNetwork = async (network) => {
        setLoading(true);
        setError(null); // Reset error state before trying to change network
        
        try {
            // Initialize the Defiway bridge
            const bridge = new DefiwayBridge();
            
            // Call the method to change the network
            await bridge.changeNetwork(network);
            setSelectedNetwork(network); // Update the selected network
            alert(`Network changed to ${network}`); // Notify user of success
        } catch (err) {
            // Handle any errors that occur during network change
            console.error('Error changing network:', err);
            setError('Failed to change the network. Please try again.'); // Update error message
        } finally {
            setLoading(false); // Reset loading state
        }
    };

    return (
        <div>
            <h1>Change Cryptocurrency Network</h1>
            
            {/* Button to trigger network change to Ethereum */}
            <button onClick={() => changeNetwork('Ethereum')} disabled={loading}>
                {loading ? 'Changing...' : 'Switch to Ethereum'}
            </button>
            
            {/* Button to trigger network change to Binance Smart Chain */}
            <button onClick={() => changeNetwork('Binance Smart Chain')} disabled={loading}>
                {loading ? 'Changing...' : 'Switch to BSC'}
            </button>
            
            {/* Button to trigger network change to Polygon */}
            <button onClick={() => changeNetwork('Polygon')} disabled={loading}>
                {loading ? 'Changing...' : 'Switch to Polygon'}
            </button>
            
            {/* Display error message if any */}
            {error && <p style={{ color: 'red' }}>{error}</p>}
        </div>
    );
};

// Export the component for use in other parts of the application
export default NetworkSwitcher;
```
