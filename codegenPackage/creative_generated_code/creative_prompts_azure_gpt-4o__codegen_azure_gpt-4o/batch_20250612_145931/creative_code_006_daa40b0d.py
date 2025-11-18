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
// Import necessary libraries
import Web3 from 'web3';

// Define constant values
const CONTRACT_ADDRESS = "0xYourContractAddress"; // Replace with your NFT contract address
const CONTRACT_ABI = []; // Replace with your contract's ABI
const TOTAL_SUPPLY = 150; // Replace with your total NFT supply

// Function to initialize Web3 and fetch NFT minted count
async function displayMintedCount() {
  try {
    // Check if Web3 is injected by the browser (e.g., MetaMask)
    if (typeof window.ethereum === 'undefined') {
      throw new Error("Web3 provider not found. Please install MetaMask or use a Web3-enabled browser.");
    }

    // Create a Web3 instance
    const web3 = new Web3(window.ethereum);

    // Request account access if needed
    await window.ethereum.request({ method: "eth_requestAccounts" });

    // Instantiate the contract
    const nftContract = new web3.eth.Contract(CONTRACT_ABI, CONTRACT_ADDRESS);

    // Call the contract method to get the number of minted NFTs
    const mintedNFTs = await nftContract.methods.totalSupply().call();

    // Display the minted count as "120/150 Minted"
    const mintedDisplay = `${mintedNFTs}/${TOTAL_SUPPLY} Minted`;
    console.log(mintedDisplay); // Log the minted count
    document.getElementById("mintedCount").innerText = mintedDisplay; // Display on the webpage
  } catch (error) {
    // Handle errors gracefully
    console.error("Error fetching minted count:", error.message);
    document.getElementById("mintedCount").innerText = "Error fetching minted count.";
  }
}

// Ensure the DOM content is loaded before running the function
document.addEventListener("DOMContentLoaded", () => {
  displayMintedCount();
});
```

```html
<!-- HTML element to display minted count -->
<div id="mintedCount"></div>
```
