"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-io-dashborad.pages.dev
Prompt: Write a smart contract in Solidity for staking DOGE20 tokens on Ethereum that distributes rewards to stakers proportionally over a two-year period, as described in the Dogecoin20 roadmap.
Generated: DETERMINISTIC_0bfc0cc5a0e5873d
Batch ID: 20250612_153526
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

// Import required OpenZeppelin contracts
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for DOGE20 token
contract Doge20Staking is Ownable {
    // Define the DOGE20 token interface
    IERC20 public doge20Token;

    // Staking structure to hold user information
    struct Staker {
        uint256 amountStaked;
        uint256 rewardDebt;
        uint256 lastStakedTime;
    }

    // Mapping to track each staker's information
    mapping(address => Staker) public stakers;

    // Total amount of DOGE20 tokens staked
    uint256 public totalStaked;

    // Reward distribution parameters
    uint256 public constant REWARD_PERIOD = 730 days; // 2 years in seconds
    uint256 public rewardRate; // Reward rate per second
    uint256 public totalRewards; // Total rewards to distribute

    // Event for staking
    event Staked(address indexed user, uint256 amount);
    
    // Event for unstaking
    event Unstaked(address indexed user, uint256 amount);

    // Event for reward claiming
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize contract
    constructor(address _doge20Token, uint256 _totalRewards) {
        doge20Token = IERC20(_doge20Token);
        totalRewards = _totalRewards;
        rewardRate = totalRewards / REWARD_PERIOD; // Calculate reward rate
    }

    // Function to stake DOGE20 tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        
        // Transfer DOGE20 tokens from user to contract
        doge20Token.transferFrom(msg.sender, address(this), _amount);
        
        // Update staker's data
        Staker storage staker = stakers[msg.sender];
        staker.amountStaked += _amount;
        staker.rewardDebt += calculatePendingRewards(msg.sender);
        staker.lastStakedTime = block.timestamp;

        // Update total staked amount
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake DOGE20 tokens
    function unstake(uint256 _amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= _amount, "Insufficient staked amount");

        // Calculate and claim pending rewards before unstaking
        uint256 pendingRewards = calculatePendingRewards(msg.sender);
        if (pendingRewards > 0) {
            claimRewards();
        }

        // Update staker's data
        staker.amountStaked -= _amount;
        totalStaked -= _amount;

        // Transfer DOGE20 tokens back to the user
        doge20Token.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    // Function to claim rewards
    function claimRewards() public {
        Staker storage staker = stakers[msg.sender];
        uint256 pendingRewards = calculatePendingRewards(msg.sender);
        
        require(pendingRewards > 0, "No rewards to claim");

        // Reset reward debt and last staked time
        staker.rewardDebt = 0;
        staker.lastStakedTime = block.timestamp;

        // Transfer rewards to the user
        doge20Token.transfer(msg.sender, pendingRewards);

        emit RewardsClaimed(msg.sender, pendingRewards);
    }

    // Function to calculate pending rewards for a staker
    function calculatePendingRewards(address _staker) internal view returns (uint256) {
        Staker storage staker = stakers[_staker];
        uint256 timeStaked = block.timestamp - staker.lastStakedTime;
        return (staker.amountStaked * rewardRate * timeStaked);
    }

    // Fallback function to prevent accidental ETH transfers
    receive() external payable {
        revert("Contract does not accept ETH");
    }
}
```
