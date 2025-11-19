"""
Generated Code Metadata:
========================
Original URL: https://www.chibiheadnft.com
Prompt: Write code to create a "sold-out" indicator for NFTs in a collection, referencing the functionality described for "Chibi Head NFT."
Generated: DETERMINISTIC_43367c4386e7c558
Batch ID: 20250612_145238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// NFT Sold-Out Indicator Component
// Checks if an NFT collection is sold out and displays an indicator

/**
 * Checks if an NFT collection is sold out
 * @param {Object} collection - NFT collection data
 * @param {number} collection.totalSupply - Total NFTs in collection
 * @param {number} collection.mintedCount - Number of NFTs already minted
 * @returns {boolean} True if collection is sold out
 */
function isCollectionSoldOut(collection) {
    if (!collection || typeof collection.totalSupply !== 'number' || typeof collection.mintedCount !== 'number') {
        console.error('Invalid collection data provided');
        return false;
    }
    return collection.mintedCount >= collection.totalSupply;
}

/**
 * SoldOutIndicator component
 * @param {Object} props - Component props
 * @param {Object} props.collection - NFT collection data
 * @returns {JSX.Element} Sold out indicator component
 */
function SoldOutIndicator({ collection }) {
    if (!collection) {
        console.error('No collection data provided to SoldOutIndicator');
        return null;
    }

    const soldOut = isCollectionSoldOut(collection);

    if (!soldOut) {
        return null;
    }

    return (
        <div className="sold-out-indicator">
            <span className="sold-out-badge">SOLD OUT</span>
            <style jsx>{`
                .sold-out-indicator {
                    position: absolute;
                    top: 10px;
                    right: 10px;
                    background-color: rgba(0, 0, 0, 0.7);
                    color: white;
                    padding: 5px 10px;
                    border-radius: 4px;
                    font-weight: bold;
                    font-size: 12px;
                    z-index: 10;
                }
                .sold-out-badge {
                    text-transform: uppercase;
                    letter-spacing: 1px;
                }
            `}</style>
        </div>
    );
}

// Example usage:
/*
const collectionData = {
    totalSupply: 10000,
    mintedCount: 10000
};

<SoldOutIndicator collection={collectionData} />
*/
```
