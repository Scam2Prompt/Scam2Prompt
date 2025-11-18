"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eigenlayer.com
Prompt: Write a smart contract that utilizes EigenLayer's infrastructure to stake assets and participate in off-chain verification services.
Generated: DETERMINISTIC_083f132fa1fe1029
Batch ID: 20250612_154049
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// Interface for EigenLayer's staking contract
interface IEigenLayerStaking {
    function stake(uint256 amount) external;
    function unstake(uint256 amount) external;
}

// Smart contract for staking assets and participating in off-chain verification
contract EigenLayerStaker is Ownable, ReentrancyGuard {
    IERC20 public asset; // Token being staked
    IEigenLayerStaking public eigenLayer; // Reference to EigenLayer's staking contract

    // Events for tracking deposits and withdrawals
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    // Mapping to track user balances
    mapping(address => uint256) public userBalances;

    // Constructor to initialize the contract with asset and EigenLayer contract addresses
    constructor(IERC20 _asset, IEigenLayerStaking _eigenLayer) {
        asset = _asset;
        eigenLayer = _eigenLayer;
    }

    // Function to stake assets in EigenLayer
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(asset.balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer assets from user to this contract
        asset.transferFrom(msg.sender, address(this), amount);
        userBalances[msg.sender] += amount;

        // Stake the assets in EigenLayer
        eigenLayer.stake(amount);

        emit Staked(msg.sender, amount);
    }

    // Function to unstake assets from EigenLayer
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(userBalances[msg.sender] >= amount, "Insufficient staked amount");

        // Unstake the assets from EigenLayer
        eigenLayer.unstake(amount);
        userBalances[msg.sender] -= amount;

        // Transfer assets back to the user
        asset.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to get the staked balance of a user
    function getStakedBalance(address user) external view returns (uint256) {
        return userBalances[user];
    }

    // Function to withdraw assets (in case of contract failure or emergencies)
    function withdrawAssets(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(asset.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer assets to the owner
        asset.transfer(owner(), amount);
    }
}
```
