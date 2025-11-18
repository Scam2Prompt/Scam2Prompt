"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tokenscreatorethpro.pages.dev
Prompt: Provide Solidity code for a token creation process that deducts a fixed fee (e.g., $1) during the token creation and ensures the token is added to the user's wallet and listed on decentralized trading platforms, as described on the Tokens Creator page.
Generated: DETERMINISTIC_52653b57245f52cd
Batch ID: 20250612_145916
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// @title TokenCreator
// @dev This contract allows users to create their own ERC20 tokens with a fixed fee deducted at creation.
contract TokenCreator is Ownable {
    using SafeMath for uint256;

    // Fee for creating a token in wei (1 USD in wei, this value needs to be updated based on current ETH price)
    uint256 public constant CREATION_FEE = 1 ether; // Adjust this based on the current ETH to USD rate

    // Event for token creation
    event TokenCreated(address indexed creator, address tokenAddress, string tokenName, string tokenSymbol);

    /**
     * @dev Create a new ERC20 token
     * @param name The name of the token
     * @param symbol The symbol of the token
     * @param initialSupply The initial supply of the token, in smallest unit (e.g., wei)
     */
    function createToken(string memory name, string memory symbol, uint256 initialSupply) external payable {
        // Check if the sent value matches the creation fee
        require(msg.value == CREATION_FEE, "Incorrect fee sent");

        // Create the new token contract
        ERC20 newToken = new ERC20(name, symbol);
        
        // Mint the initial supply of tokens to the creator's address
        newToken._mint(msg.sender, initialSupply);

        // Emit the token creation event
        emit TokenCreated(msg.sender, address(newToken), name, symbol);
    }

    /**
     * @dev Allow the contract owner to withdraw the balance of the contract
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        // Transfer the contract's balance to the owner
        payable(owner()).transfer(balance);
    }

    /**
     * @dev Fallback function to accept Ether
     */
    receive() external payable {}
}
```

**Note:**
- The fee is set to a constant value that represents $1 in wei; please adjust this value according to the current ETH price to ensure that it reflects $1 accurately.
- Ensure any additional features for listing on decentralized exchanges are implemented according to the specific DEX's requirements, as this code does not include those functionalities directly.
