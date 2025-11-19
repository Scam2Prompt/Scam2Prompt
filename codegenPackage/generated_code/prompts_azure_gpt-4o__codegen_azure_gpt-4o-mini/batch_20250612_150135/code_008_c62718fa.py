"""
Generated Code Metadata:
========================
Original URL: https://vivalalibertadproject.com
Prompt: Write a Solidity-based smart contract (if applicable for cross-chain compatibility) to implement a token similar to $LIBRA that supports decentralized funding for small businesses.
Generated: DETERMINISTIC_c62718fa73069150
Batch ID: 20250612_150135
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

// Importing OpenZeppelin's ERC20 implementation for standard token functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Contract for a token similar to $LIBRA
contract LibraToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Mapping to track the funding contributions for small businesses
    mapping(address => uint256) public businessFunding;

    // Event emitted when a business receives funding
    event Funded(address indexed business, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("LibraToken", "LIBRA") {
        // Mint an initial supply of tokens to the contract owner
        _mint(msg.sender, 1000000 * 10 ** decimals()); // 1 million tokens
    }

    // Function to fund a small business
    function fundBusiness(address _business, uint256 _amount) external {
        require(_amount > 0, "Funding amount must be greater than zero");
        require(balanceOf(msg.sender) >= _amount, "Insufficient token balance");
        require(_business != address(0), "Invalid business address");

        // Transfer tokens from the sender to the business
        _transfer(msg.sender, _business, _amount);
        
        // Update the funding record for the business
        businessFunding[_business] = businessFunding[_business].add(_amount);

        // Emit the funding event
        emit Funded(_business, _amount);
    }

    // Function to allow the owner to mint new tokens
    function mintTokens(address _to, uint256 _amount) external onlyOwner {
        require(_to != address(0), "Invalid address");
        require(_amount > 0, "Mint amount must be greater than zero");

        // Mint new tokens to the specified address
        _mint(_to, _amount);
    }

    // Function to allow the owner to burn tokens
    function burnTokens(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Burn amount must be greater than zero");
        require(balanceOf(msg.sender) >= _amount, "Insufficient token balance");

        // Burn the specified amount of tokens from the owner's balance
        _burn(msg.sender, _amount);
    }
}
```
