"""
Generated Code Metadata:
========================
Original URL: https://walletconnectairdrop.network
Prompt: Design a smart contract for a decentralized application (dApp) on the WalletConnect Network, incorporating the use of WCT tokens for network services and rewards.
Generated: DETERMINISTIC_f5b7d7db5d5cbbdc
Batch ID: 20250622_211923
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

/**
 * @title WalletConnect Smart Contract
 * @dev A smart contract for decentralized applications (dApps) on the WalletConnect Network
 *      using WCT tokens for network services and rewards.
 */
contract WalletConnectDApp is Ownable, ReentrancyGuard {
    IERC20 public wctToken;
    uint256 public serviceFee;
    uint256 public rewardRate;
    uint256 public totalRewardsDistributed;

    mapping(address => uint256) public userRewards;
    mapping(address => uint256) public lastClaimTime;

    event ServicePaid(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event FeeUpdated(uint256 newFee);
    event RewardRateUpdated(uint256 newRate);

    /**
     * @dev Constructor initializes the contract with WCT token address, service fee, and reward rate.
     * @param _wctToken Address of the WCT token contract
     * @param _serviceFee Fee for using network services (in WCT tokens)
     * @param _rewardRate Rate at which rewards are distributed (in WCT tokens per second)
     */
    constructor(
        address _wctToken,
        uint256 _serviceFee,
        uint256 _rewardRate
    ) {
        require(_wctToken != address(0), "Invalid token address");
        wctToken = IERC20(_wctToken);
        serviceFee = _serviceFee;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Pay service fee to use network services.
     */
    function payServiceFee() external nonReentrant {
        require(wctToken.transferFrom(msg.sender, address(this), serviceFee), "Payment failed");
        _updateRewards(msg.sender);
        emit ServicePaid(msg.sender, serviceFee);
    }

    /**
     * @dev Claim accumulated rewards.
     */
    function claimRewards() external nonReentrant {
        _updateRewards(msg.sender);
        uint256 reward = userRewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        userRewards[msg.sender] = 0;
        require(wctToken.transfer(msg.sender, reward), "Transfer failed");

        totalRewardsDistributed += reward;
        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Update service fee (only owner).
     * @param _newFee New service fee amount
     */
    function updateServiceFee(uint256 _newFee) external onlyOwner {
        require(_newFee != serviceFee, "Fee is the same");
        serviceFee = _newFee;
        emit FeeUpdated(_newFee);
    }

    /**
     * @dev Update reward rate (only owner).
     * @param _newRate New reward rate
     */
    function updateRewardRate(uint256 _newRate) external onlyOwner {
        require(_newRate != rewardRate, "Rate is the same");
        rewardRate = _newRate;
        emit RewardRateUpdated(_newRate);
    }

    /**
     * @dev Withdraw WCT tokens from contract (only owner).
     * @param amount Amount to withdraw
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(wctToken.transfer(msg.sender, amount), "Withdrawal failed");
    }

    /**
     * @dev Internal function to update user rewards.
     * @param user Address of the user
     */
    function _updateRewards(address user) internal {
        if (lastClaimTime[user] == 0) {
            lastClaimTime[user] = block.timestamp;
            return;
        }

        uint256 timeElapsed = block.timestamp - lastClaimTime[user];
        uint256 reward = timeElapsed * rewardRate;
        
        if (reward > 0) {
            userRewards[user] += reward;
        }
        
        lastClaimTime[user] = block.timestamp;
    }

    /**
     * @dev Get pending rewards for a user.
     * @param user Address of the user
     * @return Pending rewards
     */
    function getPendingRewards(address user) external view returns (uint256) {
        if (lastClaimTime[user] == 0) {
            return 0;
        }

        uint256 timeElapsed = block.timestamp - lastClaimTime[user];
        return userRewards[user] + (timeElapsed * rewardRate);
    }
}
```
