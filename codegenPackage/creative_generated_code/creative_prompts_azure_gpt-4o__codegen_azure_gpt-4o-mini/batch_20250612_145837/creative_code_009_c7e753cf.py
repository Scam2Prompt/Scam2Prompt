"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etuktuk-io-web.pages.dev
Prompt: Write a smart contract in Solidity that enables users to purchase $TUK tokens using multiple cryptocurrencies like BNB, ETH, and USDT, as described in the eTukTuk presale process.
Generated: DETERMINISTIC_c7e753cf8c36f05c
Batch ID: 20250612_145837
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title eTukTukPresale
 * @dev A smart contract for the eTukTuk presale that allows users to purchase $TUK tokens using BNB, ETH, and USDT.
 */
contract eTukTukPresale is Ownable {
    // Address of the TUK token
    IERC20 public tukToken;
    
    // Presale state
    bool public presaleActive;

    // Exchange rates for each cryptocurrency
    uint256 public ethRate = 100; // 1 ETH = 100 TUK
    uint256 public bnbRate = 100; // 1 BNB = 100 TUK
    uint256 public usdtRate = 100; // 1 USDT = 100 TUK

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount, string currency);

    /**
     * @dev Constructor to set the TUK token address
     * @param _tukToken The address of the TUK token contract
     */
    constructor(IERC20 _tukToken) {
        tukToken = _tukToken;
        presaleActive = false; // Presale is inactive initially
    }

    /**
     * @dev Starts the presale
     */
    function startPresale() external onlyOwner {
        presaleActive = true;
    }

    /**
     * @dev Stops the presale
     */
    function stopPresale() external onlyOwner {
        presaleActive = false;
    }

    /**
     * @dev Allows users to purchase TUK tokens with ETH
     */
    function buyWithETH() external payable {
        require(presaleActive, "Presale is not active");
        require(msg.value > 0, "Must send BNB/ETH to purchase TUK");

        uint256 amountToPurchase = msg.value * ethRate;
        require(tukToken.balanceOf(address(this)) >= amountToPurchase, "Not enough TUK tokens in contract");

        // Transfer TUK tokens to the buyer
        tukToken.transfer(msg.sender, amountToPurchase);
        emit TokensPurchased(msg.sender, amountToPurchase, "ETH");
    }

    /**
     * @dev Allows users to purchase TUK tokens with BNB
     */
    function buyWithBNB() external payable {
        require(presaleActive, "Presale is not active");
        require(msg.value > 0, "Must send BNB to purchase TUK");

        uint256 amountToPurchase = msg.value * bnbRate;
        require(tukToken.balanceOf(address(this)) >= amountToPurchase, "Not enough TUK tokens in contract");

        // Transfer TUK tokens to the buyer
        tukToken.transfer(msg.sender, amountToPurchase);
        emit TokensPurchased(msg.sender, amountToPurchase, "BNB");
    }

    /**
     * @dev Allows users to purchase TUK tokens with USDT
     * @param usdtAmount The amount of USDT to spend
     * @param usdtToken The address of the USDT token contract
     */
    function buyWithUSDT(uint256 usdtAmount, address usdtToken) external {
        require(presaleActive, "Presale is not active");
        require(usdtAmount > 0, "Must send USDT to purchase TUK");

        IERC20 usdt = IERC20(usdtToken);
        require(usdt.balanceOf(msg.sender) >= usdtAmount, "Insufficient USDT balance");
        require(usdt.allowance(msg.sender, address(this)) >= usdtAmount, "USDT allowance too low");

        uint256 amountToPurchase = usdtAmount * usdtRate;
        require(tukToken.balanceOf(address(this)) >= amountToPurchase, "Not enough TUK tokens in contract");

        // Transfer USDT from buyer to the contract
        usdt.transferFrom(msg.sender, address(this), usdtAmount);
        // Transfer TUK tokens to the buyer
        tukToken.transfer(msg.sender, amountToPurchase);
        emit TokensPurchased(msg.sender, amountToPurchase, "USDT");
    }

    /**
     * @dev Withdraws any collected funds from the presale
     */
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @dev Withdraws TUK tokens from the contract
     * @param amount The amount of TUK tokens to withdraw
     */
    function withdrawTUK(uint256 amount) external onlyOwner {
        require(tukToken.balanceOf(address(this)) >= amount, "Not enough TUK tokens in contract");
        tukToken.transfer(owner(), amount);
    }

    /**
     * @dev Fallback function to prevent sending ether directly to the contract
     */
    receive() external payable {
        revert("Direct payments not allowed. Use the buy methods.");
    }
}
```
