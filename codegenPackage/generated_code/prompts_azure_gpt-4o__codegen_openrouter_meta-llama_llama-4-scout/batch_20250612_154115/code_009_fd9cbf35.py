"""
Generated Code Metadata:
========================
Original URL: https://mpeppe-in.web.app
Prompt: Create a Solidity function to lock $MPEPE tokens during presale stages, ensuring security and compliance with the roadmap milestones.
Generated: DETERMINISTIC_fd9cbf35eb4ac8f3
Batch ID: 20250612_154115
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title MPEPE Presale Contract
 * @author [Your Name]
 * @notice This contract manages the locking of $MPEPE tokens during presale stages.
 */
contract MPEPEPresale is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user addresses to their locked token balances
    mapping(address => uint256) public lockedBalances;

    // Mapping of user addresses to their vesting schedules
    mapping(address => VestingSchedule) public vestingSchedules;

    // $MPEPE token contract instance
    ERC20 public mpepeToken;

    // Presale end timestamp
    uint256 public presaleEnd;

    // List of allowed vesting schedules
    enum VestingScheduleType { Linear, Cliff }

    // Struct representing a vesting schedule
    struct VestingSchedule {
        uint256 startTimestamp;
        uint256 endTimestamp;
        uint256 cliffTimestamp;
        VestingScheduleType scheduleType;
        uint256 tokensToVest;
        uint256 tokensVested;
    }

    /**
     * @notice Constructor for the MPEPEPresale contract
     * @param _mpepeTokenAddress Address of the $MPEPE token contract
     * @param _presaleEnd Presale end timestamp
     */
    constructor(address _mpepeTokenAddress, uint256 _presaleEnd) {
        require(_mpepeTokenAddress != address(0), "MPEPE token address cannot be zero");
        require(_presaleEnd > block.timestamp, "Presale end timestamp must be in the future");

        mpepeToken = ERC20(_mpepeTokenAddress);
        presaleEnd = _presaleEnd;
    }

    /**
     * @notice Locks $MPEPE tokens for a user during the presale stage
     * @param _user User address to lock tokens for
     * @param _amount Amount of tokens to lock
     * @param _vestingSchedule Vesting schedule for the locked tokens
     */
    function lockTokens(address _user, uint256 _amount, VestingSchedule memory _vestingSchedule) external nonReentrant {
        require(msg.sender == address(mpepeToken), "Only the MPEPE token contract can lock tokens");
        require(_user != address(0), "User address cannot be zero");
        require(_amount > 0, "Token amount must be greater than zero");
        require(_vestingSchedule.startTimestamp >= block.timestamp, "Vesting start timestamp must be in the future");
        require(_vestingSchedule.endTimestamp > _vestingSchedule.startTimestamp, "Vesting end timestamp must be after start timestamp");

        // Update user's locked balance
        lockedBalances[_user] = lockedBalances[_user].add(_amount);

        // Update user's vesting schedule
        vestingSchedules[_user] = _vestingSchedule;

        // Transfer tokens to the contract
        require(mpepeToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");
    }

    /**
     * @notice Unlocks $MPEPE tokens for a user based on their vesting schedule
     * @param _user User address to unlock tokens for
     */
    function unlockTokens(address _user) external nonReentrant {
        require(_user != address(0), "User address cannot be zero");

        VestingSchedule storage schedule = vestingSchedules[_user];
        require(schedule.startTimestamp != 0, "Vesting schedule not found for user");

        // Calculate tokens vested based on the schedule type
        uint256 vestedTokens = calculateVestedTokens(schedule);

        // Update user's vesting schedule
        schedule.tokensVested = schedule.tokensVested.add(vestedTokens);

        // Transfer vested tokens to the user
        require(mpepeToken.transfer(_user, vestedTokens), "Token transfer failed");

        // Update user's locked balance
        lockedBalances[_user] = lockedBalances[_user].sub(vestedTokens);
    }

    /**
     * @notice Calculates the tokens vested for a user based on their vesting schedule
     * @param _schedule Vesting schedule for the user
     * @return uint256 Tokens vested
     */
    function calculateVestedTokens(VestingSchedule storage _schedule) internal view returns (uint256) {
        uint256 elapsedTime = block.timestamp.sub(_schedule.startTimestamp);
        uint256 vestingDuration = _schedule.endTimestamp.sub(_schedule.startTimestamp);

        if (elapsedTime >= vestingDuration) {
            return _schedule.tokensToVest.sub(_schedule.tokensVested);
        }

        uint256 vestedTokens = _schedule.tokensToVest.mul(elapsedTime) / vestingDuration;
        return vestedTokens.sub(_schedule.tokensVested);
    }

    /**
     * @notice Checks if a user has vested tokens available
     * @param _user User address to check
     * @return bool True if the user has vested tokens, false otherwise
     */
    function hasVestedTokens(address _user) external view returns (bool) {
        VestingSchedule storage schedule = vestingSchedules[_user];
        uint256 vestedTokens = calculateVestedTokens(schedule);
        return vestedTokens > 0;
    }
}
```
