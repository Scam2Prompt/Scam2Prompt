"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sponge-claim.pages.dev
Prompt: Generate a Solidity smart contract snippet for staking $SPONGE tokens and calculating rewards based on the Sponge V2 reward rate of 343% p/a.
Generated: DETERMINISTIC_5645681fa3985039
Batch ID: 20250612_152000
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

// Import the ERC20 interface to interact with the $SPONGE token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// A contract for staking $SPONGE tokens and calculating rewards
contract SpongeStaking {
    // Variables to store references to the $SPONGE token and rewards
    IERC20 public spongeToken;
    uint256 public annualRewardRate = 343; // Annual reward rate in percentage
    uint256 public constant SECONDS_IN_A_YEAR = 365 * 24 * 60 * 60; // Total seconds in a year

    // Struct to hold staking information for each staker
    struct Staker {
        uint256 amountStaked; // Amount of tokens staked
        uint256 lastStakeTime; // Last time the staker staked tokens
    }

    // Mapping to hold staker information
    mapping(address => Staker) public stakers;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);
    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to initialize the contract with the $SPONGE token address
    constructor(address _spongeToken) {
        require(_spongeToken != address(0), "Invalid token address");
        spongeToken = IERC20(_spongeToken);
    }

    // Function to stake $SPONGE tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(spongeToken.balanceOf(msg.sender) >= _amount, "Insufficient balance");
        
        // Transfer tokens from the staker to the contract
        spongeToken.transferFrom(msg.sender, address(this), _amount);

        // Update the staker's information
        Staker storage staker = stakers[msg.sender];
        staker.amountStaked += _amount;
        staker.lastStakeTime = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    // Function to calculate the reward for a staker
    function calculateReward(address _staker) public view returns (uint256) {
        Staker storage staker = stakers[_staker];
        if (staker.amountStaked == 0) return 0;

        // Calculate the elapsed time since last stake
        uint256 elapsedTime = block.timestamp - staker.lastStakeTime;

        // Calculate the reward based on the annual rate
        uint256 reward = (staker.amountStaked * annualRewardRate / 100) * elapsedTime / SECONDS_IN_A_YEAR;
        return reward;
    }

    // Function to claim rewards
    function claimReward() external {
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards available");

        // Transfer rewards to the staker
        require(spongeToken.balanceOf(address(this)) >= reward, "Insufficient contract balance");
        spongeToken.transfer(msg.sender, reward);

        // Update last stake time after claiming rewards
        stakers[msg.sender].lastStakeTime = block.timestamp;

        emit RewardClaimed(msg.sender, reward);
    }

    // Function to get the total staked amount by a staker
    function getStakedAmount(address _staker) external view returns (uint256) {
        return stakers[_staker].amountStaked;
    }
}
```
