"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://too1m.pages.dev
Prompt: Write Solidity code for a decentralized exchange (DEX) feature that supports $POON token trading on the BASE chain.
Generated: DETERMINISTIC_d25cad63ac9b6c9d
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

/**
 * @title Decentralized Exchange (DEX) for $POON Token on BASE chain
 * @notice This contract allows users to trade $POON tokens.
 * @dev Assumes $POON token follows the ERC20 standard.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
}

contract POONDex {
    IERC20 public poonToken; // $POON token contract address
    address public owner;    // Contract owner
    uint256 public exchangeRate; // Number of $POON tokens per 1 BASE (example rate)

    event TokenPurchased(address indexed user, uint256 baseAmount, uint256 poonAmount);
    event TokenSold(address indexed user, uint256 poonAmount, uint256 baseAmount);
    event ExchangeRateUpdated(uint256 newRate);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    constructor(address _poonTokenAddress, uint256 _initialRate) {
        require(_poonTokenAddress != address(0), "Invalid token address");
        require(_initialRate > 0, "Exchange rate must be greater than zero");
        poonToken = IERC20(_poonTokenAddress);
        owner = msg.sender;
        exchangeRate = _initialRate;
    }

    /**
     * @notice Allows users to buy $POON tokens using BASE currency.
     * @dev Assumes msg.value is the amount of BASE sent.
     */
    function buyTokens() external payable {
        require(msg.value > 0, "BASE amount must be greater than zero");

        uint256 poonAmount = msg.value * exchangeRate;
        require(poonToken.balanceOf(address(this)) >= poonAmount, "Insufficient $POON liquidity in contract");

        // Transfer $POON tokens to the buyer
        require(poonToken.transfer(msg.sender, poonAmount), "Token transfer failed");

        emit TokenPurchased(msg.sender, msg.value, poonAmount);
    }

    /**
     * @notice Allows users to sell $POON tokens in exchange for BASE currency.
     * @param poonAmount The amount of $POON tokens to sell.
     */
    function sellTokens(uint256 poonAmount) external {
        require(poonAmount > 0, "$POON amount must be greater than zero");

        uint256 baseAmount = poonAmount / exchangeRate;
        require(address(this).balance >= baseAmount, "Insufficient BASE liquidity in contract");

        // Transfer $POON tokens from seller to the contract
        require(poonToken.transferFrom(msg.sender, address(this), poonAmount), "Token transfer failed");

        // Send BASE currency to the seller
        (bool success, ) = msg.sender.call{value: baseAmount}("");
        require(success, "BASE transfer failed");

        emit TokenSold(msg.sender, poonAmount, baseAmount);
    }

    /**
     * @notice Allows the owner to update the exchange rate.
     * @param newRate The new exchange rate (number of $POON tokens per BASE).
     */
    function updateExchangeRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Exchange rate must be greater than zero");
        exchangeRate = newRate;
        emit ExchangeRateUpdated(newRate);
    }

    /**
     * @notice Allows the owner to withdraw accumulated BASE currency from the contract.
     * @param amount The amount of BASE currency to withdraw.
     */
    function withdrawBase(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient BASE balance in contract");

        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "BASE withdrawal failed");
    }

    /**
     * @notice Allows the owner to withdraw $POON tokens from the contract.
     * @param amount The amount of $POON tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(poonToken.balanceOf(address(this)) >= amount, "Insufficient $POON balance in contract");

        require(poonToken.transfer(msg.sender, amount), "Token transfer failed");
    }

    /**
     * @notice Fallback function to prevent accidental ETH transfers.
     */
    fallback() external payable {
        revert("Use buyTokens() to purchase $POON");
    }

    /**
     * @notice Receive function to allow deposits of BASE currency.
     */
    receive() external payable {}
}
```
