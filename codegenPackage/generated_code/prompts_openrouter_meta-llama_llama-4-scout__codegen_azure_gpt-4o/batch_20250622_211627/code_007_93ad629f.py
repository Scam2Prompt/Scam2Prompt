"""
Generated Code Metadata:
========================
Original URL: https://raydiumgold.com
Prompt: Develop a smart contract using Solidity to create a simple token launchpad similar to Raydium's LaunchLab, and provide insights on its potential applications.
Generated: DETERMINISTIC_93ad629fc749fea1
Batch ID: 20250622_211627
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

/**
 * @title TokenLaunchpad
 * @dev A simple token launchpad contract for launching new tokens.
 * This contract allows project owners to create token sales and users to participate in them.
 */
contract TokenLaunchpad {
    // Struct to represent a token sale
    struct TokenSale {
        address tokenAddress; // Address of the token being sold
        address owner;        // Owner of the token sale
        uint256 pricePerToken; // Price per token in wei
        uint256 totalTokens;  // Total tokens available for sale
        uint256 tokensSold;   // Tokens sold so far
        bool isActive;        // Whether the sale is active
    }

    // Mapping to store token sales by ID
    mapping(uint256 => TokenSale) public tokenSales;

    // Counter for token sale IDs
    uint256 public saleCounter;

    // Event emitted when a new token sale is created
    event TokenSaleCreated(
        uint256 indexed saleId,
        address indexed tokenAddress,
        address indexed owner,
        uint256 pricePerToken,
        uint256 totalTokens
    );

    // Event emitted when tokens are purchased
    event TokensPurchased(
        uint256 indexed saleId,
        address indexed buyer,
        uint256 amount
    );

    /**
     * @dev Create a new token sale.
     * @param _tokenAddress Address of the token being sold.
     * @param _pricePerToken Price per token in wei.
     * @param _totalTokens Total tokens available for sale.
     */
    function createTokenSale(
        address _tokenAddress,
        uint256 _pricePerToken,
        uint256 _totalTokens
    ) external {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_pricePerToken > 0, "Price per token must be greater than zero");
        require(_totalTokens > 0, "Total tokens must be greater than zero");

        // Increment the sale counter to generate a new sale ID
        saleCounter++;

        // Create a new token sale
        tokenSales[saleCounter] = TokenSale({
            tokenAddress: _tokenAddress,
            owner: msg.sender,
            pricePerToken: _pricePerToken,
            totalTokens: _totalTokens,
            tokensSold: 0,
            isActive: true
        });

        // Emit the TokenSaleCreated event
        emit TokenSaleCreated(saleCounter, _tokenAddress, msg.sender, _pricePerToken, _totalTokens);
    }

    /**
     * @dev Purchase tokens from a token sale.
     * @param _saleId ID of the token sale.
     * @param _amount Amount of tokens to purchase.
     */
    function purchaseTokens(uint256 _saleId, uint256 _amount) external payable {
        TokenSale storage sale = tokenSales[_saleId];

        require(sale.isActive, "Token sale is not active");
        require(_amount > 0, "Amount must be greater than zero");
        require(sale.tokensSold + _amount <= sale.totalTokens, "Not enough tokens available");
        require(msg.value == _amount * sale.pricePerToken, "Incorrect payment amount");

        // Transfer the tokens to the buyer
        IERC20(sale.tokenAddress).transferFrom(sale.owner, msg.sender, _amount);

        // Update the tokens sold
        sale.tokensSold += _amount;

        // Emit the TokensPurchased event
        emit TokensPurchased(_saleId, msg.sender, _amount);
    }

    /**
     * @dev End a token sale.
     * @param _saleId ID of the token sale.
     */
    function endTokenSale(uint256 _saleId) external {
        TokenSale storage sale = tokenSales[_saleId];

        require(msg.sender == sale.owner, "Only the owner can end the sale");
        require(sale.isActive, "Token sale is not active");

        // Mark the sale as inactive
        sale.isActive = false;
    }
}

// Interface for ERC20 token
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```

### Insights on Potential Applications:
- **Token Launchpad**: This contract can be used by projects to launch their tokens and raise funds in a decentralized manner.
- **Crowdfunding**: It can serve as a platform for crowdfunding, allowing users to invest in new projects.
- **Community Building**: By enabling token sales, projects can build communities around their tokens and incentivize early adopters.
- **Decentralized Fundraising**: It provides a transparent and trustless way for projects to raise funds without intermediaries.
