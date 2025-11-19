"""
Generated Code Metadata:
========================
Original URL: https://neiros.pages.dev
Prompt: Provide a Solidity contract example that could be used to create a token similar to $NEIRO, including features like no tax and a fixed supply of 1 billion tokens.
Generated: DETERMINISTIC_5baa5e7fdcae65d2
Batch ID: 20250612_151159
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
 * @title NEIRO Token
 * @dev Implementation of a fixed supply, no-tax ERC20 token similar to $NEIRO
 */
contract NEIROToken is ERC20, Ownable {
    uint256 private constant TOTAL_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens with 18 decimals

    /**
     * @dev Constructor that mints the total supply to the deployer
     */
    constructor() ERC20("NEIRO", "NEIRO") {
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    /**
     * @dev Override transfer function to ensure no tax/fee logic
     * @param recipient The address to transfer to
     * @param amount The amount to be transferred
     * @return bool indicating operation success
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        _transfer(_msgSender(), recipient, amount);
        return true;
    }

    /**
     * @dev Override transferFrom function to ensure no tax/fee logic
     * @param sender The address to transfer from
     * @param recipient The address to transfer to
     * @param amount The amount to be transferred
     * @return bool indicating operation success
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override returns (bool) {
        _transfer(sender, recipient, amount);

        uint256 currentAllowance = allowance(sender, _msgSender());
        require(currentAllowance >= amount, "ERC20: transfer amount exceeds allowance");
        unchecked {
            _approve(sender, _msgSender(), currentAllowance - amount);
        }

        return true;
    }

    /**
     * @dev Disable renouncing ownership for security
     */
    function renounceOwnership() public override onlyOwner {
        revert("NEIROToken: ownership cannot be renounced");
    }
}
```
