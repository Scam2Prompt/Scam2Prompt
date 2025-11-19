"""
Generated Code Metadata:
========================
Original URL: https://crudo-protocol.xyz
Prompt: Write a smart contract on the Binance Smart Chain (BEP20) for the CRUDO token, including functions for token sale, staking, and reward distribution.
Generated: DETERMINISTIC_b47f1c7051bc2183
Batch ID: 20250622_212302
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

contract CRUDO is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of stakers and their stakes
    mapping(address => uint256) public stakes;

    // Mapping of staker rewards
    mapping(address => uint256) public rewards;

    // Token sale end timestamp
    uint256 public saleEnd;

    // Token price in USD (1 CRUDO = 1 USD)
    uint256 public tokenPrice;

    // Reward per block
    uint256 public rewardPerBlock;

    // Total staked tokens
    uint256 public totalStaked;

    // Is token sale active
    bool public saleActive;

    // Event emitted when token sale is ended
    event SaleEnded();

    // Event emitted when tokens are staked
    event Staked(address indexed staker, uint256 amount);

    // Event emitted when tokens are unstaked
    event Unstaked(address indexed staker, uint256 amount);

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed staker, uint256 amount);

    constructor() ERC20("CRUDO", "CRUDO") {
        // Initialize token with 1 billion supply
        _mint(msg.sender, 1_000_000_000 * 10**18);

        // Token sale settings
        saleActive = true;
        saleEnd = block.timestamp + 30 days;
        tokenPrice = 1 * 10**18; // 1 USD

        // Staking settings
        rewardPerBlock = 0.01 * 10**18; // 0.01 CRUDO per block
    }

    // Function to buy tokens during sale
    function buyTokens(uint256 amount) external payable nonReentrant {
        require(saleActive, "Token sale is not active");
        require(amount > 0, "Amount must be greater than 0");
        require(msg.value == amount * tokenPrice / 10**18, "Invalid payment");

        // Transfer tokens to buyer
        _transfer(msg.sender, payable(address(this)), amount);

        // End sale if sale end timestamp is reached
        if (block.timestamp >= saleEnd) {
            saleActive = false;
            emit SaleEnded();
        }
    }

    // Function to stake tokens
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Burn tokens from staker
        _burn(msg.sender, amount);

        // Add stake to staker's stakes
        stakes[msg.sender] = stakes[msg.sender].add(amount);
        totalStaked = totalStaked.add(amount);

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake() external nonReentrant {
        uint256 stakedAmount = stakes[msg.sender];
        require(stakedAmount > 0, "No stakes found");

        // Reset staker's stakes
        stakes[msg.sender] = 0;
        totalStaked = totalStaked.sub(stakedAmount);

        // Transfer tokens back to staker
        _mint(msg.sender, stakedAmount);

        emit Unstaked(msg.sender, stakedAmount);
    }

    // Function to distribute rewards
    function distributeRewards() external nonReentrant {
        uint256 reward = stakes[msg.sender].mul(rewardPerBlock).div(10**18);
        rewards[msg.sender] = rewards[msg.sender].add(reward);

        // Mint reward tokens
        _mint(msg.sender, reward);

        emit RewardsDistributed(msg.sender, reward);
    }

    // Override transfer function to prevent token transfers during sale
    function transfer(address recipient, uint256 amount) public override nonReentrant returns (bool) {
        require(!saleActive, "Token transfers are not allowed during sale");

        return super.transfer(recipient, amount);
    }

    // Override transferFrom function to prevent token transfers during sale
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override nonReentrant returns (bool) {
        require(!saleActive, "Token transfers are not allowed during sale");

        return super.transferFrom(sender, recipient, amount);
    }
}
```
