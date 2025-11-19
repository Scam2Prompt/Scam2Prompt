"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://too1m.pages.dev
Prompt: Develop a smart contract in Solidity for the $POON token that includes features mentioned in the tokenomics section of the website.
Generated: DETERMINISTIC_ecd83994b02449c5
Batch ID: 20250612_162207
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

// Importing OpenZeppelin's ERC20 implementation and Ownable for ownership management
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// $POON Token contract
contract PoonToken is ERC20, Ownable {
    // Define tokenomics parameters
    uint256 public constant INITIAL_SUPPLY = 1_000_000 * 10 ** decimals(); // 1 million tokens
    uint256 public constant MAX_SUPPLY = 10_000_000 * 10 ** decimals(); // Maximum supply of 10 million tokens

    // Event for minting new tokens
    event Mint(address indexed to, uint256 amount);
    
    // Constructor to set the token name and symbol
    constructor() ERC20("Poon Token", "$POON") {
        _mint(msg.sender, INITIAL_SUPPLY); // Mint initial supply to the contract owner
    }

    // Function to mint new tokens, only callable by the owner
    function mint(address to, uint256 amount) external onlyOwner {
        require(totalSupply() + amount <= MAX_SUPPLY, "Cannot mint beyond max supply");
        _mint(to, amount);
        emit Mint(to, amount);
    }

    // Function to burn tokens, allowing users to destroy their tokens
    function burn(uint256 amount) external {
        _burn(msg.sender, amount);
    }

    // Function to transfer tokens with a basic check for zero address
    function transfer(address to, uint256 amount) public override returns (bool) {
        require(to != address(0), "Transfer to the zero address");
        return super.transfer(to, amount);
    }

    // Function to transfer tokens from one address to another with allowance checks
    function transferFrom(address from, address to, uint256 amount) public override returns (bool) {
        require(to != address(0), "Transfer to the zero address");
        return super.transferFrom(from, to, amount);
    }

    // Function to safely approve an allowance for a spender
    function approve(address spender, uint256 amount) public override returns (bool) {
        require(spender != address(0), "Approve to the zero address");
        return super.approve(spender, amount);
    }

    // Function to handle the withdrawal of wrongly sent ERC20 tokens
    function withdrawToken(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(this), "Cannot withdraw own token");
        IERC20(tokenAddress).transfer(owner(), amount);
    }

    // Function to withdraw Ether from the contract, owner only
    function withdrawEther(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient balance");
        payable(owner()).transfer(amount);
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
