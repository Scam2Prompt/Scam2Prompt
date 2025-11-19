"""
Generated Code Metadata:
========================
Original URL: https://artyfact-gaming.pages.dev
Prompt: Create a smart contract on Binance Smart Chain (BSC) that mirrors the vesting functionality described on the Artyfact website, including allocation tracking and multi-round claiming.
Generated: DETERMINISTIC_5277ff59b87d1287
Batch ID: 20250612_152526
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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Vesting contract for Artyfact
 * @author [Your Name]
 * @notice This contract manages the vesting of tokens for Artyfact
 */
contract ArtyfactVesting {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of vesting allocations
    mapping(address => Allocation) public allocations;

    // Mapping of claim history
    mapping(address => mapping(uint256 => bool)) public claimHistory;

    // Token being vested
    IERC20 public token;

    // Total vesting rounds
    uint256 public totalRounds;

    // Vesting start time
    uint256 public startTime;

    // Vesting duration
    uint256 public duration;

    // Claiming interval
    uint256 public claimingInterval;

    // Struct to hold allocation details
    struct Allocation {
        uint256 amount;
        uint256 claimed;
        uint256 lastClaim;
    }

    /**
     * @notice Constructor for the vesting contract
     * @param _token Token being vested
     * @param _startTime Vesting start time
     * @param _duration Vesting duration
     * @param _claimingInterval Claiming interval
     * @param _totalRounds Total vesting rounds
     */
    constructor(
        IERC20 _token,
        uint256 _startTime,
        uint256 _duration,
        uint256 _claimingInterval,
        uint256 _totalRounds
    ) {
        require(_startTime > block.timestamp, "Start time must be in the future");
        require(_duration > 0, "Duration must be greater than 0");
        require(_claimingInterval > 0, "Claiming interval must be greater than 0");
        require(_totalRounds > 0, "Total rounds must be greater than 0");

        token = _token;
        startTime = _startTime;
        duration = _duration;
        claimingInterval = _claimingInterval;
        totalRounds = _totalRounds;
    }

    /**
     * @notice Add a new allocation
     * @param _recipient Address of the recipient
     * @param _amount Amount of tokens to vest
     */
    function addAllocation(address _recipient, uint256 _amount) public onlyOwner {
        require(_recipient != address(0), "Recipient address cannot be 0");
        require(_amount > 0, "Amount must be greater than 0");

        allocations[_recipient] = Allocation(_amount, 0, startTime);
    }

    /**
     * @notice Claim vested tokens
     */
    function claim() public {
        require(allocations[msg.sender].amount > 0, "No allocation found");
        require(block.timestamp >= allocations[msg.sender].lastClaim.add(claimingInterval), "Claiming interval not met");

        uint256 vestedAmount = calculateVestedAmount(msg.sender);
        require(vestedAmount > 0, "No vested tokens to claim");

        allocations[msg.sender].claimed = allocations[msg.sender].claimed.add(vestedAmount);
        allocations[msg.sender].lastClaim = block.timestamp;

        token.safeTransfer(msg.sender, vestedAmount);

        // Update claim history
        for (uint256 i = 1; i <= totalRounds; i++) {
            if (block.timestamp >= startTime.add(duration.mul(i).div(totalRounds))) {
                claimHistory[msg.sender][i] = true;
            }
        }
    }

    /**
     * @notice Calculate vested amount for an address
     * @param _address Address to calculate vested amount for
     * @return Vested amount
     */
    function calculateVestedAmount(address _address) internal view returns (uint256) {
        uint256 allocationAmount = allocations[_address].amount;
        uint256 claimedAmount = allocations[_address].claimed;
        uint256 timeElapsed = block.timestamp.sub(allocations[_address].lastClaim);

        // Calculate vested amount based on time elapsed and total duration
        uint256 vestedAmount = allocationAmount.mul(timeElapsed).div(duration);

        // Ensure vested amount does not exceed remaining unclaimed amount
        vestedAmount = vestedAmount.sub(claimedAmount);

        return vestedAmount;
    }

    // Restrict access to only the contract owner
    modifier onlyOwner {
        require(msg.sender == owner(), "Only the owner can call this function");
        _;
    }

    // Get the contract owner
    function owner() public view returns (address) {
        return msg.sender;
    }
}
```
