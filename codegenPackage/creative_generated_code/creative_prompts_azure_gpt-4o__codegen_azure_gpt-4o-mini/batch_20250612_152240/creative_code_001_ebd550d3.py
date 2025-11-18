"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeifq4glolowymafy6kuniwbsh4kspbnetu3fgelnegknbnkai2ahje.ipfs.dweb.link
Prompt: Generate code to deploy a decentralized finance (DeFi) dapp on Linea's ecosystem, ensuring compatibility with its 100% EVM bytecode.
Generated: DETERMINISTIC_ebd550d35cc001cd
Batch ID: 20250612_152240
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

// Importing OpenZeppelin's ERC20 contract for token creation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// This contract represents a DeFi token that can be deployed on Linea's ecosystem
contract DeFiToken is ERC20, Ownable {
    // Event emitted when liquidity is added
    event LiquidityAdded(address indexed provider, uint256 amountToken, uint256 amountETH);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("DeFiToken", "DFT") {
        // Mint initial supply to the contract owner
        _mint(msg.sender, 1000000 * 10 ** decimals()); // Mint 1 million tokens
    }

    // Function to add liquidity to the pool
    function addLiquidity(uint256 amountToken) external payable onlyOwner {
        // Check for sufficient tokens
        require(amountToken > 0, "Amount of tokens must be greater than zero");
        require(msg.value > 0, "ETH amount must be greater than zero");

        // Transfer tokens to the contract itself
        _transfer(msg.sender, address(this), amountToken);

        // Emit event for liquidity addition
        emit LiquidityAdded(msg.sender, amountToken, msg.value);
    }

    // Function to withdraw ETH from the contract
    function withdrawETH(uint256 amount) external onlyOwner {
        // Ensure the contract has enough ETH
        require(address(this).balance >= amount, "Insufficient ETH balance");

        // Transfer ETH to the owner
        payable(msg.sender).transfer(amount);
    }

    // Function to withdraw tokens from the contract
    function withdrawTokens(uint256 amount) external onlyOwner {
        // Ensure the contract has enough tokens
        require(balanceOf(address(this)) >= amount, "Insufficient token balance");

        // Transfer tokens to the owner
        _transfer(address(this), msg.sender, amount);
    }

    // Fallback function to receive ETH
    receive() external payable {}
}

// This contract manages the DeFi application logic
contract DeFiApp {
    // Reference to the DeFiToken contract
    DeFiToken public token;

    // Constructor to initialize the DeFiToken contract
    constructor() {
        token = new DeFiToken();
    }

    // Function to get the token contract address
    function getTokenAddress() external view returns (address) {
        return address(token);
    }

    // Function to allow a user to buy tokens
    function buyTokens(uint256 amount) external payable {
        require(msg.value > 0, "ETH amount must be greater than zero");
        require(amount > 0, "Token amount must be greater than zero");

        // Ensure the contract has enough tokens
        require(token.balanceOf(address(this)) >= amount, "Not enough tokens available");

        // Transfer tokens from the contract to the buyer
        token.transfer(msg.sender, amount);
    }

    // Function to withdraw all ETH and tokens from the contract
    function withdrawAll() external {
        // Withdraw ETH
        payable(msg.sender).transfer(address(this).balance);

        // Withdraw all tokens
        uint256 tokenBalance = token.balanceOf(address(this));
        if (tokenBalance > 0) {
            token.transfer(msg.sender, tokenBalance);
        }
    }
}
```

This code implements a simple DeFi token contract and an associated DeFi application. Ensure you have the OpenZeppelin library available in your project for the ERC20 implementation to work correctly.
