"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sale-humanizedai.web.app
Prompt: Develop a staking mechanism in Solidity where users can stake tokens and claim rewards, inspired by the staking functionality mentioned on the HumanizedAi presale site.
Generated: DETERMINISTIC_3febec09ca6bd7cc
Batch ID: 20250612_152109
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

// Importing OpenZeppelin ERC20 and Ownable contracts for token handling and ownership management
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking Contract for ERC20 Tokens
contract Staking is Ownable {
    // Struct to hold staking information for each user
    struct Staker {
        uint256 amountStaked; // Amount of tokens staked
        uint256 rewardDebt;   // Reward debt for calculating rewards
        uint256 lastStakedTime; // Timestamp of the last stake
    }

    // Mapping of user addresses to their staking information
    mapping(address => Staker) private stakers;

    // The ERC20 token being staked
    IERC20 public stakingToken;

    // Total rewards available for distribution
    uint256 public totalRewards;

    // Accumulated rewards per staked token
    uint256 public accRewardsPerShare;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event Claimed(address indexed user, uint256 reward);

    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to initialize the staking contract with the token address
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake 0 tokens");

        // Update the user's reward before staking
        _updateReward(msg.sender);

        // Transfer tokens from the user to the contract
        stakingToken.transferFrom(msg.sender, address(this), _amount);
        
        // Update the staker's information
        stakers[msg.sender].amountStaked += _amount;
        stakers[msg.sender].lastStakedTime = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        // Update the user's reward before claiming
        _updateReward(msg.sender);

        // Calculate the reward to claim
        uint256 reward = stakers[msg.sender].rewardDebt;
        require(reward > 0, "No rewards available to claim");

        // Set user's reward debt to zero after claiming
        stakers[msg.sender].rewardDebt = 0;

        // Transfer rewards to the user
        require(totalRewards >= reward, "Not enough rewards available");
        totalRewards -= reward;

        // Send reward to the user
        payable(msg.sender).transfer(reward);

        emit Claimed(msg.sender, reward);
    }

    // Function to unstake tokens
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Cannot unstake 0 tokens");
        require(stakers[msg.sender].amountStaked >= _amount, "Insufficient staked balance");

        // Update the user's reward before unstaking
        _updateReward(msg.sender);

        // Reduce the staker's amount and transfer tokens back
        stakers[msg.sender].amountStaked -= _amount;
        stakingToken.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    // Internal function to update rewards for a user
    function _updateReward(address _user) internal {
        Staker storage staker = stakers[_user];

        // Calculate the accumulated rewards based on the staked amount and time staked
        if (staker.amountStaked > 0) {
            uint256 pending = (staker.amountStaked * accRewardsPerShare / 1e12) - staker.rewardDebt;
            staker.rewardDebt += pending;
        }

        // Update the last staked time
        staker.lastStakedTime = block.timestamp;
    }

    // Function to add rewards to the pool
    function addRewards(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Cannot add 0 rewards");

        // Transfer rewards to the contract
        payable(address(this)).transfer(_amount);
        totalRewards += _amount;
    }

    // Function to set the reward amount per share
    function setRewardPerShare(uint256 _reward) external onlyOwner {
        accRewardsPerShare += _reward; // Update rewards per share
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
