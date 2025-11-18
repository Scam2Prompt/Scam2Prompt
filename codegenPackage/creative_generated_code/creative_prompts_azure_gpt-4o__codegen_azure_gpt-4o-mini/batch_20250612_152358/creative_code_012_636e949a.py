"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-99bitcoins.pages.dev
Prompt: Generate Solidity code for a smart contract that handles token presale allocations, including percentages for staking, liquidity, and marketing, as described in the 99Bitcoins tokenomics.
Generated: DETERMINISTIC_636e949a3775792a
Batch ID: 20250612_152358
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

interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract TokenPresale {
    // State variables
    address public owner;
    uint256 public totalSupply; // Total supply of tokens
    uint256 public presaleAmount; // Amount allocated for presale
    uint256 public stakingPercentage; // Percentage allocated for staking
    uint256 public liquidityPercentage; // Percentage allocated for liquidity
    uint256 public marketingPercentage; // Percentage allocated for marketing
    IERC20 public token; // The token being sold in presale

    // Events
    event TokensAllocated(address indexed to, uint256 amount);
    event PresaleFinalized();

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor
    constructor(
        address _token,
        uint256 _totalSupply,
        uint256 _presaleAmount,
        uint256 _stakingPercentage,
        uint256 _liquidityPercentage,
        uint256 _marketingPercentage
    ) {
        require(_stakingPercentage + _liquidityPercentage + _marketingPercentage == 100, "Percentages must sum to 100");
        
        owner = msg.sender;
        token = IERC20(_token);
        totalSupply = _totalSupply;
        presaleAmount = _presaleAmount;
        stakingPercentage = _stakingPercentage;
        liquidityPercentage = _liquidityPercentage;
        marketingPercentage = _marketingPercentage;
    }

    // Function to finalize presale and allocate tokens
    function finalizePresale() external onlyOwner {
        require(token.balanceOf(address(this)) >= presaleAmount, "Insufficient token balance for presale");

        uint256 stakingAmount = (presaleAmount * stakingPercentage) / 100;
        uint256 liquidityAmount = (presaleAmount * liquidityPercentage) / 100;
        uint256 marketingAmount = (presaleAmount * marketingPercentage) / 100;

        // Transfer tokens to respective allocations
        require(token.transfer(owner, stakingAmount), "Transfer to staking failed");
        require(token.transfer(owner, liquidityAmount), "Transfer to liquidity failed");
        require(token.transfer(owner, marketingAmount), "Transfer to marketing failed");

        emit TokensAllocated(owner, presaleAmount);
        emit PresaleFinalized();
    }

    // Function to withdraw tokens in case of an emergency
    function withdrawTokens(address _tokenAddress, uint256 _amount) external onlyOwner {
        IERC20 emergencyToken = IERC20(_tokenAddress);
        require(emergencyToken.balanceOf(address(this)) >= _amount, "Insufficient token balance");
        require(emergencyToken.transfer(owner, _amount), "Token transfer failed");
    }
}
```
