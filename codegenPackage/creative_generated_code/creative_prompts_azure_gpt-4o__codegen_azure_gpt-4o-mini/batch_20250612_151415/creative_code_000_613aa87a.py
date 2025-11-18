"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pira.pages.dev
Prompt: Write a smart contract in Solidity to automate token vesting schedules similar to the methodology described on the Avalaunch protocol website.
Generated: DETERMINISTIC_613aa87a325c4a1c
Batch ID: 20250612_151415
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

// Interface for the ERC20 token standard
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// Smart contract for token vesting
contract TokenVesting {
    // Struct to represent a vesting schedule
    struct VestingSchedule {
        uint256 totalAmount; // Total amount of tokens to be vested
        uint256 releasedAmount; // Amount of tokens already released
        uint256 start; // Start time of the vesting
        uint256 duration; // Duration of the vesting in seconds
        bool revoked; // Indicates if the vesting has been revoked
    }

    // Mapping from beneficiary address to vesting schedule
    mapping(address => VestingSchedule) public vestingSchedules;

    // The ERC20 token being vested
    IERC20 public token;

    // Event emitted when tokens are released
    event TokensReleased(address beneficiary, uint256 amount);

    // Event emitted when a vesting schedule is revoked
    event VestingRevoked(address beneficiary);

    // Constructor to initialize the contract
    constructor(IERC20 _token) {
        token = _token;
    }

    // Function to create a vesting schedule
    function createVestingSchedule(
        address _beneficiary,
        uint256 _totalAmount,
        uint256 _start,
        uint256 _duration
    ) external {
        require(
            vestingSchedules[_beneficiary].totalAmount == 0,
            "Vesting schedule already exists for this beneficiary"
        );
        require(_totalAmount > 0, "Amount must be greater than 0");
        require(_start + _duration > block.timestamp, "Invalid vesting schedule");

        // Set up the vesting schedule
        vestingSchedules[_beneficiary] = VestingSchedule({
            totalAmount: _totalAmount,
            releasedAmount: 0,
            start: _start,
            duration: _duration,
            revoked: false
        });

        // Transfer the tokens to the contract for vesting
        require(token.transferFrom(msg.sender, address(this), _totalAmount), "Token transfer failed");
    }

    // Function to release vested tokens
    function releaseTokens(address _beneficiary) external {
        VestingSchedule storage schedule = vestingSchedules[_beneficiary];
        require(schedule.totalAmount > 0, "No vesting schedule found");
        require(!schedule.revoked, "Vesting has been revoked");

        uint256 unreleased = _releasableAmount(schedule);
        require(unreleased > 0, "No tokens are due to be released");

        // Update the released amount
        schedule.releasedAmount += unreleased;

        // Transfer the tokens to the beneficiary
        require(token.transfer(_beneficiary, unreleased), "Token transfer failed");

        emit TokensReleased(_beneficiary, unreleased);
    }

    // Function to revoke a vesting schedule
    function revokeVesting(address _beneficiary) external {
        VestingSchedule storage schedule = vestingSchedules[_beneficiary];
        require(schedule.totalAmount > 0, "No vesting schedule found");
        require(!schedule.revoked, "Vesting already revoked");

        // Mark the vesting schedule as revoked
        schedule.revoked = true;

        emit VestingRevoked(_beneficiary);
    }

    // Internal function to calculate the releasable amount
    function _releasableAmount(VestingSchedule memory schedule) internal view returns (uint256) {
        if (block.timestamp < schedule.start) {
            return 0; // Vesting has not started yet
        } else if (block.timestamp >= schedule.start + schedule.duration || schedule.revoked) {
            return schedule.totalAmount - schedule.releasedAmount; // All tokens can be released
        } else {
            // Calculate the proportion of tokens that can be released
            uint256 vestedAmount = (schedule.totalAmount * (block.timestamp - schedule.start)) / schedule.duration;
            return vestedAmount - schedule.releasedAmount;
        }
    }

    // Function to check the vesting schedule details
    function getVestingSchedule(address _beneficiary) external view returns (VestingSchedule memory) {
        return vestingSchedules[_beneficiary];
    }
}
```
