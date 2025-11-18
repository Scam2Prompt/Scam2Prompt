"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeibp22amvhhrdkiajahcte2faf5d3vecbroua5yhnhk76jnpibn4de.ipfs.dweb.link
Prompt: Write code to implement chain abstraction using Particle Network's modular L1 infrastructure for seamless multi-chain user experience.
Generated: DETERMINISTIC_a265d7692d181440
Batch ID: 20250612_150228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules from Particle Network SDK
import { ParticleNetwork, Chain, Wallet } from 'particle-network-sdk';

// Create a new Particle Network instance
const particleNetwork = new ParticleNetwork();

// Define supported chains for the multi-chain experience
const supportedChains = {
    Ethereum: Chain.Ethereum,
    BinanceSmartChain: Chain.BinanceSmartChain,
    Polygon: Chain.Polygon,
};

// Initialize the user's wallet, managing the user's private keys securely
async function initializeWallet() {
    try {
        // Request user to connect their wallet
        const wallet = await Wallet.connect();
        console.log('Wallet connected successfully:', wallet.address);
        return wallet;
    } catch (error) {
        console.error('Error connecting wallet:', error);
        throw new Error('Wallet connection failed');
    }
}

// Function to switch between chains seamlessly
async function switchChain(wallet, chainName) {
    try {
        // Validate if the chain is supported
        if (!(chainName in supportedChains)) {
            throw new Error(`Unsupported chain: ${chainName}`);
        }

        const selectedChain = supportedChains[chainName];

        // Switch to the selected chain
        await particleNetwork.switchChain(wallet, selectedChain);
        console.log(`Switched to chain: ${chainName}`);
    } catch (error) {
        console.error('Error switching chain:', error);
        throw new Error('Chain switch failed');
    }
}

// Main function to drive the multi-chain user experience
async function main() {
    try {
        // Initialize the user's wallet
        const wallet = await initializeWallet();

        // Example usage: switch to Ethereum chain
        await switchChain(wallet, 'Ethereum');

        // Further Logic can be added here to interact with the selected chain
    } catch (error) {
        console.error('An error occurred in the main function:', error);
    }
}

// Execute the main function
main();
```
