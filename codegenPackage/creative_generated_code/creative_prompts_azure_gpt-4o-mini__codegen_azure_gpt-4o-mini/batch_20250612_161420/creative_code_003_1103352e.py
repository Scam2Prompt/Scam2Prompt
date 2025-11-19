"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greenbtc-token.pages.dev
Prompt: Generate code for a smart contract that allows users to stake $GBTC tokens and earn rewards based on their predictions.
Generated: DETERMINISTIC_1103352ec7aba333
Batch ID: 20250612_161420
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

// Interface for the GBTC token
interface IGBTC {
    function transfer(address to, uint256 amount) external returns (bool);
    function balanceOf(address owner) external view returns (uint256);
}

contract StakingRewards {
    // Struct to hold user staking data
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Time when the tokens were staked
        bool hasClaimed; // Flag to check if rewards have been claimed
    }

    // Mapping to track user stakes
    mapping(address => Stake) public stakes;

    // Address of the GBTC token contract
    IGBTC public gbtcToken;

    // Reward rate per second for staking
    uint256 public rewardRate; // E.g., 1 token per second

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event Claimed(address indexed user, uint256 reward);

    // Modifier to ensure user has staked tokens
    modifier hasStaked() {
        require(stakes[msg.sender].amount > 0, "No tokens staked");
        _;
    }

    // Constructor to initialize the contract with the GBTC token address and reward rate
    constructor(address _gbtcToken, uint256 _rewardRate) {
        gbtcToken = IGBTC(_gbtcToken);
        rewardRate = _rewardRate;
    }

    // Function for users to stake GBTC tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(gbtcToken.balanceOf(msg.sender) >= _amount, "Insufficient GBTC balance");

        // Transfer GBTC tokens from user to the contract
        gbtcToken.transfer(address(this), _amount);

        // Update the staking details
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].timestamp = block.timestamp;
        stakes[msg.sender].hasClaimed = false;

        emit Staked(msg.sender, _amount);
    }

    // Function to calculate the rewards for a user
    function calculateRewards(address _user) public view returns (uint256) {
        Stake memory userStake = stakes[_user];

        if (userStake.amount == 0) return 0; // No tokens staked

        // Calculate the time staked
        uint256 stakingDuration = block.timestamp - userStake.timestamp;

        // Calculate rewards based on the staking duration and reward rate
        return (stakingDuration * userStake.amount * rewardRate) / 1e18; // Using 1e18 for precision
    }

    // Function for users to claim their rewards
    function claimRewards() external hasStaked {
        uint256 reward = calculateRewards(msg.sender);
        require(reward > 0, "No rewards to claim");
        
        // Update the staking data
        stakes[msg.sender].hasClaimed = true;
        stakes[msg.sender].timestamp = block.timestamp; // Reset timestamp for new reward calculation

        // Transfer reward to the user (Assuming rewards are paid in GBTC tokens)
        require(gbtcToken.transfer(msg.sender, reward), "Transfer failed");

        emit Claimed(msg.sender, reward);
    }

    // Function to get the staked amount of the user
    function getStakedAmount() external view returns (uint256) {
        return stakes[msg.sender].amount;
    }
}
```
