"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20-is.pages.dev
Prompt: Design a basic smart contract in Solidity for distributing staking rewards to DOGE20 token holders over a period of two years, similar to the one described in the Dogecoin20 project.
Generated: DETERMINISTIC_e8c9100aa7ba66f2
Batch ID: 20250622_210918
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

// Importing the ERC20 interface for DOGE20 token interaction
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title StakingRewards
 * @dev A smart contract for distributing staking rewards to DOGE20 token holders
 */
contract StakingRewards is Ownable {
    // The DOGE20 token contract
    IERC20 public doge20Token;

    // Total rewards to be distributed
    uint256 public totalRewards;

    // Duration of the reward distribution in seconds (2 years)
    uint256 public distributionDuration = 2 * 365 days;

    // Start time of the distribution
    uint256 public startTime;

    // Mapping to track the amount of rewards for each holder
    mapping(address => uint256) public rewards;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed holder, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the DOGE20 token address and total rewards
     * @param _doge20Token Address of the DOGE20 token contract
     * @param _totalRewards Total rewards to be distributed
     */
    constructor(address _doge20Token, uint256 _totalRewards) {
        require(_doge20Token != address(0), "Invalid token address");
        require(_totalRewards > 0, "Total rewards must be greater than zero");

        doge20Token = IERC20(_doge20Token);
        totalRewards = _totalRewards;
        startTime = block.timestamp;
    }

    /**
     * @dev Function to distribute rewards to DOGE20 token holders
     * @param holder Address of the DOGE20 token holder
     */
    function distributeRewards(address holder) external onlyOwner {
        require(block.timestamp >= startTime, "Distribution has not started yet");
        require(block.timestamp <= startTime + distributionDuration, "Distribution period has ended");
        
        uint256 holderBalance = doge20Token.balanceOf(holder);
        require(holderBalance > 0, "Holder has no DOGE20 tokens");

        // Calculate the reward based on the holder's balance
        uint256 reward = (holderBalance * totalRewards) / doge20Token.totalSupply();
        require(reward > 0, "No rewards to distribute");

        // Transfer the rewards to the holder
        rewards[holder] += reward;
        emit RewardsDistributed(holder, reward);
    }

    /**
     * @dev Function for holders to claim their accumulated rewards
     */
    function claimRewards() external {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        // Reset the rewards for the holder
        rewards[msg.sender] = 0;

        // Transfer the rewards to the holder
        require(doge20Token.transfer(msg.sender, reward), "Transfer failed");
    }

    /**
     * @dev Function to withdraw any remaining tokens after the distribution period
     * @param to Address to withdraw the remaining tokens to
     * @param amount Amount of tokens to withdraw
     */
    function withdrawRemainingTokens(address to, uint256 amount) external onlyOwner {
        require(block.timestamp > startTime + distributionDuration, "Cannot withdraw before distribution ends");
        require(amount <= doge20Token.balanceOf(address(this)), "Insufficient balance");

        require(doge20Token.transfer(to, amount), "Transfer failed");
    }
}
```
