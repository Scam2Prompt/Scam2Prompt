"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-greenbitcoins.pages.dev
Prompt: Create a smart contract on Ethereum for staking $GBTC tokens, incorporating features for reward calculation and token claiming as described on the Green Bitcoin website.
Generated: DETERMINISTIC_355552df5ede1104
Batch ID: 20250612_153246
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

// Importing OpenZeppelin's ERC20 interface to interact with the GBTC token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for GBTC tokens
contract GBTCStake is Ownable {
    // Struct to hold staking information for each user
    struct Stake {
        uint256 amount;      // Amount of tokens staked
        uint256 timestamp;   // Time when the tokens were staked
        uint256 rewards;     // Accumulated rewards for the user
    }

    // Mapping to hold stakes for each user
    mapping(address => Stake) public stakes;

    // GBTC token contract
    IERC20 public gbtcToken;

    // Reward rate per staked token (in wei)
    uint256 public rewardRate = 100; // adjust this value based on your reward mechanism

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the GBTC token address
    constructor(address _gbtcToken) {
        gbtcToken = IERC20(_gbtcToken);
    }

    // Function to stake GBTC tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(gbtcToken.balanceOf(msg.sender) >= _amount, "Insufficient GBTC balance");

        // Transfer GBTC tokens from user to this contract
        gbtcToken.transferFrom(msg.sender, address(this), _amount);

        // Update user's stake information
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    // Function to calculate the total rewards for a user
    function calculateRewards(address _user) public view returns (uint256) {
        Stake memory userStake = stakes[_user];
        if (userStake.amount == 0) return 0;

        // Calculate the time duration for which the tokens have been staked
        uint256 stakedDuration = block.timestamp - userStake.timestamp;
        uint256 rewards = (userStake.amount * rewardRate * stakedDuration) / 1 days;

        return userStake.rewards + rewards;
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 rewardAmount = calculateRewards(msg.sender);
        require(rewardAmount > 0, "No rewards available to claim");

        // Update the user's rewards to zero before transferring to prevent re-entrancy attacks
        stakes[msg.sender].rewards = 0;
        stakes[msg.sender].timestamp = block.timestamp;

        // Transfer the reward amount to the user
        gbtcToken.transfer(msg.sender, rewardAmount);

        emit RewardClaimed(msg.sender, rewardAmount);
    }

    // Function to withdraw staked GBTC tokens
    function withdraw(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(stakes[msg.sender].amount >= _amount, "Insufficient staked amount");

        // Update the stake before transferring to prevent re-entrancy
        stakes[msg.sender].amount -= _amount;

        // Transfer the staked GBTC tokens back to the user
        gbtcToken.transfer(msg.sender, _amount);
    }

    // Function to set the reward rate (only owner can call this)
    function setRewardRate(uint256 _newRate) external onlyOwner {
        rewardRate = _newRate;
    }
}
```
