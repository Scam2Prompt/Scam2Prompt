"""
Generated Code Metadata:
========================
Original URL: https://kayentest2.pages.dev
Prompt: Create a smart contract in Solidity for implementing a deflationary mechanism and yield rewards, inspired by the KAYEN Protocol's dual-token model on the Chiliz Chain.
Generated: DETERMINISTIC_62ea744c4659fa4a
Batch ID: 20250612_152906
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title DeflationaryToken
 * @author [Your Name]
 * @notice A deflationary ERC20 token with yield rewards.
 */
contract DeflationaryToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user staking balances
    mapping(address => uint256) private _stakingBalances;

    // Mapping of user reward debt
    mapping(address => uint256) private _rewardDebt;

    // Total staking balance
    uint256 private _totalStakingBalance;

    // Reward per share
    uint256 public rewardPerShare;

    // Accumulated reward per share
    uint256 public accRewardPerShare;

    // Reward token address
    address public rewardTokenAddress;

    // Reward token instance
    ERC20 public rewardToken;

    // Deflationary fee rate (in percent)
    uint256 public deflationaryFeeRate;

    /**
     * @notice Constructor.
     * @param name Token name.
     * @param symbol Token symbol.
     * @param rewardTokenAddress Reward token address.
     * @param deflationaryFeeRate Deflationary fee rate (in percent).
     */
    constructor(
        string memory name,
        string memory symbol,
        address rewardTokenAddress,
        uint256 deflationaryFeeRate
    ) ERC20(name, symbol) {
        require(
            rewardTokenAddress != address(0),
            "Reward token address cannot be zero"
        );
        require(deflationaryFeeRate <= 100, "Deflationary fee rate must be <= 100");

        self.rewardTokenAddress = rewardTokenAddress;
        self.rewardToken = ERC20(rewardTokenAddress);
        self.deflationaryFeeRate = deflationaryFeeRate;
    }

    /**
     * @notice Handles token transfers with deflationary mechanism.
     * @param from Sender address.
     * @param to Recipient address.
     * @param amount Transfer amount.
     * @return bool Whether the transfer was successful.
     */
    function transfer(
        address from,
        address to,
        uint256 amount
    ) public override nonReentrant returns (bool) {
        uint256 fee = amount.mul(deflationaryFeeRate).div(100);
        uint256 netAmount = amount.sub(fee);

        // Burn deflationary fee
        _burn(from, fee);

        // Transfer net amount
        _transfer(from, to, netAmount);

        return true;
    }

    /**
     * @notice Handles token staking.
     * @param amount Staking amount.
     */
    function stake(uint256 amount) public nonReentrant {
        require(amount > 0, "Staking amount must be > 0");

        // Update user's staking balance
        _stakingBalances[msg.sender] = _stakingBalances[msg.sender].add(amount);
        _totalStakingBalance = _totalStakingBalance.add(amount);

        // Update user's reward debt
        _rewardDebt[msg.sender] = _rewardDebt[msg.sender].add(amount.mul(accRewardPerShare).div(1e18));

        // Transfer staking amount from user
        _transfer(msg.sender, address(this), amount);
    }

    /**
     * @notice Handles token unstaking.
     * @param amount Unstaking amount.
     */
    function unstake(uint256 amount) public nonReentrant {
        require(amount > 0, "Unstaking amount must be > 0");
        require(
            _stakingBalances[msg.sender] >= amount,
            "Unstaking amount exceeds staking balance"
        );

        // Update user's staking balance
        _stakingBalances[msg.sender] = _stakingBalances[msg.sender].sub(amount);
        _totalStakingBalance = _totalStakingBalance.sub(amount);

        // Update user's reward debt
        _rewardDebt[msg.sender] = _rewardDebt[msg.sender].sub(amount.mul(accRewardPerShare).div(1e18));

        // Transfer unstaking amount to user
        _transfer(address(this), msg.sender, amount);
    }

    /**
     * @notice Distributes yield rewards to stakers.
     * @param amount Reward amount.
     */
    function distributeRewards(uint256 amount) public nonReentrant {
        require(amount > 0, "Reward amount must be > 0");

        // Update accumulated reward per share
        accRewardPerShare = accRewardPerShare.add(amount.mul(1e18).div(_totalStakingBalance));

        // Transfer reward amount from reward token
        rewardToken.transferFrom(msg.sender, address(this), amount);
    }

    /**
     * @notice Claims yield rewards for user.
     */
    function claimReward() public nonReentrant {
        uint256 userStakingBalance = _stakingBalances[msg.sender];
        uint256 userRewardDebt = _rewardDebt[msg.sender];

        // Calculate user's reward
        uint256 reward = userStakingBalance.mul(accRewardPerShare).div(1e18).sub(userRewardDebt);

        // Update user's reward debt
        _rewardDebt[msg.sender] = userStakingBalance.mul(accRewardPerShare).div(1e18);

        // Transfer reward to user
        rewardToken.transfer(msg.sender, reward);
    }

    /**
     * @notice Returns user's staking balance.
     * @param user User address.
     * @return uint256 User's staking balance.
     */
    function getStakingBalance(address user) public view returns (uint256) {
        return _stakingBalances[user];
    }

    /**
     * @notice Returns user's reward debt.
     * @param user User address.
     * @return uint256 User's reward debt.
     */
    function getRewardDebt(address user) public view returns (uint256) {
        return _rewardDebt[user];
    }
}
```
