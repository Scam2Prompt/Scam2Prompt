"""
Generated Code Metadata:
========================
Original URL: https://rocket-pool.xyz
Prompt: Develop a smart contract that utilizes Rocket Pool's rETH for staking and yield generation, and describe how to distribute rewards and calculate the rETH/ETH exchange rate.
Generated: DETERMINISTIC_ee3aa635ceb51563
Batch ID: 20250622_212600
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

interface IRocketTokenRETH {
    function getEthValue(uint256 _rethAmount) external view returns (uint256);
    function getRethValue(uint256 _ethAmount) external view returns (uint256);
    function deposit() external payable;
    function withdraw(uint256 _rethAmount) external;
}

contract RETHStaking is Ownable, ReentrancyGuard {
    IERC20 public rethToken;
    IRocketTokenRETH public rocketTokenRETH;

    struct Staker {
        uint256 stakedAmount;
        uint256 rewardDebt;
    }

    uint256 public totalStaked;
    uint256 public rewardPerTokenStored;
    uint256 public lastUpdateTime;
    uint256 public rewardRate;

    mapping(address => Staker) public stakers;

    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);
    event RewardRateUpdated(uint256 newRate);

    constructor(address _rethTokenAddress, address _rocketTokenRETHAddress) {
        rethToken = IERC20(_rethTokenAddress);
        rocketTokenRETH = IRocketTokenRETH(_rocketTokenRETHAddress);
    }

    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = block.timestamp;
        if (account != address(0)) {
            stakers[account].rewardDebt = earned(account);
        }
        _;
    }

    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        return rewardPerTokenStored + 
               (((block.timestamp - lastUpdateTime) * rewardRate * 1e18) / totalStaked);
    }

    function earned(address account) public view returns (uint256) {
        return ((stakers[account].stakedAmount * 
                (rewardPerToken() - stakers[account].rewardDebt)) / 1e18);
    }

    function stake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        
        rethToken.transferFrom(msg.sender, address(this), amount);
        
        stakers[msg.sender].stakedAmount += amount;
        totalStaked += amount;
        
        emit Staked(msg.sender, amount);
    }

    function withdraw(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0");
        require(stakers[msg.sender].stakedAmount >= amount, "Insufficient balance");
        
        stakers[msg.sender].stakedAmount -= amount;
        totalStaked -= amount;
        
        rethToken.transfer(msg.sender, amount);
        
        emit Withdrawn(msg.sender, amount);
    }

    function getReward() external nonReentrant updateReward(msg.sender) {
        uint256 reward = earned(msg.sender);
        if (reward > 0) {
            stakers[msg.sender].rewardDebt = stakers[msg.sender].stakedAmount * rewardPerToken() / 1e18;
            payable(msg.sender).transfer(reward);
            emit RewardPaid(msg.sender, reward);
        }
    }

    function stakeETH() external payable nonReentrant updateReward(msg.sender) {
        require(msg.value > 0, "Cannot stake 0 ETH");
        
        uint256 rethAmount = rocketTokenRETH.getRethValue(msg.value);
        rocketTokenRETH.deposit{value: msg.value}();
        
        stakers[msg.sender].stakedAmount += rethAmount;
        totalStaked += rethAmount;
        
        emit Staked(msg.sender, rethAmount);
    }

    function withdrawETH(uint256 rethAmount) external nonReentrant updateReward(msg.sender) {
        require(rethAmount > 0, "Cannot withdraw 0");
        require(stakers[msg.sender].stakedAmount >= rethAmount, "Insufficient balance");
        
        stakers[msg.sender].stakedAmount -= rethAmount;
        totalStaked -= rethAmount;
        
        uint256 ethAmount = rocketTokenRETH.getEthValue(rethAmount);
        rocketTokenRETH.withdraw(rethAmount);
        payable(msg.sender).transfer(ethAmount);
        
        emit Withdrawn(msg.sender, rethAmount);
    }

    function getExchangeRate() external view returns (uint256) {
        return rocketTokenRETH.getEthValue(1 ether);
    }

    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
        emit RewardRateUpdated(_rewardRate);
    }

    receive() external payable {
        // Accept ETH donations for rewards
    }

    function withdrawRewardFunds(uint256 amount) external onlyOwner {
        payable(owner()).transfer(amount);
    }
}
```
