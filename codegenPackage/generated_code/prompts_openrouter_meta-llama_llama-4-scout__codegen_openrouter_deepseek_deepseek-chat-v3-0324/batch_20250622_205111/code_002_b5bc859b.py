"""
Generated Code Metadata:
========================
Original URL: https://bafybeicrx6mxjdmgvh7372dgpwudwaunxrrcmmzyotodztwlzppzgiu5xm.ipfs.dweb.link
Prompt: Generate a smart contract code in Solidity for a meme token with entertainment purposes only, including a disclaimer similar to the one on the ANDY webpage.
Generated: DETERMINISTIC_b5bc859b15992afc
Batch ID: 20250622_205111
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title MemeToken
 * @dev A meme token contract for entertainment purposes only.
 * This token has no intrinsic value and is not intended as an investment.
 */
contract MemeToken is ERC20, Ownable {
    /**
     * @dev Constructor that mints the initial supply to the contract deployer.
     * @param name The name of the token.
     * @param symbol The symbol of the token.
     * @param initialSupply The initial supply of tokens to mint.
     */
    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply
    ) ERC20(name, symbol) {
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Mint new tokens. Only callable by the owner.
     * @param to The address to mint tokens to.
     * @param amount The amount of tokens to mint.
     */
    function mint(address to, uint256 amount) public onlyOwner {
        _mint(to, amount);
    }

    /**
     * @dev Burn tokens from the caller's account.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) public {
        _burn(msg.sender, amount);
    }

    /**
     * @notice DISCLAIMER:
     * This token is purely for entertainment purposes only.
     * It has no intrinsic value, expectation of financial return,
     * or expectation of any form. This is not an investment.
     * The token is provided "as is" without warranty of any kind.
     * By interacting with this token, you agree that the developers
     * and team are not responsible for any losses or damages incurred.
     * This is a meme token - treat it as such.
     */
    function disclaimer() public pure returns (string memory) {
        return "This token is purely for entertainment purposes only. It has no intrinsic value, expectation of financial return, or expectation of any form. This is not an investment. The token is provided 'as is' without warranty of any kind. By interacting with this token, you agree that the developers and team are not responsible for any losses or damages incurred. This is a meme token - treat it as such.";
    }
}
```
