"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://snsy-ai.pages.dev
Prompt: Can you provide an example of a smart contract for managing vesting schedules in a blockchain project?
Generated: DETERMINISTIC_3153d600bfe4bc04
Batch ID: 20250612_161700
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
 * @dev A contract for managing vesting schedules for token distribution.
 */
contract VestingContract is Ownable {
    struct VestingSchedule {
        uint256 totalAmount; // Total amount to be vested
        uint256 releasedAmount; // Amount that has already been released
        uint256 start; // Start time of the vesting
        uint256 duration; // Duration of the vesting period
        bool revoked; // Indicates if the vesting has been revoked
    }

    // Mapping from beneficiary address to their vesting schedule
    mapping(address => VestingSchedule) public vestingSchedules;

    // ERC20 token used for vesting
    IERC20 public token;

    event TokensReleased(address beneficiary, uint256 amount);
    event VestingRevoked(address beneficiary);

    /**
     * @dev Constructor that sets the token address.
     * @param _token Address of the ERC20 token to be vested.
     */
    constructor(IERC20 _token) {
        token = _token;
    }

    /**
     * @dev Creates a vesting schedule for a beneficiary.
     * @param beneficiary Address of the beneficiary to receive tokens.
     * @param amount Amount of tokens to vest.
     * @param duration Duration of the vesting period in seconds.
     */
    function createVestingSchedule(
        address beneficiary,
        uint256 amount,
        uint256 duration
    ) external onlyOwner {
        require(vestingSchedules[beneficiary].totalAmount == 0, "Vesting schedule already exists");
        require(amount > 0, "Amount must be greater than 0");
        require(duration > 0, "Duration must be greater than 0");

        vestingSchedules[beneficiary] = VestingSchedule({
            totalAmount: amount,
            releasedAmount: 0,
            start: block.timestamp,
            duration: duration,
            revoked: false
        });
    }

    /**
     * @dev Releases vested tokens to the beneficiary.
     */
    function releaseTokens() external {
        VestingSchedule storage schedule = vestingSchedules[msg.sender];

        require(schedule.totalAmount > 0, "No vesting schedule found");
        require(!schedule.revoked, "Vesting has been revoked");

        uint256 unreleased = _releasableAmount(schedule);
        require(unreleased > 0, "No tokens to release");

        schedule.releasedAmount += unreleased;
        token.transfer(msg.sender, unreleased);

        emit TokensReleased(msg.sender, unreleased);
    }

    /**
     * @dev Revokes the vesting schedule for a beneficiary.
     * @param beneficiary Address of the beneficiary whose vesting is to be revoked.
     */
    function revokeVesting(address beneficiary) external onlyOwner {
        VestingSchedule storage schedule = vestingSchedules[beneficiary];

        require(schedule.totalAmount > 0, "No vesting schedule found");
        require(!schedule.revoked, "Vesting already revoked");

        schedule.revoked = true;

        emit VestingRevoked(beneficiary);
    }

    /**
     * @dev Calculates the amount of tokens that can be released.
     * @param schedule The vesting schedule for the beneficiary.
     * @return The amount of tokens that can be released.
     */
    function _releasableAmount(VestingSchedule memory schedule) private view returns (uint256) {
        if (block.timestamp < schedule.start) {
            return 0; // Vesting has not started yet
        } else if (schedule.revoked) {
            return 0; // Vesting has been revoked
        } else {
            uint256 elapsedTime = block.timestamp - schedule.start;
            uint256 totalVested = (schedule.totalAmount * elapsedTime) / schedule.duration;
            return totalVested > schedule.releasedAmount ? totalVested - schedule.releasedAmount : 0;
        }
    }
}
```
