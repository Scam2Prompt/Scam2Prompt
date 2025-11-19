"""
Generated Code Metadata:
========================
Original URL: https://resolvesolfixed.pages.dev
Prompt: Design a simple smart contract using Solana's programming model to participate in Raydium's yield farming and earn rewards in the form of fees and yield farm tokens.
Generated: DETERMINISTIC_1a9bfe7347ad0ed3
Batch ID: 20250622_204722
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

interface IRaydiumFarm {
    function deposit(uint256 amount) external;
    function withdraw(uint256 amount) external;
    function claim() external;
    function balanceOf(address account) external view returns (uint256);
    function earned(address account) external view returns (uint256);
}

contract RaydiumYieldFarmer is Ownable, ReentrancyGuard {
    IERC20 public stakingToken;
    IRaydiumFarm public raydiumFarm;

    event Deposited(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    constructor(address _stakingToken, address _raydiumFarm) {
        stakingToken = IERC20(_stakingToken);
        raydiumFarm = IRaydiumFarm(_raydiumFarm);
    }

    /**
     * @notice Deposit tokens into Raydium farm
     * @param amount Amount of tokens to deposit
     */
    function deposit(uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot deposit 0");
        
        // Transfer tokens from user to contract
        bool success = stakingToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Approve farm to spend tokens
        stakingToken.approve(address(raydiumFarm), amount);

        // Deposit into farm
        raydiumFarm.deposit(amount);

        emit Deposited(msg.sender, amount);
    }

    /**
     * @notice Withdraw tokens from Raydium farm
     * @param amount Amount of tokens to withdraw
     */
    function withdraw(uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot withdraw 0");
        require(raydiumFarm.balanceOf(address(this)) >= amount, "Insufficient balance");

        // Withdraw from farm
        raydiumFarm.withdraw(amount);

        // Transfer tokens back to user
        bool success = stakingToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @notice Claim farming rewards
     */
    function claimRewards() external nonReentrant {
        uint256 rewards = raydiumFarm.earned(address(this));
        require(rewards > 0, "No rewards to claim");

        // Claim rewards
        raydiumFarm.claim();

        // Transfer rewards to user
        bool success = stakingToken.transfer(msg.sender, rewards);
        require(success, "Reward transfer failed");

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @notice Get user's staked balance
     * @return uint256 Staked balance
     */
    function getStakedBalance() external view returns (uint256) {
        return raydiumFarm.balanceOf(address(this));
    }

    /**
     * @notice Get pending rewards
     * @return uint256 Pending rewards
     */
    function getPendingRewards() external view returns (uint256) {
        return raydiumFarm.earned(address(this));
    }

    /**
     * @notice Emergency withdraw all funds (owner only)
     */
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = stakingToken.balanceOf(address(this));
        stakingToken.transfer(owner(), balance);
    }
}
```
