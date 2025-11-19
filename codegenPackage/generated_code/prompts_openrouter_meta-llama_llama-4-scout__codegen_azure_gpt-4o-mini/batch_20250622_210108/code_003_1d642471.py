"""
Generated Code Metadata:
========================
Original URL: https://defidapp-protocol.web.app
Prompt: "Design a staking system for a Dapp using a synthetic protocol, including NFT staking and a bridge for interoperability, as per the Dapp protocol's features."
Generated: DETERMINISTIC_1d642471815c0d0b
Batch ID: 20250622_210108
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

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for the synthetic protocol
interface ISyntheticProtocol {
    function stake(uint256 amount) external;
    function unstake(uint256 amount) external;
}

// Staking contract for NFTs and ERC20 tokens
contract StakingSystem is Ownable {
    using SafeMath for uint256;

    // Struct to hold staking information
    struct StakeInfo {
        uint256 amount; // Amount staked
        uint256 timestamp; // Timestamp of the stake
    }

    // Mappings to track stakes
    mapping(address => StakeInfo) public stakes; // User stakes
    mapping(address => mapping(uint256 => bool)) public nftStakes; // User NFT stakes

    // ERC20 token used for staking rewards
    IERC20 public rewardToken;
    // NFT contract for staking
    IERC721 public nftContract;

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event NFTStaked(address indexed user, uint256 tokenId);
    event NFTUnstaked(address indexed user, uint256 tokenId);

    // Constructor to initialize the contract
    constructor(IERC20 _rewardToken, IERC721 _nftContract) {
        rewardToken = _rewardToken;
        nftContract = _nftContract;
    }

    // Function to stake ERC20 tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(rewardToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        stakes[msg.sender].amount = stakes[msg.sender].amount.add(amount);
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake ERC20 tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakes[msg.sender].amount >= amount, "Insufficient staked amount");

        stakes[msg.sender].amount = stakes[msg.sender].amount.sub(amount);
        require(rewardToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to stake NFTs
    function stakeNFT(uint256 tokenId) external {
        require(nftContract.ownerOf(tokenId) == msg.sender, "You do not own this NFT");
        nftContract.transferFrom(msg.sender, address(this), tokenId);
        nftStakes[msg.sender][tokenId] = true;

        emit NFTStaked(msg.sender, tokenId);
    }

    // Function to unstake NFTs
    function unstakeNFT(uint256 tokenId) external {
        require(nftStakes[msg.sender][tokenId], "NFT not staked");

        nftStakes[msg.sender][tokenId] = false;
        nftContract.transferFrom(address(this), msg.sender, tokenId);

        emit NFTUnstaked(msg.sender, tokenId);
    }

    // Function to calculate rewards (placeholder for actual reward logic)
    function calculateRewards(address user) public view returns (uint256) {
        // Implement reward calculation logic based on stakes and time
        return stakes[user].amount.mul(10).div(100); // Example: 10% reward
    }

    // Function to withdraw rewards (placeholder for actual reward distribution)
    function withdrawRewards() external {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards available");
        require(rewardToken.transfer(msg.sender, rewards), "Transfer failed");
    }
}
```
