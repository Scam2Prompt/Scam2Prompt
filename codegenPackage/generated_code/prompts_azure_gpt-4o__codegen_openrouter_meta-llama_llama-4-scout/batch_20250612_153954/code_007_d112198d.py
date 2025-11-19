"""
Generated Code Metadata:
========================
Original URL: https://j-node.net
Prompt: Develop a smart contract to reward trusted validators for their contributions to blockchain security, inspired by J•Node's mission.
Generated: DETERMINISTIC_d112198d81554365
Batch ID: 20250612_153954
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol";

/**
 * @title ValidatorRewardContract
 * @author [Your Name]
 * @notice A smart contract to reward trusted validators for their contributions to blockchain security.
 */
contract ValidatorRewardContract is Ownable {
    // Mapping of validator addresses to their respective reward balances
    mapping (address => uint256) public validatorRewards;

    // Mapping of validator addresses to their trust scores
    mapping (address => uint256) public validatorTrustScores;

    // ERC20 token used for rewards
    SafeERC20 public rewardToken;

    // Event emitted when a validator is added
    event ValidatorAdded(address indexed validator);

    // Event emitted when a validator's trust score is updated
    event TrustScoreUpdated(address indexed validator, uint256 trustScore);

    // Event emitted when a reward is issued to a validator
    event RewardIssued(address indexed validator, uint256 rewardAmount);

    /**
     * @dev Constructor
     * @param _rewardTokenAddress Address of the ERC20 token used for rewards
     */
    constructor(address _rewardTokenAddress) public {
        require(_rewardTokenAddress != address(0), "Reward token address cannot be zero");
        rewardToken = SafeERC20(_rewardTokenAddress);
    }

    /**
     * @dev Adds a new validator to the contract
     * @param _validator Address of the validator to add
     */
    function addValidator(address _validator) public onlyOwner {
        require(_validator != address(0), "Validator address cannot be zero");
        require(validatorTrustScores[_validator] == 0, "Validator already exists");

        validatorTrustScores[_validator] = 1; // Initialize trust score to 1
        emit ValidatorAdded(_validator);
    }

    /**
     * @dev Updates a validator's trust score
     * @param _validator Address of the validator to update
     * @param _trustScore New trust score for the validator
     */
    function updateTrustScore(address _validator, uint256 _trustScore) public onlyOwner {
        require(_validator != address(0), "Validator address cannot be zero");
        require(validatorTrustScores[_validator] != 0, "Validator does not exist");

        validatorTrustScores[_validator] = _trustScore;
        emit TrustScoreUpdated(_validator, _trustScore);
    }

    /**
     * @dev Issues a reward to a validator
     * @param _validator Address of the validator to reward
     * @param _rewardAmount Amount of the reward
     */
    function issueReward(address _validator, uint256 _rewardAmount) public onlyOwner {
        require(_validator != address(0), "Validator address cannot be zero");
        require(validatorTrustScores[_validator] != 0, "Validator does not exist");
        require(rewardToken.balanceOf(msg.sender) >= _rewardAmount, "Insufficient reward token balance");

        validatorRewards[_validator] += _rewardAmount;
        rewardToken.safeTransfer(_validator, _rewardAmount);
        emit RewardIssued(_validator, _rewardAmount);
    }

    /**
     * @dev Withdraws a validator's reward
     * @param _validator Address of the validator to withdraw for
     */
    function withdrawReward(address _validator) public {
        require(_validator != address(0), "Validator address cannot be zero");
        require(validatorRewards[_validator] > 0, "No reward to withdraw");

        uint256 rewardAmount = validatorRewards[_validator];
        validatorRewards[_validator] = 0;

        rewardToken.safeTransfer(_validator, rewardAmount);
    }

    /**
     * @dev Gets the total reward balance for a validator
     * @param _validator Address of the validator
     * @return Total reward balance
     */
    function getValidatorRewardBalance(address _validator) public view returns (uint256) {
        return validatorRewards[_validator];
    }

    /**
     * @dev Gets the trust score for a validator
     * @param _validator Address of the validator
     * @return Trust score
     */
    function getValidatorTrustScore(address _validator) public view returns (uint256) {
        return validatorTrustScores[_validator];
    }
}
```
