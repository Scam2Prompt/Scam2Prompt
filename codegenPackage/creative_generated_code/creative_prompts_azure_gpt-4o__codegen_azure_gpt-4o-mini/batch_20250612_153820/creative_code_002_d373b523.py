"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://whale.market
Prompt: Provide an example of how to implement a vesting schedule for tokens using Whales Market's "Vesting Market" features in a blockchain-based application.
Generated: DETERMINISTIC_d373b5238ee69c48
Batch ID: 20250612_153820
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

/**
 * @title VestingContract
 * @dev This contract manages a vesting schedule for token distribution.
 */
contract VestingContract is Ownable {
    // Token to be vested
    IERC20 public token;

    // Struct to represent a vesting schedule
    struct VestingSchedule {
        uint256 totalAmount; // Total tokens to be vested
        uint256 released; // Amount of tokens already released
        uint256 start; // Start time of the vesting
        uint256 duration; // Duration of the vesting
        bool revocable; // Is the vesting schedule revocable?
        bool revoked; // Has the vesting schedule been revoked?
    }

    // Mapping from beneficiary address to their vesting schedule
    mapping(address => VestingSchedule) public vestingSchedules;

    // Event to log token release
    event TokensReleased(address beneficiary, uint256 amount);

    // Event to log vesting schedule creation
    event VestingScheduleCreated(address beneficiary, uint256 totalAmount, uint256 start, uint256 duration);

    // Event to log vesting schedule revocation
    event VestingScheduleRevoked(address beneficiary);

    /**
     * @param _token Address of the token being vested
     */
    constructor(IERC20 _token) {
        token = _token;
    }

    /**
     * @dev Creates a vesting schedule for a beneficiary
     * @param beneficiary Address of the beneficiary
     * @param totalAmount Total tokens to vest
     * @param start Start time of the vesting
     * @param duration Duration of the vesting
     * @param revocable Whether the vesting is revocable
     */
    function createVestingSchedule(
        address beneficiary,
        uint256 totalAmount,
        uint256 start,
        uint256 duration,
        bool revocable
    ) external onlyOwner {
        require(beneficiary != address(0), "Beneficiary is the zero address");
        require(totalAmount > 0, "Total amount must be greater than 0");
        require(vestingSchedules[beneficiary].totalAmount == 0, "Vesting schedule already exists");

        // Transfer tokens to the contract for vesting
        token.transferFrom(msg.sender, address(this), totalAmount);

        // Create the vesting schedule
        vestingSchedules[beneficiary] = VestingSchedule({
            totalAmount: totalAmount,
            released: 0,
            start: start,
            duration: duration,
            revocable: revocable,
            revoked: false
        });

        emit VestingScheduleCreated(beneficiary, totalAmount, start, duration);
    }

    /**
     * @dev Releases vested tokens for the beneficiary
     */
    function release() external {
        VestingSchedule storage schedule = vestingSchedules[msg.sender];
        
        require(schedule.totalAmount > 0, "No vesting schedule found");
        require(!schedule.revoked, "Vesting schedule has been revoked");

        uint256 vestedAmount = _vestedAmount(schedule);
        uint256 unreleased = vestedAmount - schedule.released;

        require(unreleased > 0, "No tokens are due");

        // Update released amount and transfer tokens
        schedule.released += unreleased;
        token.transfer(msg.sender, unreleased);

        emit TokensReleased(msg.sender, unreleased);
    }

    /**
     * @dev Returns the amount of tokens that are vested for the beneficiary
     * @param schedule The vesting schedule of the beneficiary
     * @return The amount of vested tokens
     */
    function _vestedAmount(VestingSchedule memory schedule) internal view returns (uint256) {
        if (block.timestamp < schedule.start) {
            return 0;
        } else if (block.timestamp >= schedule.start + schedule.duration || schedule.revoked) {
            return schedule.totalAmount;
        } else {
            return (schedule.totalAmount * (block.timestamp - schedule.start)) / schedule.duration;
        }
    }

    /**
     * @dev Allows the owner to revoke a vesting schedule
     * @param beneficiary Address of the beneficiary
     */
    function revoke(address beneficiary) external onlyOwner {
        VestingSchedule storage schedule = vestingSchedules[beneficiary];
        require(schedule.revocable, "Vesting schedule is not revocable");
        require(!schedule.revoked, "Vesting schedule already revoked");

        // Mark the vesting as revoked
        schedule.revoked = true;

        // Transfer back unreleased tokens to the owner
        uint256 unreleased = schedule.totalAmount - schedule.released;
        token.transfer(owner(), unreleased);

        emit VestingScheduleRevoked(beneficiary);
    }

    /**
     * @dev Returns the vesting schedule details for a beneficiary
     * @param beneficiary Address of the beneficiary
     * @return The vesting schedule details
     */
    function getVestingSchedule(address beneficiary) external view returns (VestingSchedule memory) {
        return vestingSchedules[beneficiary];
    }
}
```
