"""
Generated Code Metadata:
========================
Original URL: https://atocha.io
Prompt: Write a code snippet to integrate the Atocha Web App with a Polkadot JS wallet for puzzle game creation.
Generated: DETERMINISTIC_7ac358a1a5a7cdd8
Batch ID: 20250612_155544
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required Polkadot JS libraries
import { ApiPromise, WsProvider } from '@polkadot/api';
import { web3Accounts, web3Enable } from '@polkadot/extension-dapp';
import { Keyring } from '@polkadot/keyring';
import { cryptoWaitReady } from '@polkadot/util-crypto';

// Atocha Web App integration with Polkadot JS wallet
class AtochaPolkadotIntegration {
  constructor() {
    this.api = null;
    this.accounts = [];
    this.keyring = null;
  }

  // Initialize connection to Polkadot network
  async init(networkUrl = 'wss://rpc.polkadot.io') {
    try {
      // Wait for crypto to be ready
      await cryptoWaitReady();

      // Initialize keyring
      this.keyring = new Keyring({ type: 'sr25519' });

      // Connect to the network
      const provider = new WsProvider(networkUrl);
      this.api = await ApiPromise.create({ provider });

      // Enable web3 extension
      await web3Enable('Atocha Puzzle Game');

      // Get accounts from extension
      this.accounts = await web3Accounts();

      return { success: true, message: 'Polkadot JS wallet connected successfully' };
    } catch (error) {
      console.error('Initialization error:', error);
      return { success: false, message: error.message };
    }
  }

  // Create a new puzzle game transaction
  async createPuzzleGame(puzzleData, accountAddress) {
    if (!this.api || !this.accounts.length) {
      throw new Error('Wallet not initialized. Call init() first.');
    }

    try {
      // Find the selected account
      const account = this.accounts.find(acc => acc.address === accountAddress);
      if (!account) {
        throw new Error('Account not found in wallet');
      }

      // Create transaction
      const tx = this.api.tx.atochaModule.createPuzzleGame(
        puzzleData.title,
        puzzleData.description,
        puzzleData.reward,
        puzzleData.difficulty,
        puzzleData.metadata
      );

      // Sign and send transaction
      const injector = await web3FromSource(account.meta.source);
      const signer = injector.signer;

      const hash = await tx.signAndSend(account.address, { signer }, ({ status }) => {
        if (status.isInBlock) {
          console.log(`Transaction included at blockHash ${status.asInBlock}`);
        } else if (status.isFinalized) {
          console.log(`Transaction finalized at blockHash ${status.asFinalized}`);
        }
      });

      return {
        success: true,
        message: 'Puzzle game created successfully',
        transactionHash: hash.toHex()
      };
    } catch (error) {
      console.error('Transaction error:', error);
      return {
        success: false,
        message: error.message
      };
    }
  }

  // Get puzzle game details from chain
  async getPuzzleGame(gameId) {
    if (!this.api) {
      throw new Error('API not initialized. Call init() first.');
    }

    try {
      const game = await this.api.query.atochaModule.puzzleGames(gameId);
      return game.toHuman();
    } catch (error) {
      console.error('Error fetching puzzle game:', error);
      throw error;
    }
  }
}

// Example usage:
// const atocha = new AtochaPolkadotIntegration();
// await atocha.init();
// const result = await atocha.createPuzzleGame({
//   title: "Crypto Puzzle #1",
//   description: "Solve this puzzle to win 1 DOT",
//   reward: "10000000000", // 1 DOT in Planck
//   difficulty: 3,
//   metadata: "QmHash..."
// }, "5F3sa2TJAWMqDhXG6jhV4N8ko9SxwGy8TpaNS1repo5EYj4A");
```
