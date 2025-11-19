"""
Generated Code Metadata:
========================
Original URL: https://solmeme-io.pages.dev
Prompt: Develop a Solana-based NFT marketplace, utilizing the SPL token program and token extensions for enhanced compliance.
Generated: DETERMINISTIC_3639ad1585bbacd5
Batch ID: 20250622_211011
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Solana NFT Marketplace**
==========================

**dependencies:**
* `@solana/web3.js`: ^1.10.29
* `@solana/spl-token`: ^0.3.2

```javascript
// Import required libraries
const { Connection, PublicKey, Transaction, clusterApiUrl } = require('@solana/web3.js');
const { TOKEN_PROGRAM_ID, createTransferInstruction, getTokenAccountBalance } = require('@solana/spl-token');

// Set up constants
const MARKETPLACE_PROGRAM_ID = new PublicKey('marketplace-program-id');
const SPL_TOKEN_PROGRAM_ID = TOKEN_PROGRAM_ID;
const CLUSTER_API_URL = clusterApiUrl('devnet');

// Set up marketplace class
class Marketplace {
  /**
   * @param {Connection} connection - Solana connection object
   */
  constructor(connection) {
    this.connection = connection;
  }

  /**
   * Create a new NFT listing
   * @param {PublicKey} nftMint - Public key of the NFT mint
   * @param {PublicKey} seller - Public key of the seller
   * @param {number} price - Price of the NFT
   * @returns {Promise<Transaction>} - Transaction to create the listing
   */
  async createListing(nftMint, seller, price) {
    // Create a new transaction
    const transaction = new Transaction();

    // Create an account for the listing
    const listingAccount = await this.createListingAccount();

    // Create the listing instruction
    const createListingInstruction = {
      programId: MARKETPLACE_PROGRAM_ID,
      accounts: [
        listingAccount,
        nftMint,
        seller,
      ],
      data: Buffer.from(JSON.stringify({
        instruction: 'create_listing',
        price,
      })),
    };

    // Add the instruction to the transaction
    transaction.add(createListingInstruction);

    // Sign the transaction
    transaction.sign(seller);

    return transaction;
  }

  /**
   * Buy an NFT listing
   * @param {PublicKey} listingAccount - Public key of the listing account
   * @param {PublicKey} buyer - Public key of the buyer
   * @param {PublicKey} nftMint - Public key of the NFT mint
   * @returns {Promise<Transaction>} - Transaction to buy the NFT
   */
  async buyNFT(listingAccount, buyer, nftMint) {
    // Get the listing details
    const listingDetails = await this.getListingDetails(listingAccount);

    // Check if the listing exists
    if (!listingDetails) {
      throw new Error('Listing does not exist');
    }

    // Create a new transaction
    const transaction = new Transaction();

    // Create a token account for the buyer
    const buyerTokenAccount = await this.createTokenAccount(buyer, nftMint);

    // Create the transfer instruction
    const transferInstruction = createTransferInstruction(
      buyerTokenAccount,
      listingDetails.sellerTokenAccount,
      listingDetails.seller,
      nftMint,
      SPL_TOKEN_PROGRAM_ID,
    );

    // Create the close listing instruction
    const closeListingInstruction = {
      programId: MARKETPLACE_PROGRAM_ID,
      accounts: [
        listingAccount,
      ],
      data: Buffer.from(JSON.stringify({
        instruction: 'close_listing',
      })),
    };

    // Add the instructions to the transaction
    transaction.add(transferInstruction);
    transaction.add(closeListingInstruction);

    // Sign the transaction
    transaction.sign(buyer);

    return transaction;
  }

  /**
   * Get the details of a listing
   * @param {PublicKey} listingAccount - Public key of the listing account
   * @returns {Promise<Object>} - Details of the listing
   */
  async getListingDetails(listingAccount) {
    // Get the account info
    const accountInfo = await this.connection.getAccountInfo(listingAccount);

    // Check if the account exists
    if (!accountInfo) {
      return null;
    }

    // Parse the account data
    const listingDetails = JSON.parse(accountInfo.data.toString());

    return listingDetails;
  }

  /**
   * Create a new listing account
   * @returns {Promise<PublicKey>} - Public key of the new listing account
   */
  async createListingAccount() {
    // Create a new account
    const newAccount = await this.connection.createAccount(
      new PublicKey(0),
      0,
      0,
    );

    return newAccount.publicKey;
  }

  /**
   * Create a new token account
   * @param {PublicKey} owner - Public key of the owner
   * @param {PublicKey} mint - Public key of the mint
   * @returns {Promise<PublicKey>} - Public key of the new token account
   */
  async createTokenAccount(owner, mint) {
    // Get the token account balance
    const tokenAccountBalance = await getTokenAccountBalance(
      this.connection,
      owner,
      mint,
    );

    // Check if the token account exists
    if (tokenAccountBalance) {
      return tokenAccountBalance.address;
    }

    // Create a new token account
    const newTokenAccount = await this.connection.createTokenAccount(
      owner,
      mint,
      SPL_TOKEN_PROGRAM_ID,
    );

    return newTokenAccount.publicKey;
  }
}

// Example usage
async function main() {
  // Create a new connection
  const connection = new Connection(CLUSTER_API_URL);

  // Create a new marketplace
  const marketplace = new Marketplace(connection);

  // Create a new NFT mint
  const nftMint = await connection.createMint(
    new PublicKey(0),
    0,
    0,
  );

  // Create a new seller
  const seller = await connection.createAccount(
    new PublicKey(0),
    0,
    0,
  );

  // Create a new listing
  const listingTransaction = await marketplace.createListing(
    nftMint.publicKey,
    seller.publicKey,
    10,
  );

  // Sign and send the transaction
  const signature = await connection.sendTransaction(listingTransaction);

  console.log(`Listing created: ${signature}`);

  // Buy the NFT
  const buyer = await connection.createAccount(
    new PublicKey(0),
    0,
    0,
  );

  const buyTransaction = await marketplace.buyNFT(
    listingTransaction.instructions[0].accounts[0],
    buyer.publicKey,
    nftMint.publicKey,
  );

  // Sign and send the transaction
  const buySignature = await connection.sendTransaction(buyTransaction);

  console.log(`NFT bought: ${buySignature}`);
}

main().catch((error) => {
  console.error(error);
});
```
