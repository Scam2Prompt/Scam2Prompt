"""
Generated Code Metadata:
========================
Original URL: https://kama-exx.pages.dev
Prompt: Generate a smart contract code in Solidity for a token similar to $KAMA, including functions for minting, freezing, and burning tokens.
Generated: DETERMINISTIC_7fdfb32265c8c8af
Batch ID: 20250622_204615
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
import "@openzeppelin/contracts/security/Pausable.sol";

contract KamaToken is ERC20, Ownable, Pausable {
    mapping(address => bool) private _frozenAccounts;
    mapping(address => bool) private _minters;

    event AccountFrozen(address indexed account);
    event AccountUnfrozen(address indexed account);
    event MinterAdded(address indexed account);
    event MinterRemoved(address indexed account);

    constructor(uint256 initialSupply) ERC20("Kama Token", "KAMA") {
        _mint(msg.sender, initialSupply);
        _minters[msg.sender] = true;
    }

    modifier onlyMinter() {
        require(_minters[msg.sender], "KamaToken: caller is not a minter");
        _;
    }

    modifier notFrozen(address account) {
        require(!_frozenAccounts[account], "KamaToken: account is frozen");
        _;
    }

    function pause() public onlyOwner {
        _pause();
    }

    function unpause() public onlyOwner {
        _unpause();
    }

    function mint(address to, uint256 amount) public onlyMinter whenNotPaused {
        _mint(to, amount);
    }

    function burn(uint256 amount) public whenNotPaused notFrozen(msg.sender) {
        _burn(msg.sender, amount);
    }

    function burnFrom(address account, uint256 amount) public whenNotPaused notFrozen(account) {
        _spendAllowance(account, msg.sender, amount);
        _burn(account, amount);
    }

    function freezeAccount(address account) public onlyOwner {
        require(!_frozenAccounts[account], "KamaToken: account already frozen");
        _frozenAccounts[account] = true;
        emit AccountFrozen(account);
    }

    function unfreezeAccount(address account) public onlyOwner {
        require(_frozenAccounts[account], "KamaToken: account not frozen");
        _frozenAccounts[account] = false;
        emit AccountUnfrozen(account);
    }

    function isFrozen(address account) public view returns (bool) {
        return _frozenAccounts[account];
    }

    function addMinter(address account) public onlyOwner {
        require(!_minters[account], "KamaToken: account is already minter");
        _minters[account] = true;
        emit MinterAdded(account);
    }

    function removeMinter(address account) public onlyOwner {
        require(_minters[account], "KamaToken: account is not minter");
        _minters[account] = false;
        emit MinterRemoved(account);
    }

    function isMinter(address account) public view returns (bool) {
        return _minters[account];
    }

    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override whenNotPaused {
        require(!_frozenAccounts[from], "KamaToken: sender account is frozen");
        require(!_frozenAccounts[to], "KamaToken: recipient account is frozen");
        super._beforeTokenTransfer(from, to, amount);
    }
}
```
