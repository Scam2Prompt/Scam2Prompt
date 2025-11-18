"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pablo-defi.pages.dev
Prompt: Create a smart contract for a token presale on Uniswap, incorporating the tax rules (0%-10%) and token allocation details specified in the Pablo Cartel ecosystem.
Generated: DETERMINISTIC_f9d1960b806c2618
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
 * @title TokenPresale
 * @author Pablo Cartel Ecosystem
 * @notice Smart contract for managing a token presale with tax rules (0%-10%) and token allocation details.
 */
contract TokenPresale {
    // State variables
    address public owner; // Owner of the contract
    address public tokenAddress; // Address of the token being sold
    uint256 public presaleStartTime; // Presale start time
    uint256 public presaleEndTime; // Presale end time
    uint256 public tokenRate; // Token rate (tokens per 1 ETH)
    uint256 public taxRate; // Tax rate (0% - 10%)
    uint256 public totalTokensSold; // Total tokens sold during presale
    uint256 public maxTokensForSale; // Maximum tokens allocated for the presale

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 tax);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier presaleActive() {
        require(
            block.timestamp >= presaleStartTime && block.timestamp <= presaleEndTime,
            "Presale is not active"
        );
        _;
    }

    modifier validTaxRate(uint256 rate) {
        require(rate >= 0 && rate <= 10, "Invalid tax rate");
        _;
    }

    constructor(
        address _tokenAddress,
        uint256 _presaleStartTime,
        uint256 _presaleEndTime,
        uint256 _tokenRate,
        uint256 _taxRate,
        uint256 _maxTokensForSale
    ) validTaxRate(_taxRate) {
        require(_presaleEndTime > _presaleStartTime, "End time must be after start time");
        require(_tokenAddress != address(0), "Invalid token address");

        owner = msg.sender;
        tokenAddress = _tokenAddress;
        presaleStartTime = _presaleStartTime;
        presaleEndTime = _presaleEndTime;
        tokenRate = _tokenRate;
        taxRate = _taxRate;
        maxTokensForSale = _maxTokensForSale;
    }

    /**
     * @notice Purchase tokens during the presale.
     * @dev Applies the tax rules and checks token availability.
     */
    function buyTokens() external payable presaleActive {
        require(msg.value > 0, "ETH amount must be greater than zero");

        // Calculate token amount and tax
        uint256 tokensToBuy = msg.value * tokenRate;
        uint256 taxAmount = (tokensToBuy * taxRate) / 100;
        uint256 tokensAfterTax = tokensToBuy - taxAmount;

        require(totalTokensSold + tokensAfterTax <= maxTokensForSale, "Exceeds presale allocation");

        // Transfer tokens to buyer
        require(
            IERC20(tokenAddress).transfer(msg.sender, tokensAfterTax),
            "Token transfer failed"
        );

        // Update total tokens sold
        totalTokensSold += tokensAfterTax;

        // Emit event
        emit TokensPurchased(msg.sender, tokensAfterTax, taxAmount);
    }

    /**
     * @notice Update the tax rate.
     * @dev Can only be called by the owner and must be within the valid range.
     * @param _newTaxRate New tax rate (0%-10%).
     */
    function updateTaxRate(uint256 _newTaxRate) external onlyOwner validTaxRate(_newTaxRate) {
        taxRate = _newTaxRate;
    }

    /**
     * @notice Withdraw collected ETH from the presale.
     * @dev Can only be called by the owner.
     */
    function withdrawETH() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No ETH to withdraw");
        payable(owner).transfer(balance);
    }

    /**
     * @notice Transfer ownership of the contract.
     * @dev Can only be called by the current owner.
     * @param _newOwner Address of the new owner.
     */
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "New owner is the zero address");
        emit OwnershipTransferred(owner, _newOwner);
        owner = _newOwner;
    }

    /**
     * @notice Emergency function to recover tokens sent to the contract.
     * @dev Can only be called by the owner.
     * @param _token Address of the token to recover.
     * @param _recipient Address to send the recovered tokens to.
     * @param _amount Amount of tokens to recover.
     */
    function recoverTokens(
        address _token,
        address _recipient,
        uint256 _amount
    ) external onlyOwner {
        require(IERC20(_token).transfer(_recipient, _amount), "Token recovery failed");
    }
}

// Minimal ERC20 Interface for token transfers
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
