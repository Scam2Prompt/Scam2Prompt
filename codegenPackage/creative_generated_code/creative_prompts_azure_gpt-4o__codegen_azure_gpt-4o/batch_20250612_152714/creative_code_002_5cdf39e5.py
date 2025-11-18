"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://move-e87.pages.dev
Prompt: Generate a smart contract in Solidity that allows users to claim tokens or NFTs after verifying their wallet address, similar to the MoveDrop Claim process.
Generated: DETERMINISTIC_5cdf39e54ddf374c
Batch ID: 20250612_152714
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title Token/NFT Claim Smart Contract
 * @author [Your Name]
 * @notice This smart contract allows users to claim tokens or NFTs after verifying their wallet address.
 * @dev Follows best practices and includes proper error handling.
 */
contract ClaimContract {
    // Owner of the contract
    address public owner;

    // Mapping to track if a wallet address has already claimed
    mapping(address => bool) public hasClaimed;

    // Event emitted when a claim is successful
    event Claimed(address indexed user, uint256 timestamp);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action");
        _;
    }

    /**
     * @dev Constructor to initialize the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @notice Allows users to claim tokens or NFTs.
     * @dev Verifies the wallet address and ensures the claim can only occur once.
     */
    function claim() external {
        // Ensure the user has not already claimed
        require(!hasClaimed[msg.sender], "Address has already claimed");

        // Mark the address as claimed
        hasClaimed[msg.sender] = true;

        // Emit the event for successful claim
        emit Claimed(msg.sender, block.timestamp);

        // Here you would include the logic to transfer tokens or NFTs to the user
        // Example: ERC20 token transfer or ERC721 mint logic
        // tokenContract.transfer(msg.sender, amount); OR nftContract.mint(msg.sender);
    }

    /**
     * @notice Resets the claim status for a given address (owner-only).
     * @dev This function is useful in case of errors or debugging.
     * @param user The address to reset claim status for.
     */
    function resetClaimStatus(address user) external onlyOwner {
        require(hasClaimed[user], "Address has not claimed yet");
        hasClaimed[user] = false;
    }

    /**
     * @notice Withdraws any ETH sent to the contract (owner-only).
     * @dev This is used to recover funds accidentally sent to the contract.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner).transfer(balance);
    }

    /**
     * @notice Transfers ownership of the contract to a new owner.
     * @dev Only the current owner can transfer ownership.
     * @param newOwner The address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner address cannot be zero");
        owner = newOwner;
    }

    // Fallback function to receive ETH
    receive() external payable {
        // Accept ETH deposits (optional functionality)
    }
}
```
