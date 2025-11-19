"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btcbulltoken.pages.dev
Prompt: Generate a smart contract in Solidity for staking $BTCBULL tokens that rewards users with Bitcoin airdrops as the price of Bitcoin increases.
Generated: DETERMINISTIC_86bfb30cd9e37375
Batch ID: 20250612_161041
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

// Importing OpenZeppelin's ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract BTCBULLStaking is ReentrancyGuard, Ownable {
    // ERC20 token contract for BTCBULL
    IERC20 public btcBullToken;

    // Struct to hold staking information
    struct Staker {
        uint256 amountStaked;  // Amount of BTCBULL tokens staked
        uint256 lastClaimed;   // Last time rewards were claimed
        uint256 totalReward;    // Total rewards earned
    }

    // Mapping of stakers' addresses to their staking information
    mapping(address => Staker) public stakers;

    // Event to emit when tokens are staked
    event Staked(address indexed user, uint256 amount);
    
    // Event to emit when rewards are claimed
    event Claimed(address indexed user, uint256 reward);

    // Bitcoin reward rate per second (example: 10 wei per second)
    uint256 public rewardRate = 10;

    // Constructor to initialize the contract with the BTCBULL token address
    constructor(address _btcBullToken) {
        require(_btcBullToken != address(0), "Invalid BTCBULL token address");
        btcBullToken = IERC20(_btcBullToken);
    }

    // Function to stake BTCBULL tokens
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        
        // Transfer BTCBULL tokens from msg.sender to this contract
        btcBullToken.transferFrom(msg.sender, address(this), _amount);
        
        // Update the staker's information
        Staker storage staker = stakers[msg.sender];
        staker.amountStaked += _amount;
        staker.lastClaimed = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    // Function to calculate pending rewards for a staker
    function calculateRewards(address _staker) internal view returns (uint256) {
        Staker storage staker = stakers[_staker];
        uint256 timeStaked = block.timestamp - staker.lastClaimed;
        return staker.amountStaked * rewardRate * timeStaked;
    }

    // Function to claim rewards
    function claimRewards() external nonReentrant {
        uint256 reward = calculateRewards(msg.sender);
        require(reward > 0, "No rewards to claim");

        // Update last claimed time and total rewards
        Staker storage staker = stakers[msg.sender];
        staker.lastClaimed = block.timestamp;
        staker.totalReward += reward;

        // Transfer Bitcoin rewards (in this case, we use the native token)
        payable(msg.sender).transfer(reward);

        emit Claimed(msg.sender, reward);
    }

    // Function to withdraw staked BTCBULL tokens
    function withdraw(uint256 _amount) external nonReentrant {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= _amount, "Not enough tokens staked");

        // Calculate pending rewards before withdrawal
        uint256 reward = calculateRewards(msg.sender);
        if (reward > 0) {
            staker.lastClaimed = block.timestamp;
            staker.totalReward += reward;
            payable(msg.sender).transfer(reward);
        }

        // Update staker's amount staked
        staker.amountStaked -= _amount;
        btcBullToken.transfer(msg.sender, _amount);
    }

    // Function to set a new reward rate (only owner can call)
    function setRewardRate(uint256 _newRate) external onlyOwner {
        rewardRate = _newRate;
    }

    // Fallback function to receive native tokens
    receive() external payable {}
}
```
