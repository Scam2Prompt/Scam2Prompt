"""
Generated Code Metadata:
========================
Original URL: https://renz.pages.dev
Prompt: Explain how to integrate Renzo's Liquid Restaking Token (LRT) with a smart contract to secure Actively Validated Services (AVSs) on EigenLayer.
Generated: DETERMINISTIC_c24b3072e3d949c7
Batch ID: 20250622_210027
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

// Importing the ERC20 interface for interacting with the LRT token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Interface for the EigenLayer's AVS contract
interface IAVS {
    function stake(uint256 amount) external;
    function unstake(uint256 amount) external;
}

// Main contract for integrating Renzo's Liquid Restaking Token (LRT)
contract LRTIntegration {
    // State variables
    IERC20 public lrtToken; // LRT token contract
    IAVS public avsContract; // EigenLayer's AVS contract

    // Events for logging actions
    event Staked(uint256 amount);
    event Unstaked(uint256 amount);

    // Constructor to initialize the contract with LRT token and AVS contract addresses
    constructor(address _lrtToken, address _avsContract) {
        require(_lrtToken != address(0), "Invalid LRT token address");
        require(_avsContract != address(0), "Invalid AVS contract address");

        lrtToken = IERC20(_lrtToken);
        avsContract = IAVS(_avsContract);
    }

    // Function to stake LRT tokens into the AVS contract
    function stakeLRT(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(lrtToken.balanceOf(msg.sender) >= amount, "Insufficient LRT balance");

        // Transfer LRT tokens from the user to this contract
        lrtToken.transferFrom(msg.sender, address(this), amount);

        // Approve the AVS contract to spend the LRT tokens
        lrtToken.approve(address(avsContract), amount);

        // Stake the LRT tokens in the AVS contract
        avsContract.stake(amount);

        emit Staked(amount);
    }

    // Function to unstake LRT tokens from the AVS contract
    function unstakeLRT(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Unstake the LRT tokens from the AVS contract
        avsContract.unstake(amount);

        // Transfer the unstaked LRT tokens back to the user
        lrtToken.transfer(msg.sender, amount);

        emit Unstaked(amount);
    }

    // Function to check the LRT token balance of this contract
    function getLRTBalance() external view returns (uint256) {
        return lrtToken.balanceOf(address(this));
    }
}
```
