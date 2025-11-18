"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metalcoin.vercel.app
Prompt: Write code in JavaScript using ethers.js to check the "memeability index" of METAL tokens and display it on a webpage.
Generated: DETERMINISTIC_35c09eebcc240491
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import ethers.js
const { ethers } = require("ethers");

// Function to check the "memeability index" of METAL tokens and display it on a webpage
async function checkMemeabilityIndex() {
  try {
    // Connect to Ethereum provider (using default MetaMask provider)
    const provider = new ethers.providers.Web3Provider(window.ethereum);

    // Request user to connect MetaMask
    await provider.send("eth_requestAccounts", []);

    // Define the METAL token contract details (replace with actual contract address and ABI)
    const METALTokenAddress = "0xYourMETALTokenAddressHere"; // Replace with METAL contract address
    const METALTokenABI = [
      // Replace with the actual ABI for the METAL token contract
      {
        "constant": true,
        "inputs": [],
        "name": "memeabilityIndex",
        "outputs": [{ "name": "", "type": "uint256" }],
        "type": "function",
      },
    ];

    // Create a contract instance
    const METALTokenContract = new ethers.Contract(
      METALTokenAddress,
      METALTokenABI,
      provider
    );

    // Call the memeabilityIndex function
    const memeabilityIndex = await METALTokenContract.memeabilityIndex();

    // Convert the memeability index to a human-readable format (if necessary)
    const formattedIndex = memeabilityIndex.toString();

    // Display the memeability index on the webpage
    const memeabilityElement = document.getElementById("memeabilityIndex");
    if (memeabilityElement) {
      memeabilityElement.innerText = `Memeability Index: ${formattedIndex}`;
    } else {
      console.error("Element with ID 'memeabilityIndex' not found.");
    }
  } catch (error) {
    // Handle errors gracefully
    console.error("An error occurred while checking the memeability index:", error);
  }
}

// Ensure the function runs when the page is loaded
window.onload = () => {
  checkMemeabilityIndex();
};
```

```html
<!-- Include this HTML element in your webpage -->
<div id="memeabilityIndex">Loading Memeability Index...</div>
```

### Notes:
1. Replace `0xYourMETALTokenAddressHere` and ABI with the actual METAL token contract details.
2. Ensure you have ethers.js installed (`npm install ethers`) and include MetaMask in the browser.
3. Add error handling for specific cases like user rejecting the connection or invalid contract details.
