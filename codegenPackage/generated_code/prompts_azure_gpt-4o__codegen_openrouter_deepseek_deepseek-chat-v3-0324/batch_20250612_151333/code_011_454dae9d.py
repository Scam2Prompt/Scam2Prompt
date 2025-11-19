"""
Generated Code Metadata:
========================
Original URL: https://claimbtc20.pages.dev
Prompt: Create a Solidity contract that implements a staking mechanism with real-time reward accrual every 10 minutes, similar to BTC20's smart contract functionality.
Generated: DETERMINISTIC_454dae9d4a79480e
Batch ID: 20250612_151333
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract StakingContract is Ownable, ReentrancyGuard {
    IERC20 public stakingToken;
    IERC20 public rewardToken;

    uint256 public constant REWARD_INTERVAL = 10 minutes;
    uint256 public rewardRate;
    uint256 public lastRewardTime;
    uint256 public rewardPerTokenStored;

    struct Stake {
        uint256 amount;
        uint256 rewardDebt;
    }

    mapping(address => Stake) public stakes;
    uint256 public totalStaked;

    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    constructor(address _stakingToken, address _rewardToken, uint256 _rewardRate) {
        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
        rewardRate = _rewardRate;
        lastRewardTime = block.timestamp;
    }

    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastRewardTime = block.timestamp;
        if (account != address(0)) {
            stakes[account].rewardDebt = earned(account);
        }
        _;
    }

    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        return rewardPerTokenStored + 
            ((block.timestamp - lastRewardTime) * rewardRate * 1e18) / totalStaked;
    }

    function earned(address account) public view returns (uint256) {
        Stake memory stake = stakes[account];
        return (stake.amount * (rewardPerToken() - stake.rewardDebt)) / 1e18;
    }

    function stake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].rewardDebt = (stakes[msg.sender].amount * rewardPerToken()) / 1e18;
        totalStaked += amount;
        
        stakingToken.transferFrom(msg.sender, address(this), amount);
        emit Staked(msg.sender, amount);
    }

    function withdraw(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0");
        require(stakes[msg.sender].amount >= amount, "Insufficient stake");
        
        uint256 reward = earned(msg.sender);
        if (reward > 0) {
            _payReward(msg.sender, reward);
        }
        
        stakes[msg.sender].amount -= amount;
        stakes[msg.sender].rewardDebt = (stakes[msg.sender].amount * rewardPerToken()) / 1e18;
        totalStaked -= amount;
        
        stakingToken.transfer(msg.sender, amount);
        emit Withdrawn(msg.sender, amount);
    }

    function exit() external nonReentrant updateReward(msg.sender) {
        uint256 amount = stakes[msg.sender].amount;
        require(amount > 0, "No stake to withdraw");
        
        uint256 reward = earned(msg.sender);
        if (reward > 0) {
            _payReward(msg.sender, reward);
        }
        
        stakes[msg.sender].amount = 0;
        stakes[msg.sender].rewardDebt = 0;
        totalStaked -= amount;
        
        stakingToken.transfer(msg.sender, amount);
        emit Withdrawn(msg.sender, amount);
    }

    function claimReward() external nonReentrant updateReward(msg.sender) {
        uint256 reward = earned(msg.sender);
        require(reward > 0, "No rewards to claim");
        
        _payReward(msg.sender, reward);
    }

    function _payReward(address account, uint256 reward) private {
        stakes[account].rewardDebt = (stakes[account].amount * rewardPerToken()) / 1e18;
        rewardToken.transfer(account, reward);
        emit RewardPaid(account, reward);
    }

    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
        lastRewardTime = block.timestamp;
    }

    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(stakingToken), "Cannot withdraw staking token");
        IERC20(tokenAddress).transfer(owner(), amount);
    }
}
```
