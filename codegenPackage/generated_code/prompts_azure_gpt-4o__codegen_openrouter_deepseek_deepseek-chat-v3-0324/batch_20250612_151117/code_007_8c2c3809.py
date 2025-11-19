"""
Generated Code Metadata:
========================
Original URL: https://visualprocurator.pages.dev
Prompt: Provide an example of using Multichain's veMULTI governance token in a staking contract, including reward claiming functionality.
Generated: DETERMINISTIC_8c2c380932f85ae8
Batch ID: 20250612_151117
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract VeMultiStaking is ReentrancyGuard {
    using SafeERC20 for IERC20;
    using SafeMath for uint256;

    // Interface for veMULTI token
    IERC20 public immutable veMultiToken;
    
    // Reward token (could be MULTI or another token)
    IERC20 public immutable rewardToken;
    
    // Reward rate per second
    uint256 public rewardRate;
    
    // Duration of rewards to be paid out (in seconds)
    uint256 public rewardsDuration;
    
    // Timestamp of when rewards finish
    uint256 public periodFinish;
    
    // Last time reward was updated
    uint256 public lastUpdateTime;
    
    // Reward per token stored
    uint256 public rewardPerTokenStored;
    
    // User address => rewardPerTokenStored
    mapping(address => uint256) public userRewardPerTokenPaid;
    
    // User address => rewards to be claimed
    mapping(address => uint256) public rewards;
    
    // Total staked amount
    uint256 private _totalSupply;
    
    // User address => staked amount
    mapping(address => uint256) private _balances;

    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);
    event RewardsDurationUpdated(uint256 newDuration);
    event RewardRateUpdated(uint256 newRate);

    constructor(
        address _veMultiToken,
        address _rewardToken,
        uint256 _rewardRate,
        uint256 _rewardsDuration
    ) {
        veMultiToken = IERC20(_veMultiToken);
        rewardToken = IERC20(_rewardToken);
        rewardRate = _rewardRate;
        rewardsDuration = _rewardsDuration;
    }

    // Update reward for given account
    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = lastTimeRewardApplicable();
        if (account != address(0)) {
            rewards[account] = earned(account);
            userRewardPerTokenPaid[account] = rewardPerTokenStored;
        }
        _;
    }

    // Get total staked amount
    function totalSupply() external view returns (uint256) {
        return _totalSupply;
    }

    // Get staked amount for user
    function balanceOf(address account) external view returns (uint256) {
        return _balances[account];
    }

    // Get last time reward is applicable
    function lastTimeRewardApplicable() public view returns (uint256) {
        return block.timestamp < periodFinish ? block.timestamp : periodFinish;
    }

    // Calculate reward per token
    function rewardPerToken() public view returns (uint256) {
        if (_totalSupply == 0) {
            return rewardPerTokenStored;
        }
        return
            rewardPerTokenStored.add(
                lastTimeRewardApplicable()
                    .sub(lastUpdateTime)
                    .mul(rewardRate)
                    .mul(1e18)
                    .div(_totalSupply)
            );
    }

    // Calculate earned rewards for user
    function earned(address account) public view returns (uint256) {
        return
            _balances[account]
                .mul(rewardPerToken().sub(userRewardPerTokenPaid[account]))
                .div(1e18)
                .add(rewards[account]);
    }

    // Stake veMULTI tokens
    function stake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        _totalSupply = _totalSupply.add(amount);
        _balances[msg.sender] = _balances[msg.sender].add(amount);
        veMultiToken.safeTransferFrom(msg.sender, address(this), amount);
        emit Staked(msg.sender, amount);
    }

    // Withdraw staked veMULTI tokens
    function withdraw(uint256 amount) public nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0");
        _totalSupply = _totalSupply.sub(amount);
        _balances[msg.sender] = _balances[msg.sender].sub(amount);
        veMultiToken.safeTransfer(msg.sender, amount);
        emit Withdrawn(msg.sender, amount);
    }

    // Claim rewards
    function getReward() public nonReentrant updateReward(msg.sender) {
        uint256 reward = rewards[msg.sender];
        if (reward > 0) {
            rewards[msg.sender] = 0;
            rewardToken.safeTransfer(msg.sender, reward);
            emit RewardPaid(msg.sender, reward);
        }
    }

    // Exit by withdrawing all staked tokens and claiming rewards
    function exit() external {
        withdraw(_balances[msg.sender]);
        getReward();
    }

    // Notify reward amount (only callable by owner in production)
    function notifyRewardAmount(uint256 reward) external updateReward(address(0)) {
        require(block.timestamp >= periodFinish, "Previous rewards period not complete");
        
        uint256 balance = rewardToken.balanceOf(address(this));
        require(rewardRate <= balance.div(rewardsDuration), "Provided reward too high");

        lastUpdateTime = block.timestamp;
        periodFinish = block.timestamp.add(rewardsDuration);
        
        emit RewardRateUpdated(rewardRate);
    }

    // Update rewards duration (only callable by owner in production)
    function setRewardsDuration(uint256 _rewardsDuration) external {
        require(block.timestamp > periodFinish, "Previous rewards period not complete");
        rewardsDuration = _rewardsDuration;
        emit RewardsDurationUpdated(_rewardsDuration);
    }
}
```
