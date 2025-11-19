"""
Generated Code Metadata:
========================
Original URL: https://agora-next-8n06xjzv6-voteagora.vercel.app
Prompt: Write JavaScript code to interact with the Optimism Agora platform's on-chain governance system, specifically for submitting proposals or retrieving voter data.
Generated: DETERMINISTIC_6803d9239f78220f
Batch ID: 20250612_145933
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your.optimism.rpc.url": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
const { ethers } = require("ethers");

// Define the Optimism Agora contract address and ABI
const contractAddress = "0xYourContractAddress"; // Replace with the actual contract address
const contractABI = [
    // Replace with the actual ABI of the contract
    "function submitProposal(string memory description) public returns (uint256)",
    "function getVoterData(address voter) public view returns (uint256 proposalId, bool hasVoted, bool support)"
];

// Initialize provider and signer
const provider = new ethers.providers.JsonRpcProvider("https://your.optimism.rpc.url"); // Replace with the actual RPC URL
const privateKey = "0xYourPrivateKey"; // Replace with the actual private key
const wallet = new ethers.Wallet(privateKey, provider);
const contract = new ethers.Contract(contractAddress, contractABI, wallet);

/**
 * Submits a proposal to the Optimism Agora platform.
 * @param {string} description - The description of the proposal.
 * @returns {Promise<number>} - The ID of the submitted proposal.
 */
async function submitProposal(description) {
    try {
        const tx = await contract.submitProposal(description);
        const receipt = await tx.wait(); // Wait for the transaction to be mined
        console.log(`Proposal submitted successfully. Transaction Hash: ${tx.hash}`);
        return receipt.events[0].args.proposalId.toNumber(); // Assuming the proposalId is emitted in the first event
    } catch (error) {
        console.error("Error submitting proposal:", error);
        throw new Error("Proposal submission failed.");
    }
}

/**
 * Retrieves voter data for a specific address.
 * @param {string} voterAddress - The address of the voter.
 * @returns {Promise<Object>} - An object containing proposal ID, voting status, and support.
 */
async function getVoterData(voterAddress) {
    try {
        const voterData = await contract.getVoterData(voterAddress);
        return {
            proposalId: voterData[0].toNumber(),
            hasVoted: voterData[1],
            support: voterData[2]
        };
    } catch (error) {
        console.error("Error retrieving voter data:", error);
        throw new Error("Failed to retrieve voter data.");
    }
}

// Example usage
(async () => {
    try {
        const proposalId = await submitProposal("This is a test proposal.");
        console.log(`Submitted proposal ID: ${proposalId}`);

        const voterData = await getVoterData(wallet.address);
        console.log("Voter Data:", voterData);
    } catch (error) {
        console.error("An error occurred:", error);
    }
})();
```
