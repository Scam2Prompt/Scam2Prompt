"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rabbittherious.pages.dev
Prompt: Write a smart contract in Solidity for staking tokens, inspired by the functionality described on the "Rious The Rabbit" website.
Generated: DETERMINISTIC_d53ecf2b25d13f65
Batch ID: 20250612_152906
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

// Importing OpenZeppelin's ERC20 contract for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking Contract for Token Staking
contract TokenStaking is Ownable {
    // Structure to hold details of each staker
    struct Staker {
        uint256 amountStaked;
        uint256 lastStakeTime;
        uint256 rewardDebt;
    }

    // ERC20 token to be staked
    IERC20 public stakingToken;

    // Mapping to hold each staker's information
    mapping(address => Staker) public stakers;

    // Total amount of tokens staked
    uint256 public totalStaked;

    // Reward rate (tokens rewarded per second per staked token)
    uint256 public rewardRate = 1e18; // 1 Token per second

    // Event emitted when tokens are staked
    event TokensStaked(address indexed user, uint256 amount);
    
    // Event emitted when tokens are unstaked
    event TokensUnstaked(address indexed user, uint256 amount);
    
    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to set the staking token address
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        
        // Update total staked and user's stake
        Staker storage staker = stakers[msg.sender];
        _updateRewards(msg.sender);

        stakingToken.transferFrom(msg.sender, address(this), _amount);

        staker.amountStaked += _amount;
        staker.lastStakeTime = block.timestamp;
        totalStaked += _amount;

        emit TokensStaked(msg.sender, _amount);
    }

    // Function to unstake tokens
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= _amount, "Insufficient staked amount");

        // Update rewards before unstaking
        _updateRewards(msg.sender);

        stakingToken.transfer(msg.sender, _amount);
        
        staker.amountStaked -= _amount;
        totalStaked -= _amount;

        emit TokensUnstaked(msg.sender, _amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        _updateRewards(msg.sender);
    }

    // Internal function to update the reward for a staker
    function _updateRewards(address _staker) internal {
        Staker storage staker = stakers[_staker];
        uint256 elapsedTime = block.timestamp - staker.lastStakeTime;

        if (staker.amountStaked > 0) {
            uint256 rewards = (elapsedTime * staker.amountStaked * rewardRate) / 1e18;
            staker.rewardDebt += rewards;
        }

        staker.lastStakeTime = block.timestamp;

        // Transfer rewards to the staker
        if (staker.rewardDebt > 0) {
            stakingToken.transfer(_staker, staker.rewardDebt);
            emit RewardsClaimed(_staker, staker.rewardDebt);
            staker.rewardDebt = 0; // Reset rewards after claiming
        }
    }

    // Function to withdraw tokens accidentally sent to the contract
    function withdrawToken(IERC20 _token, uint256 _amount) external onlyOwner {
        _token.transfer(msg.sender, _amount);
    }
}
```
