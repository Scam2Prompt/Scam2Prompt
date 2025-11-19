"""
Generated Code Metadata:
========================
Original URL: https://app-daomars-com.pages.dev
Prompt: Write a smart contract for an automated re-staking mechanism similar to the AUTO.FARM platform described in the MarsDAO ecosystem.
Generated: DETERMINISTIC_d791757455f0abe2
Batch ID: 20250612_152439
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Smart contract for automated re-staking mechanism
contract AutoReStake is Ownable {
    using SafeMath for uint256;

    // State variables
    IERC20 public stakingToken; // Token to be staked
    IERC20 public rewardToken;  // Token received as rewards
    uint256 public rewardRate;  // Rate at which rewards are generated
    uint256 public lastUpdateTime; // Last time rewards were updated
    uint256 public rewardPerTokenStored; // Accumulated rewards per token

    mapping(address => uint256) public userRewardPerTokenPaid; // User's reward per token paid
    mapping(address => uint256) public rewards; // User's rewards
    mapping(address => uint256) public balances; // User's staked balances

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    // Constructor to initialize the contract
    constructor(IERC20 _stakingToken, IERC20 _rewardToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
        rewardRate = _rewardRate;
        lastUpdateTime = block.timestamp;
    }

    // Modifier to update rewards
    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = block.timestamp;
        if (account != address(0)) {
            rewards[account] = earned(account);
            userRewardPerTokenPaid[account] = rewardPerTokenStored;
        }
        _;
    }

    // Function to calculate reward per token
    function rewardPerToken() public view returns (uint256) {
        if (totalSupply() == 0) {
            return rewardPerTokenStored;
        }
        return rewardPerTokenStored.add(
            block.timestamp.sub(lastUpdateTime).mul(rewardRate).div(totalSupply())
        );
    }

    // Function to calculate earned rewards for a user
    function earned(address account) public view returns (uint256) {
        return balances[account]
            .mul(rewardPerToken().sub(userRewardPerTokenPaid[account]))
            .div(1e18)
            .add(rewards[account]);
    }

    // Function to stake tokens
    function stake(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        balances[msg.sender] = balances[msg.sender].add(amount);
        stakingToken.transferFrom(msg.sender, address(this), amount);
        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0");
        require(balances[msg.sender] >= amount, "Insufficient balance");
        balances[msg.sender] = balances[msg.sender].sub(amount);
        stakingToken.transfer(msg.sender, amount);
        emit Withdrawn(msg.sender, amount);
    }

    // Function to claim rewards
    function getReward() external updateReward(msg.sender) {
        uint256 reward = rewards[msg.sender];
        if (reward > 0) {
            rewards[msg.sender] = 0;
            rewardToken.transfer(msg.sender, reward);
            emit RewardPaid(msg.sender, reward);
        }
    }

    // Function to automatically re-stake rewards
    function autoReStake() external updateReward(msg.sender) {
        uint256 reward = rewards[msg.sender];
        if (reward > 0) {
            rewards[msg.sender] = 0;
            // Stake the earned rewards
            balances[msg.sender] = balances[msg.sender].add(reward);
            stakingToken.transferFrom(address(this), msg.sender, reward);
            emit Staked(msg.sender, reward);
        }
    }

    // Function to get total supply of staked tokens
    function totalSupply() public view returns (uint256) {
        return stakingToken.balanceOf(address(this));
    }
}
```
