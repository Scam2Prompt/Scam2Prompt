"""
Generated Code Metadata:
========================
Original URL: https://iziswap.fi
Prompt: "Generate a smart contract code for a liquidity mining-based bond with no Impermanent Loss for LP Farming, similar to iZiSwap's Farm iUSD."
Generated: DETERMINISTIC_6d398ae5a5897f94
Batch ID: 20250622_210821
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

/**
 * @title Liquidity Mining Bond Contract
 * @dev A smart contract for liquidity mining-based bonds with no impermanent loss.
 *      Users can deposit liquidity and earn rewards based on their bond holdings.
 */
contract LiquidityMiningBond {
    // State variables
    address public owner; // Contract owner
    uint256 public totalBondSupply; // Total supply of bonds
    uint256 public rewardRate; // Reward rate per bond
    uint256 public bondPrice; // Price of each bond in liquidity tokens

    mapping(address => uint256) public bondBalances; // User bond balances
    mapping(address => uint256) public rewardBalances; // User reward balances
    mapping(address => uint256) public lastClaimed; // Last reward claim timestamp

    IERC20 public liquidityToken; // Liquidity token used for deposits
    IERC20 public rewardToken; // Reward token distributed to users

    // Events
    event BondPurchased(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event BondRedeemed(address indexed user, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    modifier updateRewards(address user) {
        if (bondBalances[user] > 0) {
            uint256 timeElapsed = block.timestamp - lastClaimed[user];
            rewardBalances[user] += (bondBalances[user] * rewardRate * timeElapsed) / 1e18;
        }
        lastClaimed[user] = block.timestamp;
        _;
    }

    // Constructor
    constructor(
        address _liquidityToken,
        address _rewardToken,
        uint256 _rewardRate,
        uint256 _bondPrice
    ) {
        owner = msg.sender;
        liquidityToken = IERC20(_liquidityToken);
        rewardToken = IERC20(_rewardToken);
        rewardRate = _rewardRate;
        bondPrice = _bondPrice;
    }

    /**
     * @dev Purchase bonds by depositing liquidity tokens.
     * @param amount The number of bonds to purchase.
     */
    function purchaseBond(uint256 amount) external updateRewards(msg.sender) {
        require(amount > 0, "Amount must be greater than zero");
        uint256 cost = amount * bondPrice;
        require(
            liquidityToken.transferFrom(msg.sender, address(this), cost),
            "Liquidity token transfer failed"
        );

        bondBalances[msg.sender] += amount;
        totalBondSupply += amount;

        emit BondPurchased(msg.sender, amount);
    }

    /**
     * @dev Claim accumulated rewards.
     */
    function claimRewards() external updateRewards(msg.sender) {
        uint256 rewards = rewardBalances[msg.sender];
        require(rewards > 0, "No rewards available");

        rewardBalances[msg.sender] = 0;
        require(rewardToken.transfer(msg.sender, rewards), "Reward token transfer failed");

        emit RewardClaimed(msg.sender, rewards);
    }

    /**
     * @dev Redeem bonds and withdraw liquidity tokens.
     * @param amount The number of bonds to redeem.
     */
    function redeemBond(uint256 amount) external updateRewards(msg.sender) {
        require(amount > 0, "Amount must be greater than zero");
        require(bondBalances[msg.sender] >= amount, "Insufficient bond balance");

        uint256 refund = amount * bondPrice;
        bondBalances[msg.sender] -= amount;
        totalBondSupply -= amount;

        require(liquidityToken.transfer(msg.sender, refund), "Liquidity token transfer failed");

        emit BondRedeemed(msg.sender, amount);
    }

    /**
     * @dev Update the reward rate. Only callable by the owner.
     * @param newRewardRate The new reward rate per bond.
     */
    function updateRewardRate(uint256 newRewardRate) external onlyOwner {
        rewardRate = newRewardRate;
    }

    /**
     * @dev Update the bond price. Only callable by the owner.
     * @param newBondPrice The new price of each bond in liquidity tokens.
     */
    function updateBondPrice(uint256 newBondPrice) external onlyOwner {
        bondPrice = newBondPrice;
    }

    /**
     * @dev Emergency withdrawal of tokens. Only callable by the owner.
     * @param token The token to withdraw.
     * @param amount The amount to withdraw.
     */
    function emergencyWithdraw(address token, uint256 amount) external onlyOwner {
        require(IERC20(token).transfer(owner, amount), "Token transfer failed");
    }
}

// Interface for ERC20 tokens
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);

    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);
}
```
