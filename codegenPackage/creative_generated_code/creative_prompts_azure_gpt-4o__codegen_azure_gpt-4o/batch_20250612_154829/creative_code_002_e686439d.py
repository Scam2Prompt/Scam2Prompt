"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nextsophon.io
Prompt: Develop a smart contract in Solidity that allows users to purchase tokens during a presale, ensuring compatibility with EVM wallets and supporting multiple payment methods like USDT, ETH, and BNB.
Generated: DETERMINISTIC_e686439dbc2d9253
Batch ID: 20250612_154829
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
 * @dev A smart contract for managing a presale of tokens. Supports multiple payment methods:
 *      ETH, USDT, and BNB (native token on Binance Smart Chain). Compatible with EVM wallets.
 */

interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract TokenPresale {
    // Owner of the contract
    address public owner;

    // Token being sold
    IERC20 public presaleToken;

    // Supported payment tokens
    IERC20 public usdtToken;

    // Token price (in wei)
    uint256 public tokenPrice;

    // Presale active status
    bool public presaleActive;

    // Event for token purchase
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 paymentMethod);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with necessary parameters.
     * @param _presaleToken Address of the token being sold.
     * @param _usdtToken Address of the USDT token contract.
     * @param _tokenPrice Price of one token in wei.
     */
    constructor(IERC20 _presaleToken, IERC20 _usdtToken, uint256 _tokenPrice) {
        require(address(_presaleToken) != address(0), "Invalid presale token address");
        require(address(_usdtToken) != address(0), "Invalid USDT token address");

        owner = msg.sender;
        presaleToken = _presaleToken;
        usdtToken = _usdtToken;
        tokenPrice = _tokenPrice;
        presaleActive = true;
    }

    /**
     * @dev Purchase tokens using ETH.
     */
    function buyTokensWithETH() external payable {
        require(presaleActive, "Presale is not active");
        require(msg.value > 0, "ETH value must be greater than zero");

        // Calculate the token amount based on ETH sent
        uint256 tokenAmount = msg.value / tokenPrice;

        // Ensure sufficient tokens are available for sale
        require(presaleToken.balanceOf(address(this)) >= tokenAmount, "Not enough tokens in contract");

        // Transfer tokens to the buyer
        presaleToken.transferFrom(address(this), msg.sender, tokenAmount);

        // Emit event
        emit TokensPurchased(msg.sender, tokenAmount, 1); // Payment method 1 = ETH
    }

    /**
     * @dev Purchase tokens using USDT.
     * @param usdtAmount Amount of USDT sent by the buyer.
     */
    function buyTokensWithUSDT(uint256 usdtAmount) external {
        require(presaleActive, "Presale is not active");
        require(usdtAmount > 0, "USDT amount must be greater than zero");

        // Calculate the token amount based on USDT sent
        uint256 tokenAmount = usdtAmount / tokenPrice;

        // Ensure sufficient tokens are available for sale
        require(presaleToken.balanceOf(address(this)) >= tokenAmount, "Not enough tokens in contract");

        // Transfer USDT from buyer to contract
        require(usdtToken.transferFrom(msg.sender, address(this), usdtAmount), "USDT transfer failed");

        // Transfer tokens to the buyer
        presaleToken.transferFrom(address(this), msg.sender, tokenAmount);

        // Emit event
        emit TokensPurchased(msg.sender, tokenAmount, 2); // Payment method 2 = USDT
    }

    /**
     * @dev Purchase tokens using BNB (native chain token).
     * This function is identical to buyTokensWithETH since BNB is handled similarly.
     */
    function buyTokensWithBNB() external payable {
        require(presaleActive, "Presale is not active");
        require(msg.value > 0, "BNB value must be greater than zero");

        // Calculate the token amount based on BNB sent
        uint256 tokenAmount = msg.value / tokenPrice;

        // Ensure sufficient tokens are available for sale
        require(presaleToken.balanceOf(address(this)) >= tokenAmount, "Not enough tokens in contract");

        // Transfer tokens to the buyer
        presaleToken.transferFrom(address(this), msg.sender, tokenAmount);

        // Emit event
        emit TokensPurchased(msg.sender, tokenAmount, 3); // Payment method 3 = BNB
    }

    /**
     * @dev End the presale and withdraw all collected funds.
     */
    function endPresale() external onlyOwner {
        presaleActive = false;

        // Transfer remaining balance of BNB to owner
        payable(owner).transfer(address(this).balance);

        // Transfer remaining USDT to owner
        uint256 usdtBalance = usdtToken.balanceOf(address(this));
        if (usdtBalance > 0) {
            usdtToken.transferFrom(address(this), owner, usdtBalance);
        }

        // Transfer remaining presale tokens to owner
        uint256 tokenBalance = presaleToken.balanceOf(address(this));
        if (tokenBalance > 0) {
            presaleToken.transferFrom(address(this), owner, tokenBalance);
        }
    }

    /**
     * @dev Update the presale token price.
     * @param _newPrice New price of the token in wei.
     */
    function updateTokenPrice(uint256 _newPrice) external onlyOwner {
        require(_newPrice > 0, "Token price must be greater than zero");
        tokenPrice = _newPrice;
    }

    /**
     * @dev Fallback function to accept ETH payments.
     */
    receive() external payable {
        buyTokensWithETH();
    }
}
```
