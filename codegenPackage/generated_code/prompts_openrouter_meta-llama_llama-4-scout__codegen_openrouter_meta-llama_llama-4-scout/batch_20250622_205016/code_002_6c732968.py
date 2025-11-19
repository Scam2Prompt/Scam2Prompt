"""
Generated Code Metadata:
========================
Original URL: https://babygrokai.pages.dev
Prompt: Generate a code snippet in Solidity to implement a burn mechanism for a cryptocurrency token, similar to the one described in the Baby Grok tokenomics.
Generated: DETERMINISTIC_6c73296863040901
Batch ID: 20250622_205016
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title BabyGrokToken
 * @author [Your Name]
 * @notice A token with a burn mechanism similar to Baby Grok tokenomics.
 */
contract BabyGrokToken is ERC20, ERC20Burnable, ReentrancyGuard {
    /**
     * @notice The address of the burn controller.
     */
    address private burnController;

    /**
     * @notice Event emitted when burn controller is updated.
     * @param oldController The old burn controller address.
     * @param newController The new burn controller address.
     */
    event BurnControllerUpdated(address oldController, address newController);

    /**
     * @notice Event emitted when tokens are burned.
     * @param burner The address that burned the tokens.
     * @param amount The amount of tokens burned.
     */
    event TokensBurned(address burner, uint256 amount);

    /**
     * @notice Initializes the token with a name, symbol, and initial supply.
     * @param name The name of the token.
     * @param symbol The symbol of the token.
     * @param initialSupply The initial supply of the token.
     * @param burnController_ The initial burn controller address.
     */
    constructor(string memory name, string memory symbol, uint256 initialSupply, address burnController_) ERC20(name, symbol) {
        _mint(msg.sender, initialSupply);
        burnController = burnController_;
    }

    /**
     * @notice Updates the burn controller address.
     * @param newController The new burn controller address.
     */
    function updateBurnController(address newController) public {
        require(msg.sender == burnController, "Only the current burn controller can update the address.");
        address oldController = burnController;
        burnController = newController;
        emit BurnControllerUpdated(oldController, newController);
    }

    /**
     * @notice Burns tokens from the specified address.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) public override nonReentrant {
        require(msg.sender == burnController, "Only the burn controller can burn tokens.");
        _burn(msg.sender, amount);
        emit TokensBurned(msg.sender, amount);
    }

    /**
     * @notice Burns tokens from the specified address on behalf of another address.
     * @param account The address from which to burn tokens.
     * @param amount The amount of tokens to burn.
     */
    function burnFrom(address account, uint256 amount) public override nonReentrant {
        require(msg.sender == burnController, "Only the burn controller can burn tokens on behalf of another address.");
        _burn(account, amount);
        emit TokensBurned(account, amount);
    }
}
```
