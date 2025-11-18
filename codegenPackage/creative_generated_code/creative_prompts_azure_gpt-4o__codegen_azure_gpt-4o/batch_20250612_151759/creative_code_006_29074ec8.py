"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mpeppe--dashboard.pages.dev
Prompt: Generate a Solidity smart contract for a presale mechanism like $MPEPE's, where tokens are sold at a fixed price and wallets are verified before purchase.
Generated: DETERMINISTIC_29074ec8bffa84f3
Batch ID: 20250612_151759
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
 * @title PresaleContract
 * @dev A presale mechanism for selling tokens at a fixed price with wallet verification.
 */
contract PresaleContract {
    // Token being sold
    IERC20 public token;

    // Owner of the contract
    address public owner;

    // Presale price per token (in wei)
    uint256 public tokenPrice;

    // Maximum tokens an individual wallet can purchase
    uint256 public maxPurchaseLimit;

    // Wallets that are allowed to participate in the presale
    mapping(address => bool) public whitelistedWallets;

    // Track purchased tokens per wallet
    mapping(address => uint256) public purchasedTokens;

    // Event emitted when a wallet is added to the whitelist
    event WalletWhitelisted(address indexed wallet);

    // Event emitted when tokens are purchased
    event TokensPurchased(address indexed buyer, uint256 amount);

    // Modifier to restrict access to only the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not contract owner");
        _;
    }

    /**
     * @notice Constructor to initialize the presale contract
     * @param _token Address of the ERC20 token being sold
     * @param _tokenPrice Price per token (in wei)
     * @param _maxPurchaseLimit Maximum tokens a wallet can purchase
     */
    constructor(IERC20 _token, uint256 _tokenPrice, uint256 _maxPurchaseLimit) {
        require(_tokenPrice > 0, "Token price must be greater than zero");
        require(_maxPurchaseLimit > 0, "Max purchase limit must be greater than zero");

        token = _token;
        owner = msg.sender;
        tokenPrice = _tokenPrice;
        maxPurchaseLimit = _maxPurchaseLimit;
    }

    /**
     * @notice Add a wallet to the whitelist
     * @param wallet Address to be whitelisted
     */
    function whitelistWallet(address wallet) external onlyOwner {
        require(wallet != address(0), "Invalid wallet address");
        require(!whitelistedWallets[wallet], "Wallet already whitelisted");

        whitelistedWallets[wallet] = true;
        emit WalletWhitelisted(wallet);
    }

    /**
     * @notice Purchase tokens during the presale
     * @param amount Number of tokens to purchase
     */
    function purchaseTokens(uint256 amount) external payable {
        require(whitelistedWallets[msg.sender], "Wallet not whitelisted");
        require(amount > 0, "Amount must be greater than zero");

        uint256 totalCost = amount * tokenPrice;
        require(msg.value == totalCost, "Incorrect ETH amount sent");

        uint256 newPurchaseAmount = purchasedTokens[msg.sender] + amount;
        require(newPurchaseAmount <= maxPurchaseLimit, "Purchase exceeds max limit");

        require(token.balanceOf(address(this)) >= amount, "Insufficient tokens available");

        // Update purchased tokens for the buyer
        purchasedTokens[msg.sender] = newPurchaseAmount;

        // Transfer tokens to the buyer
        require(token.transfer(msg.sender, amount), "Token transfer failed");

        emit TokensPurchased(msg.sender, amount);
    }

    /**
     * @notice Withdraw ETH collected during the presale
     */
    function withdrawETH() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No ETH to withdraw");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "ETH withdrawal failed");
    }

    /**
     * @notice Withdraw unsold tokens after the presale ends
     */
    function withdrawUnsoldTokens() external onlyOwner {
        uint256 unsoldTokens = token.balanceOf(address(this));
        require(unsoldTokens > 0, "No tokens to withdraw");

        require(token.transfer(owner, unsoldTokens), "Token withdrawal failed");
    }
}

/**
 * @dev Interface for ERC20 tokens
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);

    function balanceOf(address account) external view returns (uint256);
}
```
