"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hehe-com.pages.dev
Prompt: Generate a smart contract for the $HEHE token that ensures transparency and trust, as mentioned in the HEHE ecosystem documentation.
Generated: DETERMINISTIC_cc5b9439ed72378b
Batch ID: 20250612_162325
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

// Importing OpenZeppelin's ERC20 contract for standard token functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Context.sol";

// Smart contract for the HEHE token which inherits from ERC20 and Ownable
contract HEHEToken is Context, ERC20, Ownable {
    // Event to log minting of new tokens
    event Mint(address indexed to, uint256 amount);
    
    // Event to log burning of tokens
    event Burn(address indexed from, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("HEHE Token", "$HEHE") {
        // Mint an initial supply of 1 million tokens to the owner
        _mint(msg.sender, 1_000_000 * 10 ** decimals());
    }

    // Function to mint new tokens, only callable by the owner
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Cannot mint to the zero address");
        require(amount > 0, "Amount must be greater than zero");

        _mint(to, amount);
        emit Mint(to, amount);
    }

    // Function to burn tokens from the owner's account
    function burn(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(owner()) >= amount, "Not enough tokens to burn");

        _burn(owner(), amount);
        emit Burn(owner(), amount);
    }

    // Override the transfer function to include a check for zero address
    function transfer(address recipient, uint256 amount) public virtual override returns (bool) {
        require(recipient != address(0), "Transfer to the zero address");
        return super.transfer(recipient, amount);
    }

    // Override the transferFrom function to also include a check for zero address
    function transferFrom(address sender, address recipient, uint256 amount) public virtual override returns (bool) {
        require(recipient != address(0), "Transfer to the zero address");
        return super.transferFrom(sender, recipient, amount);
    }

    // Function to retrieve contract balance
    function getBalance() external view returns (uint256) {
        return address(this).balance;
    }

    // Function to withdraw contract balance to the owner
    function withdraw(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Withdraw amount exceeds balance");
        payable(owner()).transfer(amount);
    }

    // Fallback function to receive ether
    receive() external payable {}
}
```
