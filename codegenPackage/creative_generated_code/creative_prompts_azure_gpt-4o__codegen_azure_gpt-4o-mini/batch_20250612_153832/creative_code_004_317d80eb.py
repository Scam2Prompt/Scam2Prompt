"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stakingstory.org
Prompt: Develop a smart contract for staking assets using the Story Staking protocol, incorporating features like flexible withdrawal options and dynamic interest rates.
Generated: DETERMINISTIC_317d80eba24e7a2c
Batch ID: 20250612_153832
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

// Importing required OpenZeppelin contracts for security
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for assets using Story Staking protocol
contract StoryStaking is Ownable {
    // Struct to hold information about each staker
    struct Staker {
        uint256 amount; // Amount staked
        uint256 timestamp; // Timestamp of the last stake action
        uint256 interestRate; // Current interest rate for this staker
    }

    // Mapping to track stakers and their information
    mapping(address => Staker) private stakers;

    // Total staked amount in the contract
    uint256 public totalStaked;

    // Dynamic interest rate based on the amount staked
    function getInterestRate(uint256 amount) internal pure returns (uint256) {
        // Define interest rates based on amount staked
        if (amount < 1 ether) {
            return 5; // 5% for < 1 Ether
        } else if (amount < 5 ether) {
            return 10; // 10% for < 5 Ether
        } else {
            return 15; // 15% for >= 5 Ether
        }
    }

    // Event emitted when assets are staked
    event Staked(address indexed staker, uint256 amount);

    // Event emitted when assets are withdrawn
    event Withdrawn(address indexed staker, uint256 amount);

    // Function to stake assets
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer tokens to this contract
        IERC20 token = IERC20(address(this)); // Replace with actual token address
        require(token.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update staker's information
        stakers[msg.sender].amount += amount;
        stakers[msg.sender].timestamp = block.timestamp;
        stakers[msg.sender].interestRate = getInterestRate(stakers[msg.sender].amount);

        // Update total staked amount
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked assets along with interest
    function withdraw(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amount >= amount, "Insufficient staked balance");

        // Calculate interest based on the staker's interest rate and time
        uint256 interest = (amount * staker.interestRate * (block.timestamp - staker.timestamp)) / (100 * 365 days);
        
        // Update staker's information
        staker.amount -= amount;
        totalStaked -= amount;
        staker.timestamp = block.timestamp; // Reset timestamp

        // Transfer token and interest back to the staker
        IERC20 token = IERC20(address(this)); // Replace with actual token address
        require(token.transfer(msg.sender, amount + interest), "Transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    // Function to get the staked balance of a user
    function getStakedAmount(address user) external view returns (uint256) {
        return stakers[user].amount;
    }

    // Function to get the interest rate of a user
    function getUserInterestRate(address user) external view returns (uint256) {
        return stakers[user].interestRate;
    }

    // Function to get the total staked amount in the contract
    function getTotalStaked() external view returns (uint256) {
        return totalStaked;
    }
}
```
