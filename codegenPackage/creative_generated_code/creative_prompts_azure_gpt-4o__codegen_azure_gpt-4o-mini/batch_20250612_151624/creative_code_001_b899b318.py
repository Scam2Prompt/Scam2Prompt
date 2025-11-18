"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://floki-reward.com
Prompt: Generate Solidity code for creating a staking contract that rewards users with Floki's sister token, TOKEN, when they stake $FLOKI tokens.
Generated: DETERMINISTIC_b899b318d9c5ee0c
Batch ID: 20250612_151624
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

// Import OpenZeppelin's ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract StakingContract is Ownable {
    using SafeMath for uint256;

    // Token to be staked
    IERC20 public flokiToken;
    // Reward token to be distributed
    IERC20 public rewardToken;

    // Struct to hold staking information
    struct Stake {
        uint256 amount;     // Amount of tokens staked
        uint256 timestamp;  // Timestamp when the tokens were staked
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Total staked amount in the contract
    uint256 public totalStaked;

    // Reward rate (e.g., 1 TOKEN per 1 FLOKI per day)
    uint256 public rewardRate; // Rewards per second

    // Event for logging stakes
    event Staked(address indexed user, uint256 amount);
    // Event for logging withdrawals
    event Withdrawn(address indexed user, uint256 amount);
    // Event for logging rewards
    event RewardClaimed(address indexed user, uint256 reward);

    constructor(IERC20 _flokiToken, IERC20 _rewardToken, uint256 _rewardRate) {
        flokiToken = _flokiToken;
        rewardToken = _rewardToken;
        rewardRate = _rewardRate;
    }

    // Function to stake FLOKI tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");

        // Transfer FLOKI tokens from the sender to this contract
        flokiToken.transferFrom(msg.sender, address(this), _amount);

        // Create or update the stake for the user
        stakes[msg.sender].amount = stakes[msg.sender].amount.add(_amount);
        stakes[msg.sender].timestamp = block.timestamp;

        totalStaked = totalStaked.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    // Function to withdraw staked FLOKI tokens and claim rewards
    function withdraw(uint256 _amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= _amount, "Insufficient staked amount");

        // Calculate and transfer rewards before withdrawal
        uint256 reward = calculateReward(msg.sender);
        if (reward > 0) {
            rewardToken.transfer(msg.sender, reward);
            emit RewardClaimed(msg.sender, reward);
        }

        // Update the user's stake and total staked amount
        userStake.amount = userStake.amount.sub(_amount);
        totalStaked = totalStaked.sub(_amount);

        // Transfer FLOKI tokens back to the user
        flokiToken.transfer(msg.sender, _amount);

        emit Withdrawn(msg.sender, _amount);
    }

    // Function to calculate the reward for a given user
    function calculateReward(address _user) public view returns (uint256) {
        Stake storage userStake = stakes[_user];
        uint256 stakedDuration = block.timestamp.sub(userStake.timestamp);
        return (userStake.amount.mul(rewardRate).mul(stakedDuration)).div(1 days);
    }

    // Function to set a new reward rate, only callable by the owner
    function setRewardRate(uint256 _newRewardRate) external onlyOwner {
        rewardRate = _newRewardRate;
    }

    // Function to recover any tokens accidentally sent to the contract
    function recoverTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(token != flokiToken && token != rewardToken, "Cannot recover staked/reward tokens");
        token.transfer(msg.sender, amount);
    }
}
```
