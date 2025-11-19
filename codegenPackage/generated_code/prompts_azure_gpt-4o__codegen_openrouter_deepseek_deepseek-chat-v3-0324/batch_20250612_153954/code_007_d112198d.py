"""
Generated Code Metadata:
========================
Original URL: https://j-node.net
Prompt: Develop a smart contract to reward trusted validators for their contributions to blockchain security, inspired by J•Node's mission.
Generated: DETERMINISTIC_d112198d81554365
Batch ID: 20250612_153954
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

/**
 * @title ValidatorRewards
 * @dev A smart contract to reward trusted validators for their contributions to blockchain security
 */
contract ValidatorRewards is Ownable, ReentrancyGuard {
    // Reward token interface
    IERC20 public rewardToken;

    // Validator information
    struct Validator {
        address validatorAddress;
        uint256 totalStake;
        uint256 lastRewardTime;
        uint256 totalRewards;
        bool isActive;
    }

    // Mapping of validator addresses to their details
    mapping(address => Validator) public validators;

    // List of all validator addresses for iteration
    address[] public validatorAddresses;

    // Reward parameters
    uint256 public rewardRate; // Reward tokens per second
    uint256 public minimumStake;
    uint256 public cooldownPeriod;

    // Events
    event ValidatorRegistered(address indexed validator);
    event ValidatorDeregistered(address indexed validator);
    event RewardDistributed(address indexed validator, uint256 amount);
    event StakeUpdated(address indexed validator, uint256 newStake);
    event RewardParametersUpdated(uint256 rewardRate, uint256 minimumStake, uint256 cooldownPeriod);

    /**
     * @dev Constructor
     * @param _rewardToken Address of the ERC20 reward token
     * @param _rewardRate Initial reward rate (tokens per second)
     * @param _minimumStake Minimum stake required to be a validator
     * @param _cooldownPeriod Time between reward distributions (seconds)
     */
    constructor(
        address _rewardToken,
        uint256 _rewardRate,
        uint256 _minimumStake,
        uint256 _cooldownPeriod
    ) {
        require(_rewardToken != address(0), "Invalid reward token address");
        rewardToken = IERC20(_rewardToken);
        rewardRate = _rewardRate;
        minimumStake = _minimumStake;
        cooldownPeriod = _cooldownPeriod;
    }

    /**
     * @dev Register as a validator
     * @param _stakeAmount Amount of tokens to stake
     */
    function registerValidator(uint256 _stakeAmount) external nonReentrant {
        require(_stakeAmount >= minimumStake, "Stake below minimum");
        require(!validators[msg.sender].isActive, "Already registered");

        // Transfer stake tokens from validator
        require(
            rewardToken.transferFrom(msg.sender, address(this), _stakeAmount),
            "Stake transfer failed"
        );

        // Create new validator
        validators[msg.sender] = Validator({
            validatorAddress: msg.sender,
            totalStake: _stakeAmount,
            lastRewardTime: block.timestamp,
            totalRewards: 0,
            isActive: true
        });

        validatorAddresses.push(msg.sender);
        emit ValidatorRegistered(msg.sender);
    }

    /**
     * @dev Deregister as a validator and withdraw stake
     */
    function deregisterValidator() external nonReentrant {
        Validator storage validator = validators[msg.sender];
        require(validator.isActive, "Not an active validator");

        // Calculate and distribute any pending rewards
        _distributeRewards(msg.sender);

        // Return stake to validator
        uint256 stakeAmount = validator.totalStake;
        validator.totalStake = 0;
        validator.isActive = false;

        require(
            rewardToken.transfer(msg.sender, stakeAmount),
            "Stake return failed"
        );

        emit ValidatorDeregistered(msg.sender);
    }

    /**
     * @dev Update validator's stake
     * @param _additionalStake Additional amount to stake
     */
    function updateStake(uint256 _additionalStake) external nonReentrant {
        Validator storage validator = validators[msg.sender];
        require(validator.isActive, "Not an active validator");

        // Distribute any pending rewards before updating stake
        _distributeRewards(msg.sender);

        // Transfer additional stake
        if (_additionalStake > 0) {
            require(
                rewardToken.transferFrom(msg.sender, address(this), _additionalStake),
                "Stake transfer failed"
            );
            validator.totalStake += _additionalStake;
        }

        emit StakeUpdated(msg.sender, validator.totalStake);
    }

    /**
     * @dev Claim rewards for a validator
     */
    function claimRewards() external nonReentrant {
        _distributeRewards(msg.sender);
    }

    /**
     * @dev Internal function to calculate and distribute rewards
     * @param _validatorAddress Address of the validator
     */
    function _distributeRewards(address _validatorAddress) internal {
        Validator storage validator = validators[_validatorAddress];
        require(validator.isActive, "Not an active validator");

        uint256 timeElapsed = block.timestamp - validator.lastRewardTime;
        if (timeElapsed < cooldownPeriod) {
            return;
        }

        uint256 rewardAmount = (validator.totalStake * rewardRate * timeElapsed) / 1e18;
        if (rewardAmount > 0) {
            validator.totalRewards += rewardAmount;
            validator.lastRewardTime = block.timestamp;

            require(
                rewardToken.transfer(_validatorAddress, rewardAmount),
                "Reward transfer failed"
            );

            emit RewardDistributed(_validatorAddress, rewardAmount);
        }
    }

    /**
     * @dev Update reward parameters (owner only)
     * @param _rewardRate New reward rate (tokens per second)
     * @param _minimumStake New minimum stake amount
     * @param _cooldownPeriod New cooldown period between rewards (seconds)
     */
    function updateRewardParameters(
        uint256 _rewardRate,
        uint256 _minimumStake,
        uint256 _cooldownPeriod
    ) external onlyOwner {
        rewardRate = _rewardRate;
        minimumStake = _minimumStake;
        cooldownPeriod = _cooldownPeriod;

        emit RewardParametersUpdated(_rewardRate, _minimumStake, _cooldownPeriod);
    }

    /**
     * @dev Get total active validators count
     * @return count Number of active validators
     */
    function getActiveValidatorsCount() external view returns (uint256 count) {
        for (uint256 i = 0; i < validatorAddresses.length; i++) {
            if (validators[validatorAddresses[i]].isActive) {
                count++;
            }
        }
        return count;
    }

    /**
     * @dev Emergency withdraw tokens (owner only)
     * @param _token Address of token to withdraw
     * @param _amount Amount to withdraw
     */
    function emergencyWithdraw(address _token, uint256 _amount) external onlyOwner {
        IERC20 token = IERC20(_token);
        require(token.transfer(owner(), _amount), "Withdrawal failed");
    }
}
```
