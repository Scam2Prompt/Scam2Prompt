"""
Generated Code Metadata:
========================
Original URL: https://website-9v1.pages.dev
Prompt: Write a Python code snippet using the ERC20 Token Standard to create a smart contract for a utility token like PLRT on the Binance Smart Chain.
Generated: DETERMINISTIC_1f0ba4d5a43d9713
Batch ID: 20250622_211932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title PLRT Token Contract
 * @dev Implementation of the ERC20 standard token with additional functionality
 * for the PLRT utility token on Binance Smart Chain.
 */
contract PLRToken is ERC20, Ownable {
    uint256 private constant MAX_SUPPLY = 1000000000 * 10**18; // 1 billion tokens with 18 decimals

    /**
     * @dev Constructor that initializes the token with its name, symbol, and initial supply.
     * The entire supply is minted to the contract deployer (owner).
     */
    constructor() ERC20("Pillar Token", "PLRT") {
        _mint(msg.sender, MAX_SUPPLY);
    }

    /**
     * @dev Function to mint additional tokens. Only callable by owner.
     * @param to The address that will receive the minted tokens.
     * @param amount The amount of tokens to mint.
     */
    function mint(address to, uint256 amount) public onlyOwner {
        require(totalSupply() + amount <= MAX_SUPPLY, "PLRT: Exceeds max supply");
        _mint(to, amount);
    }

    /**
     * @dev Function to burn tokens. Any user can burn their own tokens.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) public {
        _burn(msg.sender, amount);
    }

    /**
     * @dev Function to allow owner to recover any ERC20 tokens sent to this contract by mistake.
     * @param tokenAddress The address of the ERC20 token to recover.
     * @param to The address to send the recovered tokens to.
     * @param amount The amount of tokens to recover.
     */
    function recoverERC20(address tokenAddress, address to, uint256 amount) public onlyOwner {
        IERC20(tokenAddress).transfer(to, amount);
    }
}
```

Note: This is a Solidity smart contract, not Python, as ERC20 tokens are implemented on blockchain platforms like Ethereum/BSC using Solidity. The code follows best practices including:
- Using OpenZeppelin's audited contracts
- Proper access control with Ownable
- Maximum supply protection
- Token recovery function
- Complete NatSpec documentation
- Error handling with require statements
