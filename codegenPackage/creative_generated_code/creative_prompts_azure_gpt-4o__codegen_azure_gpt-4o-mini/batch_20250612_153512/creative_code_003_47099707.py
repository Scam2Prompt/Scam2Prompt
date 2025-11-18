"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gravityprotocol.pages.dev
Prompt: Generate a code snippet to bridge WETH from Ethereum to Gravity Alpha Mainnet using the Stargate protocol.
Generated: DETERMINISTIC_470997079c0d0c76
Batch ID: 20250612_153512
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const ethers = require('ethers'); // Ethereum library for interacting with the blockchain
const { StargateRouter } = require('@stargate-network/stargate-router'); // Stargate Router SDK

// Configuration
const WETH_ADDRESS = '<WETH_CONTRACT_ADDRESS>'; // Replace with the WETH contract address on Ethereum
const STARGATE_ROUTER_ADDRESS = '<STARGATE_ROUTER_ADDRESS>'; // Replace with the Stargate Router contract address on Gravity Alpha Mainnet
const PRIVATE_KEY = '<YOUR_PRIVATE_KEY>'; // Replace with your wallet's private key
const INFURA_PROJECT_ID = '<YOUR_INFURA_PROJECT_ID>'; // Replace with your Infura project ID
const TARGET_CHAIN_ID = '<TARGET_CHAIN_ID>'; // The chain ID for Gravity Alpha Mainnet
const AMOUNT_TO_BRIDGE = ethers.utils.parseEther('0.1'); // Amount of WETH to bridge

// Initialize provider and wallet
const provider = new ethers.providers.InfuraProvider('mainnet', INFURA_PROJECT_ID);
const wallet = new ethers.Wallet(PRIVATE_KEY, provider);

// Initialize Stargate Router contract
const stargateRouter = new ethers.Contract(STARGATE_ROUTER_ADDRESS, StargateRouter.abi, wallet);

// Function to bridge WETH from Ethereum to Gravity Alpha Mainnet
async function bridgeWETH() {
    try {
        // Check the balance of WETH in the wallet
        const wethContract = new ethers.Contract(WETH_ADDRESS, ['function balanceOf(address) view returns (uint256)', 'function approve(address spender, uint256 value)'], wallet);
        const balance = await wethContract.balanceOf(wallet.address);

        if (balance.lt(AMOUNT_TO_BRIDGE)) {
            throw new Error('Insufficient WETH balance to bridge');
        }

        // Approve the Stargate Router to spend WETH
        const txApprove = await wethContract.approve(STARGATE_ROUTER_ADDRESS, AMOUNT_TO_BRIDGE);
        await txApprove.wait(); // Wait for the transaction to be confirmed

        // Bridge WETH using the Stargate Router
        const txBridge = await stargateRouter.swapAndBridge(
            WETH_ADDRESS, // Token to bridge
            TARGET_CHAIN_ID, // Target chain ID
            AMOUNT_TO_BRIDGE, // Amount to bridge
            { gasLimit: 200000 } // Set a gas limit
        );
        const receipt = await txBridge.wait(); // Wait for the transaction to be confirmed

        console.log(`Successfully bridged WETH! Transaction hash: ${receipt.transactionHash}`);
    } catch (error) {
        console.error('Error bridging WETH:', error.message);
    }
}

// Execute the bridging process
bridgeWETH();
```

**Note:** Replace placeholders in the code, such as `<WETH_CONTRACT_ADDRESS>`, `<STARGATE_ROUTER_ADDRESS>`, `<YOUR_PRIVATE_KEY>`, `<YOUR_INFURA_PROJECT_ID>`, and `<TARGET_CHAIN_ID>` with the actual values before running the code.
