"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apps-dogecoin20.pages.dev
Prompt: Create an ERC-20 token contract in Solidity for DOGE20 with a fixed supply of 140,000,000,000 tokens and tokenomics that allocate percentages for presale, marketing, treasury, staking rewards, and liquidity.
Generated: DETERMINISTIC_5205a893479fe1ee
Batch ID: 20250612_153400
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

// Import the ERC20 interface
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// DOGE20 Token Contract
contract DOGE20 is ERC20, Ownable {
    // Total supply of tokens
    uint256 public constant TOTAL_SUPPLY = 140_000_000_000 * 10 ** decimals();

    // Allocation percentages
    uint256 public constant PRESALE_ALLOCATION = 20; // 20%
    uint256 public constant MARKETING_ALLOCATION = 10; // 10%
    uint256 public constant TREASURY_ALLOCATION = 15; // 15%
    uint256 public constant STAKING_REWARDS_ALLOCATION = 25; // 25%
    uint256 public constant LIQUIDITY_ALLOCATION = 30; // 30%

    // Allocation amounts
    uint256 public presaleTokens;
    uint256 public marketingTokens;
    uint256 public treasuryTokens;
    uint256 public stakingRewardsTokens;
    uint256 public liquidityTokens;

    // Mapping to track the claimed tokens for each allocation
    mapping(address => bool) public presaleClaimed;

    // Events
    event TokensClaimed(address indexed user, uint256 amount);

    // Constructor to set up the token and allocate tokens
    constructor() ERC20("DOGE20", "DOGE20") {
        // Mint total supply to the contract creator
        _mint(msg.sender, TOTAL_SUPPLY);
        
        // Calculate token allocations based on total supply
        presaleTokens = (TOTAL_SUPPLY * PRESALE_ALLOCATION) / 100;
        marketingTokens = (TOTAL_SUPPLY * MARKETING_ALLOCATION) / 100;
        treasuryTokens = (TOTAL_SUPPLY * TREASURY_ALLOCATION) / 100;
        stakingRewardsTokens = (TOTAL_SUPPLY * STAKING_REWARDS_ALLOCATION) / 100;
        liquidityTokens = (TOTAL_SUPPLY * LIQUIDITY_ALLOCATION) / 100;
    }

    // Function to claim presale tokens
    function claimPresaleTokens() external {
        require(!presaleClaimed[msg.sender], "Tokens already claimed");
        require(presaleTokens > 0, "No presale tokens available");

        // Mark the address as having claimed tokens
        presaleClaimed[msg.sender] = true;

        // Transfer presale tokens to the user
        _transfer(owner(), msg.sender, presaleTokens);

        emit TokensClaimed(msg.sender, presaleTokens);
    }

    // Function to withdraw marketing tokens by the owner
    function withdrawMarketingTokens(address to, uint256 amount) external onlyOwner {
        require(amount <= marketingTokens, "Insufficient marketing tokens");
        marketingTokens -= amount;
        _transfer(owner(), to, amount);
    }

    // Function to withdraw treasury tokens by the owner
    function withdrawTreasuryTokens(address to, uint256 amount) external onlyOwner {
        require(amount <= treasuryTokens, "Insufficient treasury tokens");
        treasuryTokens -= amount;
        _transfer(owner(), to, amount);
    }

    // Function to withdraw staking rewards by the owner
    function withdrawStakingRewardsTokens(address to, uint256 amount) external onlyOwner {
        require(amount <= stakingRewardsTokens, "Insufficient staking rewards tokens");
        stakingRewardsTokens -= amount;
        _transfer(owner(), to, amount);
    }

    // Function to withdraw liquidity tokens by the owner
    function withdrawLiquidityTokens(address to, uint256 amount) external onlyOwner {
        require(amount <= liquidityTokens, "Insufficient liquidity tokens");
        liquidityTokens -= amount;
        _transfer(owner(), to, amount);
    }
}
```
