"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoin-etftoken.web.app
Prompt: Generate code to implement a token burning mechanism in Solidity that reduces the supply of BTCETF by 5% for every milestone event triggered.
Generated: DETERMINISTIC_d54ef77e727fbed3
Batch ID: 20250612_152410
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title BTCETF Token Contract
 * @dev This contract implements an ERC20 token with a token burning mechanism
 * that reduces the total supply by 5% for every milestone event triggered.
 */
contract BTCETF is ERC20Burnable, Ownable {
    
    // Event emitted when a milestone is triggered and tokens are burned
    event MilestoneTriggered(uint256 newSupply, uint256 burnedAmount);
    
    /**
     * @dev Constructor for the BTCETF token.
     * Initializes the token with a specific name and symbol.
     * @param initialSupply The initial supply of the token.
     */
    constructor(uint256 initialSupply) ERC20("BTCETF Token", "BTCETF") {
        require(initialSupply > 0, "Initial supply must be greater than 0");
        _mint(msg.sender, initialSupply * 10 ** decimals());
    }

    /**
     * @dev Triggers a milestone event that burns 5% of the current total supply.
     */
    function triggerMilestone() external onlyOwner {
        uint256 currentSupply = totalSupply();
        require(currentSupply > 0, "No tokens to burn");

        // Calculate 5% of the current total supply
        uint256 burnAmount = currentSupply * 5 / 100;

        // Perform the burn
        _burn(address(this), burnAmount);

        // Emit the milestone event with new supply and burned amount
        emit MilestoneTriggered(currentSupply - burnAmount, burnAmount);
    }

    /**
     * @dev Override the _burn function to ensure that only the contract's balance can be burned
     * @param account The account whose tokens will be burned.
     * @param amount The amount of tokens to burn.
     */
    function _burn(address account, uint256 amount) internal override {
        require(balanceOf(account) >= amount, "ERC20: burn amount exceeds balance");
        super._burn(account, amount);
    }
}
```
