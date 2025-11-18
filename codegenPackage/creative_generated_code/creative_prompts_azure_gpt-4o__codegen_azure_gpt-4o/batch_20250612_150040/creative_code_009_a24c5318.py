"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://patch-monorepo-linea.vercel.app
Prompt: Write a script using ethers.js to retrieve the terms of use for `.linea` domains and display them to users before minting a username.
Generated: DETERMINISTIC_a24c531848256ea6
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import ethers.js library
const { ethers } = require("ethers");

// Script configuration
const INFURA_API_KEY = "your_infura_api_key"; // Replace with your Infura API key
const LINEA_CONTRACT_ADDRESS = "0x123456789abcdef123456789abcdef123456789"; // Replace with the actual contract address
const LINEA_ABI = [ 
    // Replace with the actual ABI of the .linea contract
    {
        "constant": true,
        "inputs": [],
        "name": "termsOfUse",
        "outputs": [{ "name": "", "type": "string" }],
        "type": "function"
    },
    {
        "constant": false,
        "inputs": [{ "name": "username", "type": "string" }],
        "name": "mint",
        "outputs": [],
        "type": "function"
    }
];

// Helper function to retrieve and display terms of use
async function displayTermsOfUse(provider, contractAddress, contractABI) {
    try {
        // Connect to the .linea smart contract
        const contract = new ethers.Contract(contractAddress, contractABI, provider);

        // Call the `termsOfUse` function
        const terms = await contract.termsOfUse();

        // Display the terms of use to the user
        console.log("Terms of Use for .linea domains:");
        console.log(terms);
    } catch (error) {
        console.error("Error retrieving terms of use:", error.message);
        throw error;
    }
}

// Helper function to mint a username
async function mintUsername(wallet, contractAddress, contractABI, username) {
    try {
        // Connect to the .linea smart contract using the signer
        const contract = new ethers.Contract(contractAddress, contractABI, wallet);

        // Mint the username
        const tx = await contract.mint(username);

        // Wait for the transaction to be mined
        const receipt = await tx.wait();
        console.log(`Username '${username}' minted successfully! Transaction hash: ${receipt.transactionHash}`);
    } catch (error) {
        console.error("Error minting username:", error.message);
        throw error;
    }
}

// Main function
async function main() {
    // Validate input arguments
    const [username] = process.argv.slice(2);
    if (!username) {
        console.error("Please provide a username to mint.");
        process.exit(1);
    }

    // Create a provider using Infura
    const provider = new ethers.providers.InfuraProvider("mainnet", INFURA_API_KEY);

    // Create a wallet (use environment variables for better security in production)
    const privateKey = process.env.PRIVATE_KEY; // Replace with your private key or load from env var
    if (!privateKey) {
        console.error("Please set your PRIVATE_KEY environment variable.");
        process.exit(1);
    }
    const wallet = new ethers.Wallet(privateKey, provider);

    try {
        // Display the terms of use
        await displayTermsOfUse(provider, LINEA_CONTRACT_ADDRESS, LINEA_ABI);

        // Confirm acceptance (simplified for demonstration purposes)
        const readline = require("readline").createInterface({
            input: process.stdin,
            output: process.stdout
        });
        readline.question("Do you accept the terms of use? (yes/no): ", async (answer) => {
            readline.close();
            if (answer.toLowerCase() === "yes") {
                // Proceed to mint the username
                await mintUsername(wallet, LINEA_CONTRACT_ADDRESS, LINEA_ABI, username);
            } else {
                console.log("You must accept the terms of use to mint a username.");
            }
        });
    } catch (error) {
        console.error("An error occurred:", error.message);
    }
}

// Execute the main function
main();
```

### Notes:
- Replace placeholders (`INFURA_API_KEY`, `LINEA_CONTRACT_ADDRESS`, and `LINEA_ABI`) with real values before running the script.
- Ensure your private key is stored securely and not hard-coded into the script. Use environment variables instead (`PRIVATE_KEY`).
- This script assumes `.linea` smart contract has functions `termsOfUse` (to fetch terms of use) and `mint` (to mint usernames). You may need to adapt the ABI to match the actual contract.
