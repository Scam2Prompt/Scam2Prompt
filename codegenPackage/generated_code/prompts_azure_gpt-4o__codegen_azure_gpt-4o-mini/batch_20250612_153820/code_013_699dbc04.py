"""
Generated Code Metadata:
========================
Original URL: https://www.staderlabs.fi
Prompt: Provide an example of how to use Stader Labs' native contracts optimized for Ethereum to secure staking assets and monitor validator performance.
Generated: DETERMINISTIC_699dbc04200b8ed0
Batch ID: 20250612_153820
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for Stader Labs' staking contract
interface IStaderStaking {
    function stake(uint256 amount) external;
    function unstake(uint256 amount) external;
    function getValidatorPerformance(address validator) external view returns (uint256);
}

// Staking contract to interact with Stader Labs' native contracts
contract StaderStakingManager is Ownable {
    // State variables
    IERC20 public stakingToken; // The ERC20 token used for staking
    IStaderStaking public staderStaking; // Instance of Stader's staking contract

    // Events for logging actions
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event ValidatorPerformanceChecked(address indexed validator, uint256 performance);

    // Constructor to initialize the contract with the staking token and Stader staking contract
    constructor(address _stakingToken, address _staderStaking) {
        require(_stakingToken != address(0), "Invalid staking token address");
        require(_staderStaking != address(0), "Invalid Stader staking contract address");

        stakingToken = IERC20(_stakingToken);
        staderStaking = IStaderStaking(_staderStaking);
    }

    // Function to stake tokens in Stader's staking contract
    function stakeTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakingToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from user to this contract
        stakingToken.transferFrom(msg.sender, address(this), amount);
        // Approve the Stader staking contract to spend the tokens
        stakingToken.approve(address(staderStaking), amount);
        // Stake the tokens in Stader's contract
        staderStaking.stake(amount);

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens from Stader's staking contract
    function unstakeTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Unstake the tokens from Stader's contract
        staderStaking.unstake(amount);
        // Transfer the unstaked tokens back to the user
        stakingToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to check the performance of a validator
    function checkValidatorPerformance(address validator) external returns (uint256) {
        require(validator != address(0), "Invalid validator address");

        // Get the performance of the specified validator
        uint256 performance = staderStaking.getValidatorPerformance(validator);
        
        emit ValidatorPerformanceChecked(validator, performance);
        return performance;
    }

    // Function to withdraw tokens in case of emergency
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(stakingToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer tokens back to the owner
        stakingToken.transfer(msg.sender, amount);
    }
}
```
