"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://launchpad.seedify.de
Prompt: Provide a code example for deploying a decentralized application (dApp) on Ethereum that mimics the functionality of a launchpad like Seedify.
Generated: DETERMINISTIC_f752e895ffa94fed
Batch ID: 20250612_151858
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
 * @title Launchpad Contract
 * @dev This contract facilitates the functionality of a token launchpad
 *      where users can participate in token sales.
 */
contract Launchpad {
    // Struct to represent a token sale
    struct TokenSale {
        address tokenAddress;        // Address of the ERC20 token
        uint256 tokenPrice;          // Price per token in wei
        uint256 saleStartTime;       // Sale start time (timestamp)
        uint256 saleEndTime;         // Sale end time (timestamp)
        uint256 tokensForSale;       // Total tokens available for sale
        uint256 tokensSold;          // Tokens already sold
        address owner;               // Owner of the token sale
    }

    // Mapping to store token sales
    mapping(uint256 => TokenSale) public tokenSales;

    // Counter to track the number of sales
    uint256 public saleCounter;

    // Events
    event TokenSaleCreated(
        uint256 indexed saleId,
        address indexed tokenAddress,
        uint256 tokenPrice,
        uint256 saleStartTime,
        uint256 saleEndTime,
        uint256 tokensForSale,
        address indexed owner
    );

    event TokensPurchased(
        uint256 indexed saleId,
        address indexed buyer,
        uint256 amount
    );

    /**
     * @dev Create a new token sale.
     * @param _tokenAddress Address of the ERC20 token to sell.
     * @param _tokenPrice Price per token in wei.
     * @param _saleStartTime Sale start time (timestamp).
     * @param _saleEndTime Sale end time (timestamp).
     * @param _tokensForSale Total amount of tokens available for sale.
     */
    function createTokenSale(
        address _tokenAddress,
        uint256 _tokenPrice,
        uint256 _saleStartTime,
        uint256 _saleEndTime,
        uint256 _tokensForSale
    ) external {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_tokenPrice > 0, "Token price must be greater than zero");
        require(
            _saleStartTime < _saleEndTime,
            "Sale start time must be before end time"
        );
        require(_tokensForSale > 0, "Tokens for sale must be greater than zero");

        // Increment the sale counter to generate a unique sale ID
        saleCounter++;

        // Create the sale
        tokenSales[saleCounter] = TokenSale({
            tokenAddress: _tokenAddress,
            tokenPrice: _tokenPrice,
            saleStartTime: _saleStartTime,
            saleEndTime: _saleEndTime,
            tokensForSale: _tokensForSale,
            tokensSold: 0,
            owner: msg.sender
        });

        emit TokenSaleCreated(
            saleCounter,
            _tokenAddress,
            _tokenPrice,
            _saleStartTime,
            _saleEndTime,
            _tokensForSale,
            msg.sender
        );
    }

    /**
     * @dev Purchase tokens from an active sale.
     * @param _saleId ID of the token sale to purchase from.
     * @param _amount Number of tokens to purchase.
     */
    function purchaseTokens(uint256 _saleId, uint256 _amount) external payable {
        TokenSale storage sale = tokenSales[_saleId];

        require(sale.tokenAddress != address(0), "Sale does not exist");
        require(
            block.timestamp >= sale.saleStartTime &&
                block.timestamp <= sale.saleEndTime,
            "Sale is not active"
        );
        require(_amount > 0, "Must purchase at least one token");
        require(
            sale.tokensSold + _amount <= sale.tokensForSale,
            "Not enough tokens available"
        );
        require(
            msg.value == _amount * sale.tokenPrice,
            "Incorrect ETH amount sent"
        );

        // Transfer tokens from owner to buyer using ERC20's transferFrom
        IERC20 token = IERC20(sale.tokenAddress);
        require(
            token.transferFrom(sale.owner, msg.sender, _amount),
            "Token transfer failed"
        );

        // Update sale state
        sale.tokensSold += _amount;

        emit TokensPurchased(_saleId, msg.sender, _amount);
    }

    /**
     * @dev Withdraw funds from the contract after sale ends.
     * @param _saleId ID of the token sale to withdraw funds from.
     */
    function withdrawFunds(uint256 _saleId) external {
        TokenSale storage sale = tokenSales[_saleId];

        require(sale.tokenAddress != address(0), "Sale does not exist");
        require(block.timestamp > sale.saleEndTime, "Sale has not ended yet");
        require(sale.owner == msg.sender, "Only owner can withdraw funds");

        uint256 balance = address(this).balance;

        (bool success, ) = sale.owner.call{value: balance}("");
        require(success, "Withdrawal failed");
    }
}

// Interface for ERC20 tokens
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);
}
```
