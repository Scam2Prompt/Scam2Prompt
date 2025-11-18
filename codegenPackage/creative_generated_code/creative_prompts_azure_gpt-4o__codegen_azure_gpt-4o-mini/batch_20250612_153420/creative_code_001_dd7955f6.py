"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airdrop-inqubeta.pages.dev
Prompt: Generate Solidity code for a smart contract that implements the QUBE tokenomics, including buy and sell taxes, rewards pool allocation, and token burning mechanisms as described on the InQubeta platform.
Generated: DETERMINISTIC_dd7955f61ddc3f6e
Batch ID: 20250612_153420
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

// Importing OpenZeppelin's ERC20 and Ownable contracts
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract QUBE is ERC20, Ownable {
    // Events for logging
    event Buy(address indexed buyer, uint256 amount);
    event Sell(address indexed seller, uint256 amount);
    event TokensBurned(address indexed burner, uint256 amount);

    // Tax rates for buying and selling
    uint256 public buyTaxRate; // e.g., 5 for 5%
    uint256 public sellTaxRate; // e.g., 10 for 10%
    
    // Address for rewards pool
    address public rewardsPool;
    
    // Total supply of the token
    uint256 public constant INITIAL_SUPPLY = 1_000_000 * 10**18; // 1 million tokens

    // Mapping to track balances after tax deductions
    mapping(address => uint256) public balances;

    // Constructor to initialize the token with name and symbol
    constructor(string memory name, string memory symbol, address _rewardsPool, uint256 _buyTaxRate, uint256 _sellTaxRate) 
        ERC20(name, symbol) 
    {
        require(_rewardsPool != address(0), "Rewards pool cannot be zero address");
        require(_buyTaxRate <= 100 && _sellTaxRate <= 100, "Tax rates must be between 0 and 100");

        rewardsPool = _rewardsPool;
        buyTaxRate = _buyTaxRate;
        sellTaxRate = _sellTaxRate;

        // Mint the initial supply to the contract owner
        _mint(msg.sender, INITIAL_SUPPLY);
    }

    // Function to buy tokens with tax applied
    function buyTokens(uint256 amount) external payable {
        // Ensure that the sent value matches the required price
        require(msg.value == amount, "Incorrect Ether value sent");
        
        uint256 taxAmount = (amount * buyTaxRate) / 100;
        uint256 amountAfterTax = amount - taxAmount;

        // Transfer tokens to buyer after tax deduction
        _transfer(owner(), msg.sender, amountAfterTax);
        // Transfer tax amount to rewards pool
        _transfer(owner(), rewardsPool, taxAmount);

        emit Buy(msg.sender, amountAfterTax);
    }

    // Function to sell tokens with tax applied
    function sellTokens(uint256 amount) external {
        require(balanceOf(msg.sender) >= amount, "Insufficient token balance");

        uint256 taxAmount = (amount * sellTaxRate) / 100;
        uint256 amountAfterTax = amount - taxAmount;

        // Transfer tokens from seller to contract
        _transfer(msg.sender, address(this), amount);
        // Transfer the amount after tax back to the seller
        payable(msg.sender).transfer(amountAfterTax);
        // Transfer tax amount to rewards pool
        _transfer(msg.sender, rewardsPool, taxAmount);

        emit Sell(msg.sender, amountAfterTax);
    }

    // Function to burn tokens, reducing total supply
    function burn(uint256 amount) external {
        require(balanceOf(msg.sender) >= amount, "Insufficient token balance to burn");
        _burn(msg.sender, amount);
        emit TokensBurned(msg.sender, amount);
    }
    
    // Function to update buy tax rate
    function updateBuyTaxRate(uint256 newRate) external onlyOwner {
        require(newRate <= 100, "Tax rate must be between 0 and 100");
        buyTaxRate = newRate;
    }

    // Function to update sell tax rate
    function updateSellTaxRate(uint256 newRate) external onlyOwner {
        require(newRate <= 100, "Tax rate must be between 0 and 100");
        sellTaxRate = newRate;
    }

    // Fallback function to prevent accidental ETH transfers
    receive() external payable {
        revert("Direct Ether transfers are not allowed");
    }
}
```
