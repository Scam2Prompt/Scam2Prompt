"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-market.pages.dev
Prompt: Provide an example of how to integrate cross-chain functionality for tasks and campaigns in a DApp using the Guildhall framework.
Generated: DETERMINISTIC_56cddc9329d6e5b2
Batch ID: 20250612_160720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { ethers } from "ethers";
import { Guildhall } from "guildhall-sdk";

// Define constants for the smart contracts and networks
const NETWORKS = {
  ETHEREUM: "ethereum",
  POLYGON: "polygon",
};

// Initialize the Guildhall framework with appropriate configuration
const guildhall = new Guildhall({
  networks: [NETWORKS.ETHEREUM, NETWORKS.POLYGON],
});

// Function to create a cross-chain task
async function createCrossChainTask(title, description, reward, targetChain) {
  try {
    // Validate input parameters
    if (!title || !description || !reward || !targetChain) {
      throw new Error("All parameters are required.");
    }

    // Check if the target chain is supported
    if (!Object.values(NETWORKS).includes(targetChain)) {
      throw new Error("Unsupported target chain.");
    }

    // Create the task on the specified chain
    const taskId = await guildhall.createTask({
      title,
      description,
      reward,
      chain: targetChain,
    });

    console.log(`Task created successfully with ID: ${taskId}`);
    return taskId;
  } catch (error) {
    console.error("Error creating cross-chain task:", error.message);
    throw error; // Rethrow error to handle it further up the chain if needed
  }
}

// Function to execute a campaign across different chains
async function executeCrossChainCampaign(campaignId, chains) {
  try {
    // Validate input parameters
    if (!campaignId || !Array.isArray(chains) || chains.length === 0) {
      throw new Error("Valid campaign ID and an array of chains are required.");
    }

    // Iterate over specified chains to execute the campaign
    for (const chain of chains) {
      if (!Object.values(NETWORKS).includes(chain)) {
        throw new Error(`Unsupported chain: ${chain}`);
      }

      // Execute the campaign on the current chain
      await guildhall.executeCampaign(campaignId, chain);
      console.log(`Campaign ${campaignId} executed on ${chain}`);
    }
  } catch (error) {
    console.error("Error executing cross-chain campaign:", error.message);
    throw error; // Rethrow for further handling
  }
}

// Example usage
(async () => {
  try {
    const taskId = await createCrossChainTask(
      "Cross-Chain Task",
      "This task spans multiple chains.",
      ethers.utils.parseEther("1.0"), // Reward of 1 ETH
      NETWORKS.POLYGON
    );

    await executeCrossChainCampaign(taskId, [
      NETWORKS.ETHEREUM,
      NETWORKS.POLYGON,
    ]);
  } catch (error) {
    console.error("An error occurred during the example execution:", error.message);
  }
})();
```
