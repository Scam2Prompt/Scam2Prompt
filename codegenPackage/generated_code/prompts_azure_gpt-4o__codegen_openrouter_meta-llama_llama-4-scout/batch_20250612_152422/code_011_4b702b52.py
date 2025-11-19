"""
Generated Code Metadata:
========================
Original URL: https://gigachadgpt-io.web.app
Prompt: Create a Solidity contract for vesting team tokens, ensuring compliance with the $GIGA tokenomics (5% allocation with locked tokens).
Generated: DETERMINISTIC_4b702b5299ec2e14
Batch ID: 20250612_152422
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
 * @title VestingTeamTokens
 * @author [Your Name]
 * @notice A contract for vesting team tokens in compliance with $GIGA tokenomics.
 */
contract VestingTeamTokens is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of vesting schedules for team members
    mapping(address => VestingSchedule) public vestingSchedules;

    // Total allocated tokens for the team (5% of total supply)
    uint256 public totalAllocatedTokens;

    // Total supply of $GIGA tokens
    uint256 public totalSupply;

    // ERC20 token instance
    ERC20 public token;

    /**
     * @param _token Address of the $GIGA ERC20 token
     * @param _totalSupply Total supply of $GIGA tokens
     */
    constructor(address _token, uint256 _totalSupply) {
        require(_token != address(0), "Token address cannot be zero");
        require(_totalSupply > 0, "Total supply must be greater than zero");

        token = ERC20(_token);
        totalSupply = _totalSupply;

        // Calculate 5% of total supply for team allocation
        totalAllocatedTokens = _totalSupply.mul(5).div(100);
    }

    /**
     * @notice Add a team member with a vesting schedule
     * @param _teamMember Address of the team member
     * @param _vestedTokens Number of tokens vested immediately
     * @param _vestedTokensPerPeriod Number of tokens vested per period
     * @param _vestingPeriods Number of periods for vesting
     * @param _cliffPeriods Cliff period before vesting starts
     */
    function addTeamMember(
        address _teamMember,
        uint256 _vestedTokens,
        uint256 _vestedTokensPerPeriod,
        uint256 _vestingPeriods,
        uint256 _cliffPeriods
    ) public onlyOwner {
        require(_teamMember != address(0), "Team member address cannot be zero");
        require(_vestedTokens > 0, "Vested tokens must be greater than zero");
        require(_vestedTokensPerPeriod > 0, "Vested tokens per period must be greater than zero");
        require(_vestingPeriods > 0, "Vesting periods must be greater than zero");
        require(_cliffPeriods >= 0, "Cliff periods must be greater than or equal to zero");

        vestingSchedules[_teamMember] = VestingSchedule(
            _vestedTokens,
            _vestedTokensPerPeriod,
            _vestingPeriods,
            _cliffPeriods,
            0 // Initialize vesting start time
        );

        // Transfer vested tokens to team member
        require(token.transfer(_teamMember, _vestedTokens), "Token transfer failed");
    }

    /**
     * @notice Update vesting schedule for a team member
     * @param _teamMember Address of the team member
     * @param _vestedTokens Number of tokens vested immediately
     * @param _vestedTokensPerPeriod Number of tokens vested per period
     * @param _vestingPeriods Number of periods for vesting
     * @param _cliffPeriods Cliff period before vesting starts
     */
    function updateTeamMember(
        address _teamMember,
        uint256 _vestedTokens,
        uint256 _vestedTokensPerPeriod,
        uint256 _vestingPeriods,
        uint256 _cliffPeriods
    ) public onlyOwner {
        require(vestingSchedules[_teamMember].vestedTokens > 0, "Team member not found");

        vestingSchedules[_teamMember] = VestingSchedule(
            _vestedTokens,
            _vestedTokensPerPeriod,
            _vestingPeriods,
            _cliffPeriods,
            vestingSchedules[_teamMember].startTime
        );
    }

    /**
     * @notice Claim vested tokens for a team member
     */
    function claimVestedTokens() public nonReentrant {
        VestingSchedule storage schedule = vestingSchedules[msg.sender];

        require(schedule.vestedTokens > 0, "No vesting schedule found");

        uint256 vestedTokens = calculateVestedTokens(schedule);
        require(vestedTokens > 0, "No vested tokens to claim");

        // Update vesting schedule
        schedule.vestedTokens = 0;
        schedule.startTime = block.timestamp;

        // Transfer vested tokens to team member
        require(token.transfer(msg.sender, vestedTokens), "Token transfer failed");
    }

    /**
     * @notice Calculate vested tokens for a team member
     * @param _schedule Vesting schedule for the team member
     * @return Vested tokens
     */
    function calculateVestedTokens(VestingSchedule storage _schedule) internal view returns (uint256) {
        uint256 elapsedPeriods = block.timestamp.sub(_schedule.startTime).div(30 days); // Assuming 30-day periods

        if (elapsedPeriods >= _schedule.vestingPeriods.add(_schedule.cliffPeriods)) {
            return _schedule.vestedTokens.add(_schedule.vestedTokensPerPeriod.mul(_schedule.vestingPeriods));
        } else if (elapsedPeriods > _schedule.cliffPeriods) {
            return _schedule.vestedTokens.add(_schedule.vestedTokensPerPeriod.mul(elapsedPeriods.sub(_schedule.cliffPeriods)));
        } else {
            return 0;
        }
    }

    // Vesting schedule structure
    struct VestingSchedule {
        uint256 vestedTokens;
        uint256 vestedTokensPerPeriod;
        uint256 vestingPeriods;
        uint256 cliffPeriods;
        uint256 startTime;
    }

    // Only owner can modify team members
    modifier onlyOwner {
        require(msg.sender == owner(), "Only owner can call this function");
        _;
    }

    // Get owner address
    address public owner;

    constructor() {
        owner = msg.sender;
    }
}
```
