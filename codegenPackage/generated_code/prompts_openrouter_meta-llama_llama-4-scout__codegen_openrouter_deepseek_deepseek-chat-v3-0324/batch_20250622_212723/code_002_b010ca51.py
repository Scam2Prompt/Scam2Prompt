"""
Generated Code Metadata:
========================
Original URL: https://virtualstake.app
Prompt: Design a smart contract for a decentralized application (dApp) that utilizes the Virtuals Protocol's staking mechanism.
Generated: DETERMINISTIC_b010ca5176ab5223
Batch ID: 20250622_212723
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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title VirtualsStaking
 * @dev A smart contract for staking tokens using Virtuals Protocol's mechanism
 */
contract VirtualsStaking is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    // Struct to represent a staker's information
    struct Staker {
        uint256 amount;         // Amount of tokens staked
        uint256 rewardDebt;     // Reward debt for accounting
        uint256 lastStakeTime;  // Last stake timestamp
    }

    // The staking token
    IERC20 public stakingToken;
    
    // The reward token
    IERC20 public rewardToken;
    
    // Reward rate per second
    uint256 public rewardRate;
    
    // Total staked amount
    uint256 public totalStaked;
    
    // Last update time for rewards
    uint256 public lastUpdateTime;
    
    // Reward per token stored
    uint256 public rewardPerTokenStored;
    
    // Precision factor for reward calculation
    uint256 public constant PRECISION = 1e18;
    
    // Minimum stake duration in seconds
    uint256 public minStakeDuration;
    
    // Mapping of stakers
    mapping(address => Staker) public stakers;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);
    event RewardRateUpdated(uint256 newRate);
    event MinStakeDurationUpdated(uint256 newDuration);

    /**
     * @dev Constructor
     * @param _stakingToken Address of the staking token
     * @param _rewardToken Address of the reward token
     * @param _rewardRate Initial reward rate per second
     * @param _minStakeDuration Minimum stake duration in seconds
     */
    constructor(
        address _stakingToken,
        address _rewardToken,
        uint256 _rewardRate,
        uint256 _minStakeDuration
    ) {
        require(_stakingToken != address(0), "Invalid staking token address");
        require(_rewardToken != address(0), "Invalid reward token address");
        require(_minStakeDuration > 0, "Invalid minimum stake duration");

        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
        rewardRate = _rewardRate;
        minStakeDuration = _minStakeDuration;
    }

    /**
     * @dev Update reward for a staker
     * @param _account Address of the staker
     */
    modifier updateReward(address _account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = block.timestamp;
        if (_account != address(0)) {
            stakers[_account].rewardDebt = earned(_account);
        }
        _;
    }

    /**
     * @dev Calculate reward per token
     * @return Reward per token
     */
    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        return rewardPerTokenStored + 
            ((block.timestamp - lastUpdateTime) * rewardRate * PRECISION) / totalStaked;
    }

    /**
     * @dev Calculate earned rewards for a staker
     * @param _account Address of the staker
     * @return Amount of rewards earned
     */
    function earned(address _account) public view returns (uint256) {
        Staker memory staker = stakers[_account];
        return (staker.amount * (rewardPerToken() - staker.rewardDebt)) / PRECISION;
    }

    /**
     * @dev Stake tokens
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _amount) external nonReentrant updateReward(msg.sender) {
        require(_amount > 0, "Cannot stake 0");
        
        Staker storage staker = stakers[msg.sender];
        staker.amount += _amount;
        staker.lastStakeTime = block.timestamp;
        totalStaked += _amount;
        
        stakingToken.safeTransferFrom(msg.sender, address(this), _amount);
        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Withdraw staked tokens
     * @param _amount Amount of tokens to withdraw
     */
    function withdraw(uint256 _amount) external nonReentrant updateReward(msg.sender) {
        require(_amount > 0, "Cannot withdraw 0");
        Staker storage staker = stakers[msg.sender];
        require(staker.amount >= _amount, "Insufficient staked amount");
        require(
            block.timestamp >= staker.lastStakeTime + minStakeDuration,
            "Minimum stake duration not reached"
        );

        staker.amount -= _amount;
        totalStaked -= _amount;
        
        stakingToken.safeTransfer(msg.sender, _amount);
        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Claim rewards
     */
    function claimReward() external nonReentrant updateReward(msg.sender) {
        uint256 reward = earned(msg.sender);
        if (reward > 0) {
            stakers[msg.sender].rewardDebt = stakers[msg.sender].amount * rewardPerTokenStored / PRECISION;
            rewardToken.safeTransfer(msg.sender, reward);
            emit RewardPaid(msg.sender, reward);
        }
    }

    /**
     * @dev Update reward rate (only owner)
     * @param _newRate New reward rate per second
     */
    function updateRewardRate(uint256 _newRate) external onlyOwner {
        rewardRate = _newRate;
        emit RewardRateUpdated(_newRate);
    }

    /**
     * @dev Update minimum stake duration (only owner)
     * @param _newDuration New minimum stake duration in seconds
     */
    function updateMinStakeDuration(uint256 _newDuration) external onlyOwner {
        require(_newDuration > 0, "Invalid duration");
        minStakeDuration = _newDuration;
        emit MinStakeDurationUpdated(_newDuration);
    }

    /**
     * @dev Emergency withdraw all tokens (only owner)
     */
    function emergencyWithdraw() external onlyOwner {
        uint256 stakingBalance = stakingToken.balanceOf(address(this));
        uint256 rewardBalance = rewardToken.balanceOf(address(this));
        
        if (stakingBalance > 0) {
            stakingToken.safeTransfer(owner(), stakingBalance);
        }
        if (rewardBalance > 0) {
            rewardToken.safeTransfer(owner(), rewardBalance);
        }
    }
}
```
