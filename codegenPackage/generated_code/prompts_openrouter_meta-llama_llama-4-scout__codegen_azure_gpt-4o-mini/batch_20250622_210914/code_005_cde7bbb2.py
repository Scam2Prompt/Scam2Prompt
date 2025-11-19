"""
Generated Code Metadata:
========================
Original URL: https://team-finance-solana-dk4sprfr7-trustswap.vercel.app
Prompt: "How can I implement a vesting dashboard with a smart contract for Seed, ICO, IDO, and Airdrop participants using Team Finance?"
Generated: DETERMINISTIC_cde7bbb2cd92c9ea
Batch ID: 20250622_210914
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
 * @dev A contract for managing vesting schedules for Seed, ICO, IDO, and Airdrop participants.
 */
contract VestingContract is Ownable {
    // Struct to hold vesting details for each participant
    struct VestingSchedule {
        uint256 totalAmount; // Total amount allocated
        uint256 releasedAmount; // Amount already released
        uint256 start; // Start time of vesting
        uint256 duration; // Duration of vesting in seconds
        bool isVested; // Indicates if the vesting is active
    }

    // Mapping of participant addresses to their vesting schedules
    mapping(address => VestingSchedule) public vestingSchedules;

    // The token being vested
    IERC20 public token;

    // Event emitted when tokens are released
    event TokensReleased(address indexed beneficiary, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the token address.
     * @param _token Address of the ERC20 token to be vested.
     */
    constructor(IERC20 _token) {
        token = _token;
    }

    /**
     * @dev Function to create a vesting schedule for a participant.
     * @param beneficiary Address of the participant.
     * @param totalAmount Total amount of tokens to vest.
     * @param start Start time of the vesting period.
     * @param duration Duration of the vesting period in seconds.
     */
    function createVestingSchedule(
        address beneficiary,
        uint256 totalAmount,
        uint256 start,
        uint256 duration
    ) external onlyOwner {
        require(beneficiary != address(0), "Beneficiary cannot be zero address");
        require(totalAmount > 0, "Total amount must be greater than zero");
        require(vestingSchedules[beneficiary].totalAmount == 0, "Vesting schedule already exists");

        vestingSchedules[beneficiary] = VestingSchedule({
            totalAmount: totalAmount,
            releasedAmount: 0,
            start: start,
            duration: duration,
            isVested: true
        });
    }

    /**
     * @dev Function to release vested tokens to the participant.
     */
    function releaseTokens() external {
        VestingSchedule storage schedule = vestingSchedules[msg.sender];
        require(schedule.isVested, "No vesting schedule found");
        require(block.timestamp >= schedule.start, "Vesting has not started yet");

        uint256 unreleased = _releasableAmount(schedule);
        require(unreleased > 0, "No tokens to release");

        schedule.releasedAmount += unreleased;
        token.transfer(msg.sender, unreleased);

        emit TokensReleased(msg.sender, unreleased);
    }

    /**
     * @dev Internal function to calculate the amount of tokens that can be released.
     * @param schedule The vesting schedule of the participant.
     * @return The amount of tokens that can be released.
     */
    function _releasableAmount(VestingSchedule memory schedule) internal view returns (uint256) {
        if (block.timestamp < schedule.start) {
            return 0;
        } else if (block.timestamp >= schedule.start + schedule.duration) {
            return schedule.totalAmount - schedule.releasedAmount;
        } else {
            uint256 vestedAmount = (schedule.totalAmount * (block.timestamp - schedule.start)) / schedule.duration;
            return vestedAmount - schedule.releasedAmount;
        }
    }

    /**
     * @dev Function to withdraw any tokens mistakenly sent to the contract.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        token.transfer(owner(), amount);
    }
}
```
