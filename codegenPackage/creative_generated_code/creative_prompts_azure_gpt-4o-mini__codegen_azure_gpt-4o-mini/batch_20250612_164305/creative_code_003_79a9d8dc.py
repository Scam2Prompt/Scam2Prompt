"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeidumscxkbzdpevccsy2ccgdgfc3gj4ejh42kqhn5yis4hacugjfuy.ipfs.dweb.link
Prompt: Provide an example of using AIgentX for image generation in a Web3 project.
Generated: DETERMINISTIC_79a9d8dcd4444f02
Batch ID: 20250612_164305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const { AIgentX } = require('aigentx'); // Ensure you have the AIgentX library installed
const Web3 = require('web3'); // Import web3 for blockchain interactions
require('dotenv').config(); // For handling environment variables

// Initialize Web3 and connect to the Ethereum network
const web3 = new Web3(new Web3.providers.HttpProvider(process.env.INFURA_URL));

// Set up AIgentX with your API key
const aigentx = new AIgentX({
    apiKey: process.env.AIGENTX_API_KEY, // Store your API key in .env
});

// Function to generate an image using AIgentX
async function generateImage(prompt) {
    try {
        // Validate the input prompt
        if (typeof prompt !== 'string' || prompt.trim().length === 0) {
            throw new Error('Invalid prompt: Prompt should be a non-empty string.');
        }

        // Call AIgentX to generate the image
        const imageResponse = await aigentx.generateImage({ prompt });

        // Check for response validity
        if (!imageResponse || !imageResponse.imageUrl) {
            throw new Error('Image generation failed: No URL returned.');
        }

        console.log('Generated Image URL:', imageResponse.imageUrl);
        return imageResponse.imageUrl; // Return the generated image URL
    } catch (error) {
        console.error('Error generating image:', error.message);
        throw error; // Re-throw error for further handling if necessary
    }
}

// Function to mint an NFT with the generated image
async function mintNFT(imageUrl) {
    try {
        // Replace with appropriate NFT contract address and ABI
        const nftContractAddress = '0xYourNFTContractAddress';
        const nftContractABI = []; // Add your NFT contract ABI here

        // Get a contract instance
        const nftContract = new web3.eth.Contract(nftContractABI, nftContractAddress);

        // Assume the user's wallet is unlocked and we have the user's address
        const userAddress = process.env.USER_ADDRESS; // User's wallet address
        const privateKey = process.env.PRIVATE_KEY; // User's private key

        // Create a transaction to mint the NFT
        const tx = {
            from: userAddress,
            to: nftContractAddress,
            gas: 2000000,
            data: nftContract.methods.mint(userAddress, imageUrl).encodeABI(), // Assuming mint function takes user address and image URL
        };

        // Sign the transaction
        const signedTx = await web3.eth.accounts.signTransaction(tx, privateKey);
        
        // Send the transaction
        const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);
        console.log('NFT Minted! Transaction receipt:', receipt);
    } catch (error) {
        console.error('Error minting NFT:', error.message);
    }
}

// Main function to execute the process
async function main() {
    try {
        const prompt = "A futuristic cityscape"; // Example prompt for image generation
        const imageUrl = await generateImage(prompt);
        await mintNFT(imageUrl);
    } catch (error) {
        console.error('Main execution error:', error.message);
    }
}

// Execute the main function
main();
```
