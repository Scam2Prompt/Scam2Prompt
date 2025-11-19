"""
Generated Code Metadata:
========================
Original URL: https://defie.me
Prompt: Provide code to monitor Ethereum blockchain events for a DeFi application using Web3.js or Ethers.js.
Generated: DETERMINISTIC_5463999280a556a5
Batch ID: 20250612_154002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
const { ethers } = require('ethers');
require('dotenv').config();

// Contract ABI (simplified example for ERC20 token)
const ERC20_ABI = [
    "event Transfer(address indexed from, address indexed to, uint256 value)"
];

class BlockchainMonitor {
    constructor() {
        // Initialize provider (using Infura as example)
        this.provider = new ethers.providers.JsonRpcProvider(process.env.INFURA_URL);
        
        // Initialize contract instances
        this.tokenContract = new ethers.Contract(
            process.env.TOKEN_CONTRACT_ADDRESS,
            ERC20_ABI,
            this.provider
        );
    }

    async startMonitoring() {
        try {
            console.log('Starting blockchain event monitoring...');
            
            // Listen for Transfer events
            this.tokenContract.on('Transfer', (from, to, value, event) => {
                this.handleTransferEvent(from, to, value, event);
            });

            console.log('Successfully started monitoring Transfer events');
        } catch (error) {
            console.error('Error starting event monitoring:', error);
            throw error;
        }
    }

    async stopMonitoring() {
        try {
            console.log('Stopping blockchain event monitoring...');
            this.tokenContract.removeAllListeners('Transfer');
            console.log('Successfully stopped monitoring');
        } catch (error) {
            console.error('Error stopping event monitoring:', error);
            throw error;
        }
    }

    handleTransferEvent(from, to, value, event) {
        try {
            const formattedValue = ethers.utils.formatUnits(value, 18); // Assuming 18 decimals
            console.log(`\nNew Transfer Event:
                From: ${from}
                To: ${to}
                Value: ${formattedValue}
                Tx Hash: ${event.transactionHash}
                Block: ${event.blockNumber}`);
            
            // Add your custom business logic here
            // e.g., update database, trigger notifications, etc.
            
        } catch (error) {
            console.error('Error processing transfer event:', error);
        }
    }
}

// Example usage
(async () => {
    try {
        const monitor = new BlockchainMonitor();
        await monitor.startMonitoring();
        
        // Graceful shutdown handling
        process.on('SIGINT', async () => {
            await monitor.stopMonitoring();
            process.exit(0);
        });
        
    } catch (error) {
        console.error('Application error:', error);
        process.exit(1);
    }
})();
```
