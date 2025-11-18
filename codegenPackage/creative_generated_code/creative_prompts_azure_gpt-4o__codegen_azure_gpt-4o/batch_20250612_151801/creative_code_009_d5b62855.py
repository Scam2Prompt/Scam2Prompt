"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digitoadworld.pages.dev
Prompt: Generate code to implement the "play-to-earn" feature of DigiToads, allowing users to collect, nurture, and battle Toad NFTs in a web3 game environment.
Generated: DETERMINISTIC_d5b62855bd70bb81
Batch ID: 20250612_151801
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules
const { ethers } = require("ethers");
const { abi, bytecode } = require("./ToadNFTContract");

// Environment variables/credentials (Ensure these are securely stored)
const provider = new ethers.providers.JsonRpcProvider(process.env.RPC_URL); // RPC URL to connect to blockchain
const wallet = new ethers.Wallet(process.env.PRIVATE_KEY, provider); // Wallet for signing transactions

// Configure the contract
const toadNFTAddress = process.env.TOAD_NFT_CONTRACT_ADDRESS;
const toadNFTContract = new ethers.Contract(toadNFTAddress, abi, wallet);

/**
 * Play-to-Earn Feature Implementation
 * Includes functions for collecting, nurturing, and battling Toad NFTs.
 */
class DigiToadsGame {
  constructor(contract) {
    this.contract = contract; // ToadNFT contract instance
  }

  /**
   * Collect a new Toad NFT
   * @param {string} playerAddress - Address of the player collecting the NFT
   * @returns {Promise<string>} - Returns transaction hash upon successful minting
   */
  async collectToad(playerAddress) {
    try {
      const tx = await this.contract.mintToad(playerAddress);
      await tx.wait(); // Wait for transaction to be mined
      return tx.hash; // Return transaction hash
    } catch (error) {
      console.error("Error in collectToad:", error);
      throw new Error("Failed to collect Toad NFT.");
    }
  }

  /**
   * Nurture a Toad NFT
   * @param {number} toadId - ID of the Toad NFT to nurture
   * @param {number} amount - Amount of tokens to spend on nurturing
   * @returns {Promise<string>} - Returns transaction hash upon successful nurturing
   */
  async nurtureToad(toadId, amount) {
    try {
      const tx = await this.contract.nurtureToad(toadId, amount);
      await tx.wait(); // Wait for transaction to be mined
      return tx.hash; // Return transaction hash
    } catch (error) {
      console.error("Error in nurtureToad:", error);
      throw new Error("Failed to nurture Toad NFT.");
    }
  }

  /**
   * Battle with a Toad NFT
   * @param {number} playerToadId - ID of the player's Toad NFT
   * @param {number} opponentToadId - ID of the opponent's Toad NFT
   * @returns {Promise<object>} - Returns battle result (winner and rewards)
   */
  async battleToads(playerToadId, opponentToadId) {
    try {
      const tx = await this.contract.battleToads(playerToadId, opponentToadId);
      await tx.wait(); // Wait for transaction to be mined
      const receipt = await provider.getTransactionReceipt(tx.hash);
      const event = this.parseBattleResultEvent(receipt); // Parse battle result event
      return event; // Return battle result
    } catch (error) {
      console.error("Error in battleToads:", error);
      throw new Error("Failed to battle Toad NFTs.");
    }
  }

  /**
   * Parse Battle Result Event from Transaction Receipt
   * @param {object} receipt - Transaction receipt
   * @returns {object} - Parsed event data (winner and rewards)
   */
  parseBattleResultEvent(receipt) {
    const battleResultEvent = receipt.logs.find(
      (log) => log.topics[0] === ethers.utils.id("BattleResult(address,uint256,uint256)") // Event signature
    );
    const decodedEvent = ethers.utils.defaultAbiCoder.decode(
      ["address", "uint256", "uint256"],
      battleResultEvent.data
    );
    return {
      winner: decodedEvent[0],
      winnerToadId: decodedEvent[1],
      reward: decodedEvent[2],
    };
  }
}

// Instantiate the game
const digiToadsGame = new DigiToadsGame(toadNFTContract);

// Export for external use
module.exports = { digiToadsGame };
```

### Notes to Developers:
- Ensure the environment variables `RPC_URL`, `PRIVATE_KEY`, and `TOAD_NFT_CONTRACT_ADDRESS` are set appropriately.
- The `ToadNFTContract` ABI and bytecode are placeholders and should correspond to the actual deployed contract.
- Additional security measures, such as rate limiting or input validation, can be implemented depending on the use case.
