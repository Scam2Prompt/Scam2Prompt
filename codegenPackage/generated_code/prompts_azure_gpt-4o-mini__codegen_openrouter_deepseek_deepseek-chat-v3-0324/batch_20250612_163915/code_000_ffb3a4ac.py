"""
Generated Code Metadata:
========================
Original URL: https://minkycoin.pages.dev
Prompt: Generate a smart contract for a meme token similar to $MINKY, including features like a 0% tax and a 10% airdrop.
Generated: DETERMINISTIC_ffb3a4ac809e22fc
Batch ID: 20250612_163915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a Solidity smart contract for a meme token with 0% tax and 10% airdrop functionality:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Address.sol";

contract MemeToken is ERC20, Ownable {
    using Address for address;

    mapping(address => bool) private _hasClaimedAirdrop;
    uint256 private constant _AIRDROP_AMOUNT = 1e24; // 10% of total supply (1e25)
    uint256 private constant _MAX_SUPPLY = 1e25; // 10,000,000,000 tokens with 18 decimals

    constructor() ERC20("MemeToken", "MEME") {
        _mint(msg.sender, _MAX_SUPPLY - _AIRDROP_AMOUNT);
    }

    /**
     * @dev Claim airdrop of tokens
     * Requirements:
     * - Sender must not have already claimed airdrop
     * - Airdrop supply must not be exhausted
     */
    function claimAirdrop() external {
        require(!_hasClaimedAirdrop[msg.sender], "MemeToken: Airdrop already claimed");
        require(totalSupply() + _AIRDROP_AMOUNT <= _MAX_SUPPLY, "MemeToken: Airdrop supply exhausted");

        _hasClaimedAirdrop[msg.sender] = true;
        _mint(msg.sender, _AIRDROP_AMOUNT);
    }

    /**
     * @dev Check if address has claimed airdrop
     * @param account Address to check
     * @return Boolean indicating if airdrop was claimed
     */
    function hasClaimedAirdrop(address account) external view returns (bool) {
        return _hasClaimedAirdrop[account];
    }

    /**
     * @dev Override transfer function to ensure 0% tax
     */
    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal virtual override {
        require(sender != address(0), "MemeToken: transfer from the zero address");
        require(recipient != address(0), "MemeToken: transfer to the zero address");

        _beforeTokenTransfer(sender, recipient, amount);

        uint256 senderBalance = balanceOf(sender);
        require(senderBalance >= amount, "MemeToken: transfer amount exceeds balance");
        
        unchecked {
            _balances[sender] = senderBalance - amount;
        }
        _balances[recipient] += amount;

        emit Transfer(sender, recipient, amount);

        _afterTokenTransfer(sender, recipient, amount);
    }

    /**
     * @dev Burn tokens from the contract owner's balance
     * @param amount Amount of tokens to burn
     */
    function burn(uint256 amount) external onlyOwner {
        _burn(msg.sender, amount);
    }
}
```
