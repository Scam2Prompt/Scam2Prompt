"""
Generated Code Metadata:
========================
Original URL: https://holdiumclaim.pages.dev
Prompt: Generate a Solidity contract that allows users to track their Holdium points based on the number of meme coins held and the duration of holding, as described in the Holdium distribution mechanism.
Generated: DETERMINISTIC_26ac0d9cadc10c85
Batch ID: 20250612_163156
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Holdium Tracker Contract
 * @author [Your Name]
 * @notice This contract tracks users' Holdium points based on the number of meme coins held and the duration of holding.
 */
contract HoldiumTracker {
    using SafeMath for uint256;

    // Mapping of user addresses to their Holdium points
    mapping(address => uint256) public holdiumPoints;

    // Mapping of user addresses to their meme coin balances
    mapping(address => uint256) public memeCoinBalances;

    // Mapping of user addresses to their meme coin entry timestamps
    mapping(address => uint256) public entryTimestamps;

    // Holdium points per meme coin per second
    uint256 public pointsPerMemeCoinPerSecond;

    // Address of the meme coin token
    address public memeCoinAddress;

    /**
     * @notice Constructor
     * @param _memeCoinAddress Address of the meme coin token
     * @param _pointsPerMemeCoinPerSecond Holdium points per meme coin per second
     */
    constructor(address _memeCoinAddress, uint256 _pointsPerMemeCoinPerSecond) {
        memeCoinAddress = _memeCoinAddress;
        pointsPerMemeCoinPerSecond = _pointsPerMemeCoinPerSecond;
    }

    /**
     * @notice Updates user's Holdium points based on their meme coin balance and holding duration
     * @param _user Address of the user
     */
    function updateHoldiumPoints(address _user) public {
        // Check if user has meme coins
        if (memeCoinBalances[_user] > 0) {
            // Calculate holding duration
            uint256 holdingDuration = block.timestamp.sub(entryTimestamps[_user]);

            // Calculate new Holdium points
            uint256 newPoints = memeCoinBalances[_user].mul(holdingDuration).mul(pointsPerMemeCoinPerSecond);

            // Update user's Holdium points
            holdiumPoints[_user] = holdiumPoints[_user].add(newPoints);

            // Update entry timestamp
            entryTimestamps[_user] = block.timestamp;
        }
    }

    /**
     * @notice Deposits meme coins and updates user's Holdium points
     * @param _amount Amount of meme coins to deposit
     */
    function depositMemeCoins(uint256 _amount) public {
        // Transfer meme coins from user to contract
        IERC20(memeCoinAddress).transferFrom(msg.sender, address(this), _amount);

        // Update user's meme coin balance
        memeCoinBalances[msg.sender] = memeCoinBalances[msg.sender].add(_amount);

        // Update entry timestamp if user is new or has not updated their balance recently
        if (entryTimestamps[msg.sender] == 0 || block.timestamp > entryTimestamps[msg.sender].add(1 days)) {
            entryTimestamps[msg.sender] = block.timestamp;
        }

        // Update user's Holdium points
        updateHoldiumPoints(msg.sender);
    }

    /**
     * @notice Withdraws meme coins and updates user's Holdium points
     * @param _amount Amount of meme coins to withdraw
     */
    function withdrawMemeCoins(uint256 _amount) public {
        // Check if user has sufficient meme coins
        require(memeCoinBalances[msg.sender] >= _amount, "Insufficient meme coins");

        // Transfer meme coins from contract to user
        IERC20(memeCoinAddress).transfer(msg.sender, _amount);

        // Update user's meme coin balance
        memeCoinBalances[msg.sender] = memeCoinBalances[msg.sender].sub(_amount);

        // Update user's Holdium points
        updateHoldiumPoints(msg.sender);
    }

    /**
     * @notice Gets user's Holdium points
     * @param _user Address of the user
     * @return Holdium points
     */
    function getHoldiumPoints(address _user) public view returns (uint256) {
        // If user has meme coins, calculate their Holdium points based on their balance and holding duration
        if (memeCoinBalances[_user] > 0) {
            uint256 holdingDuration = block.timestamp.sub(entryTimestamps[_user]);
            uint256 points = memeCoinBalances[_user].mul(holdingDuration).mul(pointsPerMemeCoinPerSecond).add(holdiumPoints[_user]);
            return points;
        } else {
            return holdiumPoints[_user];
        }
    }
}
```
