"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vesting-cookie.online
Prompt: How can I use Smart contracts to manage vesting for tokens in a DAO?
Generated: DETERMINISTIC_29ae6de42ff8446c
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
pragma solidity ^0.8.17;

/**
 * @title TokenVesting
 * @dev Smart contract to manage token vesting for a DAO.
 *      Allows the DAO to distribute tokens to users with a vesting schedule.
 */
contract TokenVesting {
    // Struct to represent individual vesting schedules
    struct VestingSchedule {
        uint256 totalAmount; // Total tokens to be vested
        uint256 releasedAmount; // Tokens already released
        uint256 startTime; // Vesting start time (in seconds, Unix timestamp)
        uint256 cliffDuration; // Cliff duration (in seconds)
        uint256 vestingDuration; // Total vesting duration (in seconds)
        bool isRevocable; // Indicates if the schedule is revocable
        bool revoked; // Indicates if the schedule has been revoked
    }

    // Mapping of beneficiary addresses to their vesting schedules
    mapping(address => VestingSchedule) public vestingSchedules;

    // Token contract interface
    IERC20 public immutable token;

    // DAO owner address
    address public immutable owner;

    // Events
    event VestingScheduleCreated(
        address indexed beneficiary,
        uint256 totalAmount,
        uint256 startTime,
        uint256 cliffDuration,
        uint256 vestingDuration,
        bool isRevocable
    );
    event TokensReleased(address indexed beneficiary, uint256 amount);
    event VestingRevoked(address indexed beneficiary);

    // Modifier to restrict access to the DAO owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the TokenVesting contract.
     * @param _token Address of the ERC20 token contract.
     */
    constructor(address _token) {
        require(_token != address(0), "Invalid token address");
        token = IERC20(_token);
        owner = msg.sender;
    }

    /**
     * @dev Creates a new vesting schedule for a beneficiary.
     * @param _beneficiary Address of the beneficiary.
     * @param _totalAmount Total tokens to vest.
     * @param _startTime Vesting start time.
     * @param _cliffDuration Cliff duration in seconds.
     * @param _vestingDuration Total vesting duration in seconds.
     * @param _isRevocable Indicates if the vesting schedule is revocable.
     */
    function createVestingSchedule(
        address _beneficiary,
        uint256 _totalAmount,
        uint256 _startTime,
        uint256 _cliffDuration,
        uint256 _vestingDuration,
        bool _isRevocable
    ) external onlyOwner {
        require(_beneficiary != address(0), "Invalid beneficiary address");
        require(_totalAmount > 0, "Total amount must be greater than zero");
        require(_vestingDuration > _cliffDuration, "Cliff duration must be less than vesting duration");
        require(vestingSchedules[_beneficiary].totalAmount == 0, "Schedule already exists for beneficiary");

        // Transfer tokens to this contract for vesting
        require(token.transferFrom(msg.sender, address(this), _totalAmount), "Token transfer failed");

        // Create the vesting schedule
        vestingSchedules[_beneficiary] = VestingSchedule({
            totalAmount: _totalAmount,
            releasedAmount: 0,
            startTime: _startTime,
            cliffDuration: _cliffDuration,
            vestingDuration: _vestingDuration,
            isRevocable: _isRevocable,
            revoked: false
        });

        emit VestingScheduleCreated(_beneficiary, _totalAmount, _startTime, _cliffDuration, _vestingDuration, _isRevocable);
    }

    /**
     * @dev Releases vested tokens for the beneficiary.
     * @param _beneficiary Address of the beneficiary.
     */
    function releaseTokens(address _beneficiary) external {
        VestingSchedule storage schedule = vestingSchedules[_beneficiary];
        require(schedule.totalAmount > 0, "No vesting schedule found");
        require(!schedule.revoked, "Vesting schedule revoked");

        uint256 vestedAmount = _computeVestedAmount(schedule);
        uint256 releasableAmount = vestedAmount - schedule.releasedAmount;

        require(releasableAmount > 0, "No tokens are available for release");

        schedule.releasedAmount += releasableAmount;
        require(token.transfer(_beneficiary, releasableAmount), "Token transfer failed");

        emit TokensReleased(_beneficiary, releasableAmount);
    }

    /**
     * @dev Revokes a vesting schedule (only if revocable).
     * @param _beneficiary Address of the beneficiary.
     */
    function revokeVesting(address _beneficiary) external onlyOwner {
        VestingSchedule storage schedule = vestingSchedules[_beneficiary];
        require(schedule.isRevocable, "Vesting schedule is not revocable");
        require(!schedule.revoked, "Vesting schedule already revoked");

        schedule.revoked = true;

        uint256 vestedAmount = _computeVestedAmount(schedule);
        uint256 unreleasedAmount = schedule.totalAmount - schedule.releasedAmount;

        // Return the unreleased tokens to the DAO owner
        uint256 refundAmount = unreleasedAmount - (vestedAmount - schedule.releasedAmount);
        require(token.transfer(owner, refundAmount), "Token transfer failed");

        emit VestingRevoked(_beneficiary);
    }

    /**
     * @dev Computes the amount of tokens vested in the schedule.
     * @param schedule Vesting schedule.
     * @return Amount of vested tokens.
     */
    function _computeVestedAmount(VestingSchedule memory schedule) private view returns (uint256) {
        if (block.timestamp < schedule.startTime + schedule.cliffDuration || schedule.revoked) {
            return 0;
        }

        uint256 elapsedTime = block.timestamp - schedule.startTime;
        if (elapsedTime >= schedule.vestingDuration) {
            return schedule.totalAmount;
        }

        return (schedule.totalAmount * elapsedTime) / schedule.vestingDuration;
    }
}

/**
 * @dev Interface for ERC20 token standard
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
