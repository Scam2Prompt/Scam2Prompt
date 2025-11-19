"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletconnect-v3-presale-boilerplate-website.pages.dev
Prompt: Generate a smart contract code snippet for a token presale similar to the BOI Coin presale, including functions for purchasing tokens and tracking raised funds in USDT and ETH.
Generated: DETERMINISTIC_bc788d6e5c71e8b4
Batch ID: 20250612_135202
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
 * @title TokenPresale
 * @dev A smart contract for a token presale allowing purchases in ETH and USDT.
 */
contract TokenPresale {
    // Presale parameters
    address public owner;
    uint256 public tokenPriceInETH; // Price per token in ETH (e.g., 1 token = 0.001 ETH)
    uint256 public tokenPriceInUSDT; // Price per token in USDT (e.g., 1 token = 1 USDT)
    
    address public usdtTokenAddress; // ERC20 USDT token address
    uint256 public totalRaisedETH; // ETH raised during the presale
    uint256 public totalRaisedUSDT; // USDT raised during the presale

    mapping(address => uint256) public tokensPurchased; // Track tokens purchased by each address

    // Events
    event TokensPurchasedETH(address indexed buyer, uint256 amountTokens, uint256 amountETH);
    event TokensPurchasedUSDT(address indexed buyer, uint256 amountTokens, uint256 amountUSDT);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    constructor(uint256 _tokenPriceInETH, uint256 _tokenPriceInUSDT, address _usdtTokenAddress) {
        owner = msg.sender;
        tokenPriceInETH = _tokenPriceInETH;
        tokenPriceInUSDT = _tokenPriceInUSDT;
        usdtTokenAddress = _usdtTokenAddress;
    }

    /**
     * @dev Allows users to purchase tokens using ETH.
     * @param numTokens Number of tokens to purchase.
     */
    function purchaseTokensWithETH(uint256 numTokens) external payable {
        require(numTokens > 0, "Number of tokens must be greater than zero");
        uint256 requiredETH = numTokens * tokenPriceInETH;
        require(msg.value == requiredETH, "Incorrect ETH amount sent");

        // Track raised funds
        totalRaisedETH += msg.value;

        // Track purchased tokens
        tokensPurchased[msg.sender] += numTokens;

        emit TokensPurchasedETH(msg.sender, numTokens, msg.value);
    }

    /**
     * @dev Allows users to purchase tokens using USDT.
     * @param numTokens Number of tokens to purchase.
     */
    function purchaseTokensWithUSDT(uint256 numTokens) external {
        require(numTokens > 0, "Number of tokens must be greater than zero");
        uint256 requiredUSDT = numTokens * tokenPriceInUSDT;

        IERC20 usdtToken = IERC20(usdtTokenAddress);
        require(
            usdtToken.transferFrom(msg.sender, address(this), requiredUSDT),
            "USDT transfer failed"
        );

        // Track raised funds
        totalRaisedUSDT += requiredUSDT;

        // Track purchased tokens
        tokensPurchased[msg.sender] += numTokens;

        emit TokensPurchasedUSDT(msg.sender, numTokens, requiredUSDT);
    }

    /**
     * @dev Withdraws ETH raised during the presale to the owner.
     */
    function withdrawETH() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No ETH balance to withdraw");
        payable(owner).transfer(balance);
    }

    /**
     * @dev Withdraws USDT raised during the presale to the owner.
     */
    function withdrawUSDT() external onlyOwner {
        IERC20 usdtToken = IERC20(usdtTokenAddress);
        uint256 balance = usdtToken.balanceOf(address(this));
        require(balance > 0, "No USDT balance to withdraw");
        usdtToken.transfer(owner, balance);
    }
}

// Interface for ERC20 tokens
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
