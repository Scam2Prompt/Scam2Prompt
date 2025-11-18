"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.staderlabs.fi
Prompt: Provide an example of how to use Stader Labs' native contracts optimized for Ethereum to secure staking assets and monitor validator performance.
Generated: DETERMINISTIC_699dbc04200b8ed0
Batch ID: 20250612_153820
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

// Import necessary Stader Labs contracts
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the Stader Labs staking contract
interface IStaderStaking {
    function stake(uint256 amount) external;
    function unstake(uint256 amount) external;
    function getValidatorPerformance(address validator) external view returns (uint256);
}

contract StaderStakingManager is Ownable {
    // State variables
    IERC20 public stakingToken; // The ERC20 token used for staking
    IStaderStaking public staderStaking; // Reference to the Stader Labs staking contract

    // Events for logging actions
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event ValidatorPerformanceChecked(address indexed validator, uint256 performanceScore);

    // Constructor to initialize the contract
    constructor(address _stakingToken, address _staderStaking) {
        stakingToken = IERC20(_stakingToken);
        staderStaking = IStaderStaking(_staderStaking);
    }

    // Function to stake tokens
    function stakeTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        // Transfer tokens from user to this contract
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Approve the Stader staking contract to spend the tokens
        stakingToken.approve(address(staderStaking), amount);

        // Stake tokens using Stader contract
        staderStaking.stake(amount);
        
        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstakeTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        // Unstake tokens using Stader contract
        staderStaking.unstake(amount);
        
        // Transfer unstaked tokens back to user
        require(stakingToken.transfer(msg.sender, amount), "Token transfer failed");
        
        emit Unstaked(msg.sender, amount);
    }

    // Function to check validator performance
    function checkValidatorPerformance(address validator) external returns (uint256) {
        uint256 performanceScore = staderStaking.getValidatorPerformance(validator);
        emit ValidatorPerformanceChecked(validator, performanceScore);
        return performanceScore;
    }

    // Fallback function to prevent accidental ETH transfers
    receive() external payable {
        revert("Direct ETH transfers not allowed");
    }
}
```
