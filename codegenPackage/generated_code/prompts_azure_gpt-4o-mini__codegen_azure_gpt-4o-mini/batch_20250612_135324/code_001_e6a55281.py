"""
Generated Code Metadata:
========================
Original URL: https://zerolend.omc.zone
Prompt: How can I implement a linear vesting schedule for token distribution similar to the Zerolend model with a 25% cliff?
Generated: DETERMINISTIC_e6a552813d30e3d5
Batch ID: 20250612_135324
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

contract LinearVesting {
    // State variables
    address public beneficiary; // Address of the beneficiary
    uint256 public start; // Start time of the vesting
    uint256 public cliff; // Cliff duration in seconds
    uint256 public duration; // Total vesting duration in seconds
    uint256 public released; // Amount of tokens released

    // ERC20 token interface
    IERC20 public token;

    // Events
    event TokensReleased(uint256 amount);

    // Constructor to initialize the vesting schedule
    constructor(
        address _beneficiary,
        uint256 _start,
        uint256 _cliff,
        uint256 _duration,
        address _token
    ) {
        require(_beneficiary != address(0), "Beneficiary cannot be the zero address");
        require(_cliff <= _duration, "Cliff must be less than or equal to duration");
        require(_duration > 0, "Duration must be greater than 0");
        
        beneficiary = _beneficiary;
        start = _start;
        cliff = _start + _cliff;
        duration = _duration;
        token = IERC20(_token);
    }

    // Function to release vested tokens
    function release() public {
        // Calculate the amount of tokens that can be released
        uint256 unreleased = _releasableAmount();

        require(unreleased > 0, "No tokens are due for release");

        // Update the released amount
        released += unreleased;

        // Transfer the tokens to the beneficiary
        require(token.transfer(beneficiary, unreleased), "Token transfer failed");

        emit TokensReleased(unreleased);
    }

    // Internal function to calculate the releasable amount
    function _releasableAmount() internal view returns (uint256) {
        if (block.timestamp < cliff) {
            return 0; // No tokens are releasable before the cliff
        } else if (block.timestamp >= start + duration) {
            return token.balanceOf(address(this)); // All tokens are releasable after the vesting period
        } else {
            // Calculate the vested amount based on the elapsed time
            uint256 elapsedTime = block.timestamp - start;
            uint256 totalVested = (token.balanceOf(address(this)) * elapsedTime) / duration;
            return totalVested - released; // Return the releasable amount
        }
    }

    // Function to check the amount of tokens that can be released
    function releasableAmount() external view returns (uint256) {
        return _releasableAmount();
    }
}

// Minimal ERC20 interface for token interaction
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
