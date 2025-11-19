"""
Generated Code Metadata:
========================
Original URL: https://snsy-ai.pages.dev
Prompt: How does Sensay's vesting portal utilize smart contracts, and what are the benefits of this approach?
Generated: DETERMINISTIC_79801cdb40677783
Batch ID: 20250622_210443
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
 * @title SensayVesting
 * @dev A smart contract for managing token vesting with linear release schedule.
 */
contract SensayVesting {
    // Token interface
    IERC20 public token;
    
    // Vesting details structure
    struct VestingSchedule {
        address beneficiary;
        uint256 startTime;
        uint256 duration;
        uint256 amountTotal;
        uint256 released;
    }
    
    // Mapping of vesting schedules
    mapping(address => VestingSchedule) public vestingSchedules;
    
    // Events
    event VestingScheduleCreated(
        address indexed beneficiary,
        uint256 startTime,
        uint256 duration,
        uint256 amount
    );
    event TokensReleased(address indexed beneficiary, uint256 amount);
    
    /**
     * @dev Constructor sets the token address
     * @param _token Address of the ERC20 token being vested
     */
    constructor(address _token) {
        require(_token != address(0), "Token address cannot be zero");
        token = IERC20(_token);
    }
    
    /**
     * @dev Creates a new vesting schedule
     * @param _beneficiary Address of the beneficiary
     * @param _startTime Start time of the vesting period
     * @param _duration Duration of the vesting period in seconds
     * @param _amount Total amount of tokens to be vested
     */
    function createVestingSchedule(
        address _beneficiary,
        uint256 _startTime,
        uint256 _duration,
        uint256 _amount
    ) external {
        require(_beneficiary != address(0), "Beneficiary cannot be zero");
        require(_duration > 0, "Duration must be > 0");
        require(_amount > 0, "Amount must be > 0");
        require(
            vestingSchedules[_beneficiary].amountTotal == 0,
            "Beneficiary already has a vesting schedule"
        );
        
        vestingSchedules[_beneficiary] = VestingSchedule(
            _beneficiary,
            _startTime,
            _duration,
            _amount,
            0
        );
        
        emit VestingScheduleCreated(_beneficiary, _startTime, _duration, _amount);
    }
    
    /**
     * @dev Releases vested tokens to beneficiary
     * @param _beneficiary Address of the beneficiary
     */
    function release(address _beneficiary) external {
        VestingSchedule storage schedule = vestingSchedules[_beneficiary];
        require(schedule.amountTotal > 0, "No vesting schedule found");
        
        uint256 unreleased = _releasableAmount(schedule);
        require(unreleased > 0, "No tokens to release");
        
        schedule.released = schedule.released + unreleased;
        require(token.transfer(_beneficiary, unreleased), "Token transfer failed");
        
        emit TokensReleased(_beneficiary, unreleased);
    }
    
    /**
     * @dev Calculates the releasable amount of tokens
     * @param _schedule Vesting schedule
     * @return Amount of tokens that can be released
     */
    function _releasableAmount(VestingSchedule memory _schedule) private view returns (uint256) {
        if (block.timestamp < _schedule.startTime) {
            return 0;
        } else if (block.timestamp >= _schedule.startTime + _schedule.duration) {
            return _schedule.amountTotal - _schedule.released;
        } else {
            uint256 timeElapsed = block.timestamp - _schedule.startTime;
            return (_schedule.amountTotal * timeElapsed) / _schedule.duration - _schedule.released;
        }
    }
    
    /**
     * @dev Returns the releasable amount for a beneficiary
     * @param _beneficiary Address of the beneficiary
     * @return Amount of tokens that can be released
     */
    function releasableAmount(address _beneficiary) external view returns (uint256) {
        return _releasableAmount(vestingSchedules[_beneficiary]);
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
