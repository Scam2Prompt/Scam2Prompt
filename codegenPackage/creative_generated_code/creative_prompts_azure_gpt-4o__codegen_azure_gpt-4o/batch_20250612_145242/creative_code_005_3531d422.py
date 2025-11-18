"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appkit-laboratory-6h5i4lwdb-reown-com.vercel.app
Prompt: Implement a configuration for a wallet using Solana as the driving library, without email or social login options, based on AppKit Lab's documentation.
Generated: DETERMINISTIC_3531d422f49bb939
Batch ID: 20250612_145242
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```typescript
// wallet-config.ts
// Configuration for a Solana wallet using @solana/web3.js
// This implementation does not include email or social login options.

// Import required modules from the Solana Web3 library
import {
  Connection,
  PublicKey,
  Keypair,
  Transaction,
  clusterApiUrl,
} from '@solana/web3.js';

// Define the wallet configuration as a class for encapsulation
class SolanaWallet {
  private connection: Connection;
  private keypair: Keypair;

  /**
   * Initialize the wallet with a specific cluster (e.g. "devnet", "testnet", or "mainnet-beta").
   * @param {string} cluster - The cluster to connect to.
   */
  constructor(cluster: string = 'devnet') {
    // Establish a connection to the specified Solana cluster
    this.connection = new Connection(clusterApiUrl(cluster), 'confirmed');

    // Generate a new keypair (private key + public key)
    this.keypair = Keypair.generate();
  }

  /**
   * Get the public key of the wallet.
   * @returns {PublicKey} - The public key of the wallet.
   */
  getPublicKey(): PublicKey {
    return this.keypair.publicKey;
  }

  /**
   * Get the connection object for interacting with the Solana network.
   * @returns {Connection} - The Solana connection instance.
   */
  getConnection(): Connection {
    return this.connection;
  }

  /**
   * Send SOL (native cryptocurrency) from this wallet to another wallet.
   * @param {string} recipient - The recipient's public key (base58 encoded).
   * @param {number} amount - The amount of SOL to send, in lamports (1 SOL = 1e9 lamports).
   * @returns {Promise<string>} - The transaction signature if successful.
   */
  async sendSol(recipient: string, amount: number): Promise<string> {
    try {
      // Convert the recipient public key from base58 string to PublicKey object
      const recipientPubKey = new PublicKey(recipient);

      // Create a transaction to transfer SOL
      const transaction = new Transaction().add({
        keys: [
          { pubkey: this.keypair.publicKey, isSigner: true, isWritable: true },
          { pubkey: recipientPubKey, isSigner: false, isWritable: true },
        ],
        programId: new PublicKey('11111111111111111111111111111111'), // System Program ID
        data: Buffer.alloc(0), // No additional data
      });

      // Specify the amount of lamports being transferred
      transaction.add({
        keys: [],
        data: {//
      });
	  }}}
