"""
Generated Code Metadata:
========================
Original URL: https://cxcxcxcxxccxvcvc.pages.dev
Prompt: Create a simple smart contract in Solidity that demonstrates a community-driven distribution strategy similar to Catcoin's, with no taxes and LP tokens burnt.
Generated: DETERMINISTIC_7ca6022dc587ebd4
Batch ID: 20250622_210802
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

contract CommunityToken is ERC20, Ownable {
    address public immutable uniswapPair;
    bool private _liquidityAdded;

    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply,
        address _uniswapPair
    ) ERC20(name, symbol) {
        _mint(msg.sender, initialSupply);
        uniswapPair = _uniswapPair;
        _liquidityAdded = false;
    }

    // Override transfer to ensure no taxes
    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal virtual override {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");

        _beforeTokenTransfer(sender, recipient, amount);

        uint256 senderBalance = balanceOf(sender);
        require(senderBalance >= amount, "ERC20: transfer amount exceeds balance");
        unchecked {
            _balances[sender] = senderBalance - amount;
        }
        _balances[recipient] += amount;

        emit Transfer(sender, recipient, amount);

        _afterTokenTransfer(sender, recipient, amount);
    }

    // Function to burn LP tokens (can only be called once after liquidity is added)
    function burnLPTokens() external onlyOwner {
        require(!_liquidityAdded, "LP tokens already burnt");
        uint256 lpBalance = balanceOf(uniswapPair);
        _burn(uniswapPair, lpBalance);
        _liquidityAdded = true;
    }

    // Prevent renouncing ownership to maintain community control
    function renounceOwnership() public override onlyOwner {
        revert("Ownership cannot be renounced");
    }
}
```
