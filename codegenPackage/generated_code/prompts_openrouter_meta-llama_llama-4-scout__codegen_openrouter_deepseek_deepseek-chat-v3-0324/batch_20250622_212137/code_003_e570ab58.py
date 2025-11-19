"""
Generated Code Metadata:
========================
Original URL: https://usdccash.xyz
Prompt: Develop a simple Ethereum smart contract in Solidity that distributes USDC rewards to $UPRINT holders on every transaction, considering the tokenomics and contract address provided.
Generated: DETERMINISTIC_e570ab58cd3545c3
Batch ID: 20250622_212137
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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract UPRINTRewardDistributor is Ownable {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Token addresses
    IERC20 public uprintToken;
    IERC20 public usdcToken;

    // Reward parameters
    uint256 public rewardPercentage; // Percentage of transaction amount to distribute as rewards (in basis points, e.g. 100 = 1%)
    uint256 public totalDistributed;

    // Mapping to track last claim time per address
    mapping(address => uint256) public lastClaimTime;

    event RewardsDistributed(address indexed holder, uint256 amount);
    event RewardPercentageUpdated(uint256 newPercentage);

    constructor(
        address _uprintToken,
        address _usdcToken,
        uint256 _rewardPercentage
    ) {
        require(_uprintToken != address(0), "UPRINT token address cannot be zero");
        require(_usdcToken != address(0), "USDC token address cannot be zero");
        require(_rewardPercentage <= 10000, "Reward percentage cannot exceed 100%");

        uprintToken = IERC20(_uprintToken);
        usdcToken = IERC20(_usdcToken);
        rewardPercentage = _rewardPercentage;
    }

    function distributeRewards(uint256 transactionAmount) external {
        require(transactionAmount > 0, "Transaction amount must be greater than zero");

        uint256 rewardAmount = transactionAmount.mul(rewardPercentage).div(10000);
        require(rewardAmount > 0, "Reward amount must be greater than zero");

        uint256 contractBalance = usdcToken.balanceOf(address(this));
        require(contractBalance >= rewardAmount, "Insufficient USDC balance in contract");

        uint256 totalUprintSupply = uprintToken.totalSupply();
        require(totalUprintSupply > 0, "No UPRINT tokens exist");

        // Calculate rewards for each holder based on their proportion of total supply
        address[] memory holders = _getTokenHolders();
        for (uint256 i = 0; i < holders.length; i++) {
            address holder = holders[i];
            uint256 holderBalance = uprintToken.balanceOf(holder);
            if (holderBalance == 0) continue;

            uint256 holderReward = rewardAmount.mul(holderBalance).div(totalUprintSupply);
            if (holderReward == 0) continue;

            usdcToken.safeTransfer(holder, holderReward);
            lastClaimTime[holder] = block.timestamp;
            totalDistributed = totalDistributed.add(holderReward);

            emit RewardsDistributed(holder, holderReward);
        }
    }

    function setRewardPercentage(uint256 _rewardPercentage) external onlyOwner {
        require(_rewardPercentage <= 10000, "Reward percentage cannot exceed 100%");
        rewardPercentage = _rewardPercentage;
        emit RewardPercentageUpdated(_rewardPercentage);
    }

    function withdrawExcessUSDC(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        uint256 contractBalance = usdcToken.balanceOf(address(this));
        require(contractBalance >= amount, "Insufficient USDC balance");

        usdcToken.safeTransfer(owner(), amount);
    }

    function _getTokenHolders() internal view returns (address[] memory) {
        // In a real implementation, you would need to track holders or use an external service
        // This is a simplified version that assumes holders can be retrieved
        // For production, consider using a snapshot mechanism or off-chain indexing
        return new address[](0);
    }

    function emergencyWithdraw() external onlyOwner {
        uint256 contractBalance = usdcToken.balanceOf(address(this));
        usdcToken.safeTransfer(owner(), contractBalance);
    }
}
```
