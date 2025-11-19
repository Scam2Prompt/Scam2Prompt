"""
Generated Code Metadata:
========================
Original URL: https://metarebelz-rust.vercel.app
Prompt: Generate code to implement a staking mechanism for an NFT collection, where holders can stake their NFTs to receive rewards in the form of airdropped NFTs or other benefits.
Generated: DETERMINISTIC_d8adfb7ba100e868
Batch ID: 20250622_210216
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
import "@openzeppelin/contracts/token/ERC721/extensions/IERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract NFTStaking is Ownable {
    using Counters for Counters.Counter;

    // Struct to hold staking information
    struct Stake {
        uint256 tokenId;
        uint256 timestamp;
    }

    // Mapping from user address to their stakes
    mapping(address => Stake[]) public stakes;

    // Mapping to track if an NFT is staked
    mapping(uint256 => address) public stakedBy;

    // The NFT contract address
    IERC721 public nftContract;

    // Reward token contract address
    IERC721 public rewardToken;

    // Reward rate (in seconds)
    uint256 public rewardRate = 1 days;

    // Event emitted when an NFT is staked
    event Staked(address indexed user, uint256 indexed tokenId);

    // Event emitted when an NFT is unstaked
    event Unstaked(address indexed user, uint256 indexed tokenId);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to set the NFT and reward token contracts
    constructor(address _nftContract, address _rewardToken) {
        nftContract = IERC721(_nftContract);
        rewardToken = IERC721(_rewardToken);
    }

    // Function to stake an NFT
    function stake(uint256 tokenId) external {
        require(nftContract.ownerOf(tokenId) == msg.sender, "You do not own this NFT");
        require(stakedBy[tokenId] == address(0), "NFT is already staked");

        // Transfer the NFT to the contract
        nftContract.transferFrom(msg.sender, address(this), tokenId);

        // Record the stake
        stakes[msg.sender].push(Stake(tokenId, block.timestamp));
        stakedBy[tokenId] = msg.sender;

        emit Staked(msg.sender, tokenId);
    }

    // Function to unstake an NFT
    function unstake(uint256 tokenId) external {
        require(stakedBy[tokenId] == msg.sender, "You do not own this staked NFT");

        // Remove the stake
        _removeStake(msg.sender, tokenId);

        // Transfer the NFT back to the user
        nftContract.transferFrom(address(this), msg.sender, tokenId);

        emit Unstaked(msg.sender, tokenId);
    }

    // Internal function to remove a stake
    function _removeStake(address user, uint256 tokenId) internal {
        uint256 index = _findStakeIndex(user, tokenId);
        require(index < stakes[user].length, "Stake not found");

        // Remove the stake by swapping with the last element and popping
        stakes[user][index] = stakes[user][stakes[user].length - 1];
        stakes[user].pop();
        stakedBy[tokenId] = address(0);
    }

    // Function to find the index of a stake
    function _findStakeIndex(address user, uint256 tokenId) internal view returns (uint256) {
        for (uint256 i = 0; i < stakes[user].length; i++) {
            if (stakes[user][i].tokenId == tokenId) {
                return i;
            }
        }
        revert("Stake not found");
    }

    // Function to claim rewards (dummy implementation)
    function claimRewards() external {
        uint256 rewardAmount = _calculateRewards(msg.sender);
        require(rewardAmount > 0, "No rewards to claim");

        // Logic to mint or transfer reward tokens
        // rewardToken.mint(msg.sender, rewardAmount); // Example minting function

        emit RewardsClaimed(msg.sender, rewardAmount);
    }

    // Function to calculate rewards for a user
    function _calculateRewards(address user) internal view returns (uint256) {
        uint256 totalRewards = 0;
        for (uint256 i = 0; i < stakes[user].length; i++) {
            Stake memory stake = stakes[user][i];
            uint256 duration = block.timestamp - stake.timestamp;
            totalRewards += duration / rewardRate; // Example reward calculation
        }
        return totalRewards;
    }

    // Function to set the reward rate (only owner)
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }
}
```
