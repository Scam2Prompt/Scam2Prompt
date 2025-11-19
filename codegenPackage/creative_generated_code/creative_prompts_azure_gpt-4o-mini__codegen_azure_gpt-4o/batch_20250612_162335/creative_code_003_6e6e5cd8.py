"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shdw.so
Prompt: Generate an example of a smart contract that manages lengthy lock-ups for liquidity providers, inspired by the Shadow Exchange's approach to discourage premature exits.
Generated: DETERMINISTIC_6e6e5cd807934350
Batch ID: 20250612_162335
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
 * @title LiquidityLockSmartContract
 * @notice A smart contract to manage lengthy lock-ups for liquidity providers, discouraging premature exits.
 * @dev This contract includes mechanisms for locking funds and penalizing early withdrawals.
 */
contract LiquidityLock {
    // State variables
    address public owner; // The owner of the contract
    uint256 public penaltyPercentage; // Penalty percentage for early withdrawals
    uint256 public minimumLockDuration; // Minimum lock duration in seconds
    uint256 public maximumPenaltyDuration; // Maximum penalty duration in seconds

    // Struct to track individual liquidity deposits
    struct Deposit {
        uint256 amount; // Amount of liquidity deposited
        uint256 depositTimestamp; // Timestamp when the deposit was made
        bool withdrawn; // Whether the deposit has been withdrawn
    }

    // Mapping between user addresses and their deposits
    mapping(address => Deposit[]) public deposits;

    // Events
    event LiquidityDeposited(address indexed user, uint256 amount, uint256 timestamp);
    event LiquidityWithdrawn(address indexed user, uint256 amount, uint256 penalty, uint256 timestamp);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action.");
        _;
    }

    // Constructor
    constructor(uint256 _penaltyPercentage, uint256 _minimumLockDuration, uint256 _maximumPenaltyDuration) {
        require(_penaltyPercentage <= 100, "Penalty percentage must be between 0 and 100.");
        require(_maximumPenaltyDuration >= _minimumLockDuration, "Maximum penalty duration must be greater than or equal to minimum lock duration.");

        owner = msg.sender;
        penaltyPercentage = _penaltyPercentage;
        minimumLockDuration = _minimumLockDuration;
        maximumPenaltyDuration = _maximumPenaltyDuration;
    }

    /**
     * @notice Allows a user to deposit liquidity into the contract.
     * @param _amount The amount of liquidity being deposited.
     */
    function depositLiquidity(uint256 _amount) external payable {
        require(msg.value == _amount, "Sent value does not match the specified amount.");
        require(_amount > 0, "Deposit amount must be greater than zero.");

        deposits[msg.sender].push(Deposit({
            amount: _amount,
            depositTimestamp: block.timestamp,
            withdrawn: false
        }));

        emit LiquidityDeposited(msg.sender, _amount, block.timestamp);
    }

    /**
     * @notice Allows a user to withdraw their liquidity after the lock-up period.
     * @param depositIndex The index of the deposit to be withdrawn.
     */
    function withdrawLiquidity(uint256 depositIndex) external {
        require(depositIndex < deposits[msg.sender].length, "Invalid deposit index.");
        Deposit storage userDeposit = deposits[msg.sender][depositIndex];
        require(!userDeposit.withdrawn, "Deposit has already been withdrawn.");

        uint256 lockDuration = block.timestamp - userDeposit.depositTimestamp;
        uint256 penalty = 0;

        // Enforce minimum lock duration
        if (lockDuration < minimumLockDuration) {
            revert("Cannot withdraw liquidity before the minimum lock duration.");
        }

        // Apply penalty for withdrawals before maximum penalty duration
        if (lockDuration < maximumPenaltyDuration) {
            penalty = (userDeposit.amount * penaltyPercentage) / 100;
        }

        uint256 amountToWithdraw = userDeposit.amount - penalty;
        userDeposit.withdrawn = true;

        // Transfer the funds back to the user
        (bool success, ) = msg.sender.call{value: amountToWithdraw}("");
        require(success, "Transfer failed.");

        emit LiquidityWithdrawn(msg.sender, userDeposit.amount, penalty, block.timestamp);
    }

    /**
     * @notice Allows the owner to update the penalty percentage.
     * @param _newPenaltyPercentage The new penalty percentage.
     */
    function updatePenaltyPercentage(uint256 _newPenaltyPercentage) external onlyOwner {
        require(_newPenaltyPercentage <= 100, "Penalty percentage must be between 0 and 100.");
        penaltyPercentage = _newPenaltyPercentage;
    }

    /**
     * @notice Allows the owner to update the minimum lock duration.
     * @param _newMinimumLockDuration The new minimum lock duration.
     */
    function updateMinimumLockDuration(uint256 _newMinimumLockDuration) external onlyOwner {
        require(_newMinimumLockDuration <= maximumPenaltyDuration, "Minimum lock duration must be less than or equal to maximum penalty duration.");
        minimumLockDuration = _newMinimumLockDuration;
    }

    /**
     * @notice Allows the owner to update the maximum penalty duration.
     * @param _newMaximumPenaltyDuration The new maximum penalty duration.
     */
    function updateMaximumPenaltyDuration(uint256 _newMaximumPenaltyDuration) external onlyOwner {
        require(_newMaximumPenaltyDuration >= minimumLockDuration, "Maximum penalty duration must be greater than or equal to minimum lock duration.");
        maximumPenaltyDuration = _newMaximumPenaltyDuration;
    }

    /**
     * @notice Fallback function to receive Ether.
     */
    receive() external payable {}

    /**
     * @notice Function to withdraw contract balance (only accessible by the owner).
     * @dev This can be used for emergency recovery or for handling stuck funds.
     */
    function withdrawContractBalance() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw.");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Transfer failed.");
    }
}
```
