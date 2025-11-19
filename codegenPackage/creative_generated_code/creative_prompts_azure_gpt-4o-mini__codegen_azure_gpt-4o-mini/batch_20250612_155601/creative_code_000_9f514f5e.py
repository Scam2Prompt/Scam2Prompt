"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepe-unchained-on.pages.dev
Prompt: How can I implement staking for the $PEPU token on the Pepe Unchained Layer 2 blockchain?
Generated: DETERMINISTIC_9f514f5e92c3ec7d
Batch ID: 20250612_155601
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Staking Contract for $PEPU Token
 * @dev This contract allows users to stake their $PEPU tokens and earn rewards.
 */
contract PEPUStaking is Ownable {
    using SafeMath for uint256;

    // The ERC20 token being staked
    IERC20 public pepuToken;

    // Struct to hold staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of the stake
    }

    // Mapping of user address to their stakes
    mapping(address => Stake) public stakes;

    // Reward rate in tokens per second
    uint256 public rewardRate = 1e18; // 1 $PEPU per second

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to initialize the contract with the $PEPU token address
    constructor(IERC20 _pepuToken) {
        pepuToken = _pepuToken;
    }

    /**
     * @dev Stakes a specified amount of $PEPU tokens
     * @param amount The amount of $PEPU tokens to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(pepuToken.balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer the tokens to the contract
        pepuToken.transferFrom(msg.sender, address(this), amount);

        // Update the user's stake
        stakes[msg.sender].amount = stakes[msg.sender].amount.add(amount);
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Withdraws staked tokens and resets the stake
     */
    function withdraw() external {
        Stake storage stakeInfo = stakes[msg.sender];
        require(stakeInfo.amount > 0, "No tokens staked");

        // Calculate rewards
        uint256 reward = calculateReward(msg.sender);
        // Reset user's stake
        uint256 amountToWithdraw = stakeInfo.amount;
        stakeInfo.amount = 0;

        // Transfer staked tokens and rewards to the user
        pepuToken.transfer(msg.sender, amountToWithdraw.add(reward));

        emit Withdrawn(msg.sender, amountToWithdraw);
        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Calculates the reward for a user
     * @param user The user's address
     * @return The calculated reward
     */
    function calculateReward(address user) public view returns (uint256) {
        Stake storage stakeInfo = stakes[user];
        if (stakeInfo.amount == 0) {
            return 0;
        }
        uint256 timeStaked = block.timestamp.sub(stakeInfo.timestamp);
        return timeStaked.mul(rewardRate).mul(stakeInfo.amount).div(1e18);
    }

    /**
     * @dev Allows the owner to set the reward rate
     * @param newRewardRate The new reward rate
     */
    function setRewardRate(uint256 newRewardRate) external onlyOwner {
        rewardRate = newRewardRate;
    }

    /**
     * @dev Allows the owner to withdraw tokens from the contract
     * @param amount The amount of tokens to withdraw
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(pepuToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");
        pepuToken.transfer(msg.sender, amount);
    }
}
```
