"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallstreetmemes-in.pages.dev
Prompt: Write a smart contract for the $WSM token that ensures transparency and trustworthiness, as outlined in the Wall Street Memes roadmap.
Generated: DETERMINISTIC_9a15eded3c576a22
Batch ID: 20250612_162504
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

// Importing OpenZeppelin's ERC20 implementation for standard compliance
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Contract for Wall Street Memes Token (WSM)
contract WSMToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Event to log token minting
    event Mint(address indexed to, uint256 amount);
    
    // Mapping to track addresses that can mint tokens
    mapping(address => bool) public minters;

    // Constructor to initialize the token with name and symbol
    constructor() ERC20("Wall Street Memes", "$WSM") {
        // Mint an initial supply of tokens to the contract deployer
        _mint(msg.sender, 1_000_000 * 10**decimals()); // 1 million tokens
    }

    // Modifier to check if the caller is a minter
    modifier onlyMinter() {
        require(minters[msg.sender], "Caller is not a minter");
        _;
    }

    // Function to add a minter
    function addMinter(address _minter) external onlyOwner {
        require(_minter != address(0), "Invalid address");
        minters[_minter] = true;
    }

    // Function to remove a minter
    function removeMinter(address _minter) external onlyOwner {
        require(_minter != address(0), "Invalid address");
        minters[_minter] = false;
    }

    // Mint new tokens; only minters can call this
    function mint(address to, uint256 amount) external onlyMinter {
        require(to != address(0), "Cannot mint to the zero address");
        require(amount > 0, "Amount must be greater than zero");

        // Mint the tokens and emit the event
        _mint(to, amount);
        emit Mint(to, amount);
    }

    // Override the transfer function to include additional checks if necessary
    function transfer(address recipient, uint256 amount) public virtual override returns (bool) {
        require(recipient != address(0), "Transfer to the zero address not allowed");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Call the parent class's transfer function
        _transfer(_msgSender(), recipient, amount);
        return true;
    }

    // Override the transferFrom function
    function transferFrom(address sender, address recipient, uint256 amount) public virtual override returns (bool) {
        require(sender != address(0), "Transfer from the zero address not allowed");
        require(recipient != address(0), "Transfer to the zero address not allowed");
        require(balanceOf(sender) >= amount, "Insufficient balance");
        require(allowance(sender, _msgSender()) >= amount, "Allowance exceeded");

        // Call the parent class's transferFrom function
        _transfer(sender, recipient, amount);
        _approve(sender, _msgSender(), allowance(sender, _msgSender()).sub(amount));
        return true;
    }
}
```
