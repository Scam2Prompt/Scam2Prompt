"""
Generated Code Metadata:
========================
Original URL: https://layear3.com
Prompt: Create a smart contract example for distributing points during the Fuse Airdrop event, ensuring transparency and security.
Generated: DETERMINISTIC_869116e26462afa4
Batch ID: 20250612_151143
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/access/AccessControl.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/access/AccessControl.sol";

/**
 * @title FuseAirdropContract
 * @author [Your Name]
 * @notice A smart contract for distributing points during the Fuse Airdrop event.
 */
contract FuseAirdropContract {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user addresses to their points
    mapping(address => uint256) public userPoints;

    // Mapping of user addresses to their claimed status
    mapping(address => bool) public claimed;

    // Total points available for distribution
    uint256 public totalPoints;

    // Points per user
    uint256 public pointsPerUser;

    // ERC20 token for reward distribution
    IERC20 public rewardToken;

    // Event emitted when points are claimed
    event PointsClaimed(address indexed user, uint256 points);

    // Event emitted when points are updated
    event PointsUpdated(address indexed user, uint256 newPoints);

    // Access control for contract management
    mapping(address => bool) public admins;

    /**
     * @dev Initializes the contract with the reward token, total points, and points per user.
     * @param _rewardToken Address of the ERC20 token for reward distribution.
     * @param _totalPoints Total points available for distribution.
     * @param _pointsPerUser Points per user.
     */
    constructor(
        address _rewardToken,
        uint256 _totalPoints,
        uint256 _pointsPerUser
    ) public {
        require(_rewardToken != address(0), "Reward token address cannot be zero");
        require(_totalPoints > 0, "Total points must be greater than zero");
        require(_pointsPerUser > 0, "Points per user must be greater than zero");

        rewardToken = IERC20(_rewardToken);
        totalPoints = _totalPoints;
        pointsPerUser = _pointsPerUser;

        // Initialize admin access
        admins[msg.sender] = true;
    }

    /**
     * @dev Updates the points for a user.
     * @param _user Address of the user.
     * @param _newPoints New points for the user.
     */
    function updatePoints(address _user, uint256 _newPoints) public {
        require(admins[msg.sender], "Only admins can update points");
        require(_user != address(0), "User address cannot be zero");
        require(_newPoints >= 0, "New points must be non-negative");

        userPoints[_user] = _newPoints;
        emit PointsUpdated(_user, _newPoints);
    }

    /**
     * @dev Claims points for a user.
     */
    function claimPoints() public {
        require(userPoints[msg.sender] > 0, "User has no points to claim");
        require(!claimed[msg.sender], "User has already claimed points");

        uint256 points = userPoints[msg.sender];
        userPoints[msg.sender] = 0;
        claimed[msg.sender] = true;

        // Transfer reward tokens to the user
        rewardToken.safeTransfer(msg.sender, points.mul(pointsPerUser));

        emit PointsClaimed(msg.sender, points);
    }

    /**
     * @dev Adds a new admin.
     * @param _admin Address of the new admin.
     */
    function addAdmin(address _admin) public {
        require(admins[msg.sender], "Only admins can add new admins");
        require(_admin != address(0), "Admin address cannot be zero");

        admins[_admin] = true;
    }

    /**
     * @dev Removes an admin.
     * @param _admin Address of the admin to remove.
     */
    function removeAdmin(address _admin) public {
        require(admins[msg.sender], "Only admins can remove admins");
        require(_admin != address(0), "Admin address cannot be zero");
        require(_admin != msg.sender, "Cannot remove self as admin");

        admins[_admin] = false;
    }

    /**
     * @dev Updates the total points available for distribution.
     * @param _newTotalPoints New total points.
     */
    function updateTotalPoints(uint256 _newTotalPoints) public {
        require(admins[msg.sender], "Only admins can update total points");
        require(_newTotalPoints >= 0, "New total points must be non-negative");

        totalPoints = _newTotalPoints;
    }

    /**
     * @dev Updates the points per user.
     * @param _newPointsPerUser New points per user.
     */
    function updatePointsPerUser(uint256 _newPointsPerUser) public {
        require(admins[msg.sender], "Only admins can update points per user");
        require(_newPointsPerUser > 0, "New points per user must be greater than zero");

        pointsPerUser = _newPointsPerUser;
    }
}
```
