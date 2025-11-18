"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://get-trump-gift.pages.dev
Prompt: Write a Solidity smart contract that mimics the allocation and unlocking schedule of "$TRUMP" tokens over three years.
Generated: DETERMINISTIC_e31457dca38a98dc
Batch ID: 20250612_154331
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

/**
 * @title TRUMPTokenVesting
 * @dev A smart contract for managing the allocation and unlocking schedule of "$TRUMP" tokens over three years.
 */
contract TRUMPTokenVesting {
    // The token's details
    string public constant name = "TRUMP Token";
    string public constant symbol = "TRUMP";
    uint8 public constant decimals = 18;

    // Total supply of tokens
    uint256 public constant totalSupply = 1000000 * (10 ** uint256(decimals)); // 1,000,000 tokens

    // Address of the contract owner
    address public owner;

    // Mapping to hold balances
    mapping(address => uint256) private balances;

    // Mapping to track vested tokens
    mapping(address => uint256) private vestedBalances;

    // Struct for managing vesting schedule
    struct VestingSchedule {
        uint256 amount; // Total vested tokens
        uint256 startTime; // Vesting start time
        uint256 endTime; // Vesting end time
        uint256 releasedAmount; // Amount already unlocked
    }

    // Mapping to track vesting schedules per address
    mapping(address => VestingSchedule) private vestingSchedules;

    // Events
    event TokensAllocated(address indexed beneficiary, uint256 amount);
    event TokensReleased(address indexed beneficiary, uint256 amount);

    // Modifier to restrict access to owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can execute this function");
        _;
    }

    // Modifier to check beneficiary's address
    modifier validBeneficiary(address beneficiary) {
        require(beneficiary != address(0), "Invalid beneficiary address");
        _;
    }

    // Constructor
    constructor() {
        owner = msg.sender;
        balances[owner] = totalSupply; // Assign all tokens to the owner initially
    }

    /**
     * @dev Allocate tokens to a beneficiary with a vesting schedule.
     * @param beneficiary Address of the beneficiary
     * @param amount Total tokens to be vested
     * @param startTime Vesting start time (Unix timestamp)
     * @param endTime Vesting end time (Unix timestamp)
     */
    function allocateTokens(
        address beneficiary,
        uint256 amount,
        uint256 startTime,
        uint256 endTime
    ) external onlyOwner validBeneficiary(beneficiary) {
        require(amount > 0, "Amount must be greater than 0");
        require(balances[owner] >= amount, "Insufficient tokens in owner's balance");
        require(startTime < endTime, "Start time must be before end time");

        // Update owner's balance
        balances[owner] -= amount;
        // Add to beneficiary's vested balance
        vestedBalances[beneficiary] += amount;

        // Create vesting schedule
        vestingSchedules[beneficiary] = VestingSchedule({
            amount: amount,
            startTime: startTime,
            endTime: endTime,
            releasedAmount: 0
        });

        emit TokensAllocated(beneficiary, amount);
    }

    /**
     * @dev Unlock tokens for the beneficiary according to the vesting schedule.
     */
    function unlockTokens() external {
        VestingSchedule storage schedule = vestingSchedules[msg.sender];
        require(schedule.amount > 0, "No vesting schedule found");
        require(block.timestamp > schedule.startTime, "Vesting has not started yet");

        // Calculate unlockable tokens
        uint256 unlockable;
        if (block.timestamp >= schedule.endTime) {
            // If vesting period is over, unlock all remaining tokens
            unlockable = schedule.amount - schedule.releasedAmount;
        } else {
            // Calculate the proportion of unlocked tokens
            uint256 duration = schedule.endTime - schedule.startTime;
            uint256 elapsed = block.timestamp - schedule.startTime;
            unlockable = (schedule.amount * elapsed) / duration - schedule.releasedAmount;
        }

        require(unlockable > 0, "No tokens available for unlocking");

        // Update released amount
        schedule.releasedAmount += unlockable;

        // Update beneficiary's balance
        balances[msg.sender] += unlockable;

        emit TokensReleased(msg.sender, unlockable);
    }

    /**
     * @dev View the current balance (unlocked tokens) of an address.
     * @param account Address to query the balance for
     * @return The current balance of the account
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev View the remaining vested balance of an address.
     * @param account Address to query the vested balance for
     * @return The remaining vested balance of the account
     */
    function vestedBalanceOf(address account) external view returns (uint256) {
        return vestedBalances[account];
    }

    /**
     * @dev View the vesting schedule of a beneficiary.
     * @param beneficiary Address to query the vesting schedule for
     * @return Vesting schedule details
     */
    function getVestingSchedule(address beneficiary)
        external
        view
        returns (
            uint256 amount,
            uint256 startTime,
            uint256 endTime,
            uint256 releasedAmount
        )
    {
        VestingSchedule memory schedule = vestingSchedules[beneficiary];
        return (schedule.amount, schedule.startTime, schedule.endTime, schedule.releasedAmount);
    }
}
```
