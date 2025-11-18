"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://be-solana-methods-v1.docs-62t.pages.dev
Prompt: Generate a smart contract client library in TypeScript using Código's platform that supports token exchange functionality on Solana.
Generated: DETERMINISTIC_f192895068836fc6
Batch ID: 20250612_150946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```typescript
// Import required libraries and dependencies
import { Connection, PublicKey, Transaction, clusterApiUrl } from "@solana/web3.js";
import { Token, TOKEN_PROGRAM_ID } from "@solana/spl-token";

// Define the configuration and constants
const SOLANA_NETWORK = "mainnet-beta";
const connection = new Connection(clusterApiUrl(SOLANA_NETWORK), "confirmed");

// TokenExchangeClient: A TypeScript client library for token exchange functionality on Solana
export class TokenExchangeClient {
  private connection: Connection;

  constructor() {
    this.connection = connection;
  }

  /**
   * Get the balance of a token for a specific wallet address.
   *
   * @param walletAddress - The public key of the wallet.
   * @param tokenMintAddress - The mint address of the token.
   * @returns The token balance.
   */
  async getTokenBalance(walletAddress: string, tokenMintAddress: string): Promise<number> {
    try {
      const walletPubkey = new PublicKey(walletAddress);
      const tokenMintPubkey = new PublicKey(tokenMintAddress);

      // Find associated token account
      const tokenAccounts = await this.connection.getTokenAccountsByOwner(walletPubkey, {
        mint: tokenMintPubkey,
      });

      if (tokenAccounts.value.length === 0) {
        return 0; // No associated token accounts found
      }

      const balanceInfo = await this.connection.getTokenAccountBalance(tokenAccounts.value[0].pubkey);
      return parseFloat(balanceInfo.value.amount); // Return the balance as a number
    } catch (error) {
      console.error("Failed to get token balance:", error);
      throw new Error("Failed to retrieve token balance.");
    }
  }

  /**
   * Transfer tokens between wallets.
   *
   * @param senderWallet - The sender's public key.
   * @param recipientWallet - The recipient's public key.
   * @param tokenMintAddress - The mint address of the token.
   * @param amount - The amount to transfer.
   * @param senderPrivateKey - The sender's private key for signing the transaction.
   * @returns The transaction ID.
   */
  async transferTokens(
    senderWallet: string,
    recipientWallet: string,
    tokenMintAddress: string,
    amount: number,
    senderPrivateKey: Uint8Array
  ): Promise<string> {
    try {
      const senderPubkey = new PublicKey(senderWallet);
      const recipientPubkey = new PublicKey(recipientWallet);
      const tokenMintPubkey = new PublicKey(tokenMintAddress);

      // Find sender's associated token account
      const senderTokenAccounts = await this.connection.getTokenAccountsByOwner(senderPubkey, {
        mint: tokenMintPubkey,
      });

      if (senderTokenAccounts.value.length === 0) {
        throw new Error("Sender does not have a token account for this mint.");
      }

      const senderTokenAccountPubkey = senderTokenAccounts.value[0].pubkey;

      // Find recipient's associated token account or create one if it doesn't exist
      const recipientTokenAccounts = await this.connection.getTokenAccountsByOwner(recipientPubkey, {
        mint: tokenMintPubkey,
      });

      let recipientTokenAccountPubkey: PublicKey;
      if (recipientTokenAccounts.value.length === 0) {
        const token = new Token(this.connection, tokenMintPubkey, TOKEN_PROGRAM_ID, senderPubkey);
        recipientTokenAccountPubkey = await token.createAssociatedTokenAccount(recipientPubkey);
      } else {
        recipientTokenAccountPubkey = recipientTokenAccounts.value[0].pubkey;
      }

      // Create the transaction for token transfer
      const transaction = new Transaction().add(
        Token.createTransferInstruction(
          TOKEN_PROGRAM_ID,
          senderTokenAccountPubkey,
          recipientTokenAccountPubkey,
          senderPubkey,
          [],
          amount
        )
      );

      // Sign and send the transaction
      const { blockhash } = await this.connection.getRecentBlockhash();
      transaction.recentBlockhash = blockhash;
      transaction.feePayer = senderPubkey;
      transaction.sign({ publicKey: senderPubkey, secretKey: senderPrivateKey });

      const txid = await this.connection.sendRawTransaction(transaction.serialize());
      return txid;
    } catch (error) {
      console.error("Failed to transfer tokens:", error);
      throw new Error("Token transfer failed.");
    }
  }
}
```
