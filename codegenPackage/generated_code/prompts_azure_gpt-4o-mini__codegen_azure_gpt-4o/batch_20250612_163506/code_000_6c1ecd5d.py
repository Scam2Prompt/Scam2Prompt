"""
Generated Code Metadata:
========================
Original URL: https://launchpool.live
Prompt: How can I implement a smart contract for an Initial DEX Offering (IDO) similar to those on Launchpool.live?
Generated: DETERMINISTIC_6c1ecd5d898f3584
Batch ID: 20250612_163506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here is a clean, well-documented, and production-ready smart contract for an Initial DEX Offering (IDO) written in Solidity. This contract is a simplified version and should be audited before deployment.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title IDO Smart Contract
 * @dev This contract facilitates an Initial DEX Offering (IDO) for token sales.
 */
contract IDO {
    // Address of the token being sold
    address public tokenAddress;

    // Address of the owner (project team)
    address public owner;

    // Price of the token in wei (1 token = X wei)
    uint256 public tokenPrice;

    // Maximum number of tokens that can be purchased per wallet
    uint256 public maxTokensPerWallet;

    // Total tokens available for sale
    uint256 public totalTokensForSale;

    // Mapping to track purchased tokens per wallet
    mapping(address => uint256) public tokensPurchased;

    // Event emitted when tokens are purchased
    event TokensPurchased(address indexed buyer, uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    /**
     * @dev Constructor to initialize the IDO contract.
     * @param _tokenAddress Address of the token being sold.
     * @param _tokenPrice Price of the token in wei.
     * @param _maxTokensPerWallet Maximum tokens a wallet can purchase.
     * @param _totalTokensForSale Total tokens available for sale.
     */
    constructor(
        address _tokenAddress,
        uint256 _tokenPrice,
        uint256 _maxTokensPerWallet,
        uint256 _totalTokensForSale
    ) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_tokenPrice > 0, "Token price must be greater than zero");
        require(_maxTokensPerWallet > 0, "Max tokens per wallet must be greater than zero");
        require(_totalTokensForSale > 0, "Total tokens for sale must be greater than zero");

        tokenAddress = _tokenAddress;
        tokenPrice = _tokenPrice;
        maxTokensPerWallet = _maxTokensPerWallet;
        totalTokensForSale = _totalTokensForSale;
        owner = msg.sender;
    }

    /**
     * @dev Function to purchase tokens during the IDO.
     * @param _amount Number of tokens to purchase.
     */
    function purchaseTokens(uint256 _amount) external payable {
        require(_amount > 0, "Amount must be greater than zero");
        require(tokensPurchased[msg.sender] + _amount <= maxTokensPerWallet, "Exceeds max tokens per wallet");
        require(_amount <= totalTokensForSale, "Not enough tokens available for sale");
        require(msg.value == _amount * tokenPrice, "Incorrect ETH amount sent");

        // Transfer tokens to the buyer
        require(
            IERC20(tokenAddress).transfer(msg.sender, _amount),
            "Token transfer failed"
        );

        // Update state
        tokensPurchased[msg.sender] += _amount;
        totalTokensForSale -= _amount;

        emit TokensPurchased(msg.sender, _amount);
    }

    /**
     * @dev Function to withdraw funds collected during the IDO.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Function to withdraw unsold tokens after the IDO ends.
     */
    function withdrawUnsoldTokens() external onlyOwner {
        uint256 unsoldTokens = totalTokensForSale;
        require(unsoldTokens > 0, "No unsold tokens to withdraw");

        require(
            IERC20(tokenAddress).transfer(owner, unsoldTokens),
            "Token transfer failed"
        );

        totalTokensForSale = 0;
    }
}

/**
 * @dev Interface for ERC20 token standard.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```

### Notes:
- This contract assumes the token being sold is an ERC20-compliant token.
- Proper testing and auditing are required before deploying this contract to a production environment.
- Ensure the token contract has sufficient tokens allocated to this contract before starting the IDO.
