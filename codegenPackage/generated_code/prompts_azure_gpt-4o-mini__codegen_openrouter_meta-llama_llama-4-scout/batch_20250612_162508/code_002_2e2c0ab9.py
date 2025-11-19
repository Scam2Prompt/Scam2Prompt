"""
Generated Code Metadata:
========================
Original URL: https://bongers-testnets-r8pj.vercel.app
Prompt: How can I implement a marketplace feature for trading Bongers Origin NFTs on the Solana blockchain?
Generated: DETERMINISTIC_2e2c0ab95d0377c2
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Solana Marketplace for Bongers Origin NFTs**
=====================================================

**dependencies:**
* `@solana/web3.js`: ^1.10.23
* `@solana/spl-token`: ^0.3.1

```javascript
// Import required libraries
const { Connection, PublicKey, Transaction, clusterApiUrl } = require('@solana/web3.js');
const { TOKEN_PROGRAM_ID } = require('@solana/spl-token');

// Set up constants
const BONGERS_ORIGIN_NFT_PROGRAM_ID = new PublicKey('BongersOriginNFTProgramId');
const MARKETPLACE_PROGRAM_ID = new PublicKey('MarketplaceProgramId');
const SOLANA_CLUSTER_URL = clusterApiUrl('devnet');

// Set up the Solana connection
const connection = new Connection(SOLANA_CLUSTER_URL, 'confirmed');

/**
 * Create a new marketplace listing for a Bongers Origin NFT
 * @param {PublicKey} nftMintAddress - The mint address of the NFT to list
 * @param {PublicKey} sellerAddress - The address of the seller
 * @param {number} price - The price of the NFT in SOL
 */
async function createListing(nftMintAddress, sellerAddress, price) {
  try {
    // Create a new transaction
    const transaction = new Transaction();

    // Create a new listing account
    const listingAccount = PublicKey.unique();

    // Create the listing instruction
    const createListingInstruction = await MarketplaceProgram.createListingInstruction(
      listingAccount,
      nftMintAddress,
      sellerAddress,
      price,
      MARKETPLACE_PROGRAM_ID,
      BONGERS_ORIGIN_NFT_PROGRAM_ID,
    );

    // Add the instruction to the transaction
    transaction.add(createListingInstruction);

    // Sign the transaction
    const signature = await connection.sendTransaction(transaction, [sellerAddress]);

    return signature;
  } catch (error) {
    console.error(error);
    throw error;
  }
}

/**
 * Buy a Bongers Origin NFT from the marketplace
 * @param {PublicKey} listingAccountAddress - The address of the listing account
 * @param {PublicKey} buyerAddress - The address of the buyer
 */
async function buyNFT(listingAccountAddress, buyerAddress) {
  try {
    // Get the listing account data
    const listingAccountData = await MarketplaceProgram.getListingAccountData(listingAccountAddress);

    // Create a new transaction
    const transaction = new Transaction();

    // Create the buy instruction
    const buyInstruction = await MarketplaceProgram.buyInstruction(
      listingAccountAddress,
      listingAccountData.nftMintAddress,
      buyerAddress,
      listingAccountData.sellerAddress,
      listingAccountData.price,
      MARKETPLACE_PROGRAM_ID,
      BONGERS_ORIGIN_NFT_PROGRAM_ID,
      TOKEN_PROGRAM_ID,
    );

    // Add the instruction to the transaction
    transaction.add(buyInstruction);

    // Sign the transaction
    const signature = await connection.sendTransaction(transaction, [buyerAddress]);

    return signature;
  } catch (error) {
    console.error(error);
    throw error;
  }
}

// Example usage:
async function main() {
  try {
    // Create a new listing
    const nftMintAddress = new PublicKey('NFTMintAddress');
    const sellerAddress = new PublicKey('SellerAddress');
    const price = 1.0;
    const listingSignature = await createListing(nftMintAddress, sellerAddress, price);
    console.log(`Listing created: ${listingSignature}`);

    // Buy the NFT
    const listingAccountAddress = new PublicKey('ListingAccountAddress');
    const buyerAddress = new PublicKey('BuyerAddress');
    const buySignature = await buyNFT(listingAccountAddress, buyerAddress);
    console.log(`NFT bought: ${buySignature}`);
  } catch (error) {
    console.error(error);
  }
}

main();
```

**MarketplaceProgram.js**
```javascript
// Marketplace program implementation
const { Program } = require('@solana/anchor');

class MarketplaceProgram {
  constructor(connection) {
    this.connection = connection;
    this.program = new Program(
      'marketplace',
      'MarketplaceProgramId',
      this.connection,
    );
  }

  async createListingInstruction(
    listingAccount,
    nftMintAddress,
    sellerAddress,
    price,
    marketplaceProgramId,
    bongersOriginNFTProgramId,
  ) {
    return this.program.methods
      .createListing(
        {
          nftMintAddress: nftMintAddress,
          sellerAddress: sellerAddress,
          price: price,
        },
      )
      .accounts({
        listingAccount: listingAccount,
        nftMint: nftMintAddress,
        seller: sellerAddress,
        marketplaceProgram: marketplaceProgramId,
        bongersOriginNFTProgram: bongersOriginNFTProgramId,
      })
      .instruction();
  }

  async buyInstruction(
    listingAccountAddress,
    nftMintAddress,
    buyerAddress,
    sellerAddress,
    price,
    marketplaceProgramId,
    bongersOriginNFTProgramId,
    tokenProgramId,
  ) {
    return this.program.methods
      .buy(
        {
          listingAccountAddress: listingAccountAddress,
          nftMintAddress: nftMintAddress,
          buyerAddress: buyerAddress,
          sellerAddress: sellerAddress,
          price: price,
        },
      )
      .accounts({
        listingAccount: listingAccountAddress,
        nftMint: nftMintAddress,
        buyer: buyerAddress,
        seller: sellerAddress,
        marketplaceProgram: marketplaceProgramId,
        bongersOriginNFTProgram: bongersOriginNFTProgramId,
        tokenProgram: tokenProgramId,
      })
      .instruction();
  }

  async getListingAccountData(listingAccountAddress) {
    return this.program.account.listingAccount.fetch(listingAccountAddress);
  }
}

module.exports = MarketplaceProgram;
```
