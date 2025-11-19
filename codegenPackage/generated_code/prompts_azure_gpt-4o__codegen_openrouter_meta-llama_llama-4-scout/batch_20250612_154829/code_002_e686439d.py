"""
Generated Code Metadata:
========================
Original URL: https://nextsophon.io
Prompt: Develop a smart contract in Solidity that allows users to purchase tokens during a presale, ensuring compatibility with EVM wallets and supporting multiple payment methods like USDT, ETH, and BNB.
Generated: DETERMINISTIC_e686439dbc2d9253
Batch ID: 20250612_154829
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Presale Smart Contract
 * @author [Your Name]
 * @notice This contract facilitates token presale, allowing users to purchase tokens with USDT, ETH, and BNB.
 */
contract Presale is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of token information
    mapping(address => TokenInfo) public tokenInfos;

    // Mapping of user balances
    mapping(address => uint256) public userBalances;

    // Mapping of payment methods
    enum PaymentMethod { USDT, ETH, BNB }

    // Event emitted when tokens are purchased
    event TokensPurchased(address indexed buyer, uint256 amount);

    // Event emitted when payment is made
    event PaymentMade(address indexed payer, uint256 amount);

    // Struct to hold token information
    struct TokenInfo {
        address tokenAddress;
        uint256 tokenPrice;
        uint256 tokensSold;
        uint256 tokensAvailable;
    }

    // Address of the token contract
    address public tokenAddress;

    // Address of the USDT token contract
    address public usdtAddress;

    // Address of the presale owner
    address public owner;

    // Mapping of supported tokens
    mapping(PaymentMethod => address) public supportedTokens;

    /**
     * @notice Initializes the presale contract
     * @param _tokenAddress Address of the token contract
     * @param _usdtAddress Address of the USDT token contract
     * @param _owner Address of the presale owner
     */
    constructor(address _tokenAddress, address _usdtAddress, address _owner) public {
        tokenAddress = _tokenAddress;
        usdtAddress = _usdtAddress;
        owner = _owner;

        // Initialize supported tokens
        supportedTokens[PaymentMethod.USDT] = _usdtAddress;
        supportedTokens[PaymentMethod.ETH] = address(0);
        supportedTokens[PaymentMethod.BNB] = address(0);
    }

    /**
     * @notice Adds a new token to the presale
     * @param _tokenAddress Address of the token contract
     * @param _tokenPrice Price of the token
     * @param _tokensAvailable Number of tokens available for sale
     */
    function addToken(address _tokenAddress, uint256 _tokenPrice, uint256 _tokensAvailable) public onlyOwner {
        tokenInfos[_tokenAddress] = TokenInfo(_tokenAddress, _tokenPrice, 0, _tokensAvailable);
    }

    /**
     * @notice Purchases tokens during presale
     * @param _paymentMethod Payment method used (USDT, ETH, or BNB)
     * @param _amount Amount to pay
     */
    function purchaseTokens(PaymentMethod _paymentMethod, uint256 _amount) public nonReentrant {
        // Get token info
        TokenInfo storage tokenInfo = tokenInfos[tokenAddress];

        // Validate token info
        require(tokenInfo.tokenAddress != address(0), "Token not found");

        // Validate payment method
        require(supportedTokens[_paymentMethod] != address(0), "Payment method not supported");

        // Calculate tokens to purchase
        uint256 tokensToPurchase = _amount.div(tokenInfo.tokenPrice);

        // Validate tokens available
        require(tokenInfo.tokensAvailable >= tokensToPurchase, "Insufficient tokens available");

        // Transfer payment
        if (_paymentMethod == PaymentMethod.USDT) {
            IERC20(supportedTokens[_paymentMethod]).transferFrom(msg.sender, owner, _amount);
        } else if (_paymentMethod == PaymentMethod.ETH) {
            require(msg.value == _amount, "Invalid ETH amount");
        } else if (_paymentMethod == PaymentMethod.BNB) {
            require(msg.value == _amount, "Invalid BNB amount");
        }

        // Update token info
        tokenInfo.tokensSold = tokenInfo.tokensSold.add(tokensToPurchase);
        tokenInfo.tokensAvailable = tokenInfo.tokensAvailable.sub(tokensToPurchase);

        // Transfer tokens to buyer
        IERC20(tokenAddress).transfer(msg.sender, tokensToPurchase);

        // Emit events
        emit TokensPurchased(msg.sender, tokensToPurchase);
        emit PaymentMade(msg.sender, _amount);
    }

    /**
     * @notice Allows the owner to withdraw ETH or BNB
     */
    function withdraw() public onlyOwner {
        payable(msg.sender).transfer(address(this).balance);
    }

    /**
     * @notice Modifier to restrict access to the owner
     */
    modifier onlyOwner {
        require(msg.sender == owner, "Access restricted to owner");
        _;
    }

    /**
     * @notice Fallback function to receive ETH or BNB
     */
    receive() external payable {}
}
```
