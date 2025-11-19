"""
Generated Code Metadata:
========================
Original URL: https://redstone-finance.pages.dev
Prompt: Write a script to utilize RedStone's permanent storage on Arweave for tracking data provider reputations. Include steps for querying stored data.
Generated: DETERMINISTIC_a40f1982fafaa6ba
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const Arweave = require('arweave');
const { WarpFactory, LoggerFactory } = require('warp-contracts');
const { DeployPlugin } = require('warp-contracts-plugin-deploy');

// Initialize Arweave
const arweave = Arweave.init({
  host: 'arweave.net',
  port: 443,
  protocol: 'https'
});

// Initialize Warp
LoggerFactory.INST.logLevel('error');
const warp = WarpFactory.forMainnet().use(new DeployPlugin());

// Contract source and state
const contractSrc = `
export async function handle(state, action) {
  const { input, caller } = action;
  
  if (input.function === 'addReputation') {
    const { provider, score } = input;
    if (!state.reputations[caller]) {
      state.reputations[caller] = {};
    }
    state.reputations[caller][provider] = score;
    return { state };
  }

  if (input.function === 'getReputation') {
    const { provider } = input;
    return { result: state.reputations[caller]?.[provider] || 0 };
  }

  throw new ContractError('Invalid function');
}
`;

// Deploy contract
async function deployContract() {
  try {
    const wallet = await arweave.wallets.generate();
    const walletAddress = await arweave.wallets.getAddress(wallet);

    const initialState = {
      reputations: {}
    };

    const { contractTxId } = await warp.deploy({
      wallet,
      initState: JSON.stringify(initialState),
      src: contractSrc,
    });

    console.log('Contract deployed with TX ID:', contractTxId);
    return contractTxId;
  } catch (error) {
    console.error('Error deploying contract:', error);
    throw error;
  }
}

// Interact with contract
class ReputationTracker {
  constructor(contractTxId, wallet) {
    this.contractTxId = contractTxId;
    this.wallet = wallet;
    this.contract = warp.contract(contractTxId).connect(wallet);
  }

  async addReputation(provider, score) {
    try {
      await this.contract.writeInteraction({
        function: 'addReputation',
        provider,
        score
      });
      console.log(`Reputation added for provider: ${provider}`);
    } catch (error) {
      console.error('Error adding reputation:', error);
      throw error;
    }
  }

  async getReputation(provider) {
    try {
      const { cachedValue } = await this.contract.readState();
      const reputation = cachedValue.state.reputations[this.wallet.address]?.[provider] || 0;
      console.log(`Reputation for ${provider}:`, reputation);
      return reputation;
    } catch (error) {
      console.error('Error getting reputation:', error);
      throw error;
    }
  }
}

// Example usage
(async () => {
  try {
    // Deploy a new contract
    const contractTxId = await deployContract();
    
    // Generate a wallet for testing
    const wallet = await arweave.wallets.generate();
    
    // Initialize tracker
    const tracker = new ReputationTracker(contractTxId, wallet);
    
    // Add reputation
    await tracker.addReputation('redstone', 5);
    
    // Query reputation
    await tracker.getReputation('redstone');
  } catch (error) {
    console.error('Script error:', error);
  }
})();
```
