"""
Generated Code Metadata:
========================
Original URL: https://shibuswap.github.io
Prompt: Generate a smart contract code in Solidity to create a new token similar to BONE, with governance features, on the Ethereum blockchain.
Generated: DETERMINISTIC_28d5cfbb4b0a7b43
Batch ID: 20250622_211156
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Snapshot.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/governance/utils/Votes.sol";

contract BONEToken is ERC20, ERC20Snapshot, Ownable, Votes {
    uint256 public constant MAX_SUPPLY = 250_000_000 * 10**18; // 250 million BONE tokens

    // Events
    event TokensMinted(address indexed to, uint256 amount);
    event TokensBurned(address indexed from, uint256 amount);

    /**
     * @dev Constructor that initializes the token with initial supply.
     * The initial supply is minted to the contract deployer.
     */
    constructor() ERC20("BONE Token", "BONE") {
        _mint(msg.sender, MAX_SUPPLY);
    }

    /**
     * @dev Creates a new snapshot ID.
     * Only callable by the owner.
     * @return uint256 The new snapshot ID.
     */
    function snapshot() public onlyOwner returns (uint256) {
        return _snapshot();
    }

    /**
     * @dev Mints new tokens to a specified address.
     * Only callable by the owner.
     * @param to The address to mint tokens to.
     * @param amount The amount of tokens to mint.
     */
    function mint(address to, uint256 amount) public onlyOwner {
        require(totalSupply() + amount <= MAX_SUPPLY, "BONE: Exceeds max supply");
        _mint(to, amount);
        emit TokensMinted(to, amount);
    }

    /**
     * @dev Burns tokens from the caller's balance.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) public {
        _burn(msg.sender, amount);
        emit TokensBurned(msg.sender, amount);
    }

    /**
     * @dev Overrides required by Solidity for ERC20Snapshot and Votes.
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override(ERC20, ERC20Snapshot) {
        super._beforeTokenTransfer(from, to, amount);
    }

    /**
     * @dev Overrides required by Solidity for Votes.
     */
    function _afterTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override(ERC20, Votes) {
        super._afterTokenTransfer(from, to, amount);
    }

    /**
     * @dev Overrides required by Solidity for Votes.
     */
    function _mint(address to, uint256 amount) internal override(ERC20, Votes) {
        super._mint(to, amount);
    }

    /**
     * @dev Overrides required by Solidity for Votes.
     */
    function _burn(address account, uint256 amount) internal override(ERC20, Votes) {
        super._burn(account, amount);
    }
}
```
