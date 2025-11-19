"""
Generated Code Metadata:
========================
Original URL: https://createra-genesis-land.netlify.app
Prompt: Write a smart contract function to track the minting progress of Createra Genesis Land NFTs, considering a total supply of 777 and current minted count of 589.
Generated: DETERMINISTIC_7f63831a358766f9
Batch ID: 20250622_212859
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title CreateraGenesisLandNFT
 * @dev Smart contract to track the minting progress of Createra Genesis Land NFTs.
 */
contract CreateraGenesisLandNFT {
    // Total supply of NFTs
    uint256 public constant TOTAL_SUPPLY = 777;

    // Current minted count
    uint256 public mintedCount = 589;

    // Event to emit when minting progress is updated
    event MintingProgressUpdated(uint256 mintedCount, uint256 remainingSupply);

    /**
     * @dev Function to get the current minting progress.
     * @return minted The number of NFTs minted so far.
     * @return remaining The number of NFTs remaining to be minted.
     */
    function getMintingProgress() external view returns (uint256 minted, uint256 remaining) {
        minted = mintedCount;
        remaining = TOTAL_SUPPLY - mintedCount;
    }

    /**
     * @dev Function to update the minted count. Can only be called by the contract owner.
     * @param newMintedCount The new minted count to update.
     */
    function updateMintedCount(uint256 newMintedCount) external onlyOwner {
        require(newMintedCount <= TOTAL_SUPPLY, "Minted count exceeds total supply");
        require(newMintedCount >= mintedCount, "Minted count cannot decrease");

        mintedCount = newMintedCount;

        // Emit an event to notify about the updated minting progress
        emit MintingProgressUpdated(mintedCount, TOTAL_SUPPLY - mintedCount);
    }

    /**
     * @dev Modifier to restrict access to the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Address of the contract owner
    address public owner;

    /**
     * @dev Constructor to set the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }
}
```
