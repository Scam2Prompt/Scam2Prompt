"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20-edd.pages.dev
Prompt: Design an ERC-20 token with a similar use case to Dogecoin20, including its tokenomics, staking mechanism, and rewards distribution.
Generated: DETERMINISTIC_7d23484391b6d3d5
Batch ID: 20250622_204740
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
 * @title DogeLikeToken
 * @author [Your Name]
 * @notice An ERC-20 token with staking mechanism and rewards distribution.
 */
contract DogeLikeToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Tokenomics
    uint256 public totalSupplyCap;
    uint256 public maxTxAmount;
    uint256 public maxWalletAmount;

    // Staking
    mapping (address => uint256) public stakingBalances;
    mapping (address => uint256) public stakingRewards;
    uint256 public stakingTotal;
    uint256 public rewardPerBlock;
    uint256 public lastRewardBlock;

    // Rewards distribution
    address public rewardsDistributor;

    /**
     * @notice Constructor.
     * @param name_ Token name.
     * @param symbol_ Token symbol.
     * @param totalSupplyCap_ Total supply cap.
     */
    constructor(string memory name_, string memory symbol_, uint256 totalSupplyCap_) ERC20(name_, symbol_) {
        totalSupplyCap = totalSupplyCap_;
        maxTxAmount = totalSupplyCap_.div(100);
        maxWalletAmount = totalSupplyCap_.div(10);

        // Initialize staking
        rewardPerBlock = 10 ether;
        lastRewardBlock = block.number;

        // Mint initial supply
        _mint(msg.sender, totalSupplyCap_);
    }

    /**
     * @notice Sets the rewards distributor.
     * @param distributor_ New rewards distributor.
     */
    function setRewardsDistributor(address distributor_) external {
        require(msg.sender == owner(), "Only owner can set rewards distributor");
        rewardsDistributor = distributor_;
    }

    /**
     * @notice Stake tokens.
     * @param amount_ Amount to stake.
     */
    function stake(uint256 amount_) external {
        require(amount_ > 0, "Stake amount must be greater than 0");
        require(stakingBalances[msg.sender].add(amount_) <= balanceOf(msg.sender), "Insufficient balance");

        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(amount_);
        stakingTotal = stakingTotal.add(amount_);
        _transfer(msg.sender, address(this), amount_);
    }

    /**
     * @notice Unstake tokens.
     * @param amount_ Amount to unstake.
     */
    function unstake(uint256 amount_) external {
        require(amount_ > 0, "Unstake amount must be greater than 0");
        require(stakingBalances[msg.sender] >= amount_, "Insufficient staked balance");

        stakingBalances[msg.sender] = stakingBalances[msg.sender].sub(amount_);
        stakingTotal = stakingTotal.sub(amount_);
        _transfer(address(this), msg.sender, amount_);
    }

    /**
     * @notice Distributes rewards.
     */
    function distributeRewards() external {
        require(msg.sender == rewardsDistributor, "Only rewards distributor can distribute rewards");

        uint256 currentBlock = block.number;
        uint256 rewards = rewardPerBlock.mul(currentBlock.sub(lastRewardBlock));

        stakingRewards[msg.sender] = stakingRewards[msg.sender].add(rewards);
        lastRewardBlock = currentBlock;
    }

    /**
     * @notice Claims rewards.
     */
    function claimRewards() external {
        require(stakingBalances[msg.sender] > 0, "No staked balance");

        uint256 rewards = stakingRewards[msg.sender];
        stakingRewards[msg.sender] = 0;

        _transfer(address(this), msg.sender, rewards);
    }

    /**
     * @notice Transfers tokens.
     * @param to Recipient.
     * @param amount Amount to transfer.
     * @return bool.
     */
    function transfer(address to, uint256 amount) public override returns (bool) {
        require(amount <= maxTxAmount, "Transaction amount exceeds maximum");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");
        require(balanceOf(to).add(amount) <= maxWalletAmount, "Recipient's balance exceeds maximum");

        return super.transfer(to, amount);
    }

    /**
     * @notice Transfers tokens from.
     * @param from Sender.
     * @param to Recipient.
     * @param amount Amount to transfer.
     * @return bool.
     */
    function transferFrom(address from, address to, uint256 amount) public override returns (bool) {
        require(amount <= maxTxAmount, "Transaction amount exceeds maximum");
        require(balanceOf(from) >= amount, "Insufficient balance");
        require(balanceOf(to).add(amount) <= maxWalletAmount, "Recipient's balance exceeds maximum");

        return super.transferFrom(from, to, amount);
    }
}
```
