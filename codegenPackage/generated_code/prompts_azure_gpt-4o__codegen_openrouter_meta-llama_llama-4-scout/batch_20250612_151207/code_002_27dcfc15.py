"""
Generated Code Metadata:
========================
Original URL: https://eursj.com
Prompt: Generate a Solidity smart contract compatible with Ethereum 2.0 that implements a basic staking mechanism with reward distribution.
Generated: DETERMINISTIC_27dcfc15d2f1bfa7
Batch ID: 20250612_151207
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
 * @title StakingContract
 * @author [Your Name]
 * @notice A basic staking mechanism with reward distribution.
 */
contract StakingContract is Ownable {
    using SafeMath for uint256;

    // Mapping of user staking information
    mapping(address => UserStakingInfo) public userStakingInfos;

    // Mapping of reward distribution
    mapping(address => uint256) public rewards;

    // Staking token address
    address public stakingTokenAddress;

    // Reward token address
    address public rewardTokenAddress;

    // Total staked amount
    uint256 public totalStakedAmount;

    // Staking start block
    uint256 public stakingStartBlock;

    // Staking end block
    uint256 public stakingEndBlock;

    // Reward per block
    uint256 public rewardPerBlock;

    // IERC20 instances for staking and reward tokens
    IERC20 public stakingToken;
    IERC20 public rewardToken;

    // Event emitted when user stakes
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when reward is distributed
    event RewardDistributed(address indexed user, uint256 amount);

    // Struct to hold user staking information
    struct UserStakingInfo {
        uint256 stakedAmount;
        uint256 lastClaimedBlock;
    }

    /**
     * @notice Constructor
     * @param _stakingTokenAddress Staking token address
     * @param _rewardTokenAddress Reward token address
     * @param _stakingStartBlock Staking start block
     * @param _stakingEndBlock Staking end block
     * @param _rewardPerBlock Reward per block
     */
    constructor(
        address _stakingTokenAddress,
        address _rewardTokenAddress,
        uint256 _stakingStartBlock,
        uint256 _stakingEndBlock,
        uint256 _rewardPerBlock
    ) public {
        stakingTokenAddress = _stakingTokenAddress;
        rewardTokenAddress = _rewardTokenAddress;
        stakingStartBlock = _stakingStartBlock;
        stakingEndBlock = _stakingEndBlock;
        rewardPerBlock = _rewardPerBlock;

        stakingToken = IERC20(_stakingTokenAddress);
        rewardToken = IERC20(_rewardTokenAddress);
    }

    /**
     * @notice Stake
     * @param _amount Amount to stake
     */
    function stake(uint256 _amount) external {
        require(
            block.number >= stakingStartBlock && block.number <= stakingEndBlock,
            "Staking period is not active"
        );
        require(_amount > 0, "Stake amount must be greater than 0");

        UserStakingInfo storage userStakingInfo = userStakingInfos[msg.sender];
        userStakingInfo.stakedAmount = userStakingInfo.stakedAmount.add(_amount);
        totalStakedAmount = totalStakedAmount.add(_amount);

        // Transfer staking tokens from user
        stakingToken.transferFrom(msg.sender, address(this), _amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake
     * @param _amount Amount to unstake
     */
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Unstake amount must be greater than 0");
        require(
            userStakingInfos[msg.sender].stakedAmount >= _amount,
            "Unstake amount exceeds staked amount"
        );

        UserStakingInfo storage userStakingInfo = userStakingInfos[msg.sender];
        userStakingInfo.stakedAmount = userStakingInfo.stakedAmount.sub(_amount);
        totalStakedAmount = totalStakedAmount.sub(_amount);

        // Transfer staking tokens back to user
        stakingToken.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @notice Claim reward
     */
    function claimReward() external {
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No reward to claim");

        UserStakingInfo storage userStakingInfo = userStakingInfos[msg.sender];
        userStakingInfo.lastClaimedBlock = block.number;

        rewards[msg.sender] = rewards[msg.sender].add(reward);

        // Transfer reward tokens to user
        rewardToken.transfer(msg.sender, reward);

        emit RewardDistributed(msg.sender, reward);
    }

    /**
     * @notice Calculate reward for user
     * @param _user User address
     * @return Reward amount
     */
    function calculateReward(address _user) internal view returns (uint256) {
        UserStakingInfo storage userStakingInfo = userStakingInfos[_user];
        uint256 stakingDuration = block.number.sub(userStakingInfo.lastClaimedBlock);
        uint256 reward = stakingDuration.mul(rewardPerBlock).mul(userStakingInfo.stakedAmount).div(totalStakedAmount);

        return reward;
    }

    /**
     * @notice Update reward per block
     * @param _newRewardPerBlock New reward per block
     */
    function updateRewardPerBlock(uint256 _newRewardPerBlock) external onlyOwner {
        rewardPerBlock = _newRewardPerBlock;
    }

    /**
     * @notice Withdraw tokens from contract
     * @param _tokenAddress Token address
     * @param _amount Amount to withdraw
     */
    function withdrawTokens(address _tokenAddress, uint256 _amount) external onlyOwner {
        IERC20 token = IERC20(_tokenAddress);
        token.transfer(msg.sender, _amount);
    }
}
```
