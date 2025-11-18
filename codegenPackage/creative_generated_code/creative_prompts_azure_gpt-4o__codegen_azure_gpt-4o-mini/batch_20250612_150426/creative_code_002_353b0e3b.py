"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://idegen-claims.pages.dev
Prompt: Generate Solidity code for a smart contract implementing iDEGEN's tokenomics, including 90% allocation for auction and community and 10% for liquidity.
Generated: DETERMINISTIC_353b0e3b5f88a48d
Batch ID: 20250612_150426
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

// Import the OpenZeppelin ERC20 contract for standard token functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// @title iDEGEN Token Contract
// @dev This contract implements the tokenomics for the iDEGEN token with specified allocations.
contract IdegenToken is ERC20, Ownable {
    // Percentages for allocations
    uint256 public constant AUCTION_COMMUNITY_ALLOCATION = 90; // 90% for auction and community
    uint256 public constant LIQUIDITY_ALLOCATION = 10; // 10% for liquidity
    
    // Total supply of the token
    uint256 public constant TOTAL_SUPPLY = 1_000_000 * 10 ** decimals(); // 1 million tokens with decimals

    // Events for tracking allocations
    event TokensAllocated(address indexed recipient, uint256 amount);

    // @dev Constructor that mints tokens according to the specified allocations
    constructor() ERC20("iDEGEN Token", "IDEGEN") {
        // Mint tokens for auction and community
        uint256 auctionCommunityAmount = (TOTAL_SUPPLY * AUCTION_COMMUNITY_ALLOCATION) / 100;
        _mint(msg.sender, auctionCommunityAmount);
        emit TokensAllocated(msg.sender, auctionCommunityAmount);

        // Mint tokens for liquidity
        uint256 liquidityAmount = (TOTAL_SUPPLY * LIQUIDITY_ALLOCATION) / 100;
        _mint(address(this), liquidityAmount); // Mint liquidity tokens to the contract itself
        emit TokensAllocated(address(this), liquidityAmount);
    }

    // @dev Function to withdraw liquidity tokens by the owner
    function withdrawLiquidityTokens(uint256 amount) external onlyOwner {
        require(amount <= balanceOf(address(this)), "Insufficient liquidity tokens");
        _transfer(address(this), msg.sender, amount);
    }

    // @dev Function to get the total supply of tokens
    function totalSupply() public view override returns (uint256) {
        return TOTAL_SUPPLY;
    }

    // @dev Override the transfer function to include custom logic if needed
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        require(amount > 0, "Transfer amount must be greater than zero");
        return super.transfer(recipient, amount);
    }

    // @dev Override the approve function to include custom logic if needed
    function approve(address spender, uint256 amount) public override returns (bool) {
        require(amount > 0, "Approval amount must be greater than zero");
        return super.approve(spender, amount);
    }
}
```
