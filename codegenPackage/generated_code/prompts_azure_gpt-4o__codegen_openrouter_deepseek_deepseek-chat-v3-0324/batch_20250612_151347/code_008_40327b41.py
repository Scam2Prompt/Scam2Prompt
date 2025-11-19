"""
Generated Code Metadata:
========================
Original URL: https://pepe-buy.pages.dev
Prompt: Write a Solidity function to calculate and distribute staking rewards for $PEPU tokens, ensuring compatibility with the tokenomics described on the Pepe Unchained site.
Generated: DETERMINISTIC_40327b415dafc74c
Batch ID: 20250612_151347
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract PEPUStaking is Ownable {
    using SafeMath for uint256;

    IERC20 public pepuToken;

    struct Staker {
        uint256 amount;
        uint256 rewardDebt;
        uint256 lastRewardCalculationTime;
    }

    uint256 public totalStaked;
    uint256 public rewardPerTokenStored;
    uint256 public lastUpdateTime;
    uint256 public rewardRate;
    uint256 public rewardPeriodEnd;

    mapping(address => Staker) public stakers;

    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);
    event RewardRateUpdated(uint256 newRate, uint256 periodEnd);

    constructor(address _pepuToken) {
        pepuToken = IERC20(_pepuToken);
    }

    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = lastTimeRewardApplicable();
        if (account != address(0)) {
            stakers[account].rewardDebt = earned(account);
            stakers[account].lastRewardCalculationTime = lastUpdateTime;
        }
        _;
    }

    function lastTimeRewardApplicable() public view returns (uint256) {
        return block.timestamp < rewardPeriodEnd ? block.timestamp : rewardPeriodEnd;
    }

    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        return rewardPerTokenStored.add(
            lastTimeRewardApplicable()
                .sub(lastUpdateTime)
                .mul(rewardRate)
                .mul(1e18)
                .div(totalStaked)
        );
    }

    function earned(address account) public view returns (uint256) {
        Staker storage staker = stakers[account];
        return staker.amount
            .mul(rewardPerToken().sub(staker.rewardDebt))
            .div(1e18)
            .add(staker.rewardDebt);
    }

    function stake(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        
        Staker storage staker = stakers[msg.sender];
        if (staker.amount > 0) {
            uint256 pending = earned(msg.sender);
            if (pending > 0) {
                safePEPUTransfer(msg.sender, pending);
                emit RewardPaid(msg.sender, pending);
            }
        }

        totalStaked = totalStaked.add(amount);
        staker.amount = staker.amount.add(amount);
        staker.rewardDebt = staker.amount.mul(rewardPerTokenStored).div(1e18);

        require(pepuToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        emit Staked(msg.sender, amount);
    }

    function withdraw(uint256 amount) public updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0");
        Staker storage staker = stakers[msg.sender];
        require(staker.amount >= amount, "Insufficient balance");

        uint256 pending = earned(msg.sender);
        if (pending > 0) {
            safePEPUTransfer(msg.sender, pending);
            emit RewardPaid(msg.sender, pending);
        }

        totalStaked = totalStaked.sub(amount);
        staker.amount = staker.amount.sub(amount);
        staker.rewardDebt = staker.amount.mul(rewardPerTokenStored).div(1e18);

        require(pepuToken.transfer(msg.sender, amount), "Transfer failed");
        emit Withdrawn(msg.sender, amount);
    }

    function exit() external {
        withdraw(stakers[msg.sender].amount);
    }

    function getReward() public updateReward(msg.sender) {
        uint256 reward = earned(msg.sender);
        if (reward > 0) {
            stakers[msg.sender].rewardDebt = stakers[msg.sender].amount.mul(rewardPerTokenStored).div(1e18);
            safePEPUTransfer(msg.sender, reward);
            emit RewardPaid(msg.sender, reward);
        }
    }

    function safePEPUTransfer(address _to, uint256 _amount) internal {
        uint256 pepuBalance = pepuToken.balanceOf(address(this));
        if (_amount > pepuBalance) {
            pepuToken.transfer(_to, pepuBalance);
        } else {
            pepuToken.transfer(_to, _amount);
        }
    }

    function setRewardRate(uint256 _rewardRate, uint256 _duration) external onlyOwner {
        require(block.timestamp >= rewardPeriodEnd, "Previous rewards period not finished");
        require(_rewardRate > 0, "Reward rate must be positive");
        require(_duration > 0, "Duration must be positive");

        rewardRate = _rewardRate;
        rewardPeriodEnd = block.timestamp.add(_duration);
        lastUpdateTime = block.timestamp;

        emit RewardRateUpdated(_rewardRate, rewardPeriodEnd);
    }

    function emergencyWithdraw() external {
        Staker storage staker = stakers[msg.sender];
        uint256 amount = staker.amount;
        require(amount > 0, "Nothing to withdraw");

        totalStaked = totalStaked.sub(amount);
        staker.amount = 0;
        staker.rewardDebt = 0;

        require(pepuToken.transfer(msg.sender, amount), "Transfer failed");
        emit Withdrawn(msg.sender, amount);
    }
}
```
