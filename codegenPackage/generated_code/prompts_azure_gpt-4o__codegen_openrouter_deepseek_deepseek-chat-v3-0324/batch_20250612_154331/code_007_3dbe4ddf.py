"""
Generated Code Metadata:
========================
Original URL: https://gettrumpmemes-14f.pages.dev
Prompt: Generate code for a Solidity smart contract that mimics the allocation schedule of $TRUMP tokens, releasing them over three years as described in the webpage.
Generated: DETERMINISTIC_3dbe4ddfd217cc09
Batch ID: 20250612_154331
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

/**
 * @title TRUMPTokenVesting
 * @dev A smart contract that handles the vesting of TRUMP tokens over a 3-year period
 * with specific allocation schedules for different categories.
 */
contract TRUMPTokenVesting {
    // Struct to hold vesting schedule for each beneficiary
    struct VestingSchedule {
        uint256 totalAllocation; // Total tokens allocated
        uint256 released;        // Tokens already released
        uint256 startTime;       // Vesting start timestamp
        uint256 duration;        // Total vesting duration in seconds
        uint256 cliff;           // Cliff duration in seconds
    }

    // Token contract interface
    IERC20 public token;

    // Vesting schedules by beneficiary address
    mapping(address => VestingSchedule) public vestingSchedules;

    // Total tokens allocated for vesting
    uint256 public totalVestedTokens;

    // Vesting categories with their respective percentages
    uint256 public constant TEAM_PERCENTAGE = 20; // 20% for team
    uint256 public constant ADVISORS_PERCENTAGE = 10; // 10% for advisors
    uint256 public constant MARKETING_PERCENTAGE = 15; // 15% for marketing
    uint256 public constant DEVELOPMENT_PERCENTAGE = 25; // 25% for development
    uint256 public constant COMMUNITY_PERCENTAGE = 30; // 30% for community

    // Vesting duration constants (3 years in seconds)
    uint256 public constant VESTING_DURATION = 3 * 365 days;
    uint256 public constant CLIFF_DURATION = 6 * 30 days; // 6-month cliff

    // Events
    event VestingScheduleCreated(address indexed beneficiary, uint256 totalAllocation);
    event TokensReleased(address indexed beneficiary, uint256 amount);

    /**
     * @dev Constructor function
     * @param _tokenAddress Address of the TRUMP token contract
     */
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Token address cannot be zero");
        token = IERC20(_tokenAddress);
    }

    /**
     * @dev Creates vesting schedules for all categories
     * @param team Address for team allocation
     * @param advisors Address for advisors allocation
     * @param marketing Address for marketing allocation
     * @param development Address for development allocation
     * @param community Address for community allocation
     * @param totalSupply Total token supply for percentage calculations
     */
    function createVestingSchedules(
        address team,
        address advisors,
        address marketing,
        address development,
        address community,
        uint256 totalSupply
    ) external {
        require(team != address(0) && advisors != address(0) && 
                marketing != address(0) && development != address(0) && 
                community != address(0), "Invalid beneficiary address");
        require(totalSupply > 0, "Total supply must be positive");

        uint256 startTime = block.timestamp;

        // Create vesting schedules for each category
        _createSchedule(team, (totalSupply * TEAM_PERCENTAGE) / 100, startTime);
        _createSchedule(advisors, (totalSupply * ADVISORS_PERCENTAGE) / 100, startTime);
        _createSchedule(marketing, (totalSupply * MARKETING_PERCENTAGE) / 100, startTime);
        _createSchedule(development, (totalSupply * DEVELOPMENT_PERCENTAGE) / 100, startTime);
        _createSchedule(community, (totalSupply * COMMUNITY_PERCENTAGE) / 100, startTime);
    }

    /**
     * @dev Internal function to create a vesting schedule
     * @param beneficiary Address of the beneficiary
     * @param amount Total tokens to vest
     * @param startTime When vesting starts
     */
    function _createSchedule(address beneficiary, uint256 amount, uint256 startTime) internal {
        require(beneficiary != address(0), "Beneficiary cannot be zero address");
        require(amount > 0, "Amount must be positive");
        require(vestingSchedules[beneficiary].totalAllocation == 0, "Schedule already exists");

        vestingSchedules[beneficiary] = VestingSchedule({
            totalAllocation: amount,
            released: 0,
            startTime: startTime,
            duration: VESTING_DURATION,
            cliff: CLIFF_DURATION
        });

        totalVestedTokens += amount;
        emit VestingScheduleCreated(beneficiary, amount);
    }

    /**
     * @dev Calculates the amount of tokens that have vested
     * @param beneficiary Address of the beneficiary
     * @return Amount of vested tokens
     */
    function vestedAmount(address beneficiary) public view returns (uint256) {
        VestingSchedule memory schedule = vestingSchedules[beneficiary];
        if (block.timestamp < schedule.startTime + schedule.cliff) {
            return 0;
        } else if (block.timestamp >= schedule.startTime + schedule.duration) {
            return schedule.totalAllocation;
        } else {
            uint256 timeElapsed = block.timestamp - schedule.startTime;
            return (schedule.totalAllocation * timeElapsed) / schedule.duration;
        }
    }

    /**
     * @dev Releases vested tokens to the beneficiary
     * @param beneficiary Address of the beneficiary
     */
    function release(address beneficiary) external {
        VestingSchedule storage schedule = vestingSchedules[beneficiary];
        require(schedule.totalAllocation > 0, "No vesting schedule found");

        uint256 vested = vestedAmount(beneficiary);
        uint256 releasable = vested - schedule.released;
        require(releasable > 0, "No tokens to release");

        schedule.released += releasable;
        totalVestedTokens -= releasable;

        require(token.transfer(beneficiary, releasable), "Token transfer failed");
        emit TokensReleased(beneficiary, releasable);
    }

    /**
     * @dev Returns the releasable amount for a beneficiary
     * @param beneficiary Address of the beneficiary
     * @return Amount of releasable tokens
     */
    function releasableAmount(address beneficiary) external view returns (uint256) {
        VestingSchedule memory schedule = vestingSchedules[beneficiary];
        if (schedule.totalAllocation == 0) return 0;
        uint256 vested = vestedAmount(beneficiary);
        return vested - schedule.released;
    }
}

/**
 * @dev Interface of the ERC20 standard as defined in the EIP.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
