"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://raremintnft.com
Prompt: Provide a JavaScript example for interacting with the Rare Mint API to fetch details of top-selling NFTs and display them in a custom web application.
Generated: DETERMINISTIC_45261a1df521085e
Batch ID: 20250612_154752
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.raremint.com/v1/nfts/top-selling": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const axios = require('axios');

// Define the base URL for the Rare Mint API
const BASE_URL = 'https://api.raremint.com/v1/nfts/top-selling';

// Function to fetch top-selling NFTs from the Rare Mint API
async function fetchTopSellingNFTs() {
    try {
        // Make a GET request to the Rare Mint API
        const response = await axios.get(BASE_URL);
        
        // Check if the response is successful
        if (response.status === 200) {
            return response.data; // Return the fetched NFT data
        } else {
            throw new Error(`Unexpected response status: ${response.status}`);
        }
    } catch (error) {
        // Log error details to the console
        console.error('Error fetching top-selling NFTs:', error.message);
        throw error; // Re-throw the error for further handling if needed
    }
}

// Function to display NFTs in the web application
function displayNFTs(nfts) {
    const nftContainer = document.getElementById('nft-container');
    nftContainer.innerHTML = ''; // Clear existing contents

    // Iterate over the NFTs and create HTML elements for each
    nfts.forEach(nft => {
        const nftElement = document.createElement('div');
        nftElement.classList.add('nft-item');
        nftElement.innerHTML = `
            <h3>${nft.title}</h3>
            <img src="${nft.imageUrl}" alt="${nft.title}" />
            <p>Price: ${nft.price} ETH</p>
            <p>Creator: ${nft.creator}</p>
        `;
        nftContainer.appendChild(nftElement); // Append the NFT element to the container
    });
}

// Main function to initialize the application
async function init() {
    try {
        const topSellingNFTs = await fetchTopSellingNFTs(); // Fetch the NFTs
        displayNFTs(topSellingNFTs); // Display the NFTs in the app
    } catch (error) {
        // Handle any errors that occurred during initialization
        const nftContainer = document.getElementById('nft-container');
        nftContainer.innerHTML = '<p>Error loading NFTs. Please try again later.</p>';
    }
}

// Wait for the DOM to be fully loaded before initializing the app
document.addEventListener('DOMContentLoaded', () => {
    init(); // Start the application
});
```
