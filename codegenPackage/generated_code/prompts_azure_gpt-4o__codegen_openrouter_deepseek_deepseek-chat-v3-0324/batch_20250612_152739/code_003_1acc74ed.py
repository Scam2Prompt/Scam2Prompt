"""
Generated Code Metadata:
========================
Original URL: https://slnportal-launchpad.vercel.app
Prompt: Create a smart contract for managing passes and points within the Smart Layer Launchpad ecosystem, referencing $SLN token mechanics.
Generated: DETERMINISTIC_1acc74ed374ac5f1
Batch ID: 20250612_152739
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

contract SmartLayerLaunchpad is Ownable, ReentrancyGuard {
    // Token contract interface
    IERC20 public slnToken;

    // Pass structure
    struct Pass {
        uint256 id;
        string name;
        uint256 price;
        uint256 pointsReward;
        bool isActive;
    }

    // User structure
    struct User {
        uint256 pointsBalance;
        uint256[] ownedPasses;
        mapping(uint256 => uint256) passCount; // passId => count
    }

    // State variables
    mapping(uint256 => Pass) public passes;
    mapping(address => User) private users;
    uint256 public nextPassId = 1;
    address public treasury;

    // Events
    event PassCreated(uint256 indexed passId, string name, uint256 price, uint256 pointsReward);
    event PassPurchased(address indexed user, uint256 indexed passId, uint256 amount);
    event PointsRedeemed(address indexed user, uint256 amount);
    event PassStatusChanged(uint256 indexed passId, bool isActive);
    event TreasuryUpdated(address newTreasury);

    // Modifiers
    modifier validPass(uint256 passId) {
        require(passId > 0 && passId < nextPassId, "Invalid pass ID");
        require(passes[passId].isActive, "Pass is not active");
        _;
    }

    constructor(address _slnToken, address _treasury) {
        require(_slnToken != address(0), "SLN token address cannot be zero");
        require(_treasury != address(0), "Treasury address cannot be zero");
        slnToken = IERC20(_slnToken);
        treasury = _treasury;
    }

    /**
     * @dev Create a new pass
     * @param name Name of the pass
     * @param price Price in SLN tokens
     * @param pointsReward Points rewarded when purchasing this pass
     */
    function createPass(
        string memory name,
        uint256 price,
        uint256 pointsReward
    ) external onlyOwner {
        uint256 passId = nextPassId++;
        passes[passId] = Pass({
            id: passId,
            name: name,
            price: price,
            pointsReward: pointsReward,
            isActive: true
        });

        emit PassCreated(passId, name, price, pointsReward);
    }

    /**
     * @dev Purchase a pass
     * @param passId ID of the pass to purchase
     * @param amount Number of passes to purchase
     */
    function purchasePass(uint256 passId, uint256 amount) external validPass(passId) nonReentrant {
        require(amount > 0, "Amount must be greater than zero");

        Pass storage pass = passes[passId];
        uint256 totalCost = pass.price * amount;
        uint256 totalPoints = pass.pointsReward * amount;

        // Transfer SLN tokens from user to treasury
        require(
            slnToken.transferFrom(msg.sender, treasury, totalCost),
            "SLN transfer failed"
        );

        // Update user data
        User storage user = users[msg.sender];
        user.pointsBalance += totalPoints;

        // Add passes to user's collection if not already owned
        if (user.passCount[passId] == 0) {
            user.ownedPasses.push(passId);
        }
        user.passCount[passId] += amount;

        emit PassPurchased(msg.sender, passId, amount);
    }

    /**
     * @dev Redeem points for rewards (to be implemented by inheriting contract)
     * @param amount Amount of points to redeem
     */
    function redeemPoints(uint256 amount) external nonReentrant {
        User storage user = users[msg.sender];
        require(user.pointsBalance >= amount, "Insufficient points balance");

        user.pointsBalance -= amount;
        // Additional reward logic would go here in inheriting contract

        emit PointsRedeemed(msg.sender, amount);
    }

    /**
     * @dev Toggle pass active status
     * @param passId ID of the pass to update
     */
    function togglePassStatus(uint256 passId) external onlyOwner validPass(passId) {
        passes[passId].isActive = !passes[passId].isActive;
        emit PassStatusChanged(passId, passes[passId].isActive);
    }

    /**
     * @dev Update treasury address
     * @param newTreasury New treasury address
     */
    function updateTreasury(address newTreasury) external onlyOwner {
        require(newTreasury != address(0), "Treasury address cannot be zero");
        treasury = newTreasury;
        emit TreasuryUpdated(newTreasury);
    }

    // View functions
    function getUserPoints(address userAddress) external view returns (uint256) {
        return users[userAddress].pointsBalance;
    }

    function getUserPasses(address userAddress) external view returns (uint256[] memory) {
        return users[userAddress].ownedPasses;
    }

    function getUserPassCount(address userAddress, uint256 passId) external view returns (uint256) {
        return users[userAddress].passCount[passId];
    }

    function getPassDetails(uint256 passId) external view returns (Pass memory) {
        require(passId > 0 && passId < nextPassId, "Invalid pass ID");
        return passes[passId];
    }
}
```
