"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vesting-cookie.online
Prompt: Generate an example of a Smart contract that handles vesting schedules for a DAO.
Generated: DETERMINISTIC_7c26b5c2ff72b789
Batch ID: 20250612_162808
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title VestingContract
 * @dev This contract provides a vesting schedule for a DAO using ERC20 tokens
 */
contract VestingContract is Ownable {
    // Struct to hold vesting information for each beneficiary
    struct VestingSchedule {
        uint256 totalAmount; // Total amount of tokens to vest
        uint256 released; // Amount of tokens that have been released
        uint256 start; // Start time of the vesting period
        uint256 duration; // Duration of the vesting period
    }

    // Mapping from beneficiary address to their vesting schedule
    mapping(address => VestingSchedule) public vestingSchedules;
    
    // ERC20 token being vested
    IERC20 public token;

    // Event emitted when tokens are released
    event TokensReleased(address beneficiary, uint256 amount);

    /**
     * @dev Constructor to initialize the token and vesting schedule
     * @param _token Address of the ERC20 token contract
     */
    constructor(IERC20 _token) {
        token = _token;
    }

    /**
     * @dev Function to create a vesting schedule for a beneficiary
     * @param beneficiary Address of the beneficiary
     * @param totalAmount Total amount of tokens to vest
     * @param start Start time of the vesting period
     * @param duration Duration of the vesting period in seconds
     */
    function createVestingSchedule(
        address beneficiary,
        uint256 totalAmount,
        uint256 start,
        uint256 duration
    ) external onlyOwner {
        require(beneficiary != address(0), "Beneficiary cannot be the zero address");
        require(totalAmount > 0, "Total amount must be greater than zero");
        require(vestingSchedules[beneficiary].totalAmount == 0, "Vesting schedule already exists");

        vestingSchedules[beneficiary] = VestingSchedule({
            totalAmount: totalAmount,
            released: 0,
            start: start,
            duration: duration
        });
    }

    /**
     * @dev Function to release vested tokens to a beneficiary
     */
    function releaseTokens() external {
        VestingSchedule storage schedule = vestingSchedules[msg.sender];
        
        require(schedule.totalAmount > 0, "No vesting schedule for this address");
        
        uint256 unreleased = _releasableAmount(schedule);
        require(unreleased > 0, "No tokens to release");

        schedule.released += unreleased;
        token.transfer(msg.sender, unreleased);

        emit TokensReleased(msg.sender, unreleased);
    }

    /**
     * @dev Internal function to calculate the amount of unreleased tokens
     * @param schedule The vesting schedule of the beneficiary
     * @return The amount of tokens that can be released
     */
    function _releasableAmount(VestingSchedule memory schedule) internal view returns (uint256) {
        uint256 vestedAmount = _vestedAmount(schedule);
        return vestedAmount - schedule.released;
    }

    /**
     * @dev Internal function to calculate the amount of vested tokens
     * @param schedule The vesting schedule of the beneficiary
     * @return The amount of vested tokens
     */
    function _vestedAmount(VestingSchedule memory schedule) internal view returns (uint256) {
        if (block.timestamp < schedule.start) {
            return 0;
        } else if (block.timestamp >= schedule.start + schedule.duration) {
            return schedule.totalAmount;
        } else {
            return (schedule.totalAmount * (block.timestamp - schedule.start)) / schedule.duration;
        }
    }

    /**
     * @dev Function to withdraw any leftover tokens in the contract
     * @param amount Amount of tokens to withdraw
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(token.balanceOf(address(this)) >= amount, "Insufficient balance");
        token.transfer(owner(), amount);
    }
}
```
