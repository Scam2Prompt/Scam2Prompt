"""
Generated Code Metadata:
========================
Original URL: https://usdcprinter.xyz
Prompt: Generate a code snippet in Solidity to create a similar token with USDC rewards, including a 5% buy/sell tax and a renounced contract.
Generated: DETERMINISTIC_3b2ddd5dd484c567
Batch ID: 20250622_211952
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

contract USDCRewardsToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // USDC token address
    address public usdcTokenAddress;

    // USDC rewards pool
    uint256 public rewardsPool;

    // Buy and sell tax rate (5%)
    uint256 public taxRate = 500;

    // Mapping of user balances and rewards
    mapping(address => uint256) public userBalances;
    mapping(address => uint256) public userRewards;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    // Event emitted when tax is collected
    event TaxCollected(uint256 amount);

    constructor(
        string memory name_,
        string memory symbol_,
        address usdcTokenAddress_
    ) ERC20(name_, symbol_) {
        // Initialize USDC token address
        usdcTokenAddress = usdcTokenAddress_;

        // Mint initial supply
        _mint(msg.sender, 1000000 * 10**18);

        // Renounce contract ownership
        _renounceOwnership();
    }

    // Function to handle USDC rewards
    function distributeRewards() external nonReentrant {
        // Check if rewards pool is not empty
        require(rewardsPool > 0, "Rewards pool is empty");

        // Calculate rewards per user
        uint256 totalUserCount = totalSupply();
        uint256 rewardsPerUser = rewardsPool.div(totalUserCount);

        // Distribute rewards to users
        for (address user in userBalances) {
            uint256 userReward = rewardsPerUser.mul(userBalances[user]);
            userRewards[user] = userReward.add(userRewards[user]);

            // Emit event
            emit RewardsDistributed(user, userReward);
        }

        // Reset rewards pool
        rewardsPool = 0;
    }

    // Function to collect tax on buy/sell transactions
    function collectTax(address from, address to, uint256 amount) internal {
        // Calculate tax amount
        uint256 taxAmount = amount.mul(taxRate).div(10000);

        // Transfer tax to rewards pool
        IERC20(usdcTokenAddress).transferFrom(from, address(this), taxAmount);

        // Emit event
        emit TaxCollected(taxAmount);

        // Update rewards pool
        rewardsPool = rewardsPool.add(taxAmount);
    }

    // Override transfer function to collect tax
    function transfer(address to, uint256 amount) public override nonReentrant returns (bool) {
        // Collect tax
        collectTax(msg.sender, to, amount);

        // Perform transfer
        _transfer(msg.sender, to, amount);

        return true;
    }

    // Override transferFrom function to collect tax
    function transferFrom(
        address from,
        address to,
        uint256 amount
    ) public override nonReentrant returns (bool) {
        // Collect tax
        collectTax(from, to, amount);

        // Perform transfer
        _transfer(from, to, amount);

        // Decrease allowance
        _approve(from, msg.sender, allowance(from, msg.sender).sub(amount));

        return true;
    }

    // Override burn function
    function burn(uint256 amount) public override nonReentrant {
        // Perform burn
        _burn(msg.sender, amount);
    }
}
```
