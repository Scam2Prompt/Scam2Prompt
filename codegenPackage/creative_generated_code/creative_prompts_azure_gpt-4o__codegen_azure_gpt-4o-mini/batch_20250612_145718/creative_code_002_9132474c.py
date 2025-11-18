"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tonbox.top
Prompt: Develop a smart contract or script that handles reward claiming for NFT owners, ensuring the transaction is confirmed in the user's wallet, as specified by TON Lucky.
Generated: DETERMINISTIC_9132474c6af71d6a
Batch ID: 20250612_145718
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

// Importing OpenZeppelin's ERC721 implementation and Ownable for access control
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Main contract for handling reward claiming for NFT owners
contract NFTRewardManager is ERC721Enumerable, Ownable {
    // Mapping from NFT token ID to the rewards balance
    mapping(uint256 => uint256) private _rewards;

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed owner, uint256 indexed tokenId, uint256 amount);

    // Constructor to initialize the contract with a name and symbol for the NFT
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    // Function to mint an NFT and assign rewards
    function mint(address to, uint256 tokenId) external onlyOwner {
        _mint(to, tokenId);
        _rewards[tokenId] = 100; // Initial reward assigned to the new NFT
    }

    // Function to check rewards for a specific token ID
    function checkRewards(uint256 tokenId) external view returns (uint256) {
        return _rewards[tokenId];
    }

    // Function to claim rewards for a specific token ID
    function claimRewards(uint256 tokenId) external {
        // Ensure the caller owns the token and the token exists
        require(ownerOf(tokenId) == msg.sender, "You do not own this NFT");
        require(_rewards[tokenId] > 0, "No rewards available to claim");

        uint256 rewardsToClaim = _rewards[tokenId];
        _rewards[tokenId] = 0; // Reset rewards for the token

        // Transfer rewards to the caller (dummy implementation, replace with actual token transfer logic)
        (bool success, ) = msg.sender.call{ value: rewardsToClaim }("");
        require(success, "Reward transfer failed");

        emit RewardsClaimed(msg.sender, tokenId, rewardsToClaim);
    }

    // Function to withdraw any Ether that might be trapped in the contract
    function withdraw(uint256 amount) external onlyOwner {
        require(address(this).balance >= amount, "Insufficient balance");
        (bool success, ) = msg.sender.call{ value: amount }("");
        require(success, "Withdraw failed");
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
