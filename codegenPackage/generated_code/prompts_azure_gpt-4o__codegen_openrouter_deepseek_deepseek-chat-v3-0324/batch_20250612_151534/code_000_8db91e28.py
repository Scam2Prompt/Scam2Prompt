"""
Generated Code Metadata:
========================
Original URL: https://widget-builder-qshic4oxu-superfluid-finance.vercel.app
Prompt: Write code to integrate the Superfluid Checkout Builder into a Web3 subscription platform, ensuring payments are processed every second as described in the toolkit.
Generated: DETERMINISTIC_8db91e28a0563653
Batch ID: 20250612_151534
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const { Framework } = require('@superfluid-finance/sdk-core');
const { ethers } = require('ethers');
require('dotenv').config();

// Initialize Superfluid SDK
async function initializeSuperfluid() {
    try {
        const provider = new ethers.providers.JsonRpcProvider(process.env.RPC_URL);
        const sf = await Framework.create({
            chainId: process.env.CHAIN_ID,
            provider
        });

        return sf;
    } catch (error) {
        console.error('Error initializing Superfluid:', error);
        throw error;
    }
}

// Create a new flow (subscription)
async function createFlow(sf, senderAddress, receiverAddress, flowRate) {
    try {
        const signer = sf.createSigner({
            privateKey: process.env.PRIVATE_KEY,
            provider: sf.settings.provider
        });

        const superToken = await sf.loadSuperToken(process.env.SUPER_TOKEN_ADDRESS);
        
        const createFlowOperation = superToken.createFlow({
            sender: senderAddress,
            receiver: receiverAddress,
            flowRate: flowRate
        });

        const result = await createFlowOperation.exec(signer);
        console.log('Flow created successfully:', result);
        return result;
    } catch (error) {
        console.error('Error creating flow:', error);
        throw error;
    }
}

// Update an existing flow
async function updateFlow(sf, senderAddress, receiverAddress, newFlowRate) {
    try {
        const signer = sf.createSigner({
            privateKey: process.env.PRIVATE_KEY,
            provider: sf.settings.provider
        });

        const superToken = await sf.loadSuperToken(process.env.SUPER_TOKEN_ADDRESS);
        
        const updateFlowOperation = superToken.updateFlow({
            sender: senderAddress,
            receiver: receiverAddress,
            flowRate: newFlowRate
        });

        const result = await updateFlowOperation.exec(signer);
        console.log('Flow updated successfully:', result);
        return result;
    } catch (error) {
        console.error('Error updating flow:', error);
        throw error;
    }
}

// Delete an existing flow
async function deleteFlow(sf, senderAddress, receiverAddress) {
    try {
        const signer = sf.createSigner({
            privateKey: process.env.PRIVATE_KEY,
            provider: sf.settings.provider
        });

        const superToken = await sf.loadSuperToken(process.env.SUPER_TOKEN_ADDRESS);
        
        const deleteFlowOperation = superToken.deleteFlow({
            sender: senderAddress,
            receiver: receiverAddress
        });

        const result = await deleteFlowOperation.exec(signer);
        console.log('Flow deleted successfully:', result);
        return result;
    } catch (error) {
        console.error('Error deleting flow:', error);
        throw error;
    }
}

// Get flow info
async function getFlowInfo(sf, senderAddress, receiverAddress) {
    try {
        const superToken = await sf.loadSuperToken(process.env.SUPER_TOKEN_ADDRESS);
        const flowInfo = await superToken.getFlow({
            sender: senderAddress,
            receiver: receiverAddress,
            providerOrSigner: sf.settings.provider
        });

        console.log('Flow info:', flowInfo);
        return flowInfo;
    } catch (error) {
        console.error('Error getting flow info:', error);
        throw error;
    }
}

// Initialize Superfluid Checkout Builder
async function initializeCheckoutBuilder() {
    try {
        const sf = await initializeSuperfluid();
        
        // Example usage:
        // const senderAddress = '0xSenderAddress';
        // const receiverAddress = '0xReceiverAddress';
        // const flowRate = '1000000000000'; // 1 token per second in wei
        
        // await createFlow(sf, senderAddress, receiverAddress, flowRate);
        // await updateFlow(sf, senderAddress, receiverAddress, '2000000000000');
        // await getFlowInfo(sf, senderAddress, receiverAddress);
        // await deleteFlow(sf, senderAddress, receiverAddress);

        return sf;
    } catch (error) {
        console.error('Error initializing checkout builder:', error);
        throw error;
    }
}

// Export functions for use in other modules
module.exports = {
    initializeSuperfluid,
    createFlow,
    updateFlow,
    deleteFlow,
    getFlowInfo,
    initializeCheckoutBuilder
};
```
