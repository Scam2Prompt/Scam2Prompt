"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tonlucky.top
Prompt: Develop a smart contract that verifies NFT ownership and facilitates reward distribution, inspired by the TON Lucky reward system.
Generated: DETERMINISTIC_6e8eb20550cbc822
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

/**
 * @title NFT Reward Distribution Contract
 * @dev This contract verifies NFT ownership and facilitates reward distribution.
 * Inspired by the TON Lucky reward system.
 */
contract NFTRewardDistributor {
    // Interface to interact with ERC721 contracts (NFTs)
    interface IERC721 {
        function ownerOf(uint256 tokenId) external view returns (address);
    }

    // Address of the ERC721 (NFT) contract
    address public nftContractAddress;

    // Owner of the contract
    address public owner;

    // Mapping to track distributed rewards per tokenId
    mapping(uint256 => bool) public rewardsClaimed;

    // Event emitted when rewards are distributed
    event RewardDistributed(address indexed recipient, uint256 tokenId, uint256 amount);

    // Constructor to set the NFT contract and contract owner
    constructor(address _nftContractAddress) {
        require(_nftContractAddress != address(0), "Invalid NFT contract address");
        nftContractAddress = _nftContractAddress;
        owner = msg.sender;
    }

    // Modifier to restrict certain functions to only the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Function to distribute rewards to NFT owners
    function distributeReward(uint256 tokenId, uint256 rewardAmount) external payable onlyOwner {
        require(rewardAmount > 0, "Reward amount must be greater than zero");
        require(msg.value >= rewardAmount, "Insufficient funds sent");

        // Get the owner of the specified NFT tokenId
        address nftOwner = IERC721(nftContractAddress).ownerOf(tokenId);
        require(nftOwner != address(0), "Invalid NFT owner");

        // Ensure the reward for this tokenId has not been claimed before
        require(!rewardsClaimed[tokenId], "Reward already claimed for this tokenId");

        // Mark the reward as claimed
        rewardsClaimed[tokenId] = true;

        // Transfer the reward amount to the NFT owner
        (bool success, ) = nftOwner.call{value: rewardAmount}("");
        require(success, "Reward transfer failed");

        // Emit an event for successful reward distribution
        emit RewardDistributed(nftOwner, tokenId, rewardAmount);
    }

    // Function to withdraw remaining funds from the contract (owner only)
    function withdrawFunds() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No funds to withdraw");

        (bool success, ) = owner.call{value: contractBalance}("");
        require(success, "Withdrawal failed");
    }

    // Function to update the NFT contract address (owner only)
    function updateNFTContractAddress(address _nftContractAddress) external onlyOwner {
        require(_nftContractAddress != address(0), "Invalid NFT contract address");
        nftContractAddress = _nftContractAddress;
    }

    // Fallback function to accept Ether
    receive() external payable {}
}
```
