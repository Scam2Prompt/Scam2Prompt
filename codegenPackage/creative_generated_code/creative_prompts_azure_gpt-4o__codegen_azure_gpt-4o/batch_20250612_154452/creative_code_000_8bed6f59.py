"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://growbit.tech
Prompt: Write a smart contract in Solidity for a token similar to GrowBTC, ensuring it includes features like capped supply, token locking for a specified duration, and interoperability with other blockchains.
Generated: DETERMINISTIC_8bed6f59cdc5cb5f
Batch ID: 20250612_154452
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

/**
 * @title GrowBTC-like Token
 * @dev ERC20 token with capped supply, token locking functionality, and interoperability features.
 */
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Capped.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract GrowBTC is ERC20, ERC20Capped, Ownable {
    // Mapping to store locked tokens along with the unlock timestamps
    mapping(address => uint256) private _lockedTokens;
    mapping(address => uint256) private _unlockTimes;

    // Interoperability mapping (e.g., for cross-chain bridge)
    mapping(address => bool) private _approvedInteroperableAddresses;

    // Event for token locking
    event TokensLocked(address indexed account, uint256 amount, uint256 unlockTime);

    // Event for interoperability approval
    event InteroperableAddressAdded(address indexed account);
    event InteroperableAddressRemoved(address indexed account);

    /**
     * @dev Constructor initializes token with a name, symbol, and capped supply.
     * @param name Token name.
     * @param symbol Token symbol.
     * @param cap Token supply cap.
     */
    constructor(string memory name, string memory symbol, uint256 cap)
        ERC20(name, symbol)
        ERC20Capped(cap)
    {}

    /**
     * @dev Overrides _mint to respect the cap.
     * @param account Address to mint tokens to.
     * @param amount Number of tokens to mint.
     */
    function _mint(address account, uint256 amount) internal override(ERC20, ERC20Capped) {
        super._mint(account, amount);
    }

    /**
     * @dev Allows the owner to mint new tokens (up to the cap).
     * @param account Address to receive the tokens.
     * @param amount Tokens to mint.
     */
    function mint(address account, uint256 amount) external onlyOwner {
        _mint(account, amount);
    }

    /**
     * @dev Locks tokens for the specified duration.
     * @param amount Number of tokens to lock.
     * @param duration Duration (in seconds) for which tokens will be locked.
     */
    function lockTokens(uint256 amount, uint256 duration) external {
        require(amount > 0, "Lock amount must be greater than 0");
        require(duration > 0, "Duration must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens to the contract
        _transfer(msg.sender, address(this), amount);

        // Update locked tokens and unlock time
        _lockedTokens[msg.sender] += amount;
        _unlockTimes[msg.sender] = block.timestamp + duration;

        emit TokensLocked(msg.sender, amount, block.timestamp + duration);
    }

    /**
     * @dev Unlocks the sender's locked tokens after the duration has passed.
     */
    function unlockTokens() external {
        require(_lockedTokens[msg.sender] > 0, "No tokens to unlock");
        require(block.timestamp >= _unlockTimes[msg.sender], "Tokens are still locked");

        uint256 amount = _lockedTokens[msg.sender];

        // Reset locked tokens and unlock time
        _lockedTokens[msg.sender] = 0;
        _unlockTimes[msg.sender] = 0;

        // Transfer tokens back to the sender
        _transfer(address(this), msg.sender, amount);
    }

    /**
     * @dev Adds an address as an approved interoperable address (e.g., for cross-chain functionality).
     * @param account Address to approve.
     */
    function addInteroperableAddress(address account) external onlyOwner {
        require(account != address(0), "Invalid address");
        _approvedInteroperableAddresses[account] = true;
        emit InteroperableAddressAdded(account);
    }

    /**
     * @dev Removes an address from the list of approved interoperable addresses.
     * @param account Address to remove.
     */
    function removeInteroperableAddress(address account) external onlyOwner {
        require(_approvedInteroperableAddresses[account], "Address not approved");
        _approvedInteroperableAddresses[account] = false;
        emit InteroperableAddressRemoved(account);
    }

    /**
     * @dev Checks if an address is approved for interoperability.
     * @param account Address to check.
     * @return bool True if the address is approved, false otherwise.
     */
    function isInteroperableAddress(address account) external view returns (bool) {
        return _approvedInteroperableAddresses[account];
    }

    /**
     * @dev Returns the locked tokens of a given account.
     * @param account Address to check.
     * @return uint256 Locked token balance.
     */
    function lockedTokens(address account) external view returns (uint256) {
        return _lockedTokens[account];
    }

    /**
     * @dev Returns the unlock time of locked tokens for a given account.
     * @param account Address to check.
     * @return uint256 Unlock timestamp.
     */
    function unlockTime(address account) external view returns (uint256) {
        return _unlockTimes[account];
    }
}
```
