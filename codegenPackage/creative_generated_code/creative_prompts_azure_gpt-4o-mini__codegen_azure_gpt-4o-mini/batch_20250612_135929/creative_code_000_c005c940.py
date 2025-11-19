"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ledger-live.com.pl
Prompt: How can I customize my asset display in Ledger Live to enhance my cryptocurrency portfolio management?
Generated: DETERMINISTIC_c005c94017eb010c
Batch ID: 20250612_135929
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Ledger Live Asset Customizer Script
// This script allows users to customize the display of their cryptocurrency assets in Ledger Live.
// It modifies the asset display based on user preferences such as sorting and filtering.

// Import necessary libraries
import { getAssets, updateAssetDisplay } from 'ledger-live-sdk';
import { handleError } from './errorHandler';

// Configuration for display customization
const displayConfig = {
    sortBy: 'value', // Options: 'value', 'name', 'symbol'
    filterBy: ['BTC', 'ETH'], // Array of asset symbols to filter
    showOnlyFavorites: true, // Show only favorited assets
};

// Function to customize asset display
const customizeAssetDisplay = async (config) => {
    try {
        // Fetch the list of assets from Ledger Live
        const assets = await getAssets();

        // Filter assets based on configuration
        let filteredAssets = assets;
        if (config.filterBy.length > 0) {
            filteredAssets = assets.filter(asset => config.filterBy.includes(asset.symbol));
        }
        
        // Sort assets by configured property
        filteredAssets.sort((a, b) => {
            if (config.sortBy === 'value') {
                return b.value - a.value; // sort by descending value
            } else if (config.sortBy === 'name') {
                return a.name.localeCompare(b.name); // sort alphabetically by name
            } else {
                return a.symbol.localeCompare(b.symbol); // sort alphabetically by symbol
            }
        });

        // If the user wants to see only favorites, filter those out
        if (config.showOnlyFavorites) {
            filteredAssets = filteredAssets.filter(asset => asset.isFavorite);
        }

        // Update asset display in Ledger Live
        await updateAssetDisplay(filteredAssets);
        console.log('Asset display updated successfully.');

    } catch (error) {
        handleError(error);
    }
};

// Execute the customization with the provided configuration
customizeAssetDisplay(displayConfig);
```

```javascript
// Error handler utility
// This module handles errors that occur during the customization process.

export const handleError = (error) => {
    console.error('An error occurred while customizing asset display:', error);
    // Here you can add additional error handling logic, like logging to an external service 
    // or showing user-friendly messages in the UI.
};
```
