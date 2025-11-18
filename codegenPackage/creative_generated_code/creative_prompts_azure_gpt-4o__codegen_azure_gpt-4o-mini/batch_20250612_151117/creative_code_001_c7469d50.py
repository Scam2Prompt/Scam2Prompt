"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://weinerdog.pages.dev
Prompt: Generate Solidity code for a custom smart contract that implements staking functionality similar to WienerAI, including features like high APY rewards and secure token management.
Generated: DETERMINISTIC_c7469d50194acc59
Batch ID: 20250612_151117
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

// Importing the ERC20 interface for token management
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title StakingContract
 * @dev This contract implements a staking mechanism with high APY rewards.
 */
contract StakingContract is ReentrancyGuard, Ownable {
    // Struct to hold information about a user's stake
    struct Stake {
        uint256 amount; // Amount staked
        uint256 timestamp; // Timestamp of when the stake was created
    }

    // Mapping from user address to their stakes
    mapping(address => Stake) public stakes;

    // The token that is staked
    IERC20 public stakingToken;

    // Annual Percentage Yield (APY) expressed as a percentage
    uint256 public apy;

    // Events for logging actions
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);

    /**
     * @dev Constructor to set the staking token and APY.
     * @param _stakingToken Address of the ERC20 token to stake
     * @param _apy Annual Percentage Yield (APY) in percentage
     */
    constructor(IERC20 _stakingToken, uint256 _apy) {
        require(address(_stakingToken) != address(0), "Invalid token address");
        require(_apy > 0, "APY must be greater than zero");

        stakingToken = _stakingToken;
        apy = _apy;
    }

    /**
     * @dev Stake tokens to the contract.
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Stake amount must be greater than zero");

        // Transfer tokens from the user to the contract
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update the user's stake
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens and claim rewards.
     */
    function unstake() external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate the reward based on the APY
        uint256 reward = calculateReward(userStake.amount, userStake.timestamp);
        
        // Reset user's stake amount
        uint256 stakedAmount = userStake.amount;
        userStake.amount = 0;

        // Transfer staked tokens and rewards back to the user
        require(stakingToken.transfer(msg.sender, stakedAmount), "Token transfer failed");
        require(stakingToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit Unstaked(msg.sender, stakedAmount, reward);
    }

    /**
     * @dev Calculate the reward based on the amount staked and the time staked.
     * @param amount Amount staked
     * @param timestamp Time when the stake was created
     * @return reward Amount of reward earned
     */
    function calculateReward(uint256 amount, uint256 timestamp) internal view returns (uint256) {
        uint256 stakingDuration = block.timestamp - timestamp;
        uint256 yearlyReward = (amount * apy) / 100;
        return (yearlyReward * stakingDuration) / 365 days; // Rewards pro-rated to the staking duration
    }

    /**
     * @dev Allows the owner to update the APY.
     * @param newApy New Annual Percentage Yield (APY) in percentage
     */
    function updateApy(uint256 newApy) external onlyOwner {
        require(newApy > 0, "APY must be greater than zero");
        apy = newApy;
    }

    /**
     * @dev Allows the owner to withdraw any ERC20 tokens from the contract.
     * @param token Address of the token to withdraw
     * @param amount Amount of tokens to withdraw
     */
    function withdrawTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(token.balanceOf(address(this)) >= amount, "Insufficient balance");
        require(token.transfer(msg.sender, amount), "Token transfer failed");
    }
}
```
