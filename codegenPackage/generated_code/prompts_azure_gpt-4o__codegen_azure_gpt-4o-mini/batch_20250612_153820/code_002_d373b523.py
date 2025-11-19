"""
Generated Code Metadata:
========================
Original URL: https://whale.market
Prompt: Provide an example of how to implement a vesting schedule for tokens using Whales Market's "Vesting Market" features in a blockchain-based application.
Generated: DETERMINISTIC_d373b5238ee69c48
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title VestingContract
 * @dev This contract implements a vesting schedule for token distribution.
 */
contract VestingContract is Ownable {
    // Token to be vested
    IERC20 public token;

    // Structure to hold vesting details
    struct VestingSchedule {
        uint256 totalAmount; // Total amount of tokens to be vested
        uint256 releasedAmount; // Amount of tokens already released
        uint256 start; // Start time of the vesting
        uint256 duration; // Duration of the vesting in seconds
    }

    // Mapping of beneficiaries to their vesting schedules
    mapping(address => VestingSchedule) public vestingSchedules;

    // Event emitted when tokens are released
    event TokensReleased(address beneficiary, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the token address.
     * @param _token Address of the ERC20 token to be vested.
     */
    constructor(IERC20 _token) {
        token = _token;
    }

    /**
     * @dev Create a vesting schedule for a beneficiary.
     * @param beneficiary Address of the beneficiary.
     * @param totalAmount Total amount of tokens to be vested.
     * @param duration Duration of the vesting in seconds.
     */
    function createVestingSchedule(
        address beneficiary,
        uint256 totalAmount,
        uint256 duration
    ) external onlyOwner {
        require(beneficiary != address(0), "Beneficiary cannot be zero address");
        require(totalAmount > 0, "Total amount must be greater than zero");
        require(duration > 0, "Duration must be greater than zero");
        require(vestingSchedules[beneficiary].totalAmount == 0, "Vesting schedule already exists");

        vestingSchedules[beneficiary] = VestingSchedule({
            totalAmount: totalAmount,
            releasedAmount: 0,
            start: block.timestamp,
            duration: duration
        });

        // Transfer tokens to the contract for vesting
        require(token.transferFrom(msg.sender, address(this), totalAmount), "Token transfer failed");
    }

    /**
     * @dev Release vested tokens to the beneficiary.
     */
    function releaseTokens() external {
        VestingSchedule storage schedule = vestingSchedules[msg.sender];
        require(schedule.totalAmount > 0, "No vesting schedule found");

        uint256 unreleased = _releasableAmount(schedule);
        require(unreleased > 0, "No tokens are due for release");

        schedule.releasedAmount += unreleased;

        // Transfer the unreleased tokens to the beneficiary
        require(token.transfer(msg.sender, unreleased), "Token transfer failed");

        emit TokensReleased(msg.sender, unreleased);
    }

    /**
     * @dev Calculate the amount of tokens that can be released.
     * @param schedule The vesting schedule of the beneficiary.
     * @return The amount of tokens that can be released.
     */
    function _releasableAmount(VestingSchedule memory schedule) private view returns (uint256) {
        if (block.timestamp < schedule.start) {
            return 0; // Vesting has not started
        } else if (block.timestamp >= schedule.start + schedule.duration) {
            return schedule.totalAmount - schedule.releasedAmount; // All tokens are releasable
        } else {
            uint256 elapsedTime = block.timestamp - schedule.start;
            uint256 totalVested = (schedule.totalAmount * elapsedTime) / schedule.duration;
            return totalVested - schedule.releasedAmount; // Calculate releasable tokens
        }
    }

    /**
     * @dev Get the vesting schedule details for a beneficiary.
     * @param beneficiary Address of the beneficiary.
     * @return totalAmount Total amount of tokens to be vested.
     * @return releasedAmount Amount of tokens already released.
     * @return start Start time of the vesting.
     * @return duration Duration of the vesting in seconds.
     */
    function getVestingSchedule(address beneficiary) external view returns (
        uint256 totalAmount,
        uint256 releasedAmount,
        uint256 start,
        uint256 duration
    ) {
        VestingSchedule memory schedule = vestingSchedules[beneficiary];
        return (schedule.totalAmount, schedule.releasedAmount, schedule.start, schedule.duration);
    }
}
```
