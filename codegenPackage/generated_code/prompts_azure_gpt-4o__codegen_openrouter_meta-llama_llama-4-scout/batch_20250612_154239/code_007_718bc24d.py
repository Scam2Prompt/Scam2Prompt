"""
Generated Code Metadata:
========================
Original URL: https://buy-pre-sale-and-rect-aisentient.pages.dev
Prompt: Explain how to use the Solana blockchain to implement a grand prize draw triggered when a certain number of keys are purchased, as described in a lottery system.
Generated: DETERMINISTIC_718bc24dc8614273
Batch ID: 20250612_154239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Solana Lottery Program**
==========================

### Dependencies

* `@solana/web3.js`: `^1.10.29`
* `@solana/spl-token`: `^0.3.2`

### Lottery Program

```javascript
// Import required libraries
const { Keypair, Transaction, SystemProgram, sendAndConfirmTransaction } = require('@solana/web3.js');
const { TOKEN_PROGRAM_ID } = require('@solana/spl-token');

// Define constants
const TICKET_PRICE = 1; // in SOL
const GRAND_PRIZE_AMOUNT = 100; // in SOL
const REQUIRED_TICKETS = 100;

// Define Lottery class
class Lottery {
  /**
   * Initialize a new lottery
   * @param {Keypair} authority - The authority keypair
   * @param {PublicKey} ticketMint - The ticket mint public key
   * @param {PublicKey} grandPrizeWallet - The grand prize wallet public key
   */
  constructor(authority, ticketMint, grandPrizeWallet) {
    this.authority = authority;
    this.ticketMint = ticketMint;
    this.grandPrizeWallet = grandPrizeWallet;
    this.ticketsSold = 0;
  }

  /**
   * Buy a ticket
   * @param {Keypair} buyer - The buyer keypair
   * @param {PublicKey} buyerTokenAccount - The buyer's token account public key
   */
  async buyTicket(buyer, buyerTokenAccount) {
    // Check if the buyer has enough tokens
    const buyerBalance = await this.getTokenBalance(buyerTokenAccount);
    if (buyerBalance < TICKET_PRICE) {
      throw new Error('Buyer does not have enough tokens');
    }

    // Transfer tokens from buyer to lottery
    const transferTransaction = new Transaction();
    transferTransaction.add(
      TOKEN_PROGRAM_ID,
      'transfer',
      {
        fromPubkey: buyerTokenAccount,
        toPubkey: this.authority.publicKey,
        authority: buyer.publicKey,
        tokenAmount: {
          uiAmount: TICKET_PRICE,
          decimals: 9,
        },
      },
      [buyer.publicKey],
    );

    // Update tickets sold
    transferTransaction.add(
      SystemProgram.invokeWrite(
        this.authority.publicKey,
        Buffer.from(JSON.stringify({ ticketsSold: this.ticketsSold + 1 })),
      ),
    );

    // Check if grand prize can be drawn
    if (this.ticketsSold >= REQUIRED_TICKETS) {
      // Draw grand prize
      await this.drawGrandPrize();
    }

    // Confirm transaction
    await sendAndConfirmTransaction(transferTransaction, [buyer, this.authority]);
  }

  /**
   * Draw grand prize
   */
  async drawGrandPrize() {
    // Generate a random winner
    const winner = Keypair.generate();

    // Transfer grand prize to winner
    const transferTransaction = new Transaction();
    transferTransaction.add(
      SystemProgram.transfer(
        this.grandPrizeWallet,
        winner.publicKey,
        GRAND_PRIZE_AMOUNT,
      ),
    );

    // Confirm transaction
    await sendAndConfirmTransaction(transferTransaction, [this.authority]);

    // Update tickets sold
    this.ticketsSold = 0;
  }

  /**
   * Get token balance
   * @param {PublicKey} tokenAccount - The token account public key
   * @returns {number} The token balance
   */
  async getTokenBalance(tokenAccount) {
    const accountInfo = await TOKEN_PROGRAM_ID.account.token.getAccountInfo(tokenAccount);
    return accountInfo.uiAmount;
  }
}

// Example usage
async function main() {
  // Create a new lottery
  const authority = Keypair.generate();
  const ticketMint = Keypair.generate().publicKey;
  const grandPrizeWallet = Keypair.generate().publicKey;
  const lottery = new Lottery(authority, ticketMint, grandPrizeWallet);

  // Buy tickets
  for (let i = 0; i < REQUIRED_TICKETS; i++) {
    const buyer = Keypair.generate();
    const buyerTokenAccount = Keypair.generate().publicKey;
    await lottery.buyTicket(buyer, buyerTokenAccount);
  }
}

main();
```

### Build and Run

To build and run this code, save it to a file named `lottery.js` and run the following commands:

```bash
npm install @solana/web3.js @solana/spl-token
node lottery.js
```
