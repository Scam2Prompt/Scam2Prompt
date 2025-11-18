"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lingo-bqh.pages.dev
Prompt: Develop a smart contract that implements a priority-based token allocation system, allowing certain users to skip the queue based on predefined membership tiers.
Generated: DETERMINISTIC_144fdec8505db917
Batch ID: 20250612_150226
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

// Importing OpenZeppelin's Ownable and SafeMath for security and safety
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Define the Smart Contract
contract PriorityTokenAllocation is Ownable {
    using SafeMath for uint256;

    // Enum for membership tiers
    enum MembershipTier { None, Silver, Gold, Platinum }

    // Struct to represent a user
    struct User {
        MembershipTier tier;
        uint256 allocation;
    }

    // Mapping to store user information
    mapping(address => User) public users;

    // Total tokens available for allocation
    uint256 public totalTokens;
    // Total tokens already allocated
    uint256 public allocatedTokens;

    // Events for logging
    event TokensAllocated(address indexed user, uint256 amount);
    event MembershipUpdated(address indexed user, MembershipTier tier);

    // Modifier to check if enough tokens are available
    modifier hasSufficientTokens(uint256 _amount) {
        require(allocatedTokens.add(_amount) <= totalTokens, "Insufficient tokens available");
        _;
    }

    // Constructor to initialize total tokens
    constructor(uint256 _totalTokens) {
        require(_totalTokens > 0, "Total tokens must be greater than 0");
        totalTokens = _totalTokens;
    }

    // Function to update user membership tier
    function updateMembership(address _user, MembershipTier _tier) external onlyOwner {
        users[_user].tier = _tier;
        emit MembershipUpdated(_user, _tier);
    }

    // Function to allocate tokens based on membership tiers
    function allocateTokens(uint256 _amount) external hasSufficientTokens(_amount) {
        User storage user = users[msg.sender];
        uint256 priorityMultiplier = _getPriorityMultiplier(user.tier);
        uint256 allocationAmount = _amount.mul(priorityMultiplier);

        // Update user's allocation and total allocated tokens
        user.allocation = user.allocation.add(allocationAmount);
        allocatedTokens = allocatedTokens.add(allocationAmount);

        emit TokensAllocated(msg.sender, allocationAmount);
    }

    // Internal function to get priority multiplier based on membership tier
    function _getPriorityMultiplier(MembershipTier _tier) internal pure returns (uint256) {
        if (_tier == MembershipTier.Platinum) {
            return 4;
        } else if (_tier == MembershipTier.Gold) {
            return 3;
        } else if (_tier == MembershipTier.Silver) {
            return 2;
        } else {
            return 1; // None tier has the lowest priority
        }
    }

    // Function to retrieve user's allocation
    function getUserAllocation(address _user) external view returns (uint256) {
        return users[_user].allocation;
    }

    // Function to retrieve total available tokens
    function getRemainingTokens() external view returns (uint256) {
        return totalTokens.sub(allocatedTokens);
    }
}
```
