"""
Generated Code Metadata:
========================
Original URL: https://giveaway-associates.pages.dev
Prompt: Create a smart contract using ChainGPT's no-code smart contract generator to manage token allocations based on GAINS tier levels (Planktons, Fishes, Dolphins, Sharks, Whales).
Generated: DETERMINISTIC_a14061b917b5f13d
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract GAINSTokenAllocator is Ownable, ReentrancyGuard {
    // Tier structure
    struct Tier {
        string name;
        uint256 allocationMultiplier; // Multiplier for base allocation (e.g., 100 = 1x)
        uint256 minHoldingRequirement; // Minimum tokens required to be in this tier
    }

    // User information
    struct UserInfo {
        uint256 tierIndex;
        uint256 lastClaimTime;
        uint256 totalAllocated;
        uint256 totalClaimed;
    }

    // Token contract
    IERC20 public gainsToken;

    // Allocation settings
    uint256 public baseAllocationAmount;
    uint256 public allocationInterval; // Time between allocations in seconds

    // Tiers
    Tier[] public tiers;
    mapping(address => UserInfo) public userInfo;

    // Events
    event TierAdded(uint256 indexed tierId, string name, uint256 multiplier, uint256 minHolding);
    event AllocationClaimed(address indexed user, uint256 amount);
    event TierUpdated(address indexed user, uint256 oldTier, uint256 newTier);

    constructor(
        address _gainsToken,
        uint256 _baseAllocationAmount,
        uint256 _allocationInterval
    ) {
        require(_gainsToken != address(0), "Invalid token address");
        gainsToken = IERC20(_gainsToken);
        baseAllocationAmount = _baseAllocationAmount;
        allocationInterval = _allocationInterval;

        // Initialize default tiers
        _addTier("Planktons", 100, 0);       // 1x
        _addTier("Fishes", 150, 1000 ether); // 1.5x
        _addTier("Dolphins", 200, 5000 ether); // 2x
        _addTier("Sharks", 300, 25000 ether); // 3x
        _addTier("Whales", 500, 100000 ether); // 5x
    }

    // Add a new tier (onlyOwner)
    function addTier(
        string memory _name,
        uint256 _multiplier,
        uint256 _minHolding
    ) external onlyOwner {
        _addTier(_name, _multiplier, _minHolding);
    }

    function _addTier(
        string memory _name,
        uint256 _multiplier,
        uint256 _minHolding
    ) internal {
        tiers.push(
            Tier({
                name: _name,
                allocationMultiplier: _multiplier,
                minHoldingRequirement: _minHolding
            })
        );
        emit TierAdded(tiers.length - 1, _name, _multiplier, _minHolding);
    }

    // Update user tier based on current holdings
    function updateTier(address _user) public {
        uint256 userBalance = gainsToken.balanceOf(_user);
        uint256 newTier = 0; // Default to Planktons

        // Find the highest tier the user qualifies for
        for (uint256 i = tiers.length - 1; i >= 1; i--) {
            if (userBalance >= tiers[i].minHoldingRequirement) {
                newTier = i;
                break;
            }
        }

        uint256 oldTier = userInfo[_user].tierIndex;
        if (newTier != oldTier) {
            userInfo[_user].tierIndex = newTier;
            emit TierUpdated(_user, oldTier, newTier);
        }
    }

    // Calculate pending allocation for a user
    function calculatePendingAllocation(address _user) public view returns (uint256) {
        UserInfo storage user = userInfo[_user];
        if (user.tierIndex == 0 && user.lastClaimTime == 0) return 0;

        uint256 intervalsPassed = (block.timestamp - user.lastClaimTime) / allocationInterval;
        if (intervalsPassed == 0) return 0;

        Tier storage tier = tiers[user.tierIndex];
        uint256 allocationPerInterval = (baseAllocationAmount * tier.allocationMultiplier) / 100;
        return allocationPerInterval * intervalsPassed;
    }

    // Claim allocation
    function claimAllocation() external nonReentrant {
        address user = msg.sender;
        updateTier(user);

        uint256 pending = calculatePendingAllocation(user);
        require(pending > 0, "No pending allocation");

        UserInfo storage userData = userInfo[user];
        userData.lastClaimTime = block.timestamp;
        userData.totalAllocated += pending;
        userData.totalClaimed += pending;

        require(
            gainsToken.transfer(user, pending),
            "Token transfer failed"
        );

        emit AllocationClaimed(user, pending);
    }

    // Admin functions
    function setBaseAllocation(uint256 _amount) external onlyOwner {
        baseAllocationAmount = _amount;
    }

    function setAllocationInterval(uint256 _interval) external onlyOwner {
        allocationInterval = _interval;
    }

    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(
            gainsToken.transfer(owner(), _amount),
            "Token transfer failed"
        );
    }

    // Get tier count
    function getTierCount() external view returns (uint256) {
        return tiers.length;
    }

    // Get user info
    function getUserInfo(address _user) external view returns (UserInfo memory) {
        return userInfo[_user];
    }
}
```
