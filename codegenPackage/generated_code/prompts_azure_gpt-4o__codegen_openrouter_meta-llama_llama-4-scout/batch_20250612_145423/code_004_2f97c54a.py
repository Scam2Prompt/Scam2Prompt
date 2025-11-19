"""
Generated Code Metadata:
========================
Original URL: https://flokidongerapp.com
Prompt: Write a smart contract in Solidity for FLOKIDONGER that ensures no buying or selling tax, renounced ownership, and passive token earnings functionality.
Generated: DETERMINISTIC_2f97c54a0f421d24
Batch ID: 20250612_145423
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract FLOKIDONGER is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    mapping(address => uint256) private _balances;
    mapping(address => uint256) private _passiveEarnings;

    uint256 private _totalSupply;
    uint256 private _totalPassiveEarnings;

    bool private _isPassiveEarningsEnabled;

    address private _owner;

    /**
     * @dev Sets the initial supply and the owner.
     */
    constructor() ERC20("FLOKIDONGER", "FDG") {
        _totalSupply = 1000000 * 10**18; // 1,000,000 tokens with 18 decimals
        _balances[msg.sender] = _totalSupply;
        _owner = msg.sender;
        emit Transfer(address(0), msg.sender, _totalSupply);

        // Initialize passive earnings
        _isPassiveEarningsEnabled = true;
    }

    /**
     * @dev Returns the owner of the contract.
     */
    function owner() public view returns (address) {
        return _owner;
    }

    /**
     * @dev Renounce ownership of the contract.
     */
    function renounceOwnership() public {
        require(msg.sender == _owner, "Only the owner can renounce ownership");
        _owner = address(0);
    }

    /**
     * @dev Enables or disables passive earnings.
     * @param enabled True to enable, false to disable.
     */
    function setPassiveEarningsEnabled(bool enabled) public {
        require(msg.sender == _owner, "Only the owner can set passive earnings enabled");
        _isPassiveEarningsEnabled = enabled;
    }

    /**
     * @dev Returns the passive earnings of an address.
     * @param account The address to query.
     */
    function getPassiveEarnings(address account) public view returns (uint256) {
        return _passiveEarnings[account];
    }

    /**
     * @dev Distributes passive earnings to all holders.
     * @param amount The amount of earnings to distribute.
     */
    function distributePassiveEarnings(uint256 amount) public {
        require(msg.sender == _owner, "Only the owner can distribute passive earnings");
        require(_isPassiveEarningsEnabled, "Passive earnings are not enabled");

        _totalPassiveEarnings = _totalPassiveEarnings.add(amount);

        uint256 totalSupply = totalSupply();
        for (address account in _balances) {
            uint256 earnings = _balances[account].mul(amount).div(totalSupply);
            _passiveEarnings[account] = _passiveEarnings[account].add(earnings);
        }
    }

    /**
     * @dev Claims passive earnings for an address.
     */
    function claimPassiveEarnings() public {
        uint256 earnings = _passiveEarnings[msg.sender];
        require(earnings > 0, "No passive earnings to claim");

        _passiveEarnings[msg.sender] = 0;
        _balances[msg.sender] = _balances[msg.sender].add(earnings);
        _totalPassiveEarnings = _totalPassiveEarnings.sub(earnings);

        emit Transfer(address(0), msg.sender, earnings);
    }

    /**
     * @dev See {ERC20-_beforeTokenTransfer}.
     */
    function _beforeTokenTransfer(address from, address to, uint256[] memory ids) internal override {
        // No buying or selling tax
    }

    /**
     * @dev See {ERC20-_transfer}.
     */
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        // No buying or selling tax
        super._transfer(sender, recipient, amount);
    }

    /**
     * @dev See {ERC20-_burn}.
     */
    function _burn(address account, uint256 amount) internal override {
        super._burn(account, amount);
    }

    /**
     * @dev See {ERC20-_approve}.
     */
    function _approve(address owner, address spender, uint256 amount) internal override {
        super._approve(owner, spender, amount);
    }
}
```
