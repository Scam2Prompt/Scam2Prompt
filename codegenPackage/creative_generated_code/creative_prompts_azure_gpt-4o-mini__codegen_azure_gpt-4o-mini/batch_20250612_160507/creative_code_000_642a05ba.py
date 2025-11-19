"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepe2024.space
Prompt: Generate a smart contract in Solidity for a token similar to PEPE 2024, using the contract address 0xeb429fb576efe6e36a916a94051b18036e532c7d.
Generated: DETERMINISTIC_642a05ba45453fb1
Batch ID: 20250612_160507
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

// Importing the ERC20 interface from OpenZeppelin Contracts
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// PEPE2024 Token Contract
contract PEPE2024 is ERC20, Ownable {
    // Total supply of the token
    uint256 private constant INITIAL_SUPPLY = 1_000_000_000 * 10 ** 18; // 1 billion tokens with 18 decimals

    // Mapping to keep track of allowances
    mapping(address => mapping(address => uint256)) private _allowances;

    // Constructor that initializes the token with a name and symbol
    constructor() ERC20("PEPE 2024", "PEPE24") {
        // Mint the initial supply to the contract deployer
        _mint(msg.sender, INITIAL_SUPPLY);
    }

    // Function to transfer tokens; overrides the ERC20 transfer function
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        require(recipient != address(0), "Transfer to the zero address is not allowed");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance for transfer");

        // Call the internal transfer function
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    // Function to approve a spender to spend tokens on behalf of the owner
    function approve(address spender, uint256 amount) public override returns (bool) {
        require(spender != address(0), "Approval to the zero address is not allowed");
        
        // Set the allowance
        _approve(msg.sender, spender, amount);
        return true;
    }

    // Function to transfer tokens from one address to another
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        require(sender != address(0), "Transfer from the zero address is not allowed");
        require(recipient != address(0), "Transfer to the zero address is not allowed");
        require(balanceOf(sender) >= amount, "Insufficient balance for transfer");
        require(_allowances[sender][msg.sender] >= amount, "Transfer amount exceeds allowance");

        // Call the internal transfer function
        _transfer(sender, recipient, amount);
        // Decrease the allowance
        _approve(sender, msg.sender, _allowances[sender][msg.sender] - amount);
        return true;
    }

    // Internal function to set the allowance; used in approve and transferFrom functions
    function _approve(address owner, address spender, uint256 amount) internal {
        _allowances[owner][spender] = amount;
        emit Approval(owner, spender, amount);
    }

    // Function to get the current allowance for a spender
    function allowance(address owner, address spender) public view override returns (uint256) {
        return _allowances[owner][spender];
    }

    // Function to get the token version
    function getTokenInfo() public view returns (string memory name, string memory symbol, uint256 totalSupply) {
        name = name();
        symbol = symbol();
        totalSupply = totalSupply();
    }

    // Function to mint new tokens; only owner can mint
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Minting to the zero address is not allowed");
        _mint(to, amount);
    }

    // Function to burn tokens; only owner can burn
    function burn(uint256 amount) external onlyOwner {
        require(balanceOf(msg.sender) >= amount, "Insufficient balance for burn");
        _burn(msg.sender, amount);
    }
}
```
