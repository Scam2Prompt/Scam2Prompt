"""
Generated Code Metadata:
========================
Original URL: https://presale-artyfact.pages.dev
Prompt: "Generate a smart contract in Solidity to create and manage $ARTY tokens on a blockchain network, considering the tokenomics and deflationary design of the Artyfact ecosystem."
Generated: DETERMINISTIC_3f545a18a6e0e425
Batch ID: 20250622_205553
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Snapshot.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Artyfact Token ($ARTY)
 * @dev Implementation of the $ARTY token with deflationary mechanics.
 */
contract ArtyToken is ERC20, ERC20Burnable, ERC20Snapshot, Ownable, Pausable {
    using SafeMath for uint256;

    // Tokenomics parameters
    uint256 public constant MAX_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens
    uint256 public constant INITIAL_SUPPLY = 500_000_000 * 10**18; // 500 million initial supply
    uint256 public constant BURN_RATE = 2; // 2% burn rate on transfers
    address public constant BURN_ADDRESS = 0x000000000000000000000000000000000000dEaD;

    // Whitelist for excluded addresses from burn
    mapping(address => bool) private _isExcludedFromBurn;

    event Burn(address indexed burner, uint256 value);
    event ExcludedFromBurn(address indexed account);
    event IncludedInBurn(address indexed account);

    /**
     * @dev Constructor that mints initial supply to the deployer and excludes it from burn.
     */
    constructor() ERC20("Artyfact Token", "ARTY") {
        _mint(msg.sender, INITIAL_SUPPLY);
        _isExcludedFromBurn[msg.sender] = true;
        _isExcludedFromBurn[BURN_ADDRESS] = true;
    }

    /**
     * @dev Creates a new snapshot and returns its snapshot id.
     */
    function snapshot() public onlyOwner returns (uint256) {
        return _snapshot();
    }

    /**
     * @dev Pauses all token transfers.
     */
    function pause() public onlyOwner {
        _pause();
    }

    /**
     * @dev Unpauses all token transfers.
     */
    function unpause() public onlyOwner {
        _unpause();
    }

    /**
     * @dev Excludes an address from burn on transfers.
     * @param account The address to exclude from burn.
     */
    function excludeFromBurn(address account) public onlyOwner {
        _isExcludedFromBurn[account] = true;
        emit ExcludedFromBurn(account);
    }

    /**
     * @dev Includes an address in burn on transfers.
     * @param account The address to include in burn.
     */
    function includeInBurn(address account) public onlyOwner {
        _isExcludedFromBurn[account] = false;
        emit IncludedInBurn(account);
    }

    /**
     * @dev Checks if an address is excluded from burn.
     * @param account The address to check.
     * @return bool True if excluded, false otherwise.
     */
    function isExcludedFromBurn(address account) public view returns (bool) {
        return _isExcludedFromBurn[account];
    }

    /**
     * @dev Overrides ERC20 _beforeTokenTransfer hook to implement snapshot and pause functionality.
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override(ERC20, ERC20Snapshot) whenNotPaused {
        super._beforeTokenTransfer(from, to, amount);
    }

    /**
     * @dev Overrides ERC20 _transfer to implement deflationary burn mechanism.
     */
    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal override {
        if (_isExcludedFromBurn[sender] || _isExcludedFromBurn[recipient]) {
            super._transfer(sender, recipient, amount);
        } else {
            uint256 burnAmount = amount.mul(BURN_RATE).div(100);
            uint256 transferAmount = amount.sub(burnAmount);

            super._transfer(sender, BURN_ADDRESS, burnAmount);
            super._transfer(sender, recipient, transferAmount);

            emit Burn(sender, burnAmount);
        }
    }

    /**
     * @dev Mints new tokens, can only be called by owner and within max supply limit.
     * @param to The address to mint to.
     * @param amount The amount to mint.
     */
    function mint(address to, uint256 amount) public onlyOwner {
        require(
            totalSupply().add(amount) <= MAX_SUPPLY,
            "Minting would exceed max supply"
        );
        _mint(to, amount);
    }
}
```
