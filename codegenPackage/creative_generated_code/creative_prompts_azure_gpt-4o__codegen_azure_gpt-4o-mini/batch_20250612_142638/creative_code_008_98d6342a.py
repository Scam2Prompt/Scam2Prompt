"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hyperliquid.gg
Prompt: Create a Solidity-based smart contract for staking HYPE tokens on Hyperliquid, ensuring transparency and user control over rewards distribution.
Generated: DETERMINISTIC_98d6342a566486da
Batch ID: 20250612_142638
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

// Importing OpenZeppelin's ERC20 interface for HYPE token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract HypeStaking {
    // State variables
    IERC20 public hypeToken; // HYPE token interface
    address public owner; // Owner of the contract
    uint256 public totalStaked; // Total amount of HYPE tokens staked

    // Struct to hold user stake information
    struct Stake {
        uint256 amount; // Amount staked
        uint256 rewardDebt; // Reward debt of the user
    }

    // Mapping of user addresses to their stake information
    mapping(address => Stake) public stakes;

    // Events for logging important actions
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to initialize the contract with HYPE token address
    constructor(address _hypeToken) {
        require(_hypeToken != address(0), "Invalid HYPE token address");
        hypeToken = IERC20(_hypeToken);
        owner = msg.sender;
    }

    // Function to stake HYPE tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(hypeToken.balanceOf(msg.sender) >= _amount, "Insufficient HYPE balance");

        // Update user's stake information
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += _amount;
        userStake.rewardDebt = (_amount * calculateRewardRate()) / 1e18;

        // Transfer HYPE tokens from user to this contract
        hypeToken.transferFrom(msg.sender, address(this), _amount);

        // Update total staked amount
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake HYPE tokens
    function unstake(uint256 _amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= _amount, "Insufficient staked amount");

        // Update user's stake information
        userStake.amount -= _amount;

        // Transfer HYPE tokens back to the user
        hypeToken.transfer(msg.sender, _amount);

        // Update total staked amount
        totalStaked -= _amount;

        emit Unstaked(msg.sender, _amount);
    }

    // Function to claim staking rewards
    function claimRewards() external {
        Stake storage userStake = stakes[msg.sender];
        uint256 reward = calculateReward(userStake.amount, userStake.rewardDebt);

        require(reward > 0, "No rewards available to claim");

        // Reset the user's reward debt
        userStake.rewardDebt = (userStake.amount * calculateRewardRate()) / 1e18;

        // Transfer rewards to the user (assuming rewards are in HYPE tokens for simplicity)
        hypeToken.transfer(msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }

    // Function to calculate rewards based on user's staked amount
    function calculateReward(uint256 _amount, uint256 _rewardDebt) internal view returns (uint256) {
        // This is a placeholder for reward calculation logic
        return (_amount * calculateRewardRate() / 1e18) - _rewardDebt;
    }

    // Function to represent the reward rate (placeholder, this can be adjusted)
    function calculateRewardRate() internal view returns (uint256) {
        // Placeholder: implement actual reward rate calculation logic
        return 1e18; // 1 reward unit per staked unit (for example)
    }

    // Function to withdraw any ERC20 tokens erroneously sent to the contract
    function withdrawTokens(address _tokenAddress, uint256 _amount) external {
        require(msg.sender == owner, "Only owner can withdraw tokens");
        require(_tokenAddress != address(hypeToken), "Cannot withdraw staked HYPE tokens");
        
        IERC20(_tokenAddress).transfer(owner, _amount);
    }
}
```
