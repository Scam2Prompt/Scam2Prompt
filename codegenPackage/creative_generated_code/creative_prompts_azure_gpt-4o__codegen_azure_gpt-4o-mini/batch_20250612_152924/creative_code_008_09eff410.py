"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20en.pages.dev
Prompt: Create a Solidity contract for DOGE20 tokenomics that ensures a fixed supply distribution: 25% presale, 25% marketing, 25% treasury, 15% staking rewards, and 10% liquidity.
Generated: DETERMINISTIC_09eff41073bbfe5d
Batch ID: 20250612_152924
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

// Import the OpenZeppelin ERC20 implementation for secure token creation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// DOGE20 Token Contract
contract DOGE20 is ERC20, Ownable {
    // Define constant values for tokenomics
    uint256 public constant TOTAL_SUPPLY = 1_000_000 * 10 ** decimals(); // Total supply of 1,000,000 tokens
    uint256 public constant PRESALE_ALLOCATION = (TOTAL_SUPPLY * 25) / 100; // 25% for presale
    uint256 public constant MARKETING_ALLOCATION = (TOTAL_SUPPLY * 25) / 100; // 25% for marketing
    uint256 public constant TREASURY_ALLOCATION = (TOTAL_SUPPLY * 25) / 100; // 25% for treasury
    uint256 public constant STAKING_REWARDS_ALLOCATION = (TOTAL_SUPPLY * 15) / 100; // 15% for staking rewards
    uint256 public constant LIQUIDITY_ALLOCATION = (TOTAL_SUPPLY * 10) / 100; // 10% for liquidity

    // Addresses for different allocations
    address public presaleAddress;
    address public marketingAddress;
    address public treasuryAddress;
    address public stakingRewardsAddress;
    address public liquidityAddress;

    // Constructor to initialize the token with its name and symbol
    constructor(
        address _presaleAddress,
        address _marketingAddress,
        address _treasuryAddress,
        address _stakingRewardsAddress,
        address _liquidityAddress
    ) ERC20("DOGE20", "DOGE20") {
        // Set the allocation addresses
        presaleAddress = _presaleAddress;
        marketingAddress = _marketingAddress;
        treasuryAddress = _treasuryAddress;
        stakingRewardsAddress = _stakingRewardsAddress;
        liquidityAddress = _liquidityAddress;
        
        // Mint the tokens according to the defined allocations
        _mint(presaleAddress, PRESALE_ALLOCATION);
        _mint(marketingAddress, MARKETING_ALLOCATION);
        _mint(treasuryAddress, TREASURY_ALLOCATION);
        _mint(stakingRewardsAddress, STAKING_REWARDS_ALLOCATION);
        _mint(liquidityAddress, LIQUIDITY_ALLOCATION);
    }

    // Function to retrieve the total supply of the token
    function totalSupply() public view override returns (uint256) {
        return TOTAL_SUPPLY;
    }

    // Function to retrieve the balance of an account
    function balanceOf(address account) public view override returns (uint256) {
        return super.balanceOf(account);
    }

    // Function to transfer tokens from the sender to a recipient
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        require(amount > 0, "Transfer amount must be greater than zero.");
        return super.transfer(recipient, amount);
    }

    // Function to approve an allowance for a spender
    function approve(address spender, uint256 amount) public override returns (bool) {
        require(amount > 0, "Approval amount must be greater than zero.");
        return super.approve(spender, amount);
    }

    // Function to transfer tokens on behalf of another account
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        require(amount > 0, "Transfer amount must be greater than zero.");
        return super.transferFrom(sender, recipient, amount);
    }
}
```
