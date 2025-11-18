"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wienerdog-addtoken.pages.dev
Prompt: Write a smart contract in Solidity that implements a staking mechanism similar to WienerAI, allowing users to stake tokens and earn rewards with a customizable APY.
Generated: DETERMINISTIC_ec768044faf91c6a
Batch ID: 20250612_151255
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

/**
 * @title StakingContract
 * @dev A smart contract for staking tokens and earning rewards
 */
contract StakingContract is Ownable {
    // Struct to hold information about each staker
    struct Staker {
        uint256 amountStaked;
        uint256 rewardDebt;
        uint256 lastUpdate;
    }

    // Mapping of staker addresses to their staking details
    mapping(address => Staker) public stakers;

    // The token being staked
    IERC20 public stakedToken;

    // Annual Percentage Yield (APY) in basis points (100 basis points = 1%)
    uint256 public apy;

    // Total staked amount in the contract
    uint256 public totalStaked;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens and claims rewards
    event Unstaked(address indexed user, uint256 amount, uint256 reward);

    // Event emitted when the APY is updated
    event APYUpdated(uint256 newAPY);

    /**
     * @dev Constructor to initialize the staking contract
     * @param _stakedToken Address of the token to be staked
     * @param _apy Initial APY for staking rewards
     */
    constructor(IERC20 _stakedToken, uint256 _apy) {
        stakedToken = _stakedToken;
        apy = _apy;
    }

    /**
     * @dev Stake tokens to the contract
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakedToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Calculate pending rewards before updating the staker's info
        _updateRewards(msg.sender);

        // Update staker's info
        stakers[msg.sender].amountStaked += amount;
        totalStaked += amount;
        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens and claim rewards
     * @param amount Amount of tokens to unstake
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakers[msg.sender].amountStaked >= amount, "Insufficient staked amount");

        // Calculate pending rewards before updating the staker's info
        _updateRewards(msg.sender);

        // Update staker's info
        stakers[msg.sender].amountStaked -= amount;
        totalStaked -= amount;

        // Transfer the staked tokens back to the user
        require(stakedToken.transfer(msg.sender, amount), "Transfer failed");

        // Transfer the rewards to the user
        uint256 reward = stakers[msg.sender].rewardDebt;
        if (reward > 0) {
            // Reset reward debt after claiming
            stakers[msg.sender].rewardDebt = 0;
            payable(msg.sender).transfer(reward);
        }

        emit Unstaked(msg.sender, amount, reward);
    }

    /**
     * @dev Update the APY for staking rewards
     * @param newAPY New APY value in basis points
     */
    function updateAPY(uint256 newAPY) external onlyOwner {
        apy = newAPY;
        emit APYUpdated(newAPY);
    }

    /**
     * @dev Internal function to update rewards for a staker
     * @param account Address of the staker
     */
    function _updateRewards(address account) internal {
        // Calculate accrued rewards
        uint256 stakedAmount = stakers[account].amountStaked;
        uint256 timeStaked = block.timestamp - stakers[account].lastUpdate;
        
        // Calculate rewards based on the APY
        if (stakedAmount > 0) {
            uint256 reward = (stakedAmount * apy * timeStaked) / (365 days * 10000);
            stakers[account].rewardDebt += reward;
        }

        // Update last update timestamp
        stakers[account].lastUpdate = block.timestamp;
    }

    /**
     * @dev Fallback function to accept Ether for rewards distribution
     */
    receive() external payable {}
}
```
