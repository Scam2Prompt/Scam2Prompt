"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartdappnodes-net.pages.dev
Prompt: Develop a smart contract for pre-sale token distribution, incorporating features like whitelisting, as described on the Smart Dapps Chain website.
Generated: DETERMINISTIC_0b62db500e41b55e
Batch ID: 20250612_152321
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
 * @title PreSaleTokenDistribution
 * @dev A smart contract for managing pre-sale token distribution with whitelisting functionality.
 */
contract PreSaleTokenDistribution {
    // Token being sold
    IERC20 public token;

    // Owner of the contract
    address public owner;

    // Token price in wei (amount of ETH per token)
    uint256 public tokenPrice;

    // Max tokens a whitelisted user can purchase in pre-sale
    uint256 public maxTokensPerUser;

    // Mapping to track whitelisted addresses
    mapping(address => bool) public whitelist;

    // Mapping to track purchased tokens by user
    mapping(address => uint256) public purchasedTokens;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event Whitelisted(address indexed user);
    event RemovedFromWhitelist(address indexed user);

    // Modifier to restrict access to owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can call this function");
        _;
    }

    // Modifier to check if user is whitelisted
    modifier onlyWhitelisted() {
        require(whitelist[msg.sender], "You are not whitelisted for the pre-sale");
        _;
    }

    // Constructor
    constructor(
        address _token,
        uint256 _tokenPrice,
        uint256 _maxTokensPerUser
    ) {
        require(_token != address(0), "Invalid token address");
        require(_tokenPrice > 0, "Token price must be greater than zero");
        require(_maxTokensPerUser > 0, "Max tokens per user must be greater than zero");

        token = IERC20(_token);
        owner = msg.sender;
        tokenPrice = _tokenPrice;
        maxTokensPerUser = _maxTokensPerUser;
    }

    /**
     * @dev Add a user to the whitelist.
     * @param _user Address of the user to whitelist.
     */
    function whitelistUser(address _user) external onlyOwner {
        require(_user != address(0), "Invalid address");
        whitelist[_user] = true;
        emit Whitelisted(_user);
    }

    /**
     * @dev Remove a user from the whitelist.
     * @param _user Address of the user to remove.
     */
    function removeFromWhitelist(address _user) external onlyOwner {
        require(whitelist[_user], "User is not whitelisted");
        whitelist[_user] = false;
        emit RemovedFromWhitelist(_user);
    }

    /**
     * @dev Purchase tokens during the pre-sale.
     * @param _amount Number of tokens to purchase.
     */
    function purchaseTokens(uint256 _amount) external payable onlyWhitelisted {
        require(_amount > 0, "Token amount must be greater than zero");
        require(msg.value == _amount * tokenPrice, "Incorrect ETH amount sent");
        require(purchasedTokens[msg.sender] + _amount <= maxTokensPerUser, "Exceeds max tokens per user");

        // Transfer tokens to the buyer
        require(token.transfer(msg.sender, _amount), "Token transfer failed");
        
        // Update purchased tokens
        purchasedTokens[msg.sender] += _amount;

        emit TokensPurchased(msg.sender, _amount);
    }

    /**
     * @dev Withdraw ETH collected during pre-sale.
     */
    function withdrawETH() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No ETH to withdraw");
        (bool success, ) = owner.call{value: balance}("");
        require(success, "ETH withdrawal failed");
    }

    /**
     * @dev Withdraw remaining tokens from the contract.
     */
    function withdrawTokens() external onlyOwner {
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        require(token.transfer(owner, balance), "Token withdrawal failed");
    }
}

/**
 * @dev Interface for ERC20 token standard.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);

    function balanceOf(address account) external view returns (uint256);
}
```
