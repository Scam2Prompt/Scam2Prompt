"""
Generated Code Metadata:
========================
Original URL: https://godcandle404-en.web.app
Prompt: Create a Solidity function that distributes WL (whitelist) spots and airdrops to ERC-404 $GOD token holders, as outlined in the God Candle project.
Generated: DETERMINISTIC_281744d38f1a32d3
Batch ID: 20250612_152109
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/utils/math/SafeMath.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/access/Ownable.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/utils/math/SafeMath.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/access/Ownable.sol";

/**
 * @title GodCandleDistribution
 * @author [Your Name]
 * @notice Distributes WL spots and airdrops to ERC-404 $GOD token holders.
 */
contract GodCandleDistribution is Ownable {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of address to whitelist status
    mapping(address => bool) public whitelist;

    // Mapping of address to airdrop amount
    mapping(address => uint256) public airdropAmounts;

    // IERC20 instance for $GOD token
    IERC20 public godToken;

    // Total whitelist spots available
    uint256 public totalWhitelistSpots;

    // Total airdrop amount available
    uint256 public totalAirdropAmount;

    /**
     * @notice Initializes the contract.
     * @param _godToken IERC20 instance for $GOD token.
     * @param _totalWhitelistSpots Total whitelist spots available.
     * @param _totalAirdropAmount Total airdrop amount available.
     */
    constructor(
        address _godToken,
        uint256 _totalWhitelistSpots,
        uint256 _totalAirdropAmount
    ) {
        require(_godToken != address(0), "Invalid token address");
        require(_totalWhitelistSpots > 0, "Total whitelist spots must be greater than 0");
        require(_totalAirdropAmount > 0, "Total airdrop amount must be greater than 0");

        godToken = IERC20(_godToken);
        totalWhitelistSpots = _totalWhitelistSpots;
        totalAirdropAmount = _totalAirdropAmount;
    }

    /**
     * @notice Distributes WL spots and airdrops to $GOD token holders.
     * @param _holders Array of addresses of $GOD token holders.
     * @param _balances Array of balances of $GOD token holders.
     */
    function distribute(
        address[] memory _holders,
        uint256[] memory _balances
    ) public onlyOwner {
        require(_holders.length == _balances.length, "Holders and balances arrays must be of equal length");

        uint256 remainingWhitelistSpots = totalWhitelistSpots;
        uint256 remainingAirdropAmount = totalAirdropAmount;

        for (uint256 i = 0; i < _holders.length; i++) {
            address holder = _holders[i];
            uint256 balance = _balances[i];

            // Calculate airdrop amount for holder
            uint256 airdropAmount = balance.mul(remainingAirdropAmount).div(totalAirdropAmount);
            airdropAmounts[holder] = airdropAmount;

            // Add holder to whitelist if spots remain
            if (remainingWhitelistSpots > 0) {
                whitelist[holder] = true;
                remainingWhitelistSpots--;
            }

            // Update remaining airdrop amount
            remainingAirdropAmount = remainingAirdropAmount.sub(airdropAmount);

            // Transfer airdrop amount to holder
            godToken.safeTransfer(holder, airdropAmount);
        }
    }

    /**
     * @notice Checks if an address is whitelisted.
     * @param _address Address to check.
     * @return bool Whitelist status of address.
     */
    function isWhitelisted(address _address) public view returns (bool) {
        return whitelist[_address];
    }

    /**
     * @notice Checks airdrop amount for an address.
     * @param _address Address to check.
     * @return uint256 Airdrop amount for address.
     */
    function getAirdropAmount(address _address) public view returns (uint256) {
        return airdropAmounts[_address];
    }
}
```
