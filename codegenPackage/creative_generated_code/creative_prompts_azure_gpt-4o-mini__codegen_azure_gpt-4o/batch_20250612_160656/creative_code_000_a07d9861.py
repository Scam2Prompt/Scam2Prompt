"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-brc20.pages.dev
Prompt: Generate a code snippet for a smart contract that facilitates the public sale of the $BRC20DEX token, accepting ETH, BSC, BUSD, and USDT as payment methods.
Generated: DETERMINISTIC_a07d986141c444d8
Batch ID: 20250612_160656
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
 * @title BRC20DEX Public Sale Smart Contract
 * @dev Smart contract for facilitating the public sale of $BRC20DEX token
 *      Accepts ETH, Binance Smart Chain (BSC), BUSD, and USDT as payment methods.
 */
contract BRC20DEXSale {
    // Token being sold
    address public tokenAddress;
    // Owner of the contract
    address public owner;
    // Sale price per token in wei (adjustable)
    uint256 public tokenPrice;

    // Accepted payment tokens
    address public BUSD;
    address public USDT;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount, string paymentMethod);

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    constructor(
        address _tokenAddress,
        address _BUSD,
        address _USDT,
        uint256 _tokenPrice
    ) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_BUSD != address(0), "Invalid BUSD address");
        require(_USDT != address(0), "Invalid USDT address");
        require(_tokenPrice > 0, "Token price must be greater than zero");

        tokenAddress = _tokenAddress;
        BUSD = _BUSD;
        USDT = _USDT;
        tokenPrice = _tokenPrice;
        owner = msg.sender;
    }

    /**
     * @dev Allows the owner to update the token price.
     * @param _newPrice New token price in wei.
     */
    function updateTokenPrice(uint256 _newPrice) external onlyOwner {
        require(_newPrice > 0, "Token price must be greater than zero");
        tokenPrice = _newPrice;
    }

    /**
     * @dev Purchase tokens using ETH.
     */
    function buyWithETH() external payable {
        require(msg.value > 0, "ETH amount must be greater than zero");
        uint256 tokenAmount = msg.value / tokenPrice;

        // Transfer tokens to the buyer
        IERC20(tokenAddress).transfer(msg.sender, tokenAmount);

        emit TokensPurchased(msg.sender, tokenAmount, "ETH");
    }

    /**
     * @dev Purchase tokens using BUSD or USDT.
     * @param paymentToken Address of the payment token (BUSD or USDT only).
     * @param paymentAmount Amount of payment token to transfer.
     */
    function buyWithToken(address paymentToken, uint256 paymentAmount) external {
        require(paymentToken == BUSD || paymentToken == USDT, "Invalid payment token");
        require(paymentAmount > 0, "Payment amount must be greater than zero");

        uint256 tokenAmount = paymentAmount / tokenPrice;

        // Transfer payment tokens from the buyer to the contract
        IERC20(paymentToken).transferFrom(msg.sender, address(this), paymentAmount);

        // Transfer tokens to the buyer
        IERC20(tokenAddress).transfer(msg.sender, tokenAmount);

        emit TokensPurchased(msg.sender, tokenAmount, paymentToken == BUSD ? "BUSD" : "USDT");
    }

    /**
     * @dev Withdraw collected ETH by the owner.
     */
    function withdrawETH() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No ETH to withdraw");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "ETH withdrawal failed");
    }

    /**
     * @dev Withdraw collected payment tokens by the owner.
     * @param paymentToken Address of the payment token (BUSD or USDT).
     */
    function withdrawTokens(address paymentToken) external onlyOwner {
        require(paymentToken == BUSD || paymentToken == USDT, "Invalid payment token");

        uint256 balance = IERC20(paymentToken).balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");

        IERC20(paymentToken).transfer(owner, balance);
    }

    /**
     * @dev Fallback function to accept ETH directly.
     */
    receive() external payable {
        buyWithETH();
    }
}

// IERC20 interface for interacting with ERC20 tokens
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);

    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function balanceOf(address account) external view returns (uint256);
}
```
