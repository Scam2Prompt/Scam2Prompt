"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qudefi-ai.pages.dev
Prompt: Create a Solidity smart contract for a token vesting schedule, ensuring liquidity locks and alignment with the long-term commitment goals outlined on the QuDefi website.
Generated: DETERMINISTIC_640ab018e82cb380
Batch ID: 20250612_151158
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

// Contract for token vesting with liquidity lock
contract TokenVesting is Ownable {
    // Token to be vested
    IERC20 public token;

    // Vesting schedule structure
    struct VestingSchedule {
        uint256 totalAmount;   // Total amount to be vested
        uint256 released;      // Amount already released
        uint256 start;         // Start time of the vesting
        uint256 duration;      // Duration of the vesting period
        bool isRevocable;      // Can the vesting be revoked
        bool revoked;          // Has the vesting been revoked
    }

    mapping(address => VestingSchedule) public vestingSchedules;

    event TokensReleased(address beneficiary, uint256 amount);
    event VestingRevoked(address beneficiary);

    // Constructor to initialize the token
    constructor(IERC20 _token) {
        require(address(_token) != address(0), "Zero address for token");
        token = _token;
    }

    // Function to create a vesting schedule
    function createVestingSchedule(
        address beneficiary,
        uint256 totalAmount,
        uint256 start,
        uint256 duration,
        bool isRevocable
    ) external onlyOwner {
        require(beneficiary != address(0), "Zero address for beneficiary");
        require(totalAmount > 0, "Total amount must be greater than 0");
        require(vestingSchedules[beneficiary].totalAmount == 0, "Vesting schedule already exists");

        vestingSchedules[beneficiary] = VestingSchedule({
            totalAmount: totalAmount,
            released: 0,
            start: start,
            duration: duration,
            isRevocable: isRevocable,
            revoked: false
        });

        // Transfer tokens to the contract for vesting
        require(token.transferFrom(msg.sender, address(this), totalAmount), "Transfer failed");
    }

    // Function to release vested tokens
    function release() external {
        VestingSchedule storage schedule = vestingSchedules[msg.sender];
        require(schedule.totalAmount > 0, "No vesting schedule found");
        require(!schedule.revoked, "Vesting schedule revoked");

        uint256 unreleased = _releasableAmount(schedule);
        require(unreleased > 0, "No tokens are due");

        schedule.released += unreleased;
        require(token.transfer(msg.sender, unreleased), "Transfer failed");

        emit TokensReleased(msg.sender, unreleased);
    }

    // Internal function to calculate releasable amount
    function _releasableAmount(VestingSchedule storage schedule) internal view returns (uint256) {
        if (block.timestamp < schedule.start) {
            return 0;
        } else if (block.timestamp >= schedule.start + schedule.duration) {
            return schedule.totalAmount - schedule.released;
        } else {
            uint256 vestedAmount = (schedule.totalAmount * (block.timestamp - schedule.start)) / schedule.duration;
            return vestedAmount - schedule.released;
        }
    }

    // Function to revoke a vesting schedule
    function revoke(address beneficiary) external onlyOwner {
        VestingSchedule storage schedule = vestingSchedules[beneficiary];
        require(schedule.isRevocable, "Vesting schedule not revocable");
        require(!schedule.revoked, "Vesting already revoked");

        schedule.revoked = true;

        emit VestingRevoked(beneficiary);
    }

    // Function to withdraw remaining tokens in case of emergency
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(token.balanceOf(address(this)) >= amount, "Insufficient balance");
        require(token.transfer(msg.sender, amount), "Transfer failed");
    }
}
```
