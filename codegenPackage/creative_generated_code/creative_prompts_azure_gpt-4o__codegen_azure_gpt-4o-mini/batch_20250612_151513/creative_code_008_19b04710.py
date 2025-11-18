"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btc-etftoken.web.app
Prompt: Write a Solidity contract for an ERC-20 token that includes a dynamic staking reward system, where rewards depend on the total amount of tokens staked by the community, as described for BTCETF.
Generated: DETERMINISTIC_19b04710f052fb04
Batch ID: 20250612_151513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// ERC20Token is a standard ERC-20 token with a staking reward system
contract ERC20Token is ERC20, Ownable {
    using SafeMath for uint256;

    // Staking structure to hold data for each staker
    struct Staker {
        uint256 amountStaked;
        uint256 rewardDebt;
    }

    // Mapping of addresses to their staking information
    mapping(address => Staker) public stakers;

    // Total staked tokens in the contract
    uint256 public totalStaked;

    // Reward per token staked per block
    uint256 public rewardPerToken;

    // Reward distribution event
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    constructor(string memory name, string memory symbol) ERC20(name, symbol) {
        // Initial minting of tokens for the owner
        _mint(msg.sender, 1000000 * 10 ** decimals());
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake 0 tokens");
        require(balanceOf(msg.sender) >= _amount, "Insufficient token balance");

        // Update the user's staking information before transferring tokens
        Staker storage staker = stakers[msg.sender];
        updateReward(msg.sender);

        // Transfer tokens from the user to the contract
        _transfer(msg.sender, address(this), _amount);

        // Update staker's information
        staker.amountStaked = staker.amountStaked.add(_amount);
        totalStaked = totalStaked.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake tokens
    function unstake(uint256 _amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= _amount, "Unstaking more than staked");

        // Update rewards before unstaking
        updateReward(msg.sender);

        // Update staker's information and total staked balance
        staker.amountStaked = staker.amountStaked.sub(_amount);
        totalStaked = totalStaked.sub(_amount);

        // Transfer tokens back to the user
        _transfer(address(this), msg.sender, _amount);
        
        emit Unstaked(msg.sender, _amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        updateReward(msg.sender);
        Staker storage staker = stakers[msg.sender];

        uint256 reward = staker.rewardDebt;
        require(reward > 0, "No rewards to claim");

        // Reset reward debt after claiming
        staker.rewardDebt = 0;

        // Mint and transfer rewards to user
        _mint(msg.sender, reward);
        emit RewardClaimed(msg.sender, reward);
    }

    // Internal function to update rewards for a user
    function updateReward(address _user) internal {
        Staker storage staker = stakers[_user];
        if (totalStaked > 0) {
            uint256 userReward = staker.amountStaked.mul(rewardPerToken).div(1e18);
            staker.rewardDebt = staker.rewardDebt.add(userReward);
        }
    }

    // Function to set reward per token (only owner)
    function setRewardPerToken(uint256 _rewardPerToken) external onlyOwner {
        require(_rewardPerToken > 0, "Reward must be greater than 0");
        rewardPerToken = _rewardPerToken;
    }

    // Function to get total staked tokens
    function getTotalStaked() external view returns (uint256) {
        return totalStaked;
    }
}
```
