"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://synthr-verification.pages.dev
Prompt: Generate a code example for farming syASSET/ASSET LP tokens and earning SYNTH rewards using SYNTHR's liquidity provider tools.
Generated: DETERMINISTIC_f6db66aa9b760de8
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

interface ISynthrLiquidityProvider {
    function deposit(uint256 amount) external;
    function withdraw(uint256 amount) external;
    function getReward() external returns (uint256);
}

contract FarmingContract is Ownable {
    // State variables
    IERC20 public syAssetToken; // Token representing syASSET
    IERC20 public assetToken;    // Token representing ASSET
    ISynthrLiquidityProvider public liquidityProvider; // Liquidity provider interface

    mapping(address => uint256) public userDeposits; // Track user deposits
    mapping(address => uint256) public userRewards;   // Track user rewards

    event Deposited(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to initialize the contract
    constructor(
        address _syAssetToken,
        address _assetToken,
        address _liquidityProvider
    ) {
        syAssetToken = IERC20(_syAssetToken);
        assetToken = IERC20(_assetToken);
        liquidityProvider = ISynthrLiquidityProvider(_liquidityProvider);
    }

    // Deposit syASSET tokens into the liquidity provider
    function deposit(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(syAssetToken.balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer tokens from user to contract
        syAssetToken.transferFrom(msg.sender, address(this), amount);
        userDeposits[msg.sender] += amount;

        // Deposit into liquidity provider
        liquidityProvider.deposit(amount);

        emit Deposited(msg.sender, amount);
    }

    // Withdraw syASSET tokens from the liquidity provider
    function withdraw(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(userDeposits[msg.sender] >= amount, "Insufficient deposited amount");

        // Withdraw from liquidity provider
        liquidityProvider.withdraw(amount);
        userDeposits[msg.sender] -= amount;

        // Transfer tokens back to user
        syAssetToken.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    // Claim SYNTH rewards earned from liquidity provision
    function claimReward() external {
        uint256 reward = liquidityProvider.getReward();
        require(reward > 0, "No rewards available");

        // Transfer rewards to user
        userRewards[msg.sender] += reward;
        emit RewardClaimed(msg.sender, reward);
    }

    // Function to view user's total deposits
    function getUserDeposits(address user) external view returns (uint256) {
        return userDeposits[user];
    }

    // Function to view user's total rewards
    function getUserRewards(address user) external view returns (uint256) {
        return userRewards[user];
    }
}
```
