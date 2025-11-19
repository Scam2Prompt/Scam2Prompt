"""
Generated Code Metadata:
========================
Original URL: https://everyworld-app.pages.dev
Prompt: Create a smart contract in Solidity that mimics Everyworld's dual incentivization model, allowing users to earn points and pledge them to environmental charities.
Generated: DETERMINISTIC_77fb36756e53193b
Batch ID: 20250612_152511
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract EcoPoints is Ownable, ReentrancyGuard {
    // Struct to store user information
    struct User {
        uint256 points;
        uint256 pledgedPoints;
        uint256 lastActivity;
    }

    // Struct to store charity information
    struct Charity {
        string name;
        address wallet;
        uint256 totalPledged;
        bool isActive;
    }

    // Constants
    uint256 public constant POINTS_PER_ACTION = 10;
    uint256 public constant ACTIVITY_COOLDOWN = 1 days;

    // State variables
    mapping(address => User) public users;
    Charity[] public charities;
    IERC20 public rewardToken;

    // Events
    event PointsEarned(address indexed user, uint256 amount);
    event PointsPledged(address indexed user, uint256 charityId, uint256 amount);
    event CharityAdded(uint256 indexed charityId, string name, address wallet);
    event CharityStatusChanged(uint256 indexed charityId, bool isActive);
    event RewardsDistributed(address indexed user, uint256 amount);

    // Constructor
    constructor(address _rewardTokenAddress) {
        rewardToken = IERC20(_rewardTokenAddress);
    }

    /**
     * @dev Add a new charity
     * @param _name Name of the charity
     * @param _wallet Wallet address of the charity
     */
    function addCharity(string memory _name, address _wallet) external onlyOwner {
        charities.push(Charity({
            name: _name,
            wallet: _wallet,
            totalPledged: 0,
            isActive: true
        }));
        emit CharityAdded(charities.length - 1, _name, _wallet);
    }

    /**
     * @dev Toggle charity active status
     * @param _charityId ID of the charity
     */
    function toggleCharityStatus(uint256 _charityId) external onlyOwner {
        require(_charityId < charities.length, "Invalid charity ID");
        charities[_charityId].isActive = !charities[_charityId].isActive;
        emit CharityStatusChanged(_charityId, charities[_charityId].isActive);
    }

    /**
     * @dev Earn points by performing actions
     */
    function earnPoints() external nonReentrant {
        User storage user = users[msg.sender];
        
        // Check if user has waited the cooldown period
        require(
            block.timestamp >= user.lastActivity + ACTIVITY_COOLDOWN,
            "Cooldown period not passed"
        );

        user.points += POINTS_PER_ACTION;
        user.lastActivity = block.timestamp;
        
        emit PointsEarned(msg.sender, POINTS_PER_ACTION);
    }

    /**
     * @dev Pledge points to a charity
     * @param _charityId ID of the charity
     * @param _amount Amount of points to pledge
     */
    function pledgePoints(uint256 _charityId, uint256 _amount) external nonReentrant {
        require(_charityId < charities.length, "Invalid charity ID");
        require(charities[_charityId].isActive, "Charity is not active");
        require(_amount > 0, "Amount must be greater than 0");

        User storage user = users[msg.sender];
        require(user.points >= _amount, "Insufficient points");

        user.points -= _amount;
        user.pledgedPoints += _amount;
        charities[_charityId].totalPledged += _amount;

        emit PointsPledged(msg.sender, _charityId, _amount);
    }

    /**
     * @dev Distribute rewards based on pledged points
     */
    function claimRewards() external nonReentrant {
        User storage user = users[msg.sender];
        require(user.pledgedPoints > 0, "No pledged points");

        // Calculate reward (1:1 ratio for simplicity)
        uint256 rewardAmount = user.pledgedPoints;
        
        // Reset pledged points
        user.pledgedPoints = 0;

        // Transfer reward tokens
        require(
            rewardToken.transfer(msg.sender, rewardAmount),
            "Token transfer failed"
        );

        emit RewardsDistributed(msg.sender, rewardAmount);
    }

    /**
     * @dev Get total number of charities
     * @return Total charity count
     */
    function getCharityCount() external view returns (uint256) {
        return charities.length;
    }

    /**
     * @dev Withdraw funds (for emergency purposes)
     * @param _tokenAddress Address of the token to withdraw
     * @param _amount Amount to withdraw
     */
    function withdrawFunds(address _tokenAddress, uint256 _amount) external onlyOwner {
        IERC20 token = IERC20(_tokenAddress);
        require(
            token.transfer(msg.sender, _amount),
            "Withdrawal failed"
        );
    }
}
```
