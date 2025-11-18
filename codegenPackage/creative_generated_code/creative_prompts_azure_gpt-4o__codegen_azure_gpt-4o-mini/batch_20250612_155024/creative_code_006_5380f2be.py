"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nooxnft.top
Prompt: Develop a smart contract for staking functionality that can be integrated into a dashboard like the one on the Ankr website.
Generated: DETERMINISTIC_5380f2bedcf09f2e
Batch ID: 20250612_155024
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

// Importing OpenZeppelin's SafeMath library for safe arithmetic operations
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract StakingContract is Ownable {
    using SafeMath for uint256;

    // Structure to hold information about each stake
    struct Stake {
        uint256 amount; // Amount staked
        uint256 timestamp; // Time when the stake was made
        bool isActive; // Status of the stake
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Total amount staked in the contract
    uint256 public totalStaked;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount, uint256 timestamp);
    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount, uint256 timestamp);

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");

        // Update user's stake information
        stakes[msg.sender].amount = stakes[msg.sender].amount.add(_amount);
        stakes[msg.sender].timestamp = block.timestamp;
        stakes[msg.sender].isActive = true;

        // Update total staked amount
        totalStaked = totalStaked.add(_amount);

        // Emit stake event
        emit Staked(msg.sender, _amount, block.timestamp);
    }

    // Function to unstake tokens
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.isActive, "No active stake found");
        require(userStake.amount > 0, "Stake amount must be greater than zero");

        uint256 amountToUnstake = userStake.amount;

        // Reset user's stake information
        userStake.amount = 0;
        userStake.isActive = false;

        // Update total staked amount
        totalStaked = totalStaked.sub(amountToUnstake);

        // Emit unstake event
        emit Unstaked(msg.sender, amountToUnstake, block.timestamp);

        // Transfer tokens back to the user (assuming the contract has the appropriate token balance and permission)
        // Note: Replace `tokenAddress` with the actual token contract address
        // IERC20(tokenAddress).transfer(msg.sender, amountToUnstake);
    }

    // Function to check the user's stake details
    function getStakeDetails(address _user) external view returns (uint256 amount, uint256 timestamp, bool isActive) {
        Stake memory userStake = stakes[_user];
        return (userStake.amount, userStake.timestamp, userStake.isActive);
    }

    // Function to withdraw the contract's balance (only owner)
    function withdraw(uint256 _amount) external onlyOwner {
        require(_amount <= address(this).balance, "Insufficient balance in the contract");
        payable(owner()).transfer(_amount);
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
