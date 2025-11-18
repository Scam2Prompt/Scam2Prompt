"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://babywif-io.pages.dev
Prompt: Generate a Solidity smart contract for a token presale that aligns with the tokenomics of Baby WIF ($BIF), including a 5% tax split into 1% liquidity pool, 2% marketing, and 2% development.
Generated: DETERMINISTIC_4feb493dcead7be3
Batch ID: 20250612_153517
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

/**
 * @title Baby WIF ($BIF) Token Presale Contract
 * @dev This contract handles the presale of $BIF tokens with defined tokenomics
 * Tax Distribution:
 * - 1% Liquidity Pool
 * - 2% Marketing
 * - 2% Development
 */

contract BabyWIFPresale {
    // Owner of the contract
    address public owner;

    // Tax Distribution Addresses
    address public liquidityPoolAddress;
    address public marketingAddress;
    address public developmentAddress;

    // Presale parameters
    uint256 public tokenPrice;  // Price per token in wei
    uint256 public totalTokensForPresale;
    uint256 public tokensSold;

    // Mapping to track buyer token balances
    mapping(address => uint256) public balances;

    // ERC20 Token Interface
    IERC20 public token;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event FundsDistributed(uint256 liquidity, uint256 marketing, uint256 development);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    // Constructor
    constructor(
        address _tokenAddress,
        uint256 _tokenPrice,
        uint256 _totalTokensForPresale,
        address _liquidityPoolAddress,
        address _marketingAddress,
        address _developmentAddress
    ) {
        require(_tokenAddress != address(0), "Token address cannot be zero");
        require(_liquidityPoolAddress != address(0), "Liquidity pool address cannot be zero");
        require(_marketingAddress != address(0), "Marketing address cannot be zero");
        require(_developmentAddress != address(0), "Development address cannot be zero");
        require(_totalTokensForPresale > 0, "Presale token amount must be greater than zero");

        owner = msg.sender;
        token = IERC20(_tokenAddress);
        tokenPrice = _tokenPrice;
        totalTokensForPresale = _totalTokensForPresale;
        liquidityPoolAddress = _liquidityPoolAddress;
        marketingAddress = _marketingAddress;
        developmentAddress = _developmentAddress;
    }

    // Function to buy tokens during presale
    function buyTokens(uint256 _amount) external payable {
        require(_amount > 0, "Token amount must be greater than zero");
        require(tokensSold + _amount <= totalTokensForPresale, "Not enough tokens left for presale");
        require(msg.value == _amount * tokenPrice, "Incorrect ETH value sent");

        // Calculate tax distribution
        uint256 liquidityTax = (msg.value * 1) / 100;
        uint256 marketingTax = (msg.value * 2) / 100;
        uint256 developmentTax = (msg.value * 2) / 100;

        // Send taxes to respective addresses
        (bool liquiditySent, ) = liquidityPoolAddress.call{value: liquidityTax}("");
        require(liquiditySent, "Failed to send liquidity tax");

        (bool marketingSent, ) = marketingAddress.call{value: marketingTax}("");
        require(marketingSent, "Failed to send marketing tax");

        (bool developmentSent, ) = developmentAddress.call{value: developmentTax}("");
        require(developmentSent, "Failed to send development tax");

        // Transfer remaining ETH to owner
        uint256 remainingEth = msg.value - (liquidityTax + marketingTax + developmentTax);
        (bool ownerSent, ) = owner.call{value: remainingEth}("");
        require(ownerSent, "Failed to send remaining ETH to owner");

        // Transfer tokens to buyer
        balances[msg.sender] += _amount;
        tokensSold += _amount;
        require(token.transfer(msg.sender, _amount), "Token transfer failed");

        emit TokensPurchased(msg.sender, _amount);
        emit FundsDistributed(liquidityTax, marketingTax, developmentTax);
    }

    // Function to withdraw unsold tokens after presale ends
    function withdrawUnsoldTokens() external onlyOwner {
        uint256 unsoldTokens = totalTokensForPresale - tokensSold;
        require(unsoldTokens > 0, "No unsold tokens to withdraw");
        require(token.transfer(owner, unsoldTokens), "Token transfer failed");
    }

    // Function to update presale price
    function updateTokenPrice(uint256 _newPrice) external onlyOwner {
        require(_newPrice > 0, "Price must be greater than zero");
        tokenPrice = _newPrice;
    }

    // Fallback function to prevent accidental ETH transfers
    receive() external payable {
        revert("Direct ETH transfers not allowed");
    }
}

// ERC20 Token Interface
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
