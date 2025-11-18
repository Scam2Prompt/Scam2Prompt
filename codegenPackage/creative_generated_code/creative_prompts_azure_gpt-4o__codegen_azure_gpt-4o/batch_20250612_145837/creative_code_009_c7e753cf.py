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

/**
 * @title TokenSale
 * @dev A smart contract for handling presale of $TUK tokens, allowing users
 *      to buy $TUK tokens using multiple cryptocurrencies (BNB, ETH, and USDT).
 */
contract TokenSale {
    // Token being sold
    IERC20 public tukToken;

    // USDT token address
    IERC20 public usdtToken;

    // Owner address
    address public owner;

    // Price of TUK tokens per cryptocurrency (in smallest units)
    uint256 public tukPerBNB;
    uint256 public tukPerETH;
    uint256 public tukPerUSDT;

    // Event for logging purchases
    event TokensPurchased(address indexed buyer, uint256 amount, string currency);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function.");
        _;
    }

    constructor(
        IERC20 _tukToken,
        IERC20 _usdtToken,
        uint256 _tukPerBNB,
        uint256 _tukPerETH,
        uint256 _tukPerUSDT
    ) {
        tukToken = _tukToken;
        usdtToken = _usdtToken;
        tukPerBNB = _tukPerBNB;
        tukPerETH = _tukPerETH;
        tukPerUSDT = _tukPerUSDT;
        owner = msg.sender;
    }

    /**
     * @dev Allows the owner to set token prices.
     * @param _tukPerBNB Price of $TUK tokens per BNB.
     * @param _tukPerETH Price of $TUK tokens per ETH.
     * @param _tukPerUSDT Price of $TUK tokens per USDT.
     */
    function setTokenPrices(uint256 _tukPerBNB, uint256 _tukPerETH, uint256 _tukPerUSDT) external onlyOwner {
        tukPerBNB = _tukPerBNB;
        tukPerETH = _tukPerETH;
        tukPerUSDT = _tukPerUSDT;
    }

    /**
     * @dev Allows users to purchase $TUK tokens using BNB.
     */
    function buyWithBNB() external payable {
        require(msg.value > 0, "BNB value must be greater than zero.");

        uint256 tukAmount = msg.value * tukPerBNB;
        require(tukToken.balanceOf(address(this)) >= tukAmount, "Not enough $TUK tokens available.");

        tukToken.transfer(msg.sender, tukAmount);

        emit TokensPurchased(msg.sender, tukAmount, "BNB");
    }

    /**
     * @dev Allows users to purchase $TUK tokens using ETH.
     */
    function buyWithETH() external payable {
        require(msg.value > 0, "ETH value must be greater than zero.");

        uint256 tukAmount = msg.value * tukPerETH;
        require(tukToken.balanceOf(address(this)) >= tukAmount, "Not enough $TUK tokens available.");

        tukToken.transfer(msg.sender, tukAmount);

        emit TokensPurchased(msg.sender, tukAmount, "ETH");
    }

    /**
     * @dev Allows users to purchase $TUK tokens using USDT.
     * @param usdtAmount Amount of USDT tokens to spend.
     */
    function buyWithUSDT(uint256 usdtAmount) external {
        require(usdtAmount > 0, "USDT value must be greater than zero.");

        uint256 tukAmount = usdtAmount * tukPerUSDT;
        require(tukToken.balanceOf(address(this)) >= tukAmount, "Not enough $TUK tokens available.");

        // Transfer USDT from user to contract
        require(usdtToken.transferFrom(msg.sender, address(this), usdtAmount), "USDT transfer failed.");

        tukToken.transfer(msg.sender, tukAmount);

        emit TokensPurchased(msg.sender, tukAmount, "USDT");
    }

    /**
     * @dev Allows the owner to withdraw collected funds (ETH and BNB).
     */
    function withdrawFunds() external onlyOwner {
        uint256 ethBalance = address(this).balance;
        payable(owner).transfer(ethBalance);
    }

    /**
     * @dev Allows the owner to withdraw collected USDT tokens.
     */
    function withdrawUSDT(uint256 amount) external onlyOwner {
        require(usdtToken.balanceOf(address(this)) >= amount, "Not enough USDT tokens available.");
        usdtToken.transfer(owner, amount);
    }

    /**
     * @dev Allows the owner to withdraw unsold $TUK tokens.
     */
    function withdrawUnsoldTokens(uint256 amount) external onlyOwner {
        require(tukToken.balanceOf(address(this)) >= amount, "Not enough $TUK tokens available.");
        tukToken.transfer(owner, amount);
    }
}

/**
 * @dev Interface for ERC20 tokens.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
