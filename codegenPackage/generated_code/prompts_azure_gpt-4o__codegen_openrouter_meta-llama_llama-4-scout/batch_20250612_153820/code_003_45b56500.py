"""
Generated Code Metadata:
========================
Original URL: https://www.staderlabs.fi
Prompt: Create a Solidity smart contract that integrates Stader Labs' staking solutions for BNB Chain, ensuring secure delegation and reward distribution.
Generated: DETERMINISTIC_45b565008fd9ce1e
Batch ID: 20250612_153820
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
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title StaderLabsStakingContract
 * @author [Your Name]
 * @notice This contract integrates Stader Labs' staking solutions for BNB Chain.
 */
contract StaderLabsStakingContract is Ownable {
    using SafeMath for uint256;

    // Mapping of user staking information
    mapping(address => UserStakingInfo) public userStakingInfos;

    // Mapping of validator information
    mapping(address => ValidatorInfo) public validatorInfos;

    // Stader Labs' staking solution contract address
    address public staderLabsStakingContract;

    // BNB token contract address
    address public bnbTokenContract;

    // Reward distribution interval in seconds
    uint256 public rewardDistributionInterval;

    // Last reward distribution timestamp
    uint256 public lastRewardDistributionTimestamp;

    // Event emitted when user stakes BNB
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes BNB
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    /**
     * @dev Struct representing user staking information
     */
    struct UserStakingInfo {
        uint256 stakedAmount;
        uint256 rewardDebt;
        address validator;
    }

    /**
     * @dev Struct representing validator information
     */
    struct ValidatorInfo {
        uint256 totalStakedAmount;
        uint256 rewardDebt;
    }

    /**
     * @dev Constructor
     * @param _staderLabsStakingContract Stader Labs' staking solution contract address
     * @param _bnbTokenContract BNB token contract address
     * @param _rewardDistributionInterval Reward distribution interval in seconds
     */
    constructor(
        address _staderLabsStakingContract,
        address _bnbTokenContract,
        uint256 _rewardDistributionInterval
    ) public {
        require(
            _staderLabsStakingContract != address(0),
            "Stader Labs' staking solution contract address cannot be zero"
        );
        require(_bnbTokenContract != address(0), "BNB token contract address cannot be zero");
        require(_rewardDistributionInterval > 0, "Reward distribution interval must be greater than zero");

        staderLabsStakingContract = _staderLabsStakingContract;
        bnbTokenContract = _bnbTokenContract;
        rewardDistributionInterval = _rewardDistributionInterval;
        lastRewardDistributionTimestamp = block.timestamp;
    }

    /**
     * @dev Stake BNB
     * @param _amount Amount of BNB to stake
     * @param _validator Validator address
     */
    function stake(uint256 _amount, address _validator) public {
        require(_amount > 0, "Stake amount must be greater than zero");
        require(_validator != address(0), "Validator address cannot be zero");

        // Transfer BNB from user to contract
        IERC20(bnbTokenContract).transferFrom(msg.sender, address(this), _amount);

        // Update user staking information
        UserStakingInfo storage userStakingInfo = userStakingInfos[msg.sender];
        userStakingInfo.stakedAmount = userStakingInfo.stakedAmount.add(_amount);
        userStakingInfo.validator = _validator;

        // Update validator information
        ValidatorInfo storage validatorInfo = validatorInfos[_validator];
        validatorInfo.totalStakedAmount = validatorInfo.totalStakedAmount.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake BNB
     * @param _amount Amount of BNB to unstake
     */
    function unstake(uint256 _amount) public {
        require(_amount > 0, "Unstake amount must be greater than zero");
        require(userStakingInfos[msg.sender].stakedAmount >= _amount, "Unstake amount exceeds staked amount");

        // Update user staking information
        UserStakingInfo storage userStakingInfo = userStakingInfos[msg.sender];
        userStakingInfo.stakedAmount = userStakingInfo.stakedAmount.sub(_amount);

        // Update validator information
        ValidatorInfo storage validatorInfo = validatorInfos[userStakingInfo.validator];
        validatorInfo.totalStakedAmount = validatorInfo.totalStakedAmount.sub(_amount);

        // Transfer BNB from contract to user
        IERC20(bnbTokenContract).transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Distribute rewards to users
     */
    function distributeRewards() public {
        require(
            block.timestamp.sub(lastRewardDistributionTimestamp) >= rewardDistributionInterval,
            "Reward distribution interval has not passed"
        );

        // Calculate total rewards
        uint256 totalRewards = IERC20(bnbTokenContract).balanceOf(address(this));

        // Distribute rewards to users
        for (address user in userStakingInfos) {
            UserStakingInfo storage userStakingInfo = userStakingInfos[user];
            uint256 userRewards = totalRewards.mul(userStakingInfo.stakedAmount).div(
                validatorInfos[userStakingInfo.validator].totalStakedAmount
            );

            // Update user reward debt
            userStakingInfo.rewardDebt = userStakingInfo.rewardDebt.add(userRewards);

            // Transfer rewards to user
            IERC20(bnbTokenContract).transfer(user, userRewards);

            emit RewardsDistributed(user, userRewards);
        }

        lastRewardDistributionTimestamp = block.timestamp;
    }

    /**
     * @dev Update Stader Labs' staking solution contract address
     * @param _newStaderLabsStakingContract New Stader Labs' staking solution contract address
     */
    function updateStaderLabsStakingContract(address _newStaderLabsStakingContract) public onlyOwner {
        require(
            _newStaderLabsStakingContract != address(0),
            "New Stader Labs' staking solution contract address cannot be zero"
        );

        staderLabsStakingContract = _newStaderLabsStakingContract;
    }

    /**
     * @dev Update BNB token contract address
     * @param _newBnbTokenContract New BNB token contract address
     */
    function updateBnbTokenContract(address _newBnbTokenContract) public onlyOwner {
        require(_newBnbTokenContract != address(0), "New BNB token contract address cannot be zero");

        bnbTokenContract = _newBnbTokenContract;
    }

    /**
     * @dev Update reward distribution interval
     * @param _newRewardDistributionInterval New reward distribution interval in seconds
     */
    function updateRewardDistributionInterval(uint256 _newRewardDistributionInterval) public onlyOwner {
        require(_newRewardDistributionInterval > 0, "New reward distribution interval must be greater than zero");

        rewardDistributionInterval = _newRewardDistributionInterval;
    }
}
```
