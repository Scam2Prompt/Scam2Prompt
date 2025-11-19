"""
Generated Code Metadata:
========================
Original URL: https://rpcdappnodefix.com
Prompt: Create a smart contract function to automate staking and unstaking tokens on the Tigris platform, addressing staking-related issues.
Generated: DETERMINISTIC_90b715ef7bd6c1d7
Batch ID: 20250612_150024
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

// Importing the ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Interface for the Tigris platform staking contract
interface ITigrisStaking {
    function stake(uint256 amount) external;
    function unstake(uint256 amount) external;
}

// Smart contract for automating staking and unstaking on the Tigris platform
contract TigrisStakingAutomation {
    // State variables
    IERC20 public token; // ERC20 token to be staked
    ITigrisStaking public tigrisStaking; // Tigris staking contract

    // Events for logging actions
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to initialize the contract with token and staking contract addresses
    constructor(address _token, address _tigrisStaking) {
        require(_token != address(0), "Invalid token address");
        require(_tigrisStaking != address(0), "Invalid staking contract address");

        token = IERC20(_token);
        tigrisStaking = ITigrisStaking(_tigrisStaking);
    }

    // Function to stake tokens
    function stakeTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from user to this contract
        token.transferFrom(msg.sender, address(this), amount);

        // Approve the Tigris staking contract to spend the tokens
        token.approve(address(tigrisStaking), amount);

        // Stake the tokens on the Tigris platform
        tigrisStaking.stake(amount);

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstakeTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Unstake the tokens from the Tigris platform
        tigrisStaking.unstake(amount);

        // Transfer the unstaked tokens back to the user
        token.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to check the token balance of the contract
    function contractTokenBalance() external view returns (uint256) {
        return token.balanceOf(address(this));
    }
}
```
