"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3-community.web.app
Prompt: Write JavaScript code to display the number of NFTs minted out of a total supply (e.g., "120/150 Minted") on a Web3-based application.
Generated: DETERMINISTIC_daa40b0d11c3b409
Batch ID: 20250612_145931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries (e.g., ethers.js for Ethereum interactions)
import { ethers } from "ethers";

// Define a function to fetch and display the minted NFT count
async function displayMintedNFTCount(contractAddress, totalSupply) {
    try {
        // Connect to the Ethereum network (mainnet or testnet)
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        await provider.send("eth_requestAccounts", []); // Request user's wallet connection
        const signer = provider.getSigner();

        // Create a contract instance
        const contract = new ethers.Contract(contractAddress, [
            // Minimal ABI to fetch totalSupply and balanceOf
            "function totalSupply() view returns (uint256)",
            "function balanceOf(address owner) view returns (uint256)"
        ], signer);

        // Fetch the total supply of minted NFTs
        const mintedCount = await contract.totalSupply();
        const mintedCountFormatted = mintedCount.toString();

        // Display the minted NFTs count
        const displayElement = document.getElementById("nft-count");
        displayElement.innerText = `${mintedCountFormatted}/${totalSupply} Minted`;
    } catch (error) {
        // Handle errors gracefully
        console.error("Error fetching minted NFT count:", error);
        const displayElement = document.getElementById("nft-count");
        displayElement.innerText = "Error fetching data";
    }
}

// Call the function on page load or according to your application's flow
const contractAddress = "0xYourContractAddress"; // Replace with your NFT contract address
const totalSupply = 150; // Replace with your total supply count

// Assuming that the page has a div with id 'nft-count' for displaying the data
window.onload = () => {
    displayMintedNFTCount(contractAddress, totalSupply);
};
```

### HTML Example
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NFT Minted Count</title>
    <script type="module" src="path/to/your/javascript.js"></script>
</head>
<body>
    <div id="nft-count">Loading...</div>
</body>
</html>
```

### Note:
- Replace `"0xYourContractAddress"` with your actual NFT contract address and ensure you have the correct ABI needed for your contract.
- Ensure that you have access to a Web3 provider like MetaMask for the application to interact with the Ethereum network.
