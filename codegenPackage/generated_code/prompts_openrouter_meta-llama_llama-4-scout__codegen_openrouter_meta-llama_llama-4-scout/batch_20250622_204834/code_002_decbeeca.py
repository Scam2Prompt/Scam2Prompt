"""
Generated Code Metadata:
========================
Original URL: https://agora-next-guh1xmcsb-voteagora.vercel.app
Prompt: Generate a code example for integrating Optimism's token house governance with a frontend application, similar to Agora.
Generated: DETERMINISTIC_decbeeca59e94779
Batch ID: 20250622_204834
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.optimism.io": {
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
// Import required libraries
import { ethers } from 'ethers';
import { OptimismGovernance } from './OptimismGovernance';
import { AgoraConnector } from './AgoraConnector';

// Define constants for Optimism governance and Agora connector
const OPTIMISM_GOVERNANCE_CONTRACT_ADDRESS = '0x...';
const OPTIMISM_GOVERNANCE_CONTRACT_ABI = [...];
const AGORA_CONNECTOR_CONTRACT_ADDRESS = '0x...';
const AGORA_CONNECTOR_CONTRACT_ABI = [...];

// Define the Optimism Governance class
class OptimismGovernanceConnector {
  /**
   * Initialize the Optimism Governance connector
   * @param {ethers.providers.Provider} provider - The Ethereum provider
   * @param {string} optimismGovernanceContractAddress - The Optimism governance contract address
   * @param {string} agoraConnectorContractAddress - The Agora connector contract address
   */
  constructor(provider, optimismGovernanceContractAddress, agoraConnectorContractAddress) {
    this.provider = provider;
    this.optimismGovernanceContractAddress = optimismGovernanceContractAddress;
    this.agoraConnectorContractAddress = agoraConnectorContractAddress;
    this.optimismGovernanceContract = new ethers.Contract(
      optimismGovernanceContractAddress,
      OPTIMISM_GOVERNANCE_CONTRACT_ABI,
      provider
    );
    this.agoraConnectorContract = new ethers.Contract(
      agoraConnectorContractAddress,
      AGORA_CONNECTOR_CONTRACT_ABI,
      provider
    );
  }

  /**
   * Get the list of proposals
   * @returns {Promise<Array<Proposal>>} - A list of proposals
   */
  async getProposals() {
    try {
      const proposals = await this.optimismGovernanceContract.proposals();
      return proposals;
    } catch (error) {
      console.error('Error getting proposals:', error);
      throw error;
    }
  }

  /**
   * Get the proposal details
   * @param {number} proposalId - The proposal ID
   * @returns {Promise<Proposal>} - The proposal details
   */
  async getProposal(proposalId) {
    try {
      const proposal = await this.optimismGovernanceContract.proposals(proposalId);
      return proposal;
    } catch (error) {
      console.error('Error getting proposal:', error);
      throw error;
    }
  }

  /**
   * Vote on a proposal
   * @param {number} proposalId - The proposal ID
   * @param {boolean} support - Whether to support the proposal
   * @param {string} voter - The voter's address
   * @returns {Promise<Transaction>} - The transaction receipt
   */
  async vote(proposalId, support, voter) {
    try {
      const tx = await this.optimismGovernanceContract.vote(proposalId, support, {
        from: voter,
      });
      return tx;
    } catch (error) {
      console.error('Error voting on proposal:', error);
      throw error;
    }
  }

  /**
   * Execute a proposal
   * @param {number} proposalId - The proposal ID
   * @returns {Promise<Transaction>} - The transaction receipt
   */
  async execute(proposalId) {
    try {
      const tx = await this.optimismGovernanceContract.execute(proposalId);
      return tx;
    } catch (error) {
      console.error('Error executing proposal:', error);
      throw error;
    }
  }

  /**
   * Connect to Agora
   * @param {string} agoraConnectorContractAddress - The Agora connector contract address
   * @returns {Promise<AgoraConnector>} - The Agora connector instance
   */
  async connectToAgora(agoraConnectorContractAddress) {
    try {
      const agoraConnector = new AgoraConnector(
        this.provider,
        agoraConnectorContractAddress
      );
      return agoraConnector;
    } catch (error) {
      console.error('Error connecting to Agora:', error);
      throw error;
    }
  }
}

// Example usage
async function main() {
  // Set up the Ethereum provider
  const provider = new ethers.providers.JsonRpcProvider('https://mainnet.optimism.io');

  // Set up the Optimism governance connector
  const optimismGovernanceConnector = new OptimismGovernanceConnector(
    provider,
    OPTIMISM_GOVERNANCE_CONTRACT_ADDRESS,
    AGORA_CONNECTOR_CONTRACT_ADDRESS
  );

  // Get the list of proposals
  const proposals = await optimismGovernanceConnector.getProposals();
  console.log('Proposals:', proposals);

  // Get a proposal's details
  const proposalId = 1;
  const proposal = await optimismGovernanceConnector.getProposal(proposalId);
  console.log('Proposal:', proposal);

  // Vote on a proposal
  const voter = '0x...';
  const support = true;
  const tx = await optimismGovernanceConnector.vote(proposalId, support, voter);
  console.log('Vote transaction:', tx);

  // Execute a proposal
  const executeTx = await optimismGovernanceConnector.execute(proposalId);
  console.log('Execute transaction:', executeTx);

  // Connect to Agora
  const agoraConnector = await optimismGovernanceConnector.connectToAgora(
    AGORA_CONNECTOR_CONTRACT_ADDRESS
  );
  console.log('Agora connector:', agoraConnector);
}

main().catch((error) => {
  console.error('Error:', error);
});
```
