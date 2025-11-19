"""
Generated Code Metadata:
========================
Original URL: https://docs.matrixinfos.com
Prompt: Generate a smart contract code for $MATRIX Token, incorporating principles of decentralization, privacy protection, and financial autonomy.
Generated: DETERMINISTIC_bbb85406cb18ea59
Batch ID: 20250622_211429
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Snapshot.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/draft-ERC20Permit.sol";

/**
 * @title MATRIX Token Contract
 * @dev Implementation of the $MATRIX token with decentralization, privacy, and financial autonomy features.
 */
contract MatrixToken is ERC20, Ownable, Pausable, ERC20Burnable, ERC20Snapshot, ERC20Permit {
    uint256 private constant INITIAL_SUPPLY = 1000000000 * 10**18; // 1 billion tokens with 18 decimals
    uint256 private constant MAX_TRANSACTION_LIMIT = 10000 * 10**18; // 10k tokens max per tx
    uint256 private constant COOLDOWN_PERIOD = 1 hours;

    mapping(address => bool) private _blacklisted;
    mapping(address => uint256) private _lastTransferTimestamp;
    mapping(address => bool) private _excludedFromLimits;

    event Blacklisted(address indexed account, bool isBlacklisted);
    event ExcludedFromLimits(address indexed account, bool isExcluded);

    /**
     * @dev Constructor that initializes the token contract.
     */
    constructor() ERC20("MATRIX Token", "MATRIX") ERC20Permit("MATRIX Token") {
        _mint(msg.sender, INITIAL_SUPPLY);
        _excludedFromLimits[msg.sender] = true;
    }

    /**
     * @dev Creates a new token snapshot.
     */
    function snapshot() public onlyOwner {
        _snapshot();
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
     * @dev Blacklists or unblacklists an address.
     * @param account Address to blacklist/unblacklist
     * @param isBlacklisted Boolean indicating blacklist status
     */
    function blacklist(address account, bool isBlacklisted) public onlyOwner {
        _blacklisted[account] = isBlacklisted;
        emit Blacklisted(account, isBlacklisted);
    }

    /**
     * @dev Excludes or includes an address from transaction limits.
     * @param account Address to exclude/include
     * @param isExcluded Boolean indicating exclusion status
     */
    function excludeFromLimits(address account, bool isExcluded) public onlyOwner {
        _excludedFromLimits[account] = isExcluded;
        emit ExcludedFromLimits(account, isExcluded);
    }

    /**
     * @dev Hook that is called before any transfer of tokens.
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override(ERC20, ERC20Snapshot) whenNotPaused {
        require(!_blacklisted[from] && !_blacklisted[to], "MATRIX: Blacklisted address");
        
        if (!_excludedFromLimits[from] && !_excludedFromLimits[to]) {
            require(amount <= MAX_TRANSACTION_LIMIT, "MATRIX: Exceeds max transaction limit");
            require(block.timestamp >= _lastTransferTimestamp[from] + COOLDOWN_PERIOD, "MATRIX: Cooldown period active");
        }

        super._beforeTokenTransfer(from, to, amount);
    }

    /**
     * @dev Hook that is called after any transfer of tokens.
     */
    function _afterTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override {
        if (!_excludedFromLimits[from]) {
            _lastTransferTimestamp[from] = block.timestamp;
        }
        super._afterTokenTransfer(from, to, amount);
    }

    /**
     * @dev Returns whether an address is blacklisted.
     * @param account Address to check
     * @return Boolean indicating blacklist status
     */
    function isBlacklisted(address account) public view returns (bool) {
        return _blacklisted[account];
    }

    /**
     * @dev Returns whether an address is excluded from limits.
     * @param account Address to check
     * @return Boolean indicating exclusion status
     */
    function isExcludedFromLimits(address account) public view returns (bool) {
        return _excludedFromLimits[account];
    }

    /**
     * @dev Returns the last transfer timestamp for an address.
     * @param account Address to check
     * @return Timestamp of last transfer
     */
    function getLastTransferTimestamp(address account) public view returns (uint256) {
        return _lastTransferTimestamp[account];
    }
}
```
