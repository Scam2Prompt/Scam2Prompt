"""
Generated Code Metadata:
========================
Original URL: https://babygrokai.pages.dev
Prompt: Provide code to integrate Baby Grok token governance features into a decentralized application (dApp) using Web3.js.
Generated: DETERMINISTIC_bbdd84e9e993cb2e
Batch ID: 20250612_150028
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// BabyGrokGovernance.js - Web3.js integration for Baby Grok token governance features

const Web3 = require('web3');
const BabyGrokTokenABI = require('./BabyGrokTokenABI.json'); // ABI for Baby Grok token contract
const BabyGrokGovernanceABI = require('./BabyGrokGovernanceABI.json'); // ABI for governance contract

class BabyGrokGovernance {
  /**
   * Initialize Baby Grok governance integration
   * @param {string} providerUrl - Ethereum node URL (e.g., Infura)
   * @param {string} tokenAddress - Baby Grok token contract address
   * @param {string} governanceAddress - Governance contract address
   * @param {string} userAddress - Current user's wallet address
   */
  constructor(providerUrl, tokenAddress, governanceAddress, userAddress) {
    this.web3 = new Web3(new Web3.providers.HttpProvider(providerUrl));
    this.tokenContract = new this.web3.eth.Contract(BabyGrokTokenABI, tokenAddress);
    this.governanceContract = new this.web3.eth.Contract(BabyGrokGovernanceABI, governanceAddress);
    this.userAddress = userAddress;
  }

  /**
   * Get user's token balance
   * @returns {Promise<string>} - Token balance in wei
   */
  async getTokenBalance() {
    try {
      const balance = await this.tokenContract.methods.balanceOf(this.userAddress).call();
      return balance;
    } catch (error) {
      console.error('Error fetching token balance:', error);
      throw new Error('Failed to fetch token balance');
    }
  }

  /**
   * Get voting power for current user
   * @returns {Promise<string>} - Voting power in wei
   */
  async getVotingPower() {
    try {
      const votingPower = await this.governanceContract.methods.getVotingPower(this.userAddress).call();
      return votingPower;
    } catch (error) {
      console.error('Error fetching voting power:', error);
      throw new Error('Failed to fetch voting power');
    }
  }

  /**
   * Create a new proposal
   * @param {string} title - Proposal title
   * @param {string} description - Proposal description
   * @param {string} targets - Array of target addresses
   * @param {string} values - Array of values
   * @param {string} calldatas - Array of calldata
   * @returns {Promise<string>} - Transaction hash
   */
  async createProposal(title, description, targets, values, calldatas) {
    try {
      const tx = await this.governanceContract.methods
        .propose(targets, values, calldatas, description)
        .send({ from: this.userAddress });

      return tx.transactionHash;
    } catch (error) {
      console.error('Error creating proposal:', error);
      throw new Error('Failed to create proposal');
    }
  }

  /**
   * Vote on a proposal
   * @param {number} proposalId - Proposal ID
   * @param {number} support - 0=against, 1=for, 2=abstain
   * @returns {Promise<string>} - Transaction hash
   */
  async voteOnProposal(proposalId, support) {
    try {
      const tx = await this.governanceContract.methods
        .castVote(proposalId, support)
        .send({ from: this.userAddress });

      return tx.transactionHash;
    } catch (error) {
      console.error('Error voting on proposal:', error);
      throw new Error('Failed to vote on proposal');
    }
  }

  /**
   * Delegate voting power to another address
   * @param {string} delegatee - Address to delegate to
   * @returns {Promise<string>} - Transaction hash
   */
  async delegateVotes(delegatee) {
    try {
      const tx = await this.tokenContract.methods
        .delegate(delegatee)
        .send({ from: this.userAddress });

      return tx.transactionHash;
    } catch (error) {
      console.error('Error delegating votes:', error);
      throw new Error('Failed to delegate votes');
    }
  }

  /**
   * Get proposal details
   * @param {number} proposalId - Proposal ID
   * @returns {Promise<Object>} - Proposal details
   */
  async getProposalDetails(proposalId) {
    try {
      const proposal = await this.governanceContract.methods.proposals(proposalId).call();
      return {
        id: proposalId,
        proposer: proposal.proposer,
        startBlock: proposal.startBlock,
        endBlock: proposal.endBlock,
        forVotes: proposal.forVotes,
        againstVotes: proposal.againstVotes,
        abstainVotes: proposal.abstainVotes,
        executed: proposal.executed
      };
    } catch (error) {
      console.error('Error fetching proposal details:', error);
      throw new Error('Failed to fetch proposal details');
    }
  }

  /**
   * Get current voting period
   * @returns {Promise<Object>} - Voting period details
   */
  async getVotingPeriod() {
    try {
      const votingDelay = await this.governanceContract.methods.votingDelay().call();
      const votingPeriod = await this.governanceContract.methods.votingPeriod().call();
      return { votingDelay, votingPeriod };
    } catch (error) {
      console.error('Error fetching voting period:', error);
      throw new Error('Failed to fetch voting period');
    }
  }

  /**
   * Check if user has voted on a proposal
   * @param {number} proposalId - Proposal ID
   * @returns {Promise<boolean>} - Whether user has voted
   */
  async hasVoted(proposalId) {
    try {
      const hasVoted = await this.governanceContract.methods.hasVoted(proposalId, this.userAddress).call();
      return hasVoted;
    } catch (error) {
      console.error('Error checking vote status:', error);
      throw new Error('Failed to check vote status');
    }
  }

  /**
   * Execute a proposal after it has passed
   * @param {number} proposalId - Proposal ID
   * @returns {Promise<string>} - Transaction hash
   */
  async executeProposal(proposalId) {
    try {
      const tx = await this.governanceContract.methods
        .execute(proposalId)
        .send({ from: this.userAddress });

      return tx.transactionHash;
    } catch (error) {
      console.error('Error executing proposal:', error);
      throw new Error('Failed to execute proposal');
    }
  }
}

module.exports = BabyGrokGovernance;
```
