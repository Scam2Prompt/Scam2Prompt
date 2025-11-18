"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.chibiheadnft.com
Prompt: Generate JavaScript code to display a list of NFTs, similar to the "Chibi Head NFT" collection, with options to view items and track sold-out status.
Generated: DETERMINISTIC_14b5f8be4e2047a3
Batch ID: 20250612_145238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Define the NFT collection as an array of objects
const nftCollection = [
    { id: 1, name: "Chibi Head #001", image: "nft1.jpg", isSoldOut: false },
    { id: 2, name: "Chibi Head #002", image: "nft2.jpg", isSoldOut: true },
    { id: 3, name: "Chibi Head #003", image: "nft3.jpg", isSoldOut: false },
    { id: 4, name: "Chibi Head #004", image: "nft4.jpg", isSoldOut: true },
];

// Function to render the NFT collection in the DOM
function renderNFTCollection(collection) {
    // Get the container element where NFTs will be displayed
    const nftContainer = document.getElementById('nft-container');
    nftContainer.innerHTML = ''; // Clear any existing content

    // Iterate through the collection and create HTML elements for each NFT
    collection.forEach((nft) => {
        const nftCard = document.createElement('div');
        nftCard.className = 'nft-card';

        // Add NFT image
        const nftImage = document.createElement('img');
        nftImage.src = nft.image;
        nftImage.alt = nft.name;
        nftImage.className = 'nft-image';

        // Add NFT name
        const nftName = document.createElement('h3');
        nftName.textContent = nft.name;

        // Add sold-out status
        const nftStatus = document.createElement('span');
        nftStatus.textContent = nft.isSoldOut ? 'Sold Out' : 'Available';
        nftStatus.className = nft.isSoldOut ? 'nft-status sold-out' : 'nft-status available';

        // Add a view button
        const viewButton = document.createElement('button');
        viewButton.textContent = 'View Item';
        viewButton.className = 'view-button';
        viewButton.disabled = nft.isSoldOut; // Disable if sold out

        // Add event listener to the view button
        viewButton.addEventListener('click', () => {
            alert(`Viewing details for ${nft.name}`);
        });

        // Append all elements to the NFT card
        nftCard.appendChild(nftImage);
        nftCard.appendChild(nftName);
        nftCard.appendChild(nftStatus);
        nftCard.appendChild(viewButton);

        // Append the NFT card to the container
        nftContainer.appendChild(nftCard);
    });
}

// Render the NFTs on page load
document.addEventListener('DOMContentLoaded', () => {
    try {
        renderNFTCollection(nftCollection);
    } catch (error) {
        console.error('Error rendering NFT collection:', error);
    }
});
```

**HTML Structure:** (To make the JavaScript code functional, use the following basic HTML structure.)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NFT Collection</title>
    <style>
        /* Add minimal styling */
        .nft-card {
            border: 1px solid #ccc;
            padding: 1rem;
            margin: 1rem;
            display: inline-block;
            text-align: center;
            width: 150px;
        }
        .nft-image {
            width: 100%;
            height: auto;
        }
        .nft-status {
            display: block;
            margin: 0.5rem 0;
            font-weight: bold;
        }
        .nft-status.sold-out {
            color: red;
        }
        .nft-status.available {
            color: green;
        }
        .view-button {
            padding: 0.5rem 1rem;
            cursor: pointer;
        }
        .view-button:disabled {
            cursor: not-allowed;
            opacity: 0.5;
        }
    </style>
</head>
<body>
    <h1>NFT Collection</h1>
    <div id="nft-container"></div>
    <script src="nft.js"></script> <!-- Link to the JavaScript file -->
</body>
</html>
```
