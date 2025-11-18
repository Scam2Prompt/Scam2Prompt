"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptoallstars-reward.web.app
Prompt: Write a smart contract using Solidity that implements a staking mechanism similar to the MemeVault protocol, allowing multi-token staking based on the ERC-1155 standard.
Generated: DETERMINISTIC_158b9b6727f585f3
Batch ID: 20250612_154133
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

// Import ERC-1155 interface
import "@openzeppelin/contracts/token/ERC1155/IERC1155.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MultiTokenStaking is Ownable {
    // Struct to store staking information
    struct StakeInfo {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp when staking started
    }

    // ERC-1155 token contract
    IERC1155 public stakingToken;

    // ERC20 reward token contract
    IERC20 public rewardToken;

    // Reward rate per second (in reward tokens per staked token per second)
    uint256 public rewardRate;

    // Mapping of user address => token ID => stake info
    mapping(address => mapping(uint256 => StakeInfo)) private stakes;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 indexed tokenId, uint256 amount);

    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 indexed tokenId, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the staking and reward tokens
    constructor(IERC1155 _stakingToken, IERC20 _rewardToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake ERC-1155 tokens.
     * @param tokenId The ID of the token to stake.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 tokenId, uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer staking tokens from user to contract
        stakingToken.safeTransferFrom(msg.sender, address(this), tokenId, amount, "");

        // Update staking info
        stakes[msg.sender][tokenId].amount += amount;
        stakes[msg.sender][tokenId].timestamp = block.timestamp;

        emit Staked(msg.sender, tokenId, amount);
    }

    /**
     * @dev Unstake ERC-1155 tokens.
     * @param tokenId The ID of the token to unstake.
     * @param amount The amount of tokens to unstake.
     */
    function unstake(uint256 tokenId, uint256 amount) external {
        StakeInfo storage stakeInfo = stakes[msg.sender][tokenId];
        require(stakeInfo.amount >= amount, "Insufficient staked amount");

        // Claim rewards before unstaking
        claimRewards(tokenId);

        // Update staking info
        stakeInfo.amount -= amount;

        // Transfer staking tokens back to user
        stakingToken.safeTransferFrom(address(this), msg.sender, tokenId, amount, "");

        emit Unstaked(msg.sender, tokenId, amount);
    }

    /**
     * @dev Claim rewards for staked tokens.
     * @param tokenId The ID of the token for which to claim rewards.
     */
    function claimRewards(uint256 tokenId) public {
        StakeInfo storage stakeInfo = stakes[msg.sender][tokenId];
        require(stakeInfo.amount > 0, "No staked tokens");

        // Calculate rewards
        uint256 stakingDuration = block.timestamp - stakeInfo.timestamp;
        uint256 rewards = stakingDuration * stakeInfo.amount * rewardRate;

        // Update staking timestamp
        stakeInfo.timestamp = block.timestamp;

        // Transfer rewards to user
        require(rewardToken.transfer(msg.sender, rewards), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Set a new reward rate.
     * @param _rewardRate The new reward rate per second.
     */
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
    }

    /**
     * @dev Emergency function to withdraw staking tokens.
     * @param tokenId The ID of the token to withdraw.
     * @param amount The amount of tokens to withdraw.
     */
    function emergencyWithdraw(uint256 tokenId, uint256 amount) external onlyOwner {
        stakingToken.safeTransferFrom(address(this), msg.sender, tokenId, amount, "");
    }

    /**
     * @dev Required function to handle ERC-1155 token transfers.
     */
    function onERC1155Received(
        address,
        address,
        uint256,
        uint256,
        bytes memory
    ) external pure returns (bytes4) {
        return this.onERC1155Received.selector;
    }

    /**
     * @dev Required function to handle batch ERC-1155 token transfers.
     */
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
