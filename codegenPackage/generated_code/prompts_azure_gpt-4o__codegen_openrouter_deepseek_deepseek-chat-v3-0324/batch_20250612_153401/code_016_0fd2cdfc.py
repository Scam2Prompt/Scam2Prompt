"""
Generated Code Metadata:
========================
Original URL: https://etfswap-in.pages.dev
Prompt: Create a Solidity contract for managing a rewards pool that redistributes sell tax fees to $ETFS token holders, as described in ETFSwap's automatic rewards system.
Generated: DETERMINISTIC_0fd2cdfc7d49131c
Batch ID: 20250612_153401
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract ETFSRewardsPool is Ownable {
    using SafeMath for uint256;

    IERC20 public etfsToken;
    uint256 public totalDistributedRewards;
    uint256 public totalRewardShares;
    uint256 public rewardPerShare;
    uint256 public constant PRECISION_FACTOR = 10**36;

    struct Share {
        uint256 amount;
        uint256 rewardDebt;
    }

    mapping(address => Share) public shares;

    event RewardsDeposited(uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);
    event SharesAdded(address indexed user, uint256 amount);
    event SharesRemoved(address indexed user, uint256 amount);

    constructor(address _etfsToken) {
        require(_etfsToken != address(0), "Invalid token address");
        etfsToken = IERC20(_etfsToken);
    }

    function depositRewards(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(
            etfsToken.transferFrom(msg.sender, address(this), amount),
            "Transfer failed"
        );

        if (totalRewardShares > 0) {
            rewardPerShare = rewardPerShare.add(
                amount.mul(PRECISION_FACTOR).div(totalRewardShares)
            );
        }

        totalDistributedRewards = totalDistributedRewards.add(amount);
        emit RewardsDeposited(amount);
    }

    function updateShares(address user, uint256 newBalance) external onlyOwner {
        _updateShares(user, newBalance);
    }

    function _updateShares(address user, uint256 newBalance) internal {
        if (shares[user].amount > 0) {
            uint256 pending = shares[user]
                .amount
                .mul(rewardPerShare)
                .div(PRECISION_FACTOR)
                .sub(shares[user].rewardDebt);
            if (pending > 0) {
                _safeTransfer(user, pending);
            }
        }

        if (newBalance > 0) {
            totalRewardShares = totalRewardShares.sub(shares[user].amount).add(
                newBalance
            );
            shares[user].amount = newBalance;
            shares[user].rewardDebt = newBalance.mul(rewardPerShare).div(
                PRECISION_FACTOR
            );
            emit SharesAdded(user, newBalance);
        } else {
            totalRewardShares = totalRewardShares.sub(shares[user].amount);
            delete shares[user];
            emit SharesRemoved(user, 0);
        }
    }

    function claimRewards() external {
        uint256 pending = pendingRewards(msg.sender);
        require(pending > 0, "No rewards to claim");

        shares[msg.sender].rewardDebt = shares[msg.sender]
            .amount
            .mul(rewardPerShare)
            .div(PRECISION_FACTOR);

        _safeTransfer(msg.sender, pending);
        emit RewardsClaimed(msg.sender, pending);
    }

    function pendingRewards(address user) public view returns (uint256) {
        if (shares[user].amount == 0) return 0;

        uint256 currentRewardPerShare = rewardPerShare;
        if (totalRewardShares > 0) {
            uint256 rewardsBalance = etfsToken.balanceOf(address(this));
            currentRewardPerShare = currentRewardPerShare.add(
                rewardsBalance.mul(PRECISION_FACTOR).div(totalRewardShares)
            );
        }

        return
            shares[user]
                .amount
                .mul(currentRewardPerShare)
                .div(PRECISION_FACTOR)
                .sub(shares[user].rewardDebt);
    }

    function _safeTransfer(address to, uint256 amount) internal {
        uint256 balance = etfsToken.balanceOf(address(this));
        if (amount > balance) {
            amount = balance;
        }
        require(amount > 0, "No tokens to transfer");
        require(etfsToken.transfer(to, amount), "Transfer failed");
    }

    function emergencyWithdraw(address tokenAddress) external onlyOwner {
        require(tokenAddress != address(etfsToken), "Cannot withdraw ETFS tokens");
        IERC20 token = IERC20(tokenAddress);
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        require(token.transfer(owner(), balance), "Transfer failed");
    }
}
```
