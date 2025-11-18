"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-buck.pages.dev
Prompt: Create a smart contract in Solidity for a community-driven token similar to CoinBuck, ensuring a fair launch with no reserved tokens and a fixed supply.
Generated: DETERMINISTIC_21d41d1bcede5784
Batch ID: 20250612_152326
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

/**
 * @title CommunityToken
 * @dev A community-driven ERC20 token with a fixed supply and no reserved tokens.
 */
contract CommunityToken is ERC20, Ownable {
    // Fixed supply of tokens
    uint256 private constant _totalSupply = 1000000 * 10 ** decimals(); // 1 million tokens

    /**
     * @dev Constructor that gives msg.sender all of the existing tokens.
     * The total supply is fixed, and no tokens are reserved.
     */
    constructor() ERC20("CommunityToken", "CTK") {
        _mint(msg.sender, _totalSupply);
    }

    /**
     * @dev Function to burn tokens from the caller's account.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) external {
        _burn(msg.sender, amount);
    }

    /**
     * @dev Function to transfer tokens, overridden to include a custom logic.
     * @param recipient The address to receive the tokens.
     * @param amount The amount of tokens to transfer.
     * @return bool indicating success.
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        require(recipient != address(0), "Cannot transfer to the zero address");
        require(amount > 0, "Transfer amount must be greater than 0");

        // Call the parent transfer function
        return super.transfer(recipient, amount);
    }

    /**
     * @dev Function to approve a spender to spend tokens on behalf of the owner.
     * @param spender The address allowed to spend the tokens.
     * @param amount The amount of tokens to allow.
     * @return bool indicating success.
     */
    function approve(address spender, uint256 amount) public override returns (bool) {
        require(spender != address(0), "Cannot approve the zero address");
        require(amount > 0, "Approval amount must be greater than 0");

        // Call the parent approve function
        return super.approve(spender, amount);
    }

    /**
     * @dev Function to receive Ether. This contract does not accept Ether.
     */
    receive() external payable {
        revert("This contract does not accept Ether");
    }
}
```
