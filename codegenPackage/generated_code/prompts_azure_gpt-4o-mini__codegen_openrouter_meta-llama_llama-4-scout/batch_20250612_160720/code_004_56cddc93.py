"""
Generated Code Metadata:
========================
Original URL: https://dapp-market.pages.dev
Prompt: Provide an example of how to integrate cross-chain functionality for tasks and campaigns in a DApp using the Guildhall framework.
Generated: DETERMINISTIC_56cddc9329d6e5b2
Batch ID: 20250612_160720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const { ethers } = require('ethers');
const { Guildhall } = require('@guildhall/sdk');

// Define a class for cross-chain functionality
class CrossChainGuildhall {
  /**
   * Initialize the CrossChainGuildhall instance
   * @param {string} apiKey - API key for Guildhall
   * @param {string} apiSecret - API secret for Guildhall
   * @param {string} chainId - Chain ID for the DApp
   */
  constructor(apiKey, apiSecret, chainId) {
    this.apiKey = apiKey;
    this.apiSecret = apiSecret;
    this.chainId = chainId;
    this.guildhall = new Guildhall(apiKey, apiSecret);
  }

  /**
   * Create a task on a specific chain
   * @param {string} taskName - Name of the task
   * @param {string} taskDescription - Description of the task
   * @param {string} chainId - Chain ID for the task
   * @returns {Promise} - Promise resolving to the task ID
   */
  async createTask(taskName, taskDescription, chainId) {
    try {
      const task = await this.guildhall.tasks.create({
        name: taskName,
        description: taskDescription,
        chainId: chainId,
      });
      return task.id;
    } catch (error) {
      console.error('Error creating task:', error);
      throw error;
    }
  }

  /**
   * Create a campaign on a specific chain
   * @param {string} campaignName - Name of the campaign
   * @param {string} campaignDescription - Description of the campaign
   * @param {string} chainId - Chain ID for the campaign
   * @param {array} taskIds - Array of task IDs for the campaign
   * @returns {Promise} - Promise resolving to the campaign ID
   */
  async createCampaign(campaignName, campaignDescription, chainId, taskIds) {
    try {
      const campaign = await this.guildhall.campaigns.create({
        name: campaignName,
        description: campaignDescription,
        chainId: chainId,
        tasks: taskIds,
      });
      return campaign.id;
    } catch (error) {
      console.error('Error creating campaign:', error);
      throw error;
    }
  }

  /**
   * Execute a cross-chain task
   * @param {string} taskId - ID of the task to execute
   * @param {string} chainId - Chain ID for the task execution
   * @returns {Promise} - Promise resolving to the execution result
   */
  async executeTask(taskId, chainId) {
    try {
      const executionResult = await this.guildhall.tasks.execute({
        taskId: taskId,
        chainId: chainId,
      });
      return executionResult;
    } catch (error) {
      console.error('Error executing task:', error);
      throw error;
    }
  }

  /**
   * Execute a cross-chain campaign
   * @param {string} campaignId - ID of the campaign to execute
   * @param {string} chainId - Chain ID for the campaign execution
   * @returns {Promise} - Promise resolving to the execution result
   */
  async executeCampaign(campaignId, chainId) {
    try {
      const executionResult = await this.guildhall.campaigns.execute({
        campaignId: campaignId,
        chainId: chainId,
      });
      return executionResult;
    } catch (error) {
      console.error('Error executing campaign:', error);
      throw error;
    }
  }
}

// Example usage
async function main() {
  const apiKey = 'YOUR_API_KEY';
  const apiSecret = 'YOUR_API_SECRET';
  const chainId = '137'; // Polygon chain ID

  const crossChainGuildhall = new CrossChainGuildhall(apiKey, apiSecret, chainId);

  const taskName = 'Example Task';
  const taskDescription = 'This is an example task';
  const taskId = await crossChainGuildhall.createTask(taskName, taskDescription, chainId);
  console.log(`Task ID: ${taskId}`);

  const campaignName = 'Example Campaign';
  const campaignDescription = 'This is an example campaign';
  const taskIds = [taskId];
  const campaignId = await crossChainGuildhall.createCampaign(campaignName, campaignDescription, chainId, taskIds);
  console.log(`Campaign ID: ${campaignId}`);

  const executionResult = await crossChainGuildhall.executeTask(taskId, chainId);
  console.log(`Task execution result: ${JSON.stringify(executionResult)}`);

  const campaignExecutionResult = await crossChainGuildhall.executeCampaign(campaignId, chainId);
  console.log(`Campaign execution result: ${JSON.stringify(campaignExecutionResult)}`);
}

main().catch((error) => {
  console.error('Error:', error);
});
```
