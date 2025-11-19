"""
Generated Code Metadata:
========================
Original URL: https://kinzafinancefi.medium.com
Prompt: Create an example of a smart contract that interacts with the Kinza Finance protocol to facilitate the claiming of KZA tokens.
Generated: DETERMINISTIC_81f6836a35031335
Batch ID: 20250612_155332
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

interface IKinzaRewards {
    function claimRewards(address[] calldata holders, IERC20[] calldata tokens) external;
    function getRewardsBalance(address[] calldata holders, IERC20[] calldata tokens) external view returns (uint256[] memory);
}

contract KzaClaimer is Ownable, ReentrancyGuard {
    IKinzaRewards public kinzaRewards;
    IERC20 public kzaToken;

    event RewardsClaimed(address indexed user, uint256 amount);
    event KinzaRewardsUpdated(address newRewards);
    event KzaTokenUpdated(address newToken);

    constructor(address _kinzaRewards, address _kzaToken) {
        require(_kinzaRewards != address(0), "Invalid Kinza Rewards address");
        require(_kzaToken != address(0), "Invalid KZA token address");
        
        kinzaRewards = IKinzaRewards(_kinzaRewards);
        kzaToken = IERC20(_kzaToken);
    }

    function setKinzaRewards(address _kinzaRewards) external onlyOwner {
        require(_kinzaRewards != address(0), "Invalid Kinza Rewards address");
        kinzaRewards = IKinzaRewards(_kinzaRewards);
        emit KinzaRewardsUpdated(_kinzaRewards);
    }

    function setKzaToken(address _kzaToken) external onlyOwner {
        require(_kzaToken != address(0), "Invalid KZA token address");
        kzaToken = IERC20(_kzaToken);
        emit KzaTokenUpdated(_kzaToken);
    }

    function getClaimableRewards(address user) external view returns (uint256) {
        address[] memory holders = new address[](1);
        holders[0] = user;
        
        IERC20[] memory tokens = new IERC20[](1);
        tokens[0] = kzaToken;
        
        uint256[] memory rewards = kinzaRewards.getRewardsBalance(holders, tokens);
        return rewards[0];
    }

    function claimRewards() external nonReentrant {
        address[] memory holders = new address[](1);
        holders[0] = msg.sender;
        
        IERC20[] memory tokens = new IERC20[](1);
        tokens[0] = kzaToken;
        
        uint256 balanceBefore = kzaToken.balanceOf(msg.sender);
        kinzaRewards.claimRewards(holders, tokens);
        uint256 balanceAfter = kzaToken.balanceOf(msg.sender);
        
        uint256 claimedAmount = balanceAfter - balanceBefore;
        require(claimedAmount > 0, "No rewards to claim");
        
        emit RewardsClaimed(msg.sender, claimedAmount);
    }

    function emergencyWithdraw(address token) external onlyOwner {
        require(token != address(0), "Invalid token address");
        IERC20(token).transfer(owner(), IERC20(token).balanceOf(address(this)));
    }
}
```
