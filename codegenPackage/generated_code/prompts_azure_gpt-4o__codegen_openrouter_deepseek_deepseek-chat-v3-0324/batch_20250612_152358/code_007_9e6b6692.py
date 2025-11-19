"""
Generated Code Metadata:
========================
Original URL: https://shibanft.pages.dev
Prompt: Develop a Solidity smart contract for collaborating with Shibarium's validator nodes and distributing rewards.
Generated: DETERMINISTIC_9e6b6692b1773ff5
Batch ID: 20250612_152358
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract ShibariumValidatorRewards is Ownable, ReentrancyGuard {
    // Struct to store validator information
    struct Validator {
        address validatorAddress;
        uint256 stakedAmount;
        uint256 rewardShare;
        bool isActive;
    }

    // Token used for rewards
    IERC20 public rewardToken;

    // Total staked amount across all validators
    uint256 public totalStaked;

    // Reward distribution interval in seconds
    uint256 public rewardInterval;

    // Last reward distribution timestamp
    uint256 public lastDistributionTime;

    // Validator count
    uint256 public validatorCount;

    // Mapping of validator addresses to their details
    mapping(address => Validator) public validators;

    // Array of active validator addresses
    address[] public activeValidators;

    // Events
    event ValidatorRegistered(address indexed validator, uint256 stakedAmount);
    event ValidatorUnregistered(address indexed validator);
    event RewardsDistributed(uint256 totalRewards);
    event RewardClaimed(address indexed validator, uint256 amount);
    event Staked(address indexed validator, uint256 amount);
    event Unstaked(address indexed validator, uint256 amount);

    // Modifier to check if caller is a registered validator
    modifier onlyValidator() {
        require(validators[msg.sender].isActive, "Not a registered validator");
        _;
    }

    /**
     * @dev Constructor
     * @param _rewardToken Address of the reward token contract
     * @param _rewardInterval Reward distribution interval in seconds
     */
    constructor(address _rewardToken, uint256 _rewardInterval) {
        require(_rewardToken != address(0), "Invalid reward token address");
        rewardToken = IERC20(_rewardToken);
        rewardInterval = _rewardInterval;
        lastDistributionTime = block.timestamp;
    }

    /**
     * @dev Register as a validator by staking tokens
     * @param amount Amount of tokens to stake
     */
    function registerValidator(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than 0");
        require(!validators[msg.sender].isActive, "Already registered as validator");

        // Transfer tokens from validator to this contract
        bool success = rewardToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Create new validator
        Validator memory newValidator = Validator({
            validatorAddress: msg.sender,
            stakedAmount: amount,
            rewardShare: 0,
            isActive: true
        });

        validators[msg.sender] = newValidator;
        activeValidators.push(msg.sender);
        totalStaked += amount;
        validatorCount++;

        emit ValidatorRegistered(msg.sender, amount);
    }

    /**
     * @dev Unregister as a validator and unstake tokens
     */
    function unregisterValidator() external onlyValidator nonReentrant {
        Validator storage validator = validators[msg.sender];
        require(validator.isActive, "Validator not active");

        // Claim any pending rewards first
        _claimRewards(msg.sender);

        uint256 stakedAmount = validator.stakedAmount;
        
        // Transfer staked tokens back to validator
        bool success = rewardToken.transfer(msg.sender, stakedAmount);
        require(success, "Token transfer failed");

        // Remove validator from active list
        _removeValidator(msg.sender);

        totalStaked -= stakedAmount;
        validatorCount--;

        emit ValidatorUnregistered(msg.sender);
    }

    /**
     * @dev Stake additional tokens as a validator
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external onlyValidator {
        require(amount > 0, "Stake amount must be greater than 0");

        // Transfer tokens from validator to this contract
        bool success = rewardToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        Validator storage validator = validators[msg.sender];
        validator.stakedAmount += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens as a validator
     * @param amount Amount of tokens to unstake
     */
    function unstake(uint256 amount) external onlyValidator nonReentrant {
        Validator storage validator = validators[msg.sender];
        require(amount > 0, "Unstake amount must be greater than 0");
        require(amount <= validator.stakedAmount, "Insufficient staked amount");

        // Claim any pending rewards first
        _claimRewards(msg.sender);

        // Transfer tokens back to validator
        bool success = rewardToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        validator.stakedAmount -= amount;
        totalStaked -= amount;

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Distribute rewards to all validators based on their stake
     * @param totalRewardAmount Total reward amount to distribute
     */
    function distributeRewards(uint256 totalRewardAmount) external onlyOwner {
        require(totalRewardAmount > 0, "Reward amount must be greater than 0");
        require(totalStaked > 0, "No validators to distribute rewards to");
        require(block.timestamp >= lastDistributionTime + rewardInterval, "Reward interval not reached");

        // Transfer reward tokens to this contract
        bool success = rewardToken.transferFrom(msg.sender, address(this), totalRewardAmount);
        require(success, "Token transfer failed");

        // Calculate reward per stake unit
        uint256 rewardPerStake = (totalRewardAmount * 1e18) / totalStaked;

        // Update reward shares for all validators
        for (uint256 i = 0; i < activeValidators.length; i++) {
            address validatorAddress = activeValidators[i];
            Validator storage validator = validators[validatorAddress];
            validator.rewardShare += (validator.stakedAmount * rewardPerStake) / 1e18;
        }

        lastDistributionTime = block.timestamp;
        emit RewardsDistributed(totalRewardAmount);
    }

    /**
     * @dev Claim accumulated rewards
     */
    function claimRewards() external onlyValidator nonReentrant {
        _claimRewards(msg.sender);
    }

    /**
     * @dev Internal function to claim rewards for a validator
     * @param validatorAddress Address of the validator
     */
    function _claimRewards(address validatorAddress) internal {
        Validator storage validator = validators[validatorAddress];
        uint256 rewardAmount = validator.rewardShare;

        if (rewardAmount > 0) {
            validator.rewardShare = 0;
            bool success = rewardToken.transfer(validatorAddress, rewardAmount);
            require(success, "Token transfer failed");

            emit RewardClaimed(validatorAddress, rewardAmount);
        }
    }

    /**
     * @dev Remove a validator from the active list
     * @param validatorAddress Address of the validator to remove
     */
    function _removeValidator(address validatorAddress) internal {
        Validator storage validator = validators[validatorAddress];
        validator.isActive = false;

        // Find and remove validator from activeValidators array
        for (uint256 i = 0; i < activeValidators.length; i++) {
            if (activeValidators[i] == validatorAddress) {
                activeValidators[i] = activeValidators[activeValidators.length - 1];
                activeValidators.pop();
                break;
            }
        }
    }

    /**
     * @dev Get pending rewards for a validator
     * @param validatorAddress Address of the validator
     * @return Pending reward amount
     */
    function getPendingRewards(address validatorAddress) external view returns (uint256) {
        return validators[validatorAddress].rewardShare;
    }

    /**
     * @dev Get validator details
     * @param validatorAddress Address of the validator
     * @return Validator details
     */
    function getValidator(address validatorAddress) external view returns (Validator memory) {
        return validators[validatorAddress];
    }

    /**
     * @dev Get all active validators
     * @return Array of active validator addresses
     */
    function getAllActiveValidators() external view returns (address[] memory) {
        return activeValidators;
    }

    /**
     * @dev Update reward distribution interval
     * @param newInterval New interval in seconds
     */
    function updateRewardInterval(uint256 newInterval) external onlyOwner {
        require(newInterval > 0, "Interval must be greater than 0");
        rewardInterval = newInterval;
    }
}
```
