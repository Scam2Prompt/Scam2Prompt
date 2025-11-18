"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://earnm-boxes.pages.dev
Prompt: Write a smart contract in Solidity that implements the vesting and distribution mechanics described in the $EARNM 'Fractal Box' protocol, ensuring a 12-month holding period and automatic redistribution of forfeited assets.
Generated: DETERMINISTIC_7c337ca1621ea956
Batch ID: 20250612_150130
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
 * @title FractalBoxVesting
 * @dev Implements vesting and redistribution mechanics for $EARNM tokens.
 */
contract FractalBoxVesting {
    // Structure for a beneficiary's vesting schedule
    struct VestingSchedule {
        uint256 amount;        // Total amount of tokens vested
        uint256 startTime;     // Timestamp when vesting starts
        uint256 cliffTime;     // Timestamp when vesting cliff ends
        uint256 duration;      // Total vesting duration
        bool revoked;          // Status indicating if vesting is revoked
    }

    address public tokenAddress; // Address of the token contract
    address public owner;        // Owner of the contract

    mapping(address => VestingSchedule) public vestingSchedules; // Beneficiaries' vesting schedules
    mapping(address => uint256) public forfeitedBalance;         // Forfeited balances for redistribution

    uint256 public totalForfeited; // Total forfeited tokens

    event VestingCreated(address indexed beneficiary, uint256 amount, uint256 startTime, uint256 cliffTime, uint256 duration);
    event VestingRevoked(address indexed beneficiary, uint256 forfeitedAmount);
    event ForfeitedRedistributed(address indexed recipient, uint256 amount);

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier validBeneficiary(address beneficiary) {
        require(beneficiary != address(0), "Invalid beneficiary address");
        _;
    }

    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        tokenAddress = _tokenAddress;
        owner = msg.sender;
    }

    /**
     * @dev Creates a vesting schedule for a beneficiary.
     * @param beneficiary Address of the beneficiary.
     * @param amount Amount of tokens to vest.
     * @param cliffInMonths Cliff period in months.
     * @param durationInMonths Total vesting duration in months.
     */
    function createVestingSchedule(
        address beneficiary,
        uint256 amount,
        uint256 cliffInMonths,
        uint256 durationInMonths
    ) external onlyOwner validBeneficiary(beneficiary) {
        require(amount > 0, "Amount must be greater than zero");
        require(durationInMonths > 0, "Duration must be greater than zero");
        require(cliffInMonths <= durationInMonths, "Cliff cannot exceed duration");

        VestingSchedule storage schedule = vestingSchedules[beneficiary];
        require(schedule.amount == 0, "Vesting schedule already exists");

        uint256 startTime = block.timestamp;
        uint256 cliffTime = startTime + (cliffInMonths * 30 days);
        uint256 duration = durationInMonths * 30 days;

        vestingSchedules[beneficiary] = VestingSchedule({
            amount: amount,
            startTime: startTime,
            cliffTime: cliffTime,
            duration: duration,
            revoked: false
        });

        emit VestingCreated(beneficiary, amount, startTime, cliffTime, duration);
    }

    /**
     * @dev Revokes the vesting schedule of a beneficiary, forfeiting remaining tokens.
     * @param beneficiary Address of the beneficiary.
     */
    function revokeVesting(address beneficiary) external onlyOwner validBeneficiary(beneficiary) {
        VestingSchedule storage schedule = vestingSchedules[beneficiary];
        require(schedule.amount > 0, "Vesting schedule does not exist");
        require(!schedule.revoked, "Vesting already revoked");

        uint256 elapsed = block.timestamp - schedule.startTime;
        uint256 vested = (schedule.amount * elapsed) / schedule.duration;

        uint256 forfeitedAmount = schedule.amount - vested;
        schedule.revoked = true;
        forfeitedBalance[beneficiary] += forfeitedAmount;
        totalForfeited += forfeitedAmount;

        emit VestingRevoked(beneficiary, forfeitedAmount);
    }

    /**
     * @dev Redistributes forfeited tokens to a specific recipient.
     * @param recipient Address of the recipient.
     * @param amount Amount of tokens to redistribute.
     */
    function redistributeForfeited(address recipient, uint256 amount) external onlyOwner validBeneficiary(recipient) {
        require(totalForfeited >= amount, "Insufficient forfeited balance");

        totalForfeited -= amount;

        // Assuming the token contract implements a transfer function.
        require(ERC20(tokenAddress).transfer(recipient, amount), "Token transfer failed");

        emit ForfeitedRedistributed(recipient, amount);
    }

    /**
     * @dev Withdraws unallocated tokens back to the owner.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawUnallocatedTokens(uint256 amount) external onlyOwner {
        require(ERC20(tokenAddress).transfer(owner, amount), "Token transfer failed");
    }
}

// Interface for ERC20 token interactions
interface ERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
