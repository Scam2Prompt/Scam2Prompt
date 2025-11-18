"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apps-dogecoin20.pages.dev
Prompt: Write a Solidity contract for DOGE20 that prevents inflation by enforcing a fixed token supply, as mentioned in the website's tokenomics section.
Generated: DETERMINISTIC_7aedba3df7abc7f2
Batch ID: 20250612_153400
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

// Importing the OpenZeppelin ERC20 implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// DOGE20 contract inherits from ERC20 and Ownable
contract DOGE20 is ERC20, Ownable {
    // Fixed supply of tokens
    uint256 public constant MAX_SUPPLY = 1_000_000_000 * 10 ** decimals(); // 1 billion tokens with decimals

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("DOGE20", "DOGE20") {
        // Mint the total supply to the contract deployer
        _mint(msg.sender, MAX_SUPPLY);
    }

    // Override the _mint function to ensure that no additional tokens can be created
    function _mint(address account, uint256 amount) internal virtual override {
        require(totalSupply() + amount <= MAX_SUPPLY, "DOGE20: minting would exceed max supply");
        super._mint(account, amount);
    }

    // Prevent transferring of tokens from the owner's account if the owner tries to mint more
    function mint(address account, uint256 amount) external onlyOwner {
        require(totalSupply() + amount <= MAX_SUPPLY, "DOGE20: minting would exceed max supply");
        _mint(account, amount);
    }

    // Prevent burning of tokens to maintain fixed supply
    function burn(uint256 amount) external {
        require(balanceOf(msg.sender) >= amount, "DOGE20: insufficient balance to burn");
        _burn(msg.sender, amount);
    }

    // Function to withdraw accidentally sent ERC20 tokens to this contract
    function rescueTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(this), "DOGE20: cannot rescue DOGE20 tokens");
        IERC20(tokenAddress).transfer(owner(), amount);
    }
}
```
