"""
Generated Code Metadata:
========================
Original URL: https://snsy-ai.pages.dev
Prompt: Generate code to audit a smart contract for a vesting portal, ensuring security and compliance with blockchain standards, inspired by Sensay's implementation.
Generated: DETERMINISTIC_97d4b47db9a1d635
Batch ID: 20250612_152924
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title VestingPortal
 * @dev A secure vesting contract that allows tokens to be vested over time with proper access control
 */
contract VestingPortal is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    struct VestingSchedule {
        uint256 totalAmount;
        uint256 releasedAmount;
        uint256 startTime;
        uint256 duration;
        uint256 cliff;
        bool revoked;
    }

    IERC20 public immutable token;
    mapping(address => VestingSchedule) public vestingSchedules;
    mapping(address => bool) public whitelistedBeneficiaries;

    event VestingCreated(address indexed beneficiary, uint256 amount, uint256 startTime, uint256 duration, uint256 cliff);
    event TokensReleased(address indexed beneficiary, uint256 amount);
    event VestingRevoked(address indexed beneficiary);
    event BeneficiaryWhitelisted(address indexed beneficiary);
    event BeneficiaryRemoved(address indexed beneficiary);

    /**
     * @dev Constructor sets the token to be vested
     * @param _token Address of the ERC20 token contract
     */
    constructor(IERC20 _token) {
        require(address(_token) != address(0), "Token address cannot be zero");
        token = _token;
    }

    /**
     * @dev Modifier to check if beneficiary is whitelisted
     */
    modifier onlyWhitelisted(address _beneficiary) {
        require(whitelistedBeneficiaries[_beneficiary], "Beneficiary not whitelisted");
        _;
    }

    /**
     * @dev Whitelist a beneficiary address
     * @param _beneficiary Address to be whitelisted
     */
    function whitelistBeneficiary(address _beneficiary) external onlyOwner {
        require(_beneficiary != address(0), "Beneficiary address cannot be zero");
        whitelistedBeneficiaries[_beneficiary] = true;
        emit BeneficiaryWhitelisted(_beneficiary);
    }

    /**
     * @dev Remove a beneficiary from whitelist
     * @param _beneficiary Address to be removed
     */
    function removeBeneficiary(address _beneficiary) external onlyOwner {
        require(whitelistedBeneficiaries[_beneficiary], "Beneficiary not in whitelist");
        whitelistedBeneficiaries[_beneficiary] = false;
        emit BeneficiaryRemoved(_beneficiary);
    }

    /**
     * @dev Create a new vesting schedule
     * @param _beneficiary Address of the beneficiary
     * @param _amount Total amount of tokens to be vested
     * @param _startTime Start time of vesting
     * @param _duration Duration of vesting in seconds
     * @param _cliff Cliff period in seconds
     */
    function createVestingSchedule(
        address _beneficiary,
        uint256 _amount,
        uint256 _startTime,
        uint256 _duration,
        uint256 _cliff
    ) external onlyOwner onlyWhitelisted(_beneficiary) {
        require(_beneficiary != address(0), "Beneficiary address cannot be zero");
        require(_amount > 0, "Amount must be greater than zero");
        require(_duration > 0, "Duration must be greater than zero");
        require(_cliff <= _duration, "Cliff must be less than or equal to duration");
        require(vestingSchedules[_beneficiary].totalAmount == 0, "Vesting schedule already exists");

        uint256 balance = token.balanceOf(address(this));
        require(balance >= _amount, "Insufficient token balance");

        vestingSchedules[_beneficiary] = VestingSchedule({
            totalAmount: _amount,
            releasedAmount: 0,
            startTime: _startTime,
            duration: _duration,
            cliff: _cliff,
            revoked: false
        });

        emit VestingCreated(_beneficiary, _amount, _startTime, _duration, _cliff);
    }

    /**
     * @dev Release vested tokens to beneficiary
     */
    function release() external nonReentrant {
        address beneficiary = msg.sender;
        VestingSchedule storage schedule = vestingSchedules[beneficiary];

        require(schedule.totalAmount > 0, "No vesting schedule found");
        require(!schedule.revoked, "Vesting schedule has been revoked");

        uint256 unreleased = _releasableAmount(schedule);
        require(unreleased > 0, "No tokens to release");

        schedule.releasedAmount = schedule.releasedAmount.add(unreleased);
        require(token.transfer(beneficiary, unreleased), "Token transfer failed");

        emit TokensReleased(beneficiary, unreleased);
    }

    /**
     * @dev Revoke vesting schedule and return remaining tokens to owner
     * @param _beneficiary Address of the beneficiary
     */
    function revoke(address _beneficiary) external onlyOwner {
        VestingSchedule storage schedule = vestingSchedules[_beneficiary];
        require(schedule.totalAmount > 0, "No vesting schedule found");
        require(!schedule.revoked, "Vesting already revoked");

        uint256 vestedAmount = _vestedAmount(schedule);
        uint256 unreleased = vestedAmount.sub(schedule.releasedAmount);
        uint256 refund = schedule.totalAmount.sub(vestedAmount);

        schedule.revoked = true;
        schedule.totalAmount = vestedAmount;

        if (unreleased > 0) {
            require(token.transfer(_beneficiary, unreleased), "Token transfer failed");
            emit TokensReleased(_beneficiary, unreleased);
        }

        if (refund > 0) {
            require(token.transfer(owner(), refund), "Token transfer failed");
        }

        emit VestingRevoked(_beneficiary);
    }

    /**
     * @dev Calculate the releasable amount of tokens
     * @param _schedule Vesting schedule to calculate from
     * @return Amount of tokens that can be released
     */
    function _releasableAmount(VestingSchedule memory _schedule) private view returns (uint256) {
        return _vestedAmount(_schedule).sub(_schedule.releasedAmount);
    }

    /**
     * @dev Calculate the vested amount of tokens
     * @param _schedule Vesting schedule to calculate from
     * @return Amount of tokens that have vested
     */
    function _vestedAmount(VestingSchedule memory _schedule) private view returns (uint256) {
        if (block.timestamp < _schedule.startTime.add(_schedule.cliff)) {
            return 0;
        } else if (block.timestamp >= _schedule.startTime.add(_schedule.duration) || _schedule.revoked) {
            return _schedule.totalAmount;
        } else {
            uint256 timeElapsed = block.timestamp.sub(_schedule.startTime);
            return _schedule.totalAmount.mul(timeElapsed).div(_schedule.duration);
        }
    }

    /**
     * @dev Get releasable amount for a beneficiary
     * @param _beneficiary Address of the beneficiary
     * @return Amount of tokens that can be released
     */
    function getReleasableAmount(address _beneficiary) external view returns (uint256) {
        return _releasableAmount(vestingSchedules[_beneficiary]);
    }

    /**
     * @dev Get vested amount for a beneficiary
     * @param _beneficiary Address of the beneficiary
     * @return Amount of tokens that have vested
     */
    function getVestedAmount(address _beneficiary) external view returns (uint256) {
        return _vestedAmount(vestingSchedules[_beneficiary]);
    }
}
```
