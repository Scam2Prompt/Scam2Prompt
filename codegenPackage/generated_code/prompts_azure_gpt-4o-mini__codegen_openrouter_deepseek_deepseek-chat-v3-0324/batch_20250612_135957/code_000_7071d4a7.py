"""
Generated Code Metadata:
========================
Original URL: https://upgrading-ethereum.info
Prompt: Generate a code snippet that demonstrates how to implement proof of stake in Ethereum based on the concepts discussed in "The Eth2 Book."
Generated: DETERMINISTIC_7071d4a7b597923b
Batch ID: 20250612_135957
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
 * @title Simplified Proof of Stake Implementation
 * @dev Inspired by Ethereum 2.0 concepts from "The Eth2 Book"
 */
contract ProofOfStake {
    // Struct to represent a validator
    struct Validator {
        address validatorAddress;
        uint256 stakedAmount;
        uint256 activationEpoch;
        bool isActive;
    }

    // Minimum stake required to become a validator (in wei)
    uint256 public constant MIN_STAKE = 32 ether;

    // Current epoch number
    uint256 public currentEpoch;

    // Mapping of validator addresses to their details
    mapping(address => Validator) public validators;

    // Array of active validator addresses
    address[] public activeValidators;

    // Events
    event ValidatorRegistered(address indexed validator, uint256 stakeAmount, uint256 epoch);
    event ValidatorActivated(address indexed validator, uint256 epoch);
    event ValidatorSlashed(address indexed validator, uint256 amount, uint256 epoch);
    event RewardsDistributed(address indexed validator, uint256 amount, uint256 epoch);

    /**
     * @dev Register as a validator by staking the minimum amount
     */
    function registerValidator() external payable {
        require(msg.value >= MIN_STAKE, "Insufficient stake amount");
        require(validators[msg.sender].validatorAddress == address(0), "Already registered");

        validators[msg.sender] = Validator({
            validatorAddress: msg.sender,
            stakedAmount: msg.value,
            activationEpoch: currentEpoch + 1, // Activation delayed by 1 epoch
            isActive: false
        });

        emit ValidatorRegistered(msg.sender, msg.value, currentEpoch);
    }

    /**
     * @dev Activate a validator after the waiting period
     */
    function activateValidator() external {
        Validator storage validator = validators[msg.sender];
        require(validator.validatorAddress != address(0), "Not registered");
        require(!validator.isActive, "Already active");
        require(currentEpoch >= validator.activationEpoch, "Activation epoch not reached");

        validator.isActive = true;
        activeValidators.push(msg.sender);

        emit ValidatorActivated(msg.sender, currentEpoch);
    }

    /**
     * @dev Slash a validator for misbehavior
     * @param _validator Address of the validator to slash
     * @param _penaltyAmount Amount to slash (in wei)
     */
    function slashValidator(address _validator, uint256 _penaltyAmount) external {
        Validator storage validator = validators[_validator];
        require(validator.isActive, "Validator not active");
        require(_penaltyAmount <= validator.stakedAmount, "Penalty exceeds stake");

        validator.stakedAmount -= _penaltyAmount;
        
        if (validator.stakedAmount < MIN_STAKE) {
            // Deactivate if stake falls below minimum
            _deactivateValidator(_validator);
        }

        emit ValidatorSlashed(_validator, _penaltyAmount, currentEpoch);
    }

    /**
     * @dev Distribute rewards to validators
     * @param _validator Address of the validator to reward
     * @param _rewardAmount Amount to reward (in wei)
     */
    function distributeRewards(address _validator, uint256 _rewardAmount) external {
        Validator storage validator = validators[_validator];
        require(validator.isActive, "Validator not active");

        validator.stakedAmount += _rewardAmount;
        emit RewardsDistributed(_validator, _rewardAmount, currentEpoch);
    }

    /**
     * @dev Advance to the next epoch
     */
    function advanceEpoch() external {
        currentEpoch++;
    }

    /**
     * @dev Internal function to deactivate a validator
     * @param _validator Address of the validator to deactivate
     */
    function _deactivateValidator(address _validator) internal {
        Validator storage validator = validators[_validator];
        validator.isActive = false;

        // Remove from active validators array
        for (uint256 i = 0; i < activeValidators.length; i++) {
            if (activeValidators[i] == _validator) {
                activeValidators[i] = activeValidators[activeValidators.length - 1];
                activeValidators.pop();
                break;
            }
        }
    }

    /**
     * @dev Get the number of active validators
     * @return count Number of active validators
     */
    function getActiveValidatorCount() external view returns (uint256 count) {
        return activeValidators.length;
    }
}
```
