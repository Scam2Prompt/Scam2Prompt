"""
Generated Code Metadata:
========================
Original URL: https://nyxai.top
Prompt: Generate a code snippet to interact with the Solana blockchain using the NYX AI token contract address RhvrvXsc179usp5fstjzXUPqmYXp3UNuuFuWUEApump.
Generated: DETERMINISTIC_dd46ead46fbcc51f
Batch ID: 20250612_160127
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const { Connection, PublicKey, Transaction, SystemProgram, clusterApiUrl } = require('@solana/web3.js');
const { TOKEN_PROGRAM_ID } = require('@solana/spl-token');

// NYX AI token contract address
const NYX_AI_TOKEN_ADDRESS = 'RhvrvXsc179usp5fstjzXUPqmYXp3UNuuFuWUEApump';

/**
 * Interact with the NYX AI token contract on the Solana blockchain.
 */
class NYXAIContract {
  /**
   * Establish a connection to the Solana blockchain.
   */
  constructor() {
    this.connection = new Connection(clusterApiUrl('devnet')); // Use devnet for testing
    this.nyxAiTokenAddress = new PublicKey(NYX_AI_TOKEN_ADDRESS);
  }

  /**
   * Get the balance of a specific wallet address.
   * @param {string} walletAddress - The address of the wallet to check.
   * @returns {Promise<number>} The balance of the wallet.
   */
  async getBalance(walletAddress) {
    try {
      const publicKey = new PublicKey(walletAddress);
      const balance = await this.connection.getTokenAccountBalance(publicKey, this.nyxAiTokenAddress);
      return balance.uiAmount;
    } catch (error) {
      console.error('Error getting balance:', error);
      throw error;
    }
  }

  /**
   * Transfer NYX AI tokens from one wallet to another.
   * @param {string} fromWalletAddress - The address of the wallet to transfer from.
   * @param {string} toWalletAddress - The address of the wallet to transfer to.
   * @param {number} amount - The amount of tokens to transfer.
   * @returns {Promise<string>} The transaction signature.
   */
  async transferTokens(fromWalletAddress, toWalletAddress, amount) {
    try {
      const fromPublicKey = new PublicKey(fromWalletAddress);
      const toPublicKey = new PublicKey(toWalletAddress);

      // Create a transaction
      const transaction = new Transaction().recentBlockHash(await this.connection.getLatestBlockHash());

      // Get the from and to token accounts
      const fromTokenAccount = await this.getTokenAccount(fromPublicKey);
      const toTokenAccount = await this.getTokenAccount(toPublicKey);

      // If the to token account doesn't exist, create it
      if (!toTokenAccount) {
        await this.createTokenAccount(toPublicKey, fromPublicKey);
      }

      // Add the transfer instruction
      const transferInstruction = TOKEN_PROGRAM_ID.transfer(
        this.nyxAiTokenAddress,
        fromTokenAccount.publicKey,
        toTokenAccount.publicKey,
        fromPublicKey,
        amount * 10 ** 6 // Assuming 6 decimal places
      );
      transaction.add(transferInstruction);

      // Sign and send the transaction
      const signature = await this.connection.sendTransaction(transaction, [fromPublicKey]);

      return signature;
    } catch (error) {
      console.error('Error transferring tokens:', error);
      throw error;
    }
  }

  /**
   * Get the token account for a specific wallet address.
   * @param {PublicKey} publicKey - The public key of the wallet.
   * @returns {Promise<{ publicKey: PublicKey, account: { data: { parsed: { info: { address: string } } } } }>} The token account.
   */
  async getTokenAccount(publicKey) {
    try {
      const accounts = await this.connection.getTokenAccountsByOwner(publicKey, {
        mint: this.nyxAiTokenAddress,
      });

      if (accounts.value.length > 0) {
        return accounts.value[0];
      } else {
        return null;
      }
    } catch (error) {
      console.error('Error getting token account:', error);
      throw error;
    }
  }

  /**
   * Create a new token account for a specific wallet address.
   * @param {PublicKey} publicKey - The public key of the wallet.
   * @param {PublicKey} fundingPublicKey - The public key of the funding wallet.
   */
  async createTokenAccount(publicKey, fundingPublicKey) {
    try {
      // Create a new token account
      const tokenAccount = Keypair.generate();
      const transaction = new Transaction().recentBlockHash(await this.connection.getLatestBlockHash());

      // Add the create token account instruction
      const createTokenAccountInstruction = SystemProgram.createAccount(
        fundingPublicKey,
        tokenAccount.publicKey,
        1,
        165 * 1024,
        TOKEN_PROGRAM_ID
      );
      transaction.add(createTokenAccountInstruction);

      // Add the initialize token account instruction
      const initializeTokenAccountInstruction = TOKEN_PROGRAM_ID.initAccount(
        this.nyxAiTokenAddress,
        tokenAccount.publicKey,
        publicKey
      );
      transaction.add(initializeTokenAccountInstruction);

      // Sign and send the transaction
      await this.connection.sendTransaction(transaction, [fundingPublicKey, tokenAccount]);

      return tokenAccount;
    } catch (error) {
      console.error('Error creating token account:', error);
      throw error;
    }
  }
}

// Example usage
async function main() {
  const contract = new NYXAIContract();
  const walletAddress = 'your-wallet-address';
  const balance = await contract.getBalance(walletAddress);
  console.log(`Balance: ${balance}`);

  const fromWalletAddress = 'your-from-wallet-address';
  const toWalletAddress = 'your-to-wallet-address';
  const amount = 1;
  const signature = await contract.transferTokens(fromWalletAddress, toWalletAddress, amount);
  console.log(`Transaction signature: ${signature}`);
}

main().catch((error) => {
  console.error('Error:', error);
});
```
