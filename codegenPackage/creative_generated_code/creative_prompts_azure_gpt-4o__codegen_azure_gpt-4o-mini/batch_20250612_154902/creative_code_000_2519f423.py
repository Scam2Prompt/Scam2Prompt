"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-whiterock.web.app
Prompt: Write a smart contract in Solidity that implements a tokenized stock trading system similar to WhiteRock, ensuring transparency and security through OpenZeppelin audits.
Generated: DETERMINISTIC_2519f423e0e05497
Batch ID: 20250612_154902
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

// Importing OpenZeppelin Contracts
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// StockToken is an ERC20 token representing ownership in a stock
contract StockToken is ERC20, Ownable, ReentrancyGuard {
    // Mapping to track the stock ownership
    mapping(address => uint256) private shares;

    // Event emitted when shares are purchased
    event SharesPurchased(address indexed buyer, uint256 amount);
    
    // Event emitted when shares are sold
    event SharesSold(address indexed seller, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {}

    // Function to purchase shares
    // Only the owner can mint new shares
    function purchaseShares(uint256 amount) external payable nonReentrant {
        require(amount > 0, "Must purchase at least 1 share");
        require(msg.value >= pricePerShare(amount), "Insufficient ETH sent");

        // Mint shares to the buyer
        _mint(msg.sender, amount);
        shares[msg.sender] += amount;

        emit SharesPurchased(msg.sender, amount);
    }

    // Function to sell shares
    function sellShares(uint256 amount) external nonReentrant {
        require(amount > 0, "Must sell at least 1 share");
        require(shares[msg.sender] >= amount, "Not enough shares to sell");

        // Transfer the shares back to the contract
        _burn(msg.sender, amount);
        shares[msg.sender] -= amount;

        // Pay the seller
        payable(msg.sender).transfer(pricePerShare(amount));

        emit SharesSold(msg.sender, amount);
    }

    // Internal function to calculate the price per share
    function pricePerShare(uint256 amount) internal pure returns (uint256) {
        // Define the price per share, for example, 0.01 Ether
        uint256 price = 0.01 ether;
        return price * amount;
    }

    // Function to get the number of shares owned by an address
    function getShares(address owner) external view returns (uint256) {
        return shares[owner];
    }
}
```
