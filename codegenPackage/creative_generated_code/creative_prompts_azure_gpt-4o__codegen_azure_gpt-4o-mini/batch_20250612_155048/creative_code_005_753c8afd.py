"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://illuvius.com
Prompt: Provide an example of a smart contract implementation that enforces the lock-up period and vesting parameters outlined by Illuvius for MXNA tokens.
Generated: DETERMINISTIC_753c8afd8edbb621
Batch ID: 20250612_155048
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

/// @title MXNA Token Vesting Smart Contract
/// @author Your Name
/// @notice This contract implements a vesting schedule with a lock-up period for MXNA tokens.
/// @dev This contract is designed to ensure that token allocations are locked up and released according to the specified vesting parameters.

contract MXNAVesting {
    // State variables
    address public beneficiary; // Address of the token beneficiary
    uint256 public start; // Start time of the vesting period
    uint256 public cliff; // Duration of the cliff period
    uint256 public duration; // Total duration of the vesting period
    uint256 public released; // Amount of tokens released to the beneficiary
    uint256 public totalAmount; // Total amount of tokens allocated for vesting

    // ERC20 token interface
    interface IERC20 {
        function transfer(address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
    }

    IERC20 public token; // Token contract

    /// @notice Event emitted when tokens are released
    event TokensReleased(uint256 amount);

    /// @param _token Address of the ERC20 token contract
    /// @param _beneficiary Address of the beneficiary receiving the tokens
    /// @param _totalAmount Total amount of tokens for vesting
    /// @param _cliff Duration of the cliff in seconds
    /// @param _duration Total duration of the vesting in seconds
    constructor(
        address _token,
        address _beneficiary,
        uint256 _totalAmount,
        uint256 _cliff,
        uint256 _duration
    ) {
        require(_beneficiary != address(0), "Beneficiary cannot be the zero address");
        require(_totalAmount > 0, "Total amount must be greater than zero");
        require(_cliff < _duration, "Cliff must be less than duration");

        token = IERC20(_token);
        beneficiary = _beneficiary;
        totalAmount = _totalAmount;
        cliff = _cliff;
        duration = _duration;
        start = block.timestamp; // Set start time to current time
    }

    /// @notice Releases vested tokens to the beneficiary
    /// @dev Can only be called by the beneficiary
    function release() public {
        require(msg.sender == beneficiary, "Only beneficiary can release tokens");
        uint256 unreleased = _releasableAmount();

        require(unreleased > 0, "No tokens are due for release");

        released += unreleased;
        token.transfer(beneficiary, unreleased);

        emit TokensReleased(unreleased);
    }

    /// @notice Calculates the amount of tokens that are releasable
    /// @return The amount of tokens that can be released
    function _releasableAmount() private view returns (uint256) {
        return _vestedAmount() - released;
    }

    /// @notice Calculates the amount of tokens that have vested
    /// @return The amount of tokens that have vested
    function _vestedAmount() private view returns (uint256) {
        if (block.timestamp < start + cliff) {
            return 0;
        } else if (block.timestamp >= start + duration) {
            return totalAmount;
        } else {
            // Calculate the vested amount based on linear vesting
            return (totalAmount * (block.timestamp - start)) / duration;
        }
    }

    /// @notice Returns the total amount of tokens that can be released
    /// @return The total tokens that can be released to the beneficiary
    function totalReleasable() public view returns (uint256) {
        return _releasableAmount();
    }

    /// @notice Returns the current balance of the contract
    /// @return The balance of the contract
    function currentBalance() public view returns (uint256) {
        return token.balanceOf(address(this));
    }
}
```
