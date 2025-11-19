"""
Generated Code Metadata:
========================
Original URL: https://ziber.io
Prompt: Write code in Solidity to freeze 10% of Ziber tokens for one year, ensuring they cannot be withdrawn or sold during this period. Include logic to demonstrate long-range goals to ICO investors.
Generated: DETERMINISTIC_e4b3974014314a9c
Batch ID: 20250612_151531
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
 * @title ZiberToken
 * @author [Your Name]
 * @notice Ziber token contract with token freezing functionality
 */
contract ZiberToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of frozen token balances
    mapping(address => uint256) public frozenBalances;

    // Mapping of frozen token expiration timestamps
    mapping(address => uint256) public frozenExpirationTimestamps;

    // Percentage of tokens to freeze (10%)
    uint256 public constant FREEZE_PERCENTAGE = 10;

    // Duration of freeze in seconds (1 year)
    uint256 public constant FREEZE_DURATION = 365 days;

    // Timestamp when ICO ended
    uint256 public icoEndTimestamp;

    /**
     * @notice Constructor
     * @param initialSupply Initial supply of tokens
     */
    constructor(uint256 initialSupply) ERC20("Ziber", "ZBR") {
        _mint(msg.sender, initialSupply);

        // Set ICO end timestamp
        icoEndTimestamp = block.timestamp;
    }

    /**
     * @notice Freeze tokens for an address
     * @param _address Address to freeze tokens for
     */
    function freezeTokens(address _address) public onlyOwner {
        require(icoEndTimestamp > 0, "ICO has not ended");
        require(frozenExpirationTimestamps[_address] == 0, "Tokens are already frozen");

        uint256 balance = balanceOf(_address);
        uint256 freezeAmount = balance.mul(FREEZE_PERCENTAGE).div(100);

        // Update frozen balance and expiration timestamp
        frozenBalances[_address] = freezeAmount;
        frozenExpirationTimestamps[_address] = icoEndTimestamp.add(FREEZE_DURATION);

        // Burn frozen tokens from circulating supply
        _burn(_address, freezeAmount);
    }

    /**
     * @notice Unfreeze tokens for an address
     * @param _address Address to unfreeze tokens for
     */
    function unfreezeTokens(address _address) public onlyOwner {
        require(frozenExpirationTimestamps[_address] > 0, "Tokens are not frozen");
        require(frozenExpirationTimestamps[_address] <= block.timestamp, "Tokens are still frozen");

        uint256 frozenBalance = frozenBalances[_address];

        // Update frozen balance and expiration timestamp
        frozenBalances[_address] = 0;
        frozenExpirationTimestamps[_address] = 0;

        // Mint unfrozen tokens back to circulating supply
        _mint(_address, frozenBalance);
    }

    /**
     * @notice Override transfer function to prevent transfer of frozen tokens
     * @param from Sender address
     * @param to Recipient address
     * @param amount Amount to transfer
     * @return bool Success
     */
    function transfer(address from, address to, uint256 amount) public override nonReentrant returns (bool) {
        require(frozenExpirationTimestamps[from] == 0 || block.timestamp > frozenExpirationTimestamps[from], "Tokens are still frozen");

        return super.transfer(from, to, amount);
    }

    /**
     * @notice Override transferFrom function to prevent transfer of frozen tokens
     * @param from Sender address
     * @param to Recipient address
     * @param amount Amount to transfer
     * @return bool Success
     */
    function transferFrom(
        address from,
        address to,
        uint256 amount
    ) public override nonReentrant returns (bool) {
        require(frozenExpirationTimestamps[from] == 0 || block.timestamp > frozenExpirationTimestamps[from], "Tokens are still frozen");

        return super.transferFrom(from, to, amount);
    }

    /**
     * @notice Override burn function to prevent burning of frozen tokens
     * @param amount Amount to burn
     */
    function burn(uint256 amount) public override nonReentrant {
        require(frozenExpirationTimestamps[msg.sender] == 0 || block.timestamp > frozenExpirationTimestamps[msg.sender], "Tokens are still frozen");

        super.burn(amount);
    }
}
```
