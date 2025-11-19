"""
Generated Code Metadata:
========================
Original URL: https://gofurs-cash.pages.dev
Prompt: Design an ERC404 token standard implementation that allows for seamless interaction with decentralized exchanges like Uniswap, using $GOFURS as a reference.
Generated: DETERMINISTIC_412d6d6a82b710b3
Batch ID: 20250622_210918
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

// Importing OpenZeppelin's ERC20 implementation and Ownable contract
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// ERC404 Token Standard Implementation
contract ERC404Token is ERC20, Ownable {
    // Mapping to track allowances for delegated transfers
    mapping(address => mapping(address => uint256)) private _allowances;

    // Event emitted when tokens are minted
    event Mint(address indexed to, uint256 amount);

    // Event emitted when tokens are burned
    event Burn(address indexed from, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("GOFURS", "GOF") {
        // Mint initial supply to the contract deployer
        _mint(msg.sender, 1000000 * 10 ** decimals()); // 1 million tokens
    }

    // Function to mint new tokens
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "ERC404: mint to the zero address");
        require(amount > 0, "ERC404: amount must be greater than zero");

        _mint(to, amount);
        emit Mint(to, amount);
    }

    // Function to burn tokens from the caller's account
    function burn(uint256 amount) external {
        require(amount > 0, "ERC404: amount must be greater than zero");
        _burn(msg.sender, amount);
        emit Burn(msg.sender, amount);
    }

    // Override the allowance function to include custom logic if needed
    function allowance(address owner, address spender) public view override returns (uint256) {
        return _allowances[owner][spender];
    }

    // Function to approve a spender to spend tokens on behalf of the owner
    function approve(address spender, uint256 amount) public override returns (bool) {
        require(spender != address(0), "ERC404: approve to the zero address");
        _approve(msg.sender, spender, amount);
        return true;
    }

    // Function to transfer tokens from one address to another
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        require(sender != address(0), "ERC404: transfer from the zero address");
        require(recipient != address(0), "ERC404: transfer to the zero address");
        require(amount > 0, "ERC404: amount must be greater than zero");

        _transfer(sender, recipient, amount);
        _approve(sender, msg.sender, _allowances[sender][msg.sender] - amount);
        return true;
    }

    // Internal function to handle token transfers
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        require(balanceOf(sender) >= amount, "ERC404: transfer amount exceeds balance");
        super._transfer(sender, recipient, amount);
    }

    // Internal function to handle approvals
    function _approve(address owner, address spender, uint256 amount) internal override {
        require(owner != address(0), "ERC404: approve from the zero address");
        require(spender != address(0), "ERC404: approve to the zero address");

        _allowances[owner][spender] = amount;
        emit Approval(owner, spender, amount);
    }
}
```
