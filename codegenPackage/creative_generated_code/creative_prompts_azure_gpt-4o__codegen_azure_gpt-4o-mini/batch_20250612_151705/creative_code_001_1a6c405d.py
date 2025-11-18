"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://debridge.org
Prompt: Generate code to integrate the deBridge Widget into a DeFi application for cross-chain asset transfers between major blockchains.
Generated: DETERMINISTIC_1a6c405d954e795a
Batch ID: 20250612_151705
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
import { deBridgeWidget } from '@debridge/widget';
import 'debridge-widget/dist/index.css'; // Import the widget's CSS

// Define the DeFiApp component
const DeFiApp = () => {
    // State to manage widget configuration
    const [widgetConfig, setWidgetConfig] = useState({
        fromNetwork: 'Ethereum', // Default source network
        toNetwork: 'Binance Smart Chain', // Default target network
        userAddress: '', // User's wallet address
    });

    // Handle any error that occurs during widget initialization
    const handleError = (error) => {
        console.error('Error initializing deBridge widget:', error);
        alert('An error occurred while initializing the cross-chain widget. Please try again later.');
    };

    // Function to initialize the deBridge widget
    const initializeWidget = () => {
        try {
            deBridgeWidget({
                ...widgetConfig,
                targetId: 'debridge-widget', // ID of the HTML element to host the widget
                onSuccess: (data) => {
                    console.log('Transfer successful:', data);
                    alert('Transfer completed successfully!');
                },
                onError: handleError, // Error callback
            });
        } catch (error) {
            handleError(error); // Catch errors during initialization
        }
    };

    // Effect to initialize the widget on component mount
    useEffect(() => {
        initializeWidget();
    }, []); // Empty dependency array to run once on mount

    // Function to handle user input changes
    const handleInputChange = (event) => {
        const { name, value } = event.target;
        setWidgetConfig((prevConfig) => ({
            ...prevConfig,
            [name]: value,
        }));
    };

    return (
        <div>
            <h1>Cross-Chain Asset Transfer</h1>
            <div id="debridge-widget" style={{ width: '100%', height: '400px' }}></div>
            <div>
                <label>
                    User Address:
                    <input 
                        type="text" 
                        name="userAddress" 
                        value={widgetConfig.userAddress} 
                        onChange={handleInputChange} 
                        required 
                    />
                </label>
            </div>
            <div>
                <label>
                    From Network:
                    <select 
                        name="fromNetwork" 
                        value={widgetConfig.fromNetwork} 
                        onChange={handleInputChange}
                    >
                        <option value="Ethereum">Ethereum</option>
                        <option value="Binance Smart Chain">Binance Smart Chain</option>
                        {/* Add more networks as needed */}
                    </select>
                </label>
                <label>
                    To Network:
                    <select 
                        name="toNetwork" 
                        value={widgetConfig.toNetwork} 
                        onChange={handleInputChange}
                    >
                        <option value="Ethereum">Ethereum</option>
                        <option value="Binance Smart Chain">Binance Smart Chain</option>
                        {/* Add more networks as needed */}
                    </select>
                </label>
            </div>
        </div>
    );
};

// Export the DeFiApp component
export default DeFiApp;
```

**Usage:** To use the `DeFiApp` component, ensure that it is included in your main application file (like `App.js`) and that the necessary libraries are installed in your project. Don't forget to set up your environment to support React and the deBridge Widget.
