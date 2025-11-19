"""
Generated Code Metadata:
========================
Original URL: https://bulldogito.pages.dev
Prompt: Create a Solidity function that locks a portion of the BDOGITO token supply for 10 years, ensuring compliance with the tokenomics strategy.
Generated: DETERMINISTIC_75677b2b5ed8eb07
Batch ID: 20250612_154239
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

/**
 * @title BDogitoToken
 * @author [Your Name]
 * @notice This contract represents the BDogito token, with functionality for locking a portion of its supply.
 */
contract BDogitoToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of addresses to their respective locked balances
    mapping(address => uint256) public lockedBalances;

    // Mapping of addresses to their respective lock expiration timestamps
    mapping(address => uint256) public lockExpirations;

    // Address of the token owner
    address public owner;

    /**
     * @notice Constructor for the BDogitoToken contract
     * @param _name The name of the token
     * @param _symbol The symbol of the token
     * @param _totalSupply The total supply of the token
     */
    constructor(string memory _name, string memory _symbol, uint256 _totalSupply) ERC20(_name, _symbol) {
        _mint(msg.sender, _totalSupply);
        owner = msg.sender;
    }

    /**
     * @notice Locks a portion of the token supply for 10 years
     * @param _amount The amount of tokens to lock
     * @dev Only callable by the token owner
     */
    function lockTokens(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount to lock must be greater than 0");
        require(balanceOf(owner) >= _amount, "Insufficient balance to lock");

        // Calculate the lock expiration timestamp (10 years from now)
        uint256 lockExpiration = block.timestamp.add(10 * 365 * 24 * 60 * 60);

        // Transfer tokens to a temporary locked balance
        _transfer(owner, address(this), _amount);

        // Update the locked balance and lock expiration for the owner
        lockedBalances[owner] = lockedBalances[owner].add(_amount);
        lockExpirations[owner] = lockExpiration;

        emit TokensLocked(owner, _amount, lockExpiration);
    }

    /**
     * @notice Unlocks tokens previously locked by the owner
     * @dev Only callable after the lock expiration timestamp
     */
    function unlockTokens() external {
        require(lockExpirations[msg.sender] != 0, "No locked tokens found");
        require(block.timestamp >= lockExpirations[msg.sender], "Tokens are still locked");

        // Retrieve the locked balance for the owner
        uint256 lockedBalance = lockedBalances[msg.sender];

        // Reset the locked balance and lock expiration
        lockedBalances[msg.sender] = 0;
        lockExpirations[msg.sender] = 0;

        // Transfer the unlocked tokens back to the owner
        _transfer(address(this), msg.sender, lockedBalance);

        emit TokensUnlocked(msg.sender, lockedBalance);
    }

    /**
     * @notice Modifier to restrict function calls to the token owner
     */
    modifier onlyOwner {
        require(msg.sender == owner, "Only the token owner can call this function");
        _;
    }

    /**
     * @notice Event emitted when tokens are locked
     * @param indexed _owner The address of the token owner
     * @param _amount The amount of tokens locked
     * @param _expiration The lock expiration timestamp
     */
    event TokensLocked(address indexed _owner, uint256 _amount, uint256 _expiration);

    /**
     * @notice Event emitted when tokens are unlocked
     * @param indexed _owner The address of the token owner
     * @param _amount The amount of tokens unlocked
     */
    event TokensUnlocked(address indexed _owner, uint256 _amount);
}
```
