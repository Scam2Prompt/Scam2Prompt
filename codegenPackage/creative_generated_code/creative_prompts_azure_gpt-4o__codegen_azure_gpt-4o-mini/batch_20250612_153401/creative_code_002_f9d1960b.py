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

// Importing the necessary ERC20 and Ownable contracts
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for Uniswap V2 Router for token swapping
interface IUniswapV2Router {
    function swapExactTokensForTokens(
        uint amountIn,
        uint amountOutMin,
        address[] calldata path,
        address to,
        uint deadline
    ) external returns (uint[] memory amounts);
}

contract TokenPresale is Ownable {
    // State variables
    IERC20 public token; // The token being sold
    IUniswapV2Router public uniswapRouter; // Uniswap router for trading
    uint public presaleStart; // Presale start time
    uint public presaleEnd; // Presale end time
    uint public totalTokensSold; // Total tokens sold in the presale
    uint public constant MAX_TAX = 10; // Max tax percentage
    uint public taxRate; // Dynamic tax rate (0% - 10%)
    
    // Mapping from user address to amount of tokens purchased
    mapping(address => uint) public tokenBalance;

    // Events
    event TokensPurchased(address indexed buyer, uint amount);
    event TaxRateUpdated(uint newTaxRate);

    // Constructor to initialize the contract
    constructor(
        address _token,
        address _uniswapRouter,
        uint _presaleStart,
        uint _presaleEnd,
        uint _taxRate
    ) {
        require(_token != address(0), "Token address cannot be zero.");
        require(_uniswapRouter != address(0), "Uniswap router address cannot be zero.");
        require(_presaleStart < _presaleEnd, "Presale start must be before end.");
        require(_taxRate <= MAX_TAX, "Tax rate must be 0%-10%.");

        token = IERC20(_token);
        uniswapRouter = IUniswapV2Router(_uniswapRouter);
        presaleStart = _presaleStart;
        presaleEnd = _presaleEnd;
        taxRate = _taxRate;
    }

    // Modifier to check if the presale is active
    modifier onlyDuringPresale() {
        require(block.timestamp >= presaleStart && block.timestamp <= presaleEnd, "Presale is not active.");
        _;
    }

    // Function to buy tokens during the presale
    function purchaseTokens(uint amount) external onlyDuringPresale {
        require(amount > 0, "Amount must be greater than zero.");

        // Calculate the tax
        uint taxAmount = (amount * taxRate) / 100;
        uint amountAfterTax = amount - taxAmount;

        // Update state variables
        totalTokensSold += amountAfterTax;
        tokenBalance[msg.sender] += amountAfterTax;

        // Transfer tokens to the buyer
        bool sent = token.transferFrom(msg.sender, address(this), amount);
        require(sent, "Token transfer failed.");

        emit TokensPurchased(msg.sender, amountAfterTax);
    }

    // Function to update the tax rate (only owner can update)
    function updateTaxRate(uint newTaxRate) external onlyOwner {
        require(newTaxRate <= MAX_TAX, "Tax rate must be 0%-10%.");
        taxRate = newTaxRate;
        emit TaxRateUpdated(newTaxRate);
    }

    // Function to withdraw unsold tokens after the presale
    function withdrawUnsoldTokens() external onlyOwner {
        require(block.timestamp > presaleEnd, "Presale is still active.");
        uint balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw.");
        
        // Transfer unsold tokens to the owner
        bool sent = token.transfer(owner(), balance);
        require(sent, "Withdrawal of tokens failed.");
    }

    // Function to withdraw Ether (if any) from the contract
    function withdrawEther() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Fallback function to accept Ether
    receive() external payable {}
}
```
