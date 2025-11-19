"""
Generated Code Metadata:
========================
Original URL: https://etuktuk-io-web.pages.dev
Prompt: Write a smart contract in Solidity that enables users to purchase $TUK tokens using multiple cryptocurrencies like BNB, ETH, and USDT, as described in the eTukTuk presale process.
Generated: DETERMINISTIC_c7e753cf8c36f05c
Batch ID: 20250612_145837
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title eTukTukPresale
 * @dev A smart contract for the eTukTuk presale allowing users to purchase $TUK tokens
 * using BNB, ETH, and USDT.
 */
contract eTukTukPresale is Ownable {
    // The token being sold
    IERC20 public tukToken;

    // Price of 1 $TUK in BNB
    uint256 public priceInBNB = 0.01 ether; // Example price, adjust as needed

    // Price of 1 $TUK in ETH
    uint256 public priceInETH = 0.01 ether; // Example price, adjust as needed

    // Price of 1 $TUK in USDT
    uint256 public priceInUSDT = 1 * 10**18; // Example price, adjust as needed

    // Event emitted when tokens are purchased
    event TokensPurchased(address indexed buyer, uint256 amount, string currency);

    /**
     * @dev Constructor to initialize the contract with the $TUK token address.
     * @param _tukToken The address of the $TUK token contract.
     */
    constructor(address _tukToken) {
        require(_tukToken != address(0), "Invalid token address");
        tukToken = IERC20(_tukToken);
    }

    /**
     * @dev Purchase $TUK tokens using BNB.
     */
    function buyWithBNB() external payable {
        require(msg.value > 0, "Send BNB to purchase tokens");
        uint256 tokensToBuy = (msg.value * 1 ether) / priceInBNB;
        require(tukToken.balanceOf(address(this)) >= tokensToBuy, "Not enough tokens available");

        // Transfer $TUK tokens to the buyer
        tukToken.transfer(msg.sender, tokensToBuy);
        emit TokensPurchased(msg.sender, tokensToBuy, "BNB");
    }

    /**
     * @dev Purchase $TUK tokens using ETH.
     */
    function buyWithETH() external payable {
        require(msg.value > 0, "Send ETH to purchase tokens");
        uint256 tokensToBuy = (msg.value * 1 ether) / priceInETH;
        require(tukToken.balanceOf(address(this)) >= tokensToBuy, "Not enough tokens available");

        // Transfer $TUK tokens to the buyer
        tukToken.transfer(msg.sender, tokensToBuy);
        emit TokensPurchased(msg.sender, tokensToBuy, "ETH");
    }

    /**
     * @dev Purchase $TUK tokens using USDT.
     * @param amount The amount of USDT to send for purchasing tokens.
     */
    function buyWithUSDT(uint256 amount) external {
        require(amount > 0, "Send USDT to purchase tokens");
        IERC20 usdtToken = IERC20(0x...); // Replace with the actual USDT token address
        require(usdtToken.transferFrom(msg.sender, address(this), amount), "USDT transfer failed");

        uint256 tokensToBuy = (amount * 1 ether) / priceInUSDT;
        require(tukToken.balanceOf(address(this)) >= tokensToBuy, "Not enough tokens available");

        // Transfer $TUK tokens to the buyer
        tukToken.transfer(msg.sender, tokensToBuy);
        emit TokensPurchased(msg.sender, tokensToBuy, "USDT");
    }

    /**
     * @dev Withdraw BNB from the contract.
     * Only the owner can call this function.
     */
    function withdrawBNB() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @dev Withdraw USDT from the contract.
     * Only the owner can call this function.
     */
    function withdrawUSDT() external onlyOwner {
        IERC20 usdtToken = IERC20(0x...); // Replace with the actual USDT token address
        uint256 balance = usdtToken.balanceOf(address(this));
        require(balance > 0, "No USDT to withdraw");
        usdtToken.transfer(owner(), balance);
    }

    /**
     * @dev Withdraw $TUK tokens from the contract.
     * Only the owner can call this function.
     */
    function withdrawTUK() external onlyOwner {
        uint256 balance = tukToken.balanceOf(address(this));
        require(balance > 0, "No $TUK to withdraw");
        tukToken.transfer(owner(), balance);
    }

    /**
     * @dev Fallback function to accept BNB.
     */
    receive() external payable {}
}
```
