"""
Generated Code Metadata:
========================
Original URL: https://basedshibainu-com.pages.dev
Prompt: Generate a Solidity smart contract example that renounces ownership and locks liquidity, similar to the Based Shiba Inu token contract.
Generated: DETERMINISTIC_49008a28c62722d1
Batch ID: 20250612_153401
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

contract BasedShibaInuToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    address private _owner;
    address private _liquidityLocker;
    bool private _liquidityLocked;
    uint256 private _totalSupply;

    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;

    /**
     * @dev Sets the owner of the contract.
     */
    constructor() ERC20("Based Shiba Inu", "BSHI") {
        _owner = msg.sender;
        _liquidityLocker = address(0);
        _liquidityLocked = false;
        _totalSupply = 1000000000 * 10**18; // 1 billion tokens
        _balances[msg.sender] = _totalSupply;
        emit Transfer(address(0), msg.sender, _totalSupply);
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
     * @dev Locks liquidity.
     * @param liquidityLocker The address that will lock liquidity.
     */
    function lockLiquidity(address liquidityLocker) public {
        require(msg.sender == _owner, "Only the owner can lock liquidity");
        require(!_liquidityLocked, "Liquidity is already locked");
        _liquidityLocker = liquidityLocker;
        _liquidityLocked = true;
    }

    /**
     * @dev Transfers tokens.
     * @param recipient The recipient of the tokens.
     * @param amount The amount of tokens to transfer.
     */
    function transfer(address recipient, uint256 amount) public override nonReentrant returns (bool) {
        require(!_liquidityLocked || msg.sender == _liquidityLocker, "Liquidity is locked");
        _balances[msg.sender] = _balances[msg.sender].sub(amount);
        _balances[recipient] = _balances[recipient].add(amount);
        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Transfers tokens from one address to another.
     * @param sender The sender of the tokens.
     * @param recipient The recipient of the tokens.
     * @param amount The amount of tokens to transfer.
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override nonReentrant returns (bool) {
        require(!_liquidityLocked || msg.sender == _liquidityLocker, "Liquidity is locked");
        _allowances[sender][msg.sender] = _allowances[sender][msg.sender].sub(amount);
        _balances[sender] = _balances[sender].sub(amount);
        _balances[recipient] = _balances[recipient].add(amount);
        emit Transfer(sender, recipient, amount);
        return true;
    }

    /**
     * @dev Burns tokens.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) public override nonReentrant {
        require(!_liquidityLocked || msg.sender == _liquidityLocker, "Liquidity is locked");
        _balances[msg.sender] = _balances[msg.sender].sub(amount);
        _totalSupply = _totalSupply.sub(amount);
        emit Transfer(msg.sender, address(0), amount);
    }
}
```
