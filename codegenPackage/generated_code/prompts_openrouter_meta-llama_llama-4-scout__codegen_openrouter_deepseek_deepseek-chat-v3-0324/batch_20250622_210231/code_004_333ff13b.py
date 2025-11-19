"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20s.pages.dev
Prompt: Design a basic smart contract in Solidity for distributing staking rewards to DOGE20 token holders over a period of two years, utilizing Ethereum's smart contract capabilities.
Generated: DETERMINISTIC_333ff13b0c1bca3a
Batch ID: 20250622_210231
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

contract DOGE20StakingRewards is Ownable {
    using SafeMath for uint256;

    IERC20 public token;
    uint256 public totalStaked;
    uint256 public rewardRate;
    uint256 public startTime;
    uint256 public endTime;
    uint256 public lastUpdateTime;
    uint256 public rewardPerTokenStored;
    uint256 public constant DURATION = 730 days; // 2 years

    struct Staker {
        uint256 balance;
        uint256 rewards;
        uint256 userRewardPerTokenPaid;
    }

    mapping(address => Staker) public stakers;

    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    constructor(address _token, uint256 _totalRewards) {
        token = IERC20(_token);
        startTime = block.timestamp;
        endTime = startTime.add(DURATION);
        rewardRate = _totalRewards.div(DURATION);
    }

    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = lastTimeRewardApplicable();
        if (account != address(0)) {
            stakers[account].rewards = earned(account);
            stakers[account].userRewardPerTokenPaid = rewardPerTokenStored;
        }
        _;
    }

    function lastTimeRewardApplicable() public view returns (uint256) {
        return block.timestamp < endTime ? block.timestamp : endTime;
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
        return
            stakers[account]
                .balance
                .mul(rewardPerToken().sub(stakers[account].userRewardPerTokenPaid))
                .div(1e18)
                .add(stakers[account].rewards);
    }

    function stake(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        require(block.timestamp < endTime, "Staking period has ended");

        stakers[msg.sender].balance = stakers[msg.sender].balance.add(amount);
        totalStaked = totalStaked.add(amount);
        token.transferFrom(msg.sender, address(this), amount);
        emit Staked(msg.sender, amount);
    }

    function withdraw(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0");
        stakers[msg.sender].balance = stakers[msg.sender].balance.sub(amount);
        totalStaked = totalStaked.sub(amount);
        token.transfer(msg.sender, amount);
        emit Withdrawn(msg.sender, amount);
    }

    function getReward() external updateReward(msg.sender) {
        uint256 reward = stakers[msg.sender].rewards;
        if (reward > 0) {
            stakers[msg.sender].rewards = 0;
            token.transfer(msg.sender, reward);
            emit RewardPaid(msg.sender, reward);
        }
    }

    function exit() external {
        withdraw(stakers[msg.sender].balance);
        getReward();
    }

    function recoverERC20(address tokenAddress, uint256 tokenAmount) external onlyOwner {
        require(tokenAddress != address(token), "Cannot withdraw the staking token");
        IERC20(tokenAddress).transfer(owner(), tokenAmount);
    }
}
```
