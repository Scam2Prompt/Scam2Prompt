"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://popofrogs.pages.dev
Prompt: Write a Solidity contract for a fixed total supply token like $FROP, with allocations for presale, staking, marketing, rewards, and liquidity as outlined in the tokenomics section.
Generated: DETERMINISTIC_54dac851669b0c01
Batch ID: 20250612_150013
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

// Importing the OpenZeppelin ERC20 implementation and Ownable contract
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for the Fixed Supply Token
contract FROPToken is ERC20, Ownable {
    // Total supply of the token
    uint256 public constant TOTAL_SUPPLY = 1_000_000 * 10**18; // 1 million tokens with 18 decimals

    // Allocation constants as per tokenomics
    uint256 public constant PRESALE_ALLOCATION = (TOTAL_SUPPLY * 20) / 100; // 20% for presale
    uint256 public constant STAKING_ALLOCATION = (TOTAL_SUPPLY * 30) / 100; // 30% for staking
    uint256 public constant MARKETING_ALLOCATION = (TOTAL_SUPPLY * 15) / 100; // 15% for marketing
    uint256 public constant REWARDS_ALLOCATION = (TOTAL_SUPPLY * 25) / 100; // 25% for rewards
    uint256 public constant LIQUIDITY_ALLOCATION = (TOTAL_SUPPLY * 10) / 100; // 10% for liquidity

    // Mappings to track allocations
    mapping(address => uint256) public presaleWallets;
    mapping(address => uint256) public stakingWallets;
    mapping(address => uint256) public marketingWallets;
    mapping(address => uint256) public rewardsWallets;
    mapping(address => uint256) public liquidityWallets;

    // Constructor to mint total supply to the contract owner
    constructor() ERC20("FROP", "FROP") {
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    // Function to transfer presale tokens to a wallet
    function allocatePresaleTokens(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Invalid address");
        require(amount <= PRESALE_ALLOCATION, "Exceeds presale allocation");
        presaleWallets[to] += amount;
        _transfer(owner(), to, amount);
    }

    // Function to transfer staking tokens
    function allocateStakingTokens(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Invalid address");
        require(amount <= STAKING_ALLOCATION, "Exceeds staking allocation");
        stakingWallets[to] += amount;
        _transfer(owner(), to, amount);
    }

    // Function to transfer marketing tokens
    function allocateMarketingTokens(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Invalid address");
        require(amount <= MARKETING_ALLOCATION, "Exceeds marketing allocation");
        marketingWallets[to] += amount;
        _transfer(owner(), to, amount);
    }

    // Function to transfer rewards tokens
    function allocateRewardsTokens(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Invalid address");
        require(amount <= REWARDS_ALLOCATION, "Exceeds rewards allocation");
        rewardsWallets[to] += amount;
        _transfer(owner(), to, amount);
    }

    // Function to transfer liquidity tokens
    function allocateLiquidityTokens(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Invalid address");
        require(amount <= LIQUIDITY_ALLOCATION, "Exceeds liquidity allocation");
        liquidityWallets[to] += amount;
        _transfer(owner(), to, amount);
    }

    // Function to withdraw remaining tokens (if necessary) to the owner's address
    function withdrawRemainingTokens() external onlyOwner {
        uint256 remainingTokens = balanceOf(address(this));
        require(remainingTokens > 0, "No tokens to withdraw");
        _transfer(address(this), msg.sender, remainingTokens);
    }

    // Override the _beforeTokenTransfer hook to prevent transfers until allocations are set
    function _beforeTokenTransfer(address from, address to, uint256 amount) internal virtual override {
        require(from == address(0) || (presaleWallets[from] == 0 && stakingWallets[from] == 0 &&
            marketingWallets[from] == 0 && rewardsWallets[from] == 0 && liquidityWallets[from] == 0), 
            "Token transfer not allowed until allocations are set");
        super._beforeTokenTransfer(from, to, amount);
    }
}
```
