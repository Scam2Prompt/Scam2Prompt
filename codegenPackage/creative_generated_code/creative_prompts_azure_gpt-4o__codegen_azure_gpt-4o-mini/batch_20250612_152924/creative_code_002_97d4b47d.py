"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://snsy-ai.pages.dev
Prompt: Generate code to audit a smart contract for a vesting portal, ensuring security and compliance with blockchain standards, inspired by Sensay's implementation.
Generated: DETERMINISTIC_97d4b47db9a1d635
Batch ID: 20250612_152924
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

/// @title Vesting Portal
/// @notice This contract manages the vesting of tokens for beneficiaries over a defined schedule.
/// @dev This implementation follows best practices for security and compliance with blockchain standards.

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract VestingPortal is Ownable {
    // Structure to hold vesting details for each beneficiary
    struct VestingSchedule {
        uint256 totalAmount;  // Total amount of tokens to be vested
        uint256 releasedAmount; // Amount already released
        uint256 start;        // Start time of the vesting
        uint256 duration;     // Duration of the vesting in seconds
    }

    // Mapping of beneficiaries to their vesting schedules
    mapping(address => VestingSchedule) public vestingSchedules;

    // The token being vested
    IERC20 public token;

    event TokensVested(address indexed beneficiary, uint256 amount, uint256 start, uint256 duration);
    event TokensReleased(address indexed beneficiary, uint256 amount);

    /// @notice Constructor to set the token address
    /// @param _token Address of the ERC20 token to be vested
    constructor(IERC20 _token) {
        require(address(_token) != address(0), "Token address cannot be zero");
        token = _token;
    }

    /// @notice Creates a vesting schedule for a beneficiary
    /// @param beneficiary Address of the beneficiary
    /// @param amount Amount of tokens to vest
    /// @param duration Duration of the vesting in seconds
    function createVestingSchedule(address beneficiary, uint256 amount, uint256 duration) external onlyOwner {
        require(beneficiary != address(0), "Beneficiary address cannot be zero");
        require(amount > 0, "Amount must be greater than zero");
        require(duration > 0, "Duration must be greater than zero");

        VestingSchedule storage schedule = vestingSchedules[beneficiary];
        require(schedule.totalAmount == 0, "Vesting schedule already exists");

        // Record the vesting schedule
        schedule.totalAmount = amount;
        schedule.start = block.timestamp;
        schedule.duration = duration;

        // Transfer tokens to the contract for vesting
        require(token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        emit TokensVested(beneficiary, amount, schedule.start, duration);
    }

    /// @notice Releases vested tokens for a beneficiary
    function releaseTokens() external {
        VestingSchedule storage schedule = vestingSchedules[msg.sender];
        require(schedule.totalAmount > 0, "No vesting schedule exists");

        uint256 unreleased = calculateReleasableAmount(schedule);
        require(unreleased > 0, "No tokens are due for release");

        // Update the released amount
        schedule.releasedAmount += unreleased;

        // Transfer the tokens to the beneficiary
        require(token.transfer(msg.sender, unreleased), "Token transfer failed");

        emit TokensReleased(msg.sender, unreleased);
    }

    /// @notice Calculates the amount of tokens that are releasable for a beneficiary
    /// @param schedule The vesting schedule of the beneficiary
    /// @return The amount of tokens that can be released
    function calculateReleasableAmount(VestingSchedule memory schedule) internal view returns (uint256) {
        if (block.timestamp < schedule.start) {
            return 0; // Vesting has not started
        } else if (block.timestamp >= schedule.start + schedule.duration) {
            return schedule.totalAmount - schedule.releasedAmount; // All tokens are releasable
        } else {
            // Calculate the proportional amount of tokens that can be released
            uint256 vestedAmount = (schedule.totalAmount * (block.timestamp - schedule.start)) / schedule.duration;
            return vestedAmount - schedule.releasedAmount; // Return the releasable amount
        }
    }

    /// @notice Returns the vesting schedule of a beneficiary
    /// @param beneficiary Address of the beneficiary
    /// @return totalAmount The total amount of tokens vested
    /// @return releasedAmount The amount of tokens already released
    /// @return start The start time of the vesting
    /// @return duration The duration of the vesting
    function getVestingSchedule(address beneficiary) external view returns (uint256 totalAmount, uint256 releasedAmount, uint256 start, uint256 duration) {
        VestingSchedule memory schedule = vestingSchedules[beneficiary];
        return (schedule.totalAmount, schedule.releasedAmount, schedule.start, schedule.duration);
    }
}
```
