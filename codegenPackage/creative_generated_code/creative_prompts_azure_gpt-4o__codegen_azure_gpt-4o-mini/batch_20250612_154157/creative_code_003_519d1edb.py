"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://v2-thruster.fi
Prompt: Write code to unlock and manage Thruster LPTs (Liquidity Pool Tokens) for on-chain leverage and collateralization within the Blast ecosystem.
Generated: DETERMINISTIC_519d1edbfb5b31f8
Batch ID: 20250612_154157
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

// Interface for Liquidity Pool Token (LPT) interaction
interface ILPT {
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address from, address to, uint256 amount) external returns (bool);
    function balanceOf(address owner) external view returns (uint256);
}

// Interface for collateral management
interface ICollateralManager {
    function depositCollateral(address token, uint256 amount) external;
    function withdrawCollateral(address token, uint256 amount) external;
}

// Main contract for managing Thruster LPTs
contract ThrusterLPTManager {
    ILPT public lpt; // The Liquidity Pool Token contract
    ICollateralManager public collateralManager; // The collateral manager contract

    // Events for logging
    event LPTApproved(address indexed spender, uint256 amount);
    event LPTTransferred(address indexed from, address indexed to, uint256 amount);
    event CollateralDeposited(address indexed token, uint256 amount);
    event CollateralWithdrawn(address indexed token, uint256 amount);

    // Constructor to set LPT and collateral manager addresses
    constructor(address _lptAddress, address _collateralManagerAddress) {
        require(_lptAddress != address(0), "Invalid LPT address");
        require(_collateralManagerAddress != address(0), "Invalid collateral manager address");
        
        lpt = ILPT(_lptAddress);
        collateralManager = ICollateralManager(_collateralManagerAddress);
    }

    // Function to approve LPT for a spender
    function approveLPT(address spender, uint256 amount) external {
        require(spender != address(0), "Invalid spender address");
        require(amount > 0, "Amount must be greater than zero");

        bool success = lpt.approve(spender, amount);
        require(success, "LPT approval failed");

        emit LPTApproved(spender, amount);
    }

    // Function to transfer LPT from the caller to a recipient
    function transferLPT(address to, uint256 amount) external {
        require(to != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than zero");
        require(lpt.balanceOf(msg.sender) >= amount, "Insufficient balance");

        bool success = lpt.transferFrom(msg.sender, to, amount);
        require(success, "LPT transfer failed");

        emit LPTTransferred(msg.sender, to, amount);
    }

    // Function to deposit collateral for leveraging
    function depositCollateral(address token, uint256 amount) external {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");

        collateralManager.depositCollateral(token, amount);
        emit CollateralDeposited(token, amount);
    }

    // Function to withdraw collateral
    function withdrawCollateral(address token, uint256 amount) external {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");

        collateralManager.withdrawCollateral(token, amount);
        emit CollateralWithdrawn(token, amount);
    }
}
```
