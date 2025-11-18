"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethereumcv.io
Prompt: Write a Solidity function to penalize block validators who act maliciously on the Ethereum Classic Vision blockchain by forfeiting their staked deposit and validator status.
Generated: DETERMINISTIC_bf49cda936d7a3ad
Batch ID: 20250612_151847
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
 * @title ValidatorPenalty
 * @dev Contract to manage penalization of malicious block validators by forfeiting their stake and validator status.
 */
contract ValidatorPenalty {
    // Structure to store validator details
    struct Validator {
        uint256 stakedAmount; // Amount staked by the validator
        bool isActive;        // Validator status (active/inactive)
    }

    // Mapping of validators to their addresses
    mapping(address => Validator) public validators;

    // Address of the contract owner (typically the governance entity)
    address public owner;

    // Event emitted when a validator is penalized
    event ValidatorPenalized(address indexed validator, uint256 forfeitedAmount);

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to set the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to register a validator with an initial stake.
     * @param validator Address of the validator.
     * @param stake Amount staked by the validator.
     */
    function registerValidator(address validator, uint256 stake) external onlyOwner {
        require(validator != address(0), "Invalid validator address");
        require(stake > 0, "Stake must be greater than zero");
        require(!validators[validator].isActive, "Validator already registered");

        validators[validator] = Validator({
            stakedAmount: stake,
            isActive: true
        });
    }

    /**
     * @dev Penalize a malicious validator by forfeiting their stake and deactivating their status.
     * @param validator Address of the malicious validator.
     */
    function penalizeValidator(address validator) external onlyOwner {
        require(validator != address(0), "Invalid validator address");
        Validator storage validatorData = validators[validator];

        require(validatorData.isActive, "Validator is not active");

        uint256 forfeitedAmount = validatorData.stakedAmount;

        // Forfeit the stake
        validatorData.stakedAmount = 0;
        validatorData.isActive = false;

        // Emit an event to record the penalty
        emit ValidatorPenalized(validator, forfeitedAmount);
    }

    /**
     * @dev Function to retrieve the details of a validator.
     * @param validator Address of the validator.
     * @return stakedAmount The amount staked by the validator.
     * @return isActive The active status of the validator.
     */
    function getValidatorDetails(address validator) external view returns (uint256 stakedAmount, bool isActive) {
        Validator memory validatorData = validators[validator];
        return (validatorData.stakedAmount, validatorData.isActive);
    }
}
```
