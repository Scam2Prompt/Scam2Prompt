"""
Generated Code Metadata:
========================
Original URL: https://purplepepe-dashboard.pages.dev
Prompt: Generate a smart contract in Solidity for a token similar to Purple Pepe on the Solana blockchain, focusing on unique features that enhance its value.
Generated: DETERMINISTIC_7c81268601927ce6
Batch ID: 20250612_163431
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

// Contract for the Purple Pepe Token
contract PurplePepeToken is ERC20, Ownable {
    // Mapping to track the number of tokens held by each address
    mapping(address => uint256) private _balances;

    // Event to log the minting of new tokens
    event TokensMinted(address indexed to, uint256 amount);

    // Event to log the burning of tokens
    event TokensBurned(address indexed from, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("Purple Pepe", "PPEPE") {
        // Mint an initial supply of tokens to the contract owner
        _mint(msg.sender, 1000000 * 10 ** decimals()); // 1 million tokens
    }

    // Function to mint new tokens, only callable by the owner
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Cannot mint to the zero address");
        require(amount > 0, "Mint amount must be greater than zero");

        _mint(to, amount);
        emit TokensMinted(to, amount);
    }

    // Function to burn tokens from the caller's account
    function burn(uint256 amount) external {
        require(amount > 0, "Burn amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to burn");

        _burn(msg.sender, amount);
        emit TokensBurned(msg.sender, amount);
    }

    // Function to transfer tokens with a fee
    function transferWithFee(address recipient, uint256 amount, uint256 fee) external returns (bool) {
        require(recipient != address(0), "Cannot transfer to the zero address");
        require(amount > fee, "Transfer amount must be greater than fee");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance for transfer");

        uint256 amountAfterFee = amount - fee;

        // Transfer the fee to the owner
        _transfer(msg.sender, owner(), fee);
        // Transfer the remaining amount to the recipient
        _transfer(msg.sender, recipient, amountAfterFee);

        return true;
    }

    // Function to withdraw any ERC20 tokens sent to this contract by mistake
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(this), "Cannot withdraw native token");
        require(amount > 0, "Amount must be greater than zero");

        IERC20(tokenAddress).transfer(msg.sender, amount);
    }

    // Function to get the balance of tokens held by an address
    function getBalance(address account) external view returns (uint256) {
        return balanceOf(account);
    }
}
```
