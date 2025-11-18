"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stakewise.eu
Prompt: Create a smart contract example that interacts with StakeWise for staking Ethereum and distributing rewards.
Generated: DETERMINISTIC_b2ec348573be2dc1
Batch ID: 20250612_145832
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

// Interface for StakeWise staking contract
interface IStakeWise {
    function stake(uint256 amount) external;
    function withdraw(uint256 amount) external;
    function claimRewards() external;
    function getRewardBalance(address account) external view returns (uint256);
}

contract StakingManager {
    // State variables
    address public owner;
    IStakeWise public stakeWiseContract;
    mapping(address => uint256) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }
    
    // Constructor to set the StakeWise contract address
    constructor(address _stakeWiseAddress) {
        owner = msg.sender;
        stakeWiseContract = IStakeWise(_stakeWiseAddress);
    }

    // Function to stake Ether in StakeWise
    function stake() external payable {
        require(msg.value > 0, "Must stake a non-zero amount");

        // Update the user's stake
        stakes[msg.sender] += msg.value;

        // Stake the Ether in StakeWise
        stakeWiseContract.stake(msg.value);
        
        emit Staked(msg.sender, msg.value);
    }

    // Function to withdraw staked Ether from StakeWise
    function withdraw(uint256 amount) external {
        require(amount > 0, "Must withdraw a non-zero amount");
        require(stakes[msg.sender] >= amount, "Insufficient staked amount");

        // Update the user's stake
        stakes[msg.sender] -= amount;

        // Withdraw the Ether from StakeWise
        stakeWiseContract.withdraw(amount);

        // Transfer the withdrawn Ether back to the user
        payable(msg.sender).transfer(amount);
        
        emit Withdrawn(msg.sender, amount);
    }

    // Function to claim staking rewards from StakeWise
    function claimRewards() external {
        uint256 rewards = stakeWiseContract.getRewardBalance(msg.sender);
        require(rewards > 0, "No rewards to claim");

        // Claim rewards
        stakeWiseContract.claimRewards();
        
        emit RewardsClaimed(msg.sender, rewards);
    }

    // Function to withdraw ownership of the contract
    function withdrawOwnership() external onlyOwner {
        owner = address(0);
    }

    // Fallback function to accept Ether
    receive() external payable {}

    // Function to allow the owner to withdraw any Ether from the contract
    function withdrawContractBalance() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");
        payable(owner).transfer(balance);
    }
}
```
