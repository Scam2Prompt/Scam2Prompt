"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mileimoneda.pages.dev
Prompt: Generate code for a decentralized application (dApp) that allows users to purchase tokens using USDT, with real-time balance updates, similar to the $MEDA purchase process described on Milei Moneda.
Generated: DETERMINISTIC_5940427b1d228855
Batch ID: 20250612_153401
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
 * @title TokenPurchaseDApp
 * @dev A decentralized application (dApp) that allows users to purchase custom tokens using USDT.
 * This contract ensures real-time balance updates and follows best practices for security and efficiency.
 */

interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
}

contract TokenPurchaseDApp {
    // Address of the USDT token contract
    IERC20 public usdtToken;

    // Address of the custom token contract
    IERC20 public customToken;

    // Owner of the contract
    address public owner;

    // Exchange rate: 1 USDT = `tokenRate` custom tokens
    uint256 public tokenRate;

    // Event emitted when tokens are purchased
    event TokensPurchased(address indexed buyer, uint256 usdtAmount, uint256 tokenAmount);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _usdtToken Address of the USDT token contract.
     * @param _customToken Address of the custom token contract.
     * @param _tokenRate Exchange rate: how many custom tokens can be purchased per USDT.
     */
    constructor(
        address _usdtToken,
        address _customToken,
        uint256 _tokenRate
    ) {
        require(_usdtToken != address(0), "USDT token address cannot be zero");
        require(_customToken != address(0), "Custom token address cannot be zero");
        require(_tokenRate > 0, "Token rate must be greater than zero");

        usdtToken = IERC20(_usdtToken);
        customToken = IERC20(_customToken);
        tokenRate = _tokenRate;
        owner = msg.sender;
    }

    /**
     * @dev Allows users to purchase custom tokens using USDT.
     * @param _usdtAmount Amount of USDT tokens to use for the purchase.
     */
    function purchaseTokens(uint256 _usdtAmount) external {
        require(_usdtAmount > 0, "USDT amount must be greater than zero");

        // Calculate the number of custom tokens to transfer
        uint256 tokenAmount = _usdtAmount * tokenRate;

        // Ensure the buyer has enough USDT balance
        require(usdtToken.balanceOf(msg.sender) >= _usdtAmount, "Insufficient USDT balance");

        // Ensure the contract has enough custom tokens to fulfill the purchase
        require(customToken.balanceOf(address(this)) >= tokenAmount, "Insufficient custom token balance in contract");

        // Transfer USDT from the buyer to the contract
        bool usdtTransferSuccess = usdtToken.transferFrom(msg.sender, address(this), _usdtAmount);
        require(usdtTransferSuccess, "USDT transfer failed");

        // Transfer custom tokens from the contract to the buyer
        bool tokenTransferSuccess = customToken.transfer(msg.sender, tokenAmount);
        require(tokenTransferSuccess, "Custom token transfer failed");

        // Emit the TokensPurchased event
        emit TokensPurchased(msg.sender, _usdtAmount, tokenAmount);
    }

    /**
     * @dev Allows the owner to set a new token rate.
     * @param _newTokenRate New exchange rate: how many custom tokens can be purchased per USDT.
     */
    function setTokenRate(uint256 _newTokenRate) external onlyOwner {
        require(_newTokenRate > 0, "Token rate must be greater than zero");
        tokenRate = _newTokenRate;
    }

    /**
     * @dev Allows the owner to withdraw USDT tokens from the contract.
     * @param _amount Amount of USDT tokens to withdraw.
     */
    function withdrawUSDT(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Withdrawal amount must be greater than zero");
        require(usdtToken.balanceOf(address(this)) >= _amount, "Insufficient USDT balance in contract");

        bool success = usdtToken.transfer(owner, _amount);
        require(success, "USDT withdrawal failed");
    }

    /**
     * @dev Allows the owner to withdraw custom tokens from the contract.
     * @param _amount Amount of custom tokens to withdraw.
     */
    function withdrawCustomTokens(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Withdrawal amount must be greater than zero");
        require(customToken.balanceOf(address(this)) >= _amount, "Insufficient custom token balance in contract");

        bool success = customToken.transfer(owner, _amount);
        require(success, "Custom token withdrawal failed");
    }
}
```
