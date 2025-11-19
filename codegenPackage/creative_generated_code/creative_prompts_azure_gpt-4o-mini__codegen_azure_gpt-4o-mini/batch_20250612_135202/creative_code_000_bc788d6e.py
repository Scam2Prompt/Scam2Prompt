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

// Import the required OpenZeppelin contracts
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title Presale Contract
 * @dev A smart contract for a token presale where users can purchase tokens using ETH or USDT.
 */
contract TokenPresale is Ownable {
    // Token to be sold in the presale
    IERC20 public token;

    // USDT token address (ERC20)
    IERC20 public usdt;

    // Price of the token in USDT and ETH
    uint256 public tokenPriceInUSDT;
    uint256 public tokenPriceInETH;

    // Amount of funds raised in USDT and ETH
    uint256 public totalRaisedUSDT;
    uint256 public totalRaisedETH;

    // Event emitted when tokens are purchased
    event TokensPurchased(address indexed buyer, uint256 amount, string currency);

    // Constructor to set the token and USDT addresses and prices
    constructor(IERC20 _token, IERC20 _usdt, uint256 _tokenPriceInUSDT, uint256 _tokenPriceInETH) {
        token = _token;
        usdt = _usdt;
        tokenPriceInUSDT = _tokenPriceInUSDT;
        tokenPriceInETH = _tokenPriceInETH;
    }

    /**
     * @dev Purchase tokens using USDT
     * @param amount Amount of USDT to spend
     */
    function buyTokensWithUSDT(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        uint256 tokensToPurchase = amount * 1e18 / tokenPriceInUSDT; // Amount of tokens to be purchased

        // Transfer USDT from buyer to the contract
        require(usdt.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Transfer tokens to the buyer
        require(token.transfer(msg.sender, tokensToPurchase), "Token transfer failed");

        // Update total raised USDT
        totalRaisedUSDT += amount;

        // Emit event
        emit TokensPurchased(msg.sender, tokensToPurchase, "USDT");
    }

    /**
     * @dev Purchase tokens using ETH
     */
    function buyTokensWithETH() external payable {
        require(msg.value > 0, "Amount must be greater than 0");
        uint256 tokensToPurchase = msg.value * 1e18 / tokenPriceInETH; // Amount of tokens to be purchased

        // Transfer tokens to the buyer
        require(token.transfer(msg.sender, tokensToPurchase), "Token transfer failed");

        // Update total raised ETH
        totalRaisedETH += msg.value;

        // Emit event
        emit TokensPurchased(msg.sender, tokensToPurchase, "ETH");
    }

    /**
     * @dev Withdraw raised funds to the owner's address
     * @param to Address to withdraw funds to
     * @param amount Amount of USDT to withdraw
     */
    function withdrawUSDT(address to, uint256 amount) external onlyOwner {
        require(amount <= usdt.balanceOf(address(this)), "Insufficient USDT balance");
        require(usdt.transfer(to, amount), "Withdrawal failed");
    }

    /**
     * @dev Withdraw ETH raised to the owner's address
     * @param to Address to withdraw funds to
     */
    function withdrawETH(address payable to) external onlyOwner {
        require(address(this).balance > 0, "No ETH to withdraw");
        to.transfer(address(this).balance);
    }

    /**
     * @dev Fallback function to receive ETH
     */
    receive() external payable {}
}
```
