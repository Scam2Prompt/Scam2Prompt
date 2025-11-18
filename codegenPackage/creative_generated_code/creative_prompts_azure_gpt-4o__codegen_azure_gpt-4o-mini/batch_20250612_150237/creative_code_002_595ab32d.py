"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proposal-b3.com
Prompt: Generate a smart contract for staking $B3 tokens within the hyper-operable gaming ecosystem described on the B3 platform.
Generated: DETERMINISTIC_595ab32dcc0c6be5
Batch ID: 20250612_150237
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

// Import OpenZeppelin ERC20 and Ownable contracts
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for StakingRewards
interface IStakingRewards {
    function notifyRewardAmount(uint256 reward) external;
}

contract B3Staking is Ownable {
    // Token being staked
    IERC20 public stakingToken;

    // Staking structure to hold user data
    struct Stake {
        uint256 amount;
        uint256 timestamp;
    }

    // Mapping from user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Total staked amount
    uint256 public totalStaked;

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to initialize the staking contract
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");

        // Transfer tokens from user to this contract
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Update user's stake information
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;
        
        // Update total staked amount
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        // Update user's stake information
        userStake.amount -= amount;
        
        // Transfer tokens back to the user
        stakingToken.transfer(msg.sender, amount);

        // Update total staked amount
        totalStaked -= amount;

        emit Unstaked(msg.sender, amount);
    }

    // Function to get the staked amount of a user
    function getStakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }

    // Function to withdraw any tokens accidentally sent to this contract
    function withdrawTokens(IERC20 token, uint256 amount) external onlyOwner {
        token.transfer(msg.sender, amount);
    }

    // Function to withdraw Ether accidentally sent to this contract
    function withdrawEther(uint256 amount) external onlyOwner {
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Ether withdrawal failed");
    }

    // Allow contract to receive Ether
    receive() external payable {}
}
```
