"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sage-croissant-c13d3b.netlify.app
Prompt: Create a Solidity contract that allows users to swap Tether Gold (XAU₮) tokens for USD₮ tokens on the Ethereum blockchain. Include functionality for price verification.
Generated: DETERMINISTIC_c910ca9b0d73fc83
Batch ID: 20250612_154355
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
 * @title TokenSwap
 * @dev A smart contract that allows swapping between Tether Gold (XAU₮) and USD₮ tokens
 * with price verification.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

interface IPriceOracle {
    function getXAUTPrice() external view returns (uint256); // Returns the price of XAU₮ in USD (scaled by 1e18)
}

contract TokenSwap {
    // State Variables
    address public owner;
    IERC20 public xautToken; // Tether Gold (XAU₮) token
    IERC20 public usdtToken; // USD₮ token
    IPriceOracle public priceOracle; // Price oracle for verifying XAU₮ price in USD

    // Events
    event Swap(address indexed user, uint256 xautAmount, uint256 usdtAmount);

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can call this function");
        _;
    }

    // Constructor
    constructor(address _xautToken, address _usdtToken, address _priceOracle) {
        require(_xautToken != address(0), "Invalid XAU₮ token address");
        require(_usdtToken != address(0), "Invalid USD₮ token address");
        require(_priceOracle != address(0), "Invalid price oracle address");

        owner = msg.sender;
        xautToken = IERC20(_xautToken);
        usdtToken = IERC20(_usdtToken);
        priceOracle = IPriceOracle(_priceOracle);
    }

    /**
     * @dev Swap XAU₮ tokens for USD₮ tokens.
     * @param xautAmount Amount of XAU₮ tokens to swap.
     */
    function swapXAUTForUSDT(uint256 xautAmount) external {
        require(xautAmount > 0, "Amount must be greater than zero");
        uint256 xautPrice = priceOracle.getXAUTPrice(); // Get XAU₮ price in USD
        require(xautPrice > 0, "Invalid price from oracle");

        // Calculate the equivalent USD₮ amount
        uint256 usdtAmount = (xautAmount * xautPrice) / 1e18;

        // Ensure the contract has enough USD₮ tokens for the swap
        require(usdtToken.balanceOf(address(this)) >= usdtAmount, "Insufficient USD₮ liquidity in contract");

        // Transfer XAU₮ tokens from the user to the contract
        require(xautToken.transferFrom(msg.sender, address(this), xautAmount), "XAU₮ token transfer failed");

        // Transfer USD₮ tokens from the contract to the user
        require(usdtToken.transfer(msg.sender, usdtAmount), "USD₮ token transfer failed");

        emit Swap(msg.sender, xautAmount, usdtAmount);
    }

    /**
     * @dev Allows the owner to deposit USD₮ tokens into the contract.
     * @param usdtAmount Amount of USD₮ tokens to deposit.
     */
    function depositUSDT(uint256 usdtAmount) external onlyOwner {
        require(usdtAmount > 0, "Amount must be greater than zero");

        // Transfer USD₮ tokens from the owner to the contract
        require(usdtToken.transferFrom(msg.sender, address(this), usdtAmount), "USD₮ token transfer failed");
    }

    /**
     * @dev Allows the owner to withdraw USD₮ tokens from the contract.
     * @param usdtAmount Amount of USD₮ tokens to withdraw.
     */
    function withdrawUSDT(uint256 usdtAmount) external onlyOwner {
        require(usdtAmount > 0, "Amount must be greater than zero");
        require(usdtToken.balanceOf(address(this)) >= usdtAmount, "Insufficient USD₮ balance");

        // Transfer USD₮ tokens from the contract to the owner
        require(usdtToken.transfer(msg.sender, usdtAmount), "USD₮ token transfer failed");
    }

    /**
     * @dev Allows the owner to withdraw XAU₮ tokens from the contract.
     * @param xautAmount Amount of XAU₮ tokens to withdraw.
     */
    function withdrawXAUT(uint256 xautAmount) external onlyOwner {
        require(xautAmount > 0, "Amount must be greater than zero");
        require(xautToken.balanceOf(address(this)) >= xautAmount, "Insufficient XAU₮ balance");

        // Transfer XAU₮ tokens from the contract to the owner
        require(xautToken.transfer(msg.sender, xautAmount), "XAU₮ token transfer failed");
    }

    /**
     * @dev Allows the owner to update the price oracle address.
     * @param newPriceOracle Address of the new price oracle.
     */
    function updatePriceOracle(address newPriceOracle) external onlyOwner {
        require(newPriceOracle != address(0), "Invalid price oracle address");
        priceOracle = IPriceOracle(newPriceOracle);
    }
}
```
