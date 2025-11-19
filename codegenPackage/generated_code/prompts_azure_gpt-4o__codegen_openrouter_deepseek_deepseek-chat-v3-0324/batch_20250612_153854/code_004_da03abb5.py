"""
Generated Code Metadata:
========================
Original URL: https://sophan.xyz
Prompt: Write a smart contract that utilizes SOPH tokens to reward users for engagement in loyalty programs, as described in Sophon's platform features.
Generated: DETERMINISTIC_da03abb5493298ca
Batch ID: 20250612_153854
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

contract SophonLoyaltyProgram is Ownable, ReentrancyGuard {
    IERC20 public sophToken;
    
    // Mapping to track user points
    mapping(address => uint256) public userPoints;
    
    // Mapping to track claimed rewards
    mapping(address => uint256) public claimedRewards;
    
    // Conversion rate: points to SOPH tokens
    uint256 public pointsToTokenRate;
    
    // Minimum points required to claim rewards
    uint256 public minPointsToClaim;
    
    // Events
    event PointsEarned(address indexed user, uint256 points);
    event RewardsClaimed(address indexed user, uint256 amount);
    event RateUpdated(uint256 newRate);
    event MinPointsUpdated(uint256 newMinPoints);
    
    /**
     * @dev Constructor initializes the contract with SOPH token address
     * @param _sophTokenAddress Address of the SOPH token contract
     * @param _initialRate Initial conversion rate (points per SOPH token)
     * @param _initialMinPoints Initial minimum points required to claim
     */
    constructor(
        address _sophTokenAddress,
        uint256 _initialRate,
        uint256 _initialMinPoints
    ) {
        require(_sophTokenAddress != address(0), "Invalid token address");
        sophToken = IERC20(_sophTokenAddress);
        pointsToTokenRate = _initialRate;
        minPointsToClaim = _initialMinPoints;
    }
    
    /**
     * @dev Add points to a user's account (only callable by owner)
     * @param _user Address of the user to reward
     * @param _points Number of points to add
     */
    function addPoints(address _user, uint256 _points) external onlyOwner {
        require(_user != address(0), "Invalid user address");
        require(_points > 0, "Points must be greater than zero");
        
        userPoints[_user] += _points;
        emit PointsEarned(_user, _points);
    }
    
    /**
     * @dev Claim rewards by converting points to SOPH tokens
     */
    function claimRewards() external nonReentrant {
        uint256 points = userPoints[msg.sender];
        require(points >= minPointsToClaim, "Insufficient points to claim");
        
        uint256 tokenAmount = points / pointsToTokenRate;
        require(tokenAmount > 0, "No tokens to claim");
        
        // Check contract balance
        uint256 contractBalance = sophToken.balanceOf(address(this));
        require(contractBalance >= tokenAmount, "Insufficient contract balance");
        
        // Update user's points and claimed rewards
        userPoints[msg.sender] = points % pointsToTokenRate; // Keep remainder points
        claimedRewards[msg.sender] += tokenAmount;
        
        // Transfer tokens
        require(sophToken.transfer(msg.sender, tokenAmount), "Token transfer failed");
        
        emit RewardsClaimed(msg.sender, tokenAmount);
    }
    
    /**
     * @dev Update the points to token conversion rate (only callable by owner)
     * @param _newRate New conversion rate
     */
    function updateRate(uint256 _newRate) external onlyOwner {
        require(_newRate > 0, "Rate must be greater than zero");
        pointsToTokenRate = _newRate;
        emit RateUpdated(_newRate);
    }
    
    /**
     * @dev Update the minimum points required to claim (only callable by owner)
     * @param _newMinPoints New minimum points value
     */
    function updateMinPoints(uint256 _newMinPoints) external onlyOwner {
        minPointsToClaim = _newMinPoints;
        emit MinPointsUpdated(_newMinPoints);
    }
    
    /**
     * @dev Withdraw remaining SOPH tokens from the contract (only callable by owner)
     * @param _amount Amount to withdraw
     */
    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        uint256 contractBalance = sophToken.balanceOf(address(this));
        require(contractBalance >= _amount, "Insufficient contract balance");
        
        require(sophToken.transfer(owner(), _amount), "Token transfer failed");
    }
    
    /**
     * @dev Get user's claimable token amount
     * @param _user Address of the user
     * @return Amount of tokens claimable
     */
    function getClaimableTokens(address _user) external view returns (uint256) {
        return userPoints[_user] / pointsToTokenRate;
    }
    
    /**
     * @dev Get user's remaining points after claiming
     * @param _user Address of the user
     * @return Remaining points
     */
    function getRemainingPoints(address _user) external view returns (uint256) {
        return userPoints[_user] % pointsToTokenRate;
    }
}
```
