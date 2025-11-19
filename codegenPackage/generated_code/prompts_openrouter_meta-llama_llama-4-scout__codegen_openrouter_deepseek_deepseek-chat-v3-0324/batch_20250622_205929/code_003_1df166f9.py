"""
Generated Code Metadata:
========================
Original URL: https://wemix-shoebill.pages.dev
Prompt: Explain how Shoebill Finance's staking rewards cumulated to stWEMIX are returned to depositors, including the role of the stWEMIX exchange rate.
Generated: DETERMINISTIC_1df166f9e496f068
Batch ID: 20250622_205929
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title Shoebill Finance Staking Contract
 * @notice Handles staking of WEMIX tokens and distribution of rewards via stWEMIX
 */
contract ShoebillStaking is Ownable {
    using SafeERC20 for IERC20;

    IERC20 public immutable wemixToken;
    IERC20 public immutable stWemixToken;

    // Total WEMIX staked in the contract
    uint256 public totalStaked;
    
    // Exchange rate between stWEMIX and WEMIX (scaled by 1e18)
    uint256 public exchangeRate = 1e18;

    // Total rewards accumulated but not yet distributed
    uint256 public totalRewards;

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsDistributed(uint256 amount);
    event ExchangeRateUpdated(uint256 newRate);

    /**
     * @param _wemixToken Address of WEMIX token contract
     * @param _stWemixToken Address of stWEMIX token contract
     */
    constructor(address _wemixToken, address _stWemixToken) {
        require(_wemixToken != address(0), "Invalid WEMIX address");
        require(_stWemixToken != address(0), "Invalid stWEMIX address");
        wemixToken = IERC20(_wemixToken);
        stWemixToken = IERC20(_stWemixToken);
    }

    /**
     * @notice Stake WEMIX tokens to receive stWEMIX
     * @param amount Amount of WEMIX to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        
        // Transfer WEMIX from user to contract
        wemixToken.safeTransferFrom(msg.sender, address(this), amount);
        
        // Calculate stWEMIX amount based on current exchange rate
        uint256 stWemixAmount = (amount * 1e18) / exchangeRate;
        
        // Update total staked
        totalStaked += amount;
        
        // Mint stWEMIX to user
        stWemixToken.safeTransfer(msg.sender, stWemixAmount);
        
        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Unstake stWEMIX tokens to receive WEMIX
     * @param stWemixAmount Amount of stWEMIX to unstake
     */
    function unstake(uint256 stWemixAmount) external {
        require(stWemixAmount > 0, "Amount must be greater than 0");
        
        // Calculate WEMIX amount based on current exchange rate
        uint256 wemixAmount = (stWemixAmount * exchangeRate) / 1e18;
        require(wemixAmount <= totalStaked, "Insufficient staked balance");
        
        // Burn stWEMIX from user
        stWemixToken.safeTransferFrom(msg.sender, address(this), stWemixAmount);
        
        // Update total staked
        totalStaked -= wemixAmount;
        
        // Transfer WEMIX to user
        wemixToken.safeTransfer(msg.sender, wemixAmount);
        
        emit Unstaked(msg.sender, wemixAmount);
    }

    /**
     * @notice Distribute new rewards to stakers by updating exchange rate
     * @param rewardAmount Amount of WEMIX rewards to distribute
     */
    function distributeRewards(uint256 rewardAmount) external onlyOwner {
        require(rewardAmount > 0, "Reward must be greater than 0");
        
        // Transfer rewards from owner to contract
        wemixToken.safeTransferFrom(msg.sender, address(this), rewardAmount);
        
        // Update total rewards
        totalRewards += rewardAmount;
        
        // Calculate new exchange rate
        if (totalStaked > 0) {
            exchangeRate = ((totalStaked + totalRewards) * 1e18) / totalStaked;
        }
        
        emit RewardsDistributed(rewardAmount);
        emit ExchangeRateUpdated(exchangeRate);
    }

    /**
     * @notice Get the current WEMIX value of stWEMIX holdings
     * @param stWemixAmount Amount of stWEMIX
     * @return Equivalent WEMIX amount
     */
    function getWemixValue(uint256 stWemixAmount) external view returns (uint256) {
        return (stWemixAmount * exchangeRate) / 1e18;
    }
}
```
