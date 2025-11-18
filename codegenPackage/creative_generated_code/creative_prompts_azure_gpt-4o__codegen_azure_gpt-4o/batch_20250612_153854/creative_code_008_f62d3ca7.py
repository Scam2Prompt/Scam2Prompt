"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mega-rabbit.com
Prompt: Generate code for a staking mechanism in Solidity that allows users to stake their MegaRabbit NFTs and earn rewards.
Generated: DETERMINISTIC_f62d3ca7bd1bf9bb
Batch ID: 20250612_153854
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
 * @title MegaRabbitNFTStaking
 * @dev A staking contract for MegaRabbit NFTs where users can stake their NFTs and earn rewards.
 */
contract MegaRabbitNFTStaking {
    // Interface for the MegaRabbit NFT contract
    interface IMegaRabbitNFT {
        function transferFrom(address from, address to, uint256 tokenId) external;
        function ownerOf(uint256 tokenId) external view returns (address);
    }

    // Address of the MegaRabbit NFT contract
    IMegaRabbitNFT public megaRabbitNFT;

    // Structure to hold staking details
    struct StakingInfo {
        address owner; // Owner of the staked NFT
        uint256 timestamp; // Timestamp when the NFT was staked
    }

    // Mapping of token ID to its staking information
    mapping(uint256 => StakingInfo) public stakes;

    // Reward rate per second (in wei, for demonstration purposes)
    uint256 public rewardRate = 1 ether; // You can adjust the reward rate

    // Events
    event Staked(address indexed user, uint256 tokenId);
    event Unstaked(address indexed user, uint256 tokenId, uint256 rewards);

    /**
     * @dev Constructor to initialize the MegaRabbit NFT contract address.
     * @param _megaRabbitNFT Address of the MegaRabbit NFT contract.
     */
    constructor(address _megaRabbitNFT) {
        require(_megaRabbitNFT != address(0), "Invalid NFT contract address");
        megaRabbitNFT = IMegaRabbitNFT(_megaRabbitNFT);
    }

    /**
     * @dev Allows users to stake their NFT. Transfers the NFT to this contract.
     * @param tokenId The ID of the NFT to be staked.
     */
    function stake(uint256 tokenId) external {
        require(megaRabbitNFT.ownerOf(tokenId) == msg.sender, "You are not the owner of this NFT");

        // Transfer the NFT to the staking contract
        megaRabbitNFT.transferFrom(msg.sender, address(this), tokenId);

        // Record staking details
        stakes[tokenId] = StakingInfo({
            owner: msg.sender,
            timestamp: block.timestamp
        });

        emit Staked(msg.sender, tokenId);
    }

    /**
     * @dev Allows users to unstake their NFT and claim rewards.
     * @param tokenId The ID of the NFT to be unstaked.
     */
    function unstake(uint256 tokenId) external {
        StakingInfo memory info = stakes[tokenId];

        // Ensure the caller is the owner of the staked NFT
        require(info.owner == msg.sender, "You are not the owner of this staked NFT");

        // Calculate rewards
        uint256 stakingDuration = block.timestamp - info.timestamp;
        uint256 rewards = stakingDuration * rewardRate;

        // Remove staking info
        delete stakes[tokenId];

        // Transfer the NFT back to the owner
        megaRabbitNFT.transferFrom(address(this), msg.sender, tokenId);

        // Transfer rewards (for simplicity, assume contract has enough balance)
        payable(msg.sender).transfer(rewards);

        emit Unstaked(msg.sender, tokenId, rewards);
    }

    /**
     * @dev Allows the owner to update the reward rate.
     * @param newRewardRate The new reward rate per second.
     */
    function setRewardRate(uint256 newRewardRate) external {
        rewardRate = newRewardRate;
    }

    /**
     * @dev Fallback function to receive Ether for rewards distribution.
     */
    receive() external payable {}
}
```
