"""
Generated Code Metadata:
========================
Original URL: https://moonbag-org.pages.dev
Prompt: Design a smart contract in Solidity that handles token locking and vesting for a team, similar to MoonBag's tokenomics.
Generated: DETERMINISTIC_234b307743876d9b
Batch ID: 20250622_211330
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
 * @title Token Vesting Contract
 * @author [Your Name]
 * @notice A smart contract for token locking and vesting.
 */
contract TokenVesting is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of vesting schedules
    mapping (address => VestingSchedule) public vestingSchedules;

    // Mapping of team members
    mapping (address => bool) public teamMembers;

    // Token contract
    ERC20 public token;

    // Total vesting duration in seconds
    uint256 public totalVestingDuration;

    // Cliff period in seconds
    uint256 public cliffPeriod;

    /**
     * @dev Event emitted when a team member is added
     * @param member Address of the team member
     */
    event TeamMemberAdded(address member);

    /**
     * @dev Event emitted when a vesting schedule is created
     * @param beneficiary Address of the beneficiary
     * @param startTime Start time of the vesting schedule
     * @param duration Duration of the vesting schedule
     * @param amount Amount of tokens to vest
     */
    event VestingScheduleCreated(address beneficiary, uint256 startTime, uint256 duration, uint256 amount);

    /**
     * @dev Event emitted when tokens are released
     * @param beneficiary Address of the beneficiary
     * @param amount Amount of tokens released
     */
    event TokensReleased(address beneficiary, uint256 amount);

    /**
     * @dev Struct representing a vesting schedule
     */
    struct VestingSchedule {
        uint256 startTime;
        uint256 duration;
        uint256 amount;
        uint256 released;
    }

    /**
     * @dev Constructor
     * @param _token Address of the token contract
     * @param _totalVestingDuration Total vesting duration in seconds
     * @param _cliffPeriod Cliff period in seconds
     */
    constructor(ERC20 _token, uint256 _totalVestingDuration, uint256 _cliffPeriod) {
        token = _token;
        totalVestingDuration = _totalVestingDuration;
        cliffPeriod = _cliffPeriod;
    }

    /**
     * @dev Add a team member
     * @param _member Address of the team member
     */
    function addTeamMember(address _member) public onlyOwner {
        teamMembers[_member] = true;
        emit TeamMemberAdded(_member);
    }

    /**
     * @dev Create a vesting schedule for a team member
     * @param _beneficiary Address of the beneficiary
     * @param _amount Amount of tokens to vest
     */
    function createVestingSchedule(address _beneficiary, uint256 _amount) public onlyTeamMember {
        require(vestingSchedules[_beneficiary].startTime == 0, "Vesting schedule already exists");

        VestingSchedule memory schedule;
        schedule.startTime = block.timestamp;
        schedule.duration = totalVestingDuration;
        schedule.amount = _amount;
        schedule.released = 0;

        vestingSchedules[_beneficiary] = schedule;

        // Transfer tokens to the contract
        require(token.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        emit VestingScheduleCreated(_beneficiary, schedule.startTime, schedule.duration, schedule.amount);
    }

    /**
     * @dev Release tokens from a vesting schedule
     * @param _beneficiary Address of the beneficiary
     */
    function releaseTokens(address _beneficiary) public nonReentrant {
        VestingSchedule storage schedule = vestingSchedules[_beneficiary];

        require(schedule.startTime != 0, "Vesting schedule does not exist");
        require(schedule.released < schedule.amount, "All tokens have been released");

        uint256 vestingEndTime = schedule.startTime.add(schedule.duration);
        uint256 cliffEndTime = schedule.startTime.add(cliffPeriod);

        if (block.timestamp >= vestingEndTime) {
            // All tokens have vested
            uint256 tokensToRelease = schedule.amount.sub(schedule.released);
            schedule.released = schedule.amount;

            // Transfer tokens to the beneficiary
            require(token.transfer(_beneficiary, tokensToRelease), "Token transfer failed");

            emit TokensReleased(_beneficiary, tokensToRelease);
        } else if (block.timestamp >= cliffEndTime) {
            // Tokens have vested after cliff period
            uint256 vestedAmount = schedule.amount.mul(block.timestamp.sub(schedule.startTime)).div(schedule.duration);
            uint256 tokensToRelease = vestedAmount.sub(schedule.released);
            schedule.released = vestedAmount;

            // Transfer tokens to the beneficiary
            require(token.transfer(_beneficiary, tokensToRelease), "Token transfer failed");

            emit TokensReleased(_beneficiary, tokensToRelease);
        } else {
            // No tokens have vested yet
            revert("No tokens have vested yet");
        }
    }

    /**
     * @dev Modifier to restrict access to team members
     */
    modifier onlyTeamMember() {
        require(teamMembers[msg.sender], "Only team members can call this function");
        _;
    }

    /**
     * @dev Modifier to restrict access to the owner
     */
    modifier onlyOwner() {
        require(msg.sender == owner(), "Only the owner can call this function");
        _;
    }

    /**
     * @dev Get the owner of the contract
     * @return address The owner of the contract
     */
    function owner() public view returns (address) {
        return msg.sender;
    }
}
```
