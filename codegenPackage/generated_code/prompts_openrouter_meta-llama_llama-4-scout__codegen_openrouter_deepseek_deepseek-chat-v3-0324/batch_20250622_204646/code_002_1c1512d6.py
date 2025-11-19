"""
Generated Code Metadata:
========================
Original URL: https://aim-bot-app.pages.dev
Prompt: Generate a code snippet to distribute profits to investors based on their token balance and total supply, as described in the AimBot AI reward calculation formula: [ETH in reward wallet] * (your token balance / total supply).
Generated: DETERMINISTIC_1c1512d65c74a45c
Batch ID: 20250622_204646
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

contract ProfitDistributor is Ownable, ReentrancyGuard {
    IERC20 public token;
    address public rewardWallet;
    
    event ProfitDistributed(address indexed investor, uint256 amount);
    event RewardWalletUpdated(address newWallet);
    
    /**
     * @dev Initializes the contract with the token address and reward wallet
     * @param _token Address of the ERC20 token contract
     * @param _rewardWallet Address where rewards are held
     */
    constructor(address _token, address _rewardWallet) {
        require(_token != address(0), "Token address cannot be zero");
        require(_rewardWallet != address(0), "Reward wallet cannot be zero");
        
        token = IERC20(_token);
        rewardWallet = _rewardWallet;
    }
    
    /**
     * @dev Updates the reward wallet address
     * @param _newWallet New reward wallet address
     */
    function updateRewardWallet(address _newWallet) external onlyOwner {
        require(_newWallet != address(0), "Reward wallet cannot be zero");
        rewardWallet = _newWallet;
        emit RewardWalletUpdated(_newWallet);
    }
    
    /**
     * @dev Distributes profits to an investor based on their token balance
     * @param investor Address of the investor to receive rewards
     */
    function distributeProfit(address investor) external nonReentrant {
        require(investor != address(0), "Investor address cannot be zero");
        
        uint256 totalSupply = token.totalSupply();
        require(totalSupply > 0, "No tokens minted yet");
        
        uint256 investorBalance = token.balanceOf(investor);
        require(investorBalance > 0, "Investor has no tokens");
        
        uint256 rewardWalletBalance = address(rewardWallet).balance;
        require(rewardWalletBalance > 0, "No rewards available");
        
        uint256 rewardAmount = rewardWalletBalance * investorBalance / totalSupply;
        require(rewardAmount > 0, "Reward amount too small");
        
        (bool success, ) = rewardWallet.call{value: rewardAmount}("");
        require(success, "ETH transfer failed");
        
        emit ProfitDistributed(investor, rewardAmount);
    }
    
    /**
     * @dev Allows the contract to receive ETH
     */
    receive() external payable {}
}
```
