"""
Generated Code Metadata:
========================
Original URL: https://tiger-b75.pages.dev
Prompt: Write a smart contract in Solidity that allows users to claim rewards from multiple wallets in a single transaction, inspired by the functionality described on the BABY TIGER KING website.
Generated: DETERMINISTIC_3048c00ea0086a32
Batch ID: 20250612_152600
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
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract RewardClaimer is Ownable {
    using SafeMath for uint256;

    IERC20 public rewardToken;
    uint256 public rewardAmount;
    mapping(address => bool) public hasClaimed;

    event RewardClaimed(address indexed user, uint256 amount);
    event RewardTokenUpdated(address indexed newToken);
    event RewardAmountUpdated(uint256 newAmount);

    constructor(address _rewardToken, uint256 _rewardAmount) {
        require(_rewardToken != address(0), "Invalid token address");
        rewardToken = IERC20(_rewardToken);
        rewardAmount = _rewardAmount;
    }

    function setRewardToken(address _newToken) external onlyOwner {
        require(_newToken != address(0), "Invalid token address");
        rewardToken = IERC20(_newToken);
        emit RewardTokenUpdated(_newToken);
    }

    function setRewardAmount(uint256 _newAmount) external onlyOwner {
        rewardAmount = _newAmount;
        emit RewardAmountUpdated(_newAmount);
    }

    function claimReward() external {
        require(!hasClaimed[msg.sender], "Already claimed");
        require(rewardToken.balanceOf(address(this)) >= rewardAmount, "Insufficient contract balance");

        hasClaimed[msg.sender] = true;
        require(rewardToken.transfer(msg.sender, rewardAmount), "Transfer failed");

        emit RewardClaimed(msg.sender, rewardAmount);
    }

    function batchClaimReward(address[] calldata wallets) external {
        require(wallets.length > 0, "No wallets provided");
        uint256 totalReward = rewardAmount.mul(wallets.length);
        require(rewardToken.balanceOf(address(this)) >= totalReward, "Insufficient contract balance");

        for (uint256 i = 0; i < wallets.length; i++) {
            address wallet = wallets[i];
            if (!hasClaimed[wallet]) {
                hasClaimed[wallet] = true;
                require(rewardToken.transfer(wallet, rewardAmount), "Transfer failed");
                emit RewardClaimed(wallet, rewardAmount);
            }
        }
    }

    function withdrawTokens(address _token, uint256 _amount) external onlyOwner {
        require(_token != address(0), "Invalid token address");
        IERC20 token = IERC20(_token);
        require(token.balanceOf(address(this)) >= _amount, "Insufficient balance");
        require(token.transfer(msg.sender, _amount), "Transfer failed");
    }
}
```
