"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptoallstars-launch.firebaseapp.com
Prompt: Write a smart contract in Solidity that implements a multi-token staking mechanism similar to the MemeVault protocol described on the Crypto All-Stars website, using the ERC-1155 standard.
Generated: DETERMINISTIC_7231eed3616ab2b6
Batch ID: 20250612_153722
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

import "@openzeppelin/contracts/token/ERC1155/IERC1155.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MultiTokenStaking is ReentrancyGuard, Ownable {
    // Struct to represent staking information
    struct StakeInfo {
        uint256 tokenId; // ID of the token staked
        uint256 amount; // Amount of the token staked
        uint256 timestamp; // Time when the staking started
    }

    // Mapping of staker address to their stake information
    mapping(address => StakeInfo[]) public stakes;

    // ERC-1155 token contract
    IERC1155 public tokenContract;

    // Reward rate (tokens per second). Can be adjusted by the owner
    uint256 public rewardRate;

    // Events for staking and withdrawing
    event Staked(address indexed user, uint256 indexed tokenId, uint256 amount);
    event Withdrawn(address indexed user, uint256 indexed tokenId, uint256 amount, uint256 reward);

    constructor(IERC1155 _tokenContract, uint256 _rewardRate) {
        require(address(_tokenContract) != address(0), "Invalid token contract address");
        tokenContract = _tokenContract;
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 tokenId, uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot stake zero tokens");

        // Transfer the tokens to this contract for staking
        tokenContract.safeTransferFrom(msg.sender, address(this), tokenId, amount, "");

        // Add a new stake entry
        stakes[msg.sender].push(StakeInfo({
            tokenId: tokenId,
            amount: amount,
            timestamp: block.timestamp
        }));

        emit Staked(msg.sender, tokenId, amount);
    }

    // Function to withdraw staked tokens along with rewards
    function withdraw(uint256 index) external nonReentrant {
        require(index < stakes[msg.sender].length, "Invalid stake index");

        // Retrieve stake information
        StakeInfo memory stakeInfo = stakes[msg.sender][index];

        // Calculate rewards based on the time staked
        uint256 stakingDuration = block.timestamp - stakeInfo.timestamp;
        uint256 reward = stakingDuration * rewardRate * stakeInfo.amount;

        // Remove the stake from the array
        removeStake(msg.sender, index);

        // Transfer the staked tokens back to the user
        tokenContract.safeTransferFrom(address(this), msg.sender, stakeInfo.tokenId, stakeInfo.amount, "");

        // Send rewards (can be in native token or another reward mechanism)
        // NOTE: A reward token mechanism would be required to implement this fully.
        // For simplicity, rewards could be distributed through an external mechanism.

        emit Withdrawn(msg.sender, stakeInfo.tokenId, stakeInfo.amount, reward);
    }

    // Function to remove a stake by index
    function removeStake(address user, uint256 index) internal {
        require(index < stakes[user].length, "Invalid stake index");

        // Swap and pop to remove the stake efficiently
        stakes[user][index] = stakes[user][stakes[user].length - 1];
        stakes[user].pop();
    }

    // Function to update reward rate (only owner can call this)
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
    }

    // Fallback function to handle ERC-1155 safeTransferFrom
    function onERC1155Received(
        address,
        address,
        uint256,
        uint256,
        bytes memory
    ) external pure returns (bytes4) {
        return this.onERC1155Received.selector;
    }

    // Batch fallback function for ERC-1155
    function onERC1155BatchReceived(
        address,
        address,
        uint256[] memory,
        uint256[] memory,
        bytes memory
    ) external pure returns (bytes4) {
        return this.onERC1155BatchReceived.selector;
    }
}
```
