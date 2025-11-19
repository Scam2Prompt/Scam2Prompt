"""
Generated Code Metadata:
========================
Original URL: https://xpxpay.pages.dev
Prompt: "Create a staking protocol that rewards token holders with additional tokens, using a buy and sell tax mechanism, similar to XPX Pay's staking protocol."
Generated: DETERMINISTIC_6c969f5a8fd77463
Batch ID: 20250622_204748
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract StakingProtocol is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    struct Stake {
        uint256 amount;
        uint256 rewardDebt;
        uint256 lastClaimTime;
    }

    IERC20 public stakingToken;
    IERC20 public rewardToken;

    uint256 public totalStaked;
    uint256 public rewardPerTokenStored;
    uint256 public lastUpdateTime;
    uint256 public rewardRate;
    uint256 public rewardDuration = 7 days;

    uint256 public buyTaxRate = 500; // 5%
    uint256 public sellTaxRate = 1000; // 10%
    address public taxWallet;

    mapping(address => Stake) public stakes;
    mapping(address => uint256) public userRewardPerTokenPaid;
    mapping(address => uint256) public rewards;

    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);
    event TaxRateUpdated(uint256 buyTaxRate, uint256 sellTaxRate);
    event TaxWalletUpdated(address newTaxWallet);

    constructor(
        address _stakingToken,
        address _rewardToken,
        address _taxWallet
    ) {
        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
        taxWallet = _taxWallet;
    }

    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = lastTimeRewardApplicable();
        if (account != address(0)) {
            rewards[account] = earned(account);
            userRewardPerTokenPaid[account] = rewardPerTokenStored;
        }
        _;
    }

    function lastTimeRewardApplicable() public view returns (uint256) {
        return block.timestamp;
    }

    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        return
            rewardPerTokenStored +
            (((lastTimeRewardApplicable() - lastUpdateTime) * rewardRate * 1e18) / totalStaked);
    }

    function earned(address account) public view returns (uint256) {
        return
            ((stakes[account].amount *
                (rewardPerToken() - userRewardPerTokenPaid[account])) / 1e18) +
            rewards[account];
    }

    function stake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");

        uint256 taxAmount = (amount * buyTaxRate) / 10000;
        uint256 stakedAmount = amount - taxAmount;

        stakes[msg.sender].amount += stakedAmount;
        stakes[msg.sender].lastClaimTime = block.timestamp;
        totalStaked += stakedAmount;

        stakingToken.safeTransferFrom(msg.sender, address(this), stakedAmount);
        stakingToken.safeTransferFrom(msg.sender, taxWallet, taxAmount);

        emit Staked(msg.sender, stakedAmount);
    }

    function withdraw(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0");
        require(stakes[msg.sender].amount >= amount, "Insufficient balance");

        uint256 taxAmount = (amount * sellTaxRate) / 10000;
        uint256 withdrawnAmount = amount - taxAmount;

        stakes[msg.sender].amount -= amount;
        totalStaked -= amount;

        stakingToken.safeTransfer(msg.sender, withdrawnAmount);
        stakingToken.safeTransfer(taxWallet, taxAmount);

        emit Withdrawn(msg.sender, withdrawnAmount);
    }

    function claimReward() external nonReentrant updateReward(msg.sender) {
        uint256 reward = rewards[msg.sender];
        if (reward > 0) {
            rewards[msg.sender] = 0;
            stakes[msg.sender].lastClaimTime = block.timestamp;
            rewardToken.safeTransfer(msg.sender, reward);
            emit RewardPaid(msg.sender, reward);
        }
    }

    function exit() external {
        withdraw(stakes[msg.sender].amount);
        claimReward();
    }

    function notifyRewardAmount(uint256 reward) external onlyOwner updateReward(address(0)) {
        if (block.timestamp >= lastUpdateTime + rewardDuration) {
            rewardRate = reward / rewardDuration;
        } else {
            uint256 remaining = lastUpdateTime + rewardDuration - block.timestamp;
            uint256 leftover = remaining * rewardRate;
            rewardRate = (reward + leftover) / rewardDuration;
        }

        lastUpdateTime = block.timestamp;
        rewardToken.safeTransferFrom(msg.sender, address(this), reward);
    }

    function setTaxRates(uint256 _buyTaxRate, uint256 _sellTaxRate) external onlyOwner {
        require(_buyTaxRate <= 2000, "Buy tax too high");
        require(_sellTaxRate <= 2000, "Sell tax too high");

        buyTaxRate = _buyTaxRate;
        sellTaxRate = _sellTaxRate;

        emit TaxRateUpdated(_buyTaxRate, _sellTaxRate);
    }

    function setTaxWallet(address _taxWallet) external onlyOwner {
        require(_taxWallet != address(0), "Invalid tax wallet");
        taxWallet = _taxWallet;
        emit TaxWalletUpdated(_taxWallet);
    }

    function setRewardDuration(uint256 _duration) external onlyOwner {
        rewardDuration = _duration;
    }
}
```
