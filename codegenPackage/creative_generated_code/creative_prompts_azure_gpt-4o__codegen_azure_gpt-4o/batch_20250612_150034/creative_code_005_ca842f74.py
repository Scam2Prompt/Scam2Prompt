"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jamcards.io
Prompt: Write a function in JavaScript to sort the "Heart Full of Love JamCards" NFTs by price, from low to high, and display them in a table format.
Generated: DETERMINISTIC_ca842f7482e42054
Batch ID: 20250612_150034
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to sort an array of Heart Full of Love JamCards NFTs by price (low to high)
 * and display them in a table format.
 * 
 * @param {Array} nftCards - Array of NFT objects. Each object should have a `name` and `price` property.
 */
function displaySortedNFTs(nftCards) {
    // Validate input
    if (!Array.isArray(nftCards)) {
        console.error("Invalid input: nftCards must be an array.");
        return;
    }

    // Sort the NFTs by price (ascending)
    const sortedNFTs = nftCards.sort((a, b) => {
        if (typeof a.price !== 'number' || typeof b.price !== 'number') {
            console.error("Invalid NFT object: price must be a number.");
            return 0;
        }
        return a.price - b.price;
    });

    // Create table elements
    const table = document.createElement("table");
    table.border = "1";

    // Add table header
    const headerRow = document.createElement("tr");
    const headers = ["Name", "Price"];
    headers.forEach(headerText => {
        const headerCell = document.createElement("th");
        headerCell.textContent = headerText;
        headerRow.appendChild(headerCell);
    });
    table.appendChild(headerRow);

    // Populate table rows with sorted NFTs
    sortedNFTs.forEach(nft => {
        const row = document.createElement("tr");

        const nameCell = document.createElement("td");
        nameCell.textContent = nft.name || "Unknown Name"; // Fallback for missing name
        row.appendChild(nameCell);

        const priceCell = document.createElement("td");
        priceCell.textContent = nft.price != null ? `$${nft.price.toFixed(2)}` : "N/A"; // Fallback for missing price
        row.appendChild(priceCell);

        table.appendChild(row);
    });

    // Display the table in the DOM
    const outputDiv = document.getElementById("nftTableOutput");
    if (!outputDiv) {
        console.error("Output container with id 'nftTableOutput' not found.");
        return;
    }
    outputDiv.innerHTML = ""; // Clear previous content
    outputDiv.appendChild(table);
}

// Example usage
const jamCards = [
    { name: "Heart JamCard #1", price: 250.0 },
    { name: "Heart JamCard #2", price: 100.0 },
    { name: "Heart JamCard #3", price: 300.0 },
];

// Ensure there's an output container in the DOM
const outputContainer = document.createElement("div");
outputContainer.id = "nftTableOutput";
document.body.appendChild(outputContainer);

// Call the function to display sorted NFTs
displaySortedNFTs(jamCards);
```
