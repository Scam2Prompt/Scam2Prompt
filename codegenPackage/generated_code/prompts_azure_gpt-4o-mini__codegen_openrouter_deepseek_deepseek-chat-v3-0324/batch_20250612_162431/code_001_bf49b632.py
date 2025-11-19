"""
Generated Code Metadata:
========================
Original URL: https://geoins.ru
Prompt: Write a code snippet for a decentralized application that allows users to stake QI tokens and manage collateral for MAI issuance.
Generated: DETERMINISTIC_bf49b63286fecc68
Batch ID: 20250612_162431
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract QiStaking is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    // Token contracts
    IERC20 public immutable qiToken;
    IERC20 public immutable maiToken;

    // Staking parameters
    uint256 public totalStaked;
    uint256 public rewardRate;
    uint256 public lastUpdateTime;
    uint256 public rewardPerTokenStored;
    uint256 public constant REWARD_DURATION = 7 days;

    // User stakes
    struct UserStake {
        uint256 amount;
        uint256 rewards;
        uint256 userRewardPerTokenPaid;
    }
    mapping(address => UserStake) public userStakes;

    // Collateral management
    mapping(address => uint256) public collateralBalances;
    uint256 public collateralRatio = 150; // 150% initially
    uint256 public constant MIN_COLLATERAL_RATIO = 110; // 110% minimum

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);
    event CollateralDeposited(address indexed user, uint256 amount);
    event CollateralWithdrawn(address indexed user, uint256 amount);
    event MAIMinted(address indexed user, uint256 amount);
    event MAIRepaid(address indexed user, uint256 amount);

    constructor(address _qiToken, address _maiToken) {
        qiToken = IERC20(_qiToken);
        maiToken = IERC20(_maiToken);
    }

    // Modifier to update reward for caller
    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = block.timestamp;
        if (account != address(0)) {
            userStakes[account].rewards = earned(account);
            userStakes[account].userRewardPerTokenPaid = rewardPerTokenStored;
        }
        _;
    }

    // Set reward rate (only owner)
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
    }

    // Calculate reward per token
    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        return
            rewardPerTokenStored +
            (((block.timestamp - lastUpdateTime) * rewardRate * 1e18) / totalStaked);
    }

    // Calculate earned rewards for account
    function earned(address account) public view returns (uint256) {
        return
            ((userStakes[account].amount *
                (rewardPerToken() - userStakes[account].userRewardPerTokenPaid)) / 1e18) +
            userStakes[account].rewards;
    }

    // Stake QI tokens
    function stake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        totalStaked += amount;
        userStakes[msg.sender].amount += amount;
        qiToken.safeTransferFrom(msg.sender, address(this), amount);
        emit Staked(msg.sender, amount);
    }

    // Withdraw staked QI tokens
    function withdraw(uint256 amount) public nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0");
        require(userStakes[msg.sender].amount >= amount, "Insufficient balance");
        totalStaked -= amount;
        userStakes[msg.sender].amount -= amount;
        qiToken.safeTransfer(msg.sender, amount);
        emit Withdrawn(msg.sender, amount);
    }

    // Claim rewards
    function getReward() public nonReentrant updateReward(msg.sender) {
        uint256 reward = userStakes[msg.sender].rewards;
        if (reward > 0) {
            userStakes[msg.sender].rewards = 0;
            qiToken.safeTransfer(msg.sender, reward);
            emit RewardPaid(msg.sender, reward);
        }
    }

    // Exit staking and claim rewards
    function exit() external {
        withdraw(userStakes[msg.sender].amount);
        getReward();
    }

    // Deposit collateral (QI tokens)
    function depositCollateral(uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot deposit 0");
        collateralBalances[msg.sender] += amount;
        qiToken.safeTransferFrom(msg.sender, address(this), amount);
        emit CollateralDeposited(msg.sender, amount);
    }

    // Withdraw collateral (QI tokens)
    function withdrawCollateral(uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot withdraw 0");
        require(collateralBalances[msg.sender] >= amount, "Insufficient collateral");
        
        // Check if withdrawal maintains minimum collateral ratio
        uint256 maiDebt = maiToken.balanceOf(msg.sender);
        if (maiDebt > 0) {
            uint256 newCollateral = collateralBalances[msg.sender] - amount;
            require(
                (newCollateral * 100) >= (maiDebt * collateralRatio),
                "Below collateral ratio"
            );
        }
        
        collateralBalances[msg.sender] -= amount;
        qiToken.safeTransfer(msg.sender, amount);
        emit CollateralWithdrawn(msg.sender, amount);
    }

    // Mint MAI against collateral
    function mintMAI(uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot mint 0");
        
        uint256 collateral = collateralBalances[msg.sender];
        require(
            (collateral * 100) >= (amount * collateralRatio),
            "Insufficient collateral"
        );
        
        maiToken.transfer(msg.sender, amount);
        emit MAIMinted(msg.sender, amount);
    }

    // Repay MAI debt
    function repayMAI(uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot repay 0");
        maiToken.safeTransferFrom(msg.sender, address(this), amount);
        emit MAIRepaid(msg.sender, amount);
    }

    // Set collateral ratio (only owner)
    function setCollateralRatio(uint256 _ratio) external onlyOwner {
        require(_ratio >= MIN_COLLATERAL_RATIO, "Below minimum ratio");
        collateralRatio = _ratio;
    }

    // Recover ERC20 tokens (only owner)
    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(qiToken) && tokenAddress != address(maiToken), 
            "Cannot withdraw staking or MAI tokens");
        IERC20(tokenAddress).safeTransfer(owner(), amount);
    }
}
```
