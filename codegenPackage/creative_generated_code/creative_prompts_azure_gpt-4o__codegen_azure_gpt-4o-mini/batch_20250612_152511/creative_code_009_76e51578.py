"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://portal-coln.pages.dev
Prompt: Create a Solidity contract example for a token farming system where users can stake BNB or FDUSD to earn $PORTAL tokens, ensuring rewards are distributed based on staking duration.
Generated: DETERMINISTIC_76e51578477a60b4
Batch ID: 20250612_152511
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

// Import the OpenZeppelin contracts for ERC20 token and Ownable functionality
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// TokenFarm contract for staking BNB or FDUSD to earn $PORTAL tokens
contract TokenFarm is Ownable {
    // Define the struct for staking data
    struct Staker {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Reward debt for the staker
        uint256 lastStakedTime; // Last time the user staked tokens
    }

    // Mapping of user addresses to their staking details
    mapping(address => Staker) public stakers;

    // The ERC20 token that will be rewarded for staking
    IERC20 public portalToken;

    // The accepted token for staking (FDUSD)
    IERC20 public stakeToken;

    // Rate of reward per second for staked tokens
    uint256 public rewardRate = 1e18; // Example: 1 PORTAL token per second per token staked

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);
    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount);
    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the token addresses
    constructor(IERC20 _portalToken, IERC20 _stakeToken) {
        portalToken = _portalToken;
        stakeToken = _stakeToken;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake 0");
        // Transfer the stake tokens from user to this contract
        stakeToken.transferFrom(msg.sender, address(this), _amount);

        // Update staker information
        Staker storage staker = stakers[msg.sender];
        staker.amount += _amount;
        staker.lastStakedTime = block.timestamp;
        
        emit Staked(msg.sender, _amount);
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 _amount) external {
        Staker storage staker = stakers[msg.sender];
        require(_amount > 0 && _amount <= staker.amount, "Invalid withdraw amount");

        // Calculate and pay rewards before withdrawal
        uint256 reward = calculateReward(msg.sender);
        if (reward > 0) {
            portalToken.transfer(msg.sender, reward);
            emit RewardClaimed(msg.sender, reward);
        }

        // Transfer the tokens back to the user
        staker.amount -= _amount;
        stakeToken.transfer(msg.sender, _amount);
        
        emit Withdrawn(msg.sender, _amount);
    }

    // Function to calculate reward for the staker
    function calculateReward(address _user) public view returns (uint256) {
        Staker storage staker = stakers[_user];
        uint256 duration = block.timestamp - staker.lastStakedTime;
        return (staker.amount * rewardRate * duration) / 1e18; // Adjusting for token decimals
    }

    // Function to allow users to claim their rewards
    function claimReward() external {
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No reward available");

        // Update the last staked time to current block timestamp
        stakers[msg.sender].lastStakedTime = block.timestamp;
        
        // Transfer the reward tokens to the user
        portalToken.transfer(msg.sender, reward);
        emit RewardClaimed(msg.sender, reward);
    }

    // Function to update the reward rate (only callable by owner)
    function updateRewardRate(uint256 _newRate) external onlyOwner {
        rewardRate = _newRate;
    }
}
```
