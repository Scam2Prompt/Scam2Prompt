"""
Generated Code Metadata:
========================
Original URL: https://vestings-scapesmania.pages.dev
Prompt: Write a smart contract in Solidity for a token vesting system tailored for ScapesMania's $MANIA token, ensuring compatibility with the project's Web3 gaming ecosystem.
Generated: DETERMINISTIC_fefe6236912ee6bb
Batch ID: 20250612_152714
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title TokenVestingContract
 * @author [Your Name]
 * @notice A token vesting system for ScapesMania's $MANIA token.
 */
contract TokenVestingContract is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of vesting schedules
    mapping(address => VestingSchedule) public vestingSchedules;

    // $MANIA token contract
    ERC20 public token;

    /**
     * @param _token Address of the $MANIA token contract
     */
    constructor(address _token) {
        require(_token != address(0), "Token address cannot be zero");
        token = ERC20(_token);
    }

    /**
     * @notice Create a new vesting schedule for a user
     * @param _user Address of the user
     * @param _vestedAmount Amount of tokens to vest
     * @param _startTime Timestamp when vesting starts
     * @param _duration Duration of vesting in seconds
     * @param _cliffDuration Cliff duration in seconds
     */
    function createVestingSchedule(
        address _user,
        uint256 _vestedAmount,
        uint256 _startTime,
        uint256 _duration,
        uint256 _cliffDuration
    ) public onlyOwner {
        require(_user != address(0), "User address cannot be zero");
        require(_vestedAmount > 0, "Vested amount must be greater than zero");
        require(_startTime > block.timestamp, "Start time must be in the future");
        require(_duration > 0, "Duration must be greater than zero");
        require(_cliffDuration <= _duration, "Cliff duration cannot exceed duration");

        vestingSchedules[_user] = VestingSchedule(
            _vestedAmount,
            _startTime,
            _duration,
            _cliffDuration,
            0
        );

        // Transfer tokens to the contract
        require(token.transferFrom(msg.sender, address(this), _vestedAmount), "Token transfer failed");
    }

    /**
     * @notice Release vested tokens for a user
     */
    function releaseVestedTokens() public nonReentrant {
        VestingSchedule storage schedule = vestingSchedules[msg.sender];
        require(schedule.startTime != 0, "No vesting schedule found for user");

        uint256 vestedAmount = calculateVestedAmount(schedule);
        require(vestedAmount > 0, "No vested tokens to release");

        // Update vesting schedule
        schedule.releasedAmount = schedule.releasedAmount.add(vestedAmount);

        // Transfer vested tokens to user
        require(token.transfer(msg.sender, vestedAmount), "Token transfer failed");
    }

    /**
     * @notice Calculate vested amount for a user
     * @param _schedule Vesting schedule for the user
     * @return Vested amount
     */
    function calculateVestedAmount(VestingSchedule storage _schedule) internal view returns (uint256) {
        uint256 elapsedTime = block.timestamp.sub(_schedule.startTime);
        if (elapsedTime < _schedule.cliffDuration) {
            return 0;
        }

        uint256 vestedAmount = _schedule.vestedAmount.mul(
            elapsedTime.sub(_schedule.cliffDuration).min(_schedule.duration.sub(_schedule.cliffDuration))
        ).div(_schedule.duration.sub(_schedule.cliffDuration));

        return vestedAmount.sub(_schedule.releasedAmount);
    }

    /**
     * @dev Modifier to restrict access to contract owner
     */
    modifier onlyOwner {
        require(msg.sender == owner(), "Only contract owner can call this function");
        _;
    }

    /**
     * @dev Get contract owner
     * @return Owner address
     */
    function owner() public view returns (address) {
        return msg.sender;
    }

    /**
     * @dev Struct representing a vesting schedule
     */
    struct VestingSchedule {
        uint256 vestedAmount;
        uint256 startTime;
        uint256 duration;
        uint256 cliffDuration;
        uint256 releasedAmount;
    }
}
```
