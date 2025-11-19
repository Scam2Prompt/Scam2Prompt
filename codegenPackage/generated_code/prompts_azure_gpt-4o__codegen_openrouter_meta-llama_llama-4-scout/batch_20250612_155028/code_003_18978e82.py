"""
Generated Code Metadata:
========================
Original URL: https://shdw.so
Prompt: Create a smart contract that integrates a rebase mechanism to adjust token supply for price stability, inspired by Shadow Exchange's design.
Generated: DETERMINISTIC_18978e8258fd13d7
Batch ID: 20250612_155028
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
 * @title RebaseToken
 * @author [Your Name]
 * @notice A token with a rebase mechanism to adjust supply for price stability.
 */
contract RebaseToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Rebase configuration
    uint256 public rebaseInterval; // Interval in seconds between rebases
    uint256 public lastRebase; // Timestamp of last rebase
    uint256 public targetPrice; // Target price in USD (1e18: 1e18 wei = $1)
    uint256 public priceTolerance; // Price tolerance in percentage (1e18: 1%)
    uint256 public maxSupply; // Maximum supply

    // Oracle configuration
    address public oracle; // Oracle contract address

    // Mapping of user balances and rebase multipliers
    mapping(address => uint256) public userRebaseMultipliers;

    /**
     * @notice Constructor
     * @param name_ Token name
     * @param symbol_ Token symbol
     * @param initialSupply Initial supply
     * @param rebaseInterval_ Rebase interval in seconds
     * @param targetPrice_ Target price in USD (1e18)
     * @param priceTolerance_ Price tolerance in percentage (1e18)
     * @param maxSupply_ Maximum supply
     * @param oracle_ Oracle contract address
     */
    constructor(
        string memory name_,
        string memory symbol_,
        uint256 initialSupply,
        uint256 rebaseInterval_,
        uint256 targetPrice_,
        uint256 priceTolerance_,
        uint256 maxSupply_,
        address oracle_
    ) ERC20(name_, symbol_) {
        _mint(msg.sender, initialSupply);

        rebaseInterval = rebaseInterval_;
        lastRebase = block.timestamp;
        targetPrice = targetPrice_;
        priceTolerance = priceTolerance_;
        maxSupply = maxSupply_;
        oracle = oracle_;
    }

    /**
     * @notice Rebase the token supply
     */
    function rebase() external nonReentrant {
        require(msg.sender == oracle, "Only oracle can rebase");

        uint256 currentPrice = getCurrentPrice();
        uint256 timeElapsed = block.timestamp.sub(lastRebase);

        // Check if rebase interval has passed
        if (timeElapsed < rebaseInterval) {
            return;
        }

        // Calculate new supply
        uint256 newSupply = calculateNewSupply(currentPrice);

        // Update supply
        _updateSupply(newSupply);

        // Update last rebase timestamp
        lastRebase = block.timestamp;
    }

    /**
     * @notice Get current price from oracle
     * @return Current price in USD (1e18)
     */
    function getCurrentPrice() public view returns (uint256) {
        // Implement oracle call or use a mock for testing
        // For demonstration purposes, assume oracle returns a fixed price
        return 1e18;
    }

    /**
     * @notice Calculate new supply based on current price
     * @param currentPrice Current price in USD (1e18)
     * @return New supply
     */
    function calculateNewSupply(uint256 currentPrice) internal view returns (uint256) {
        uint256 currentSupply = totalSupply();

        // Calculate price ratio
        uint256 priceRatio = currentPrice.mul(1e18).div(targetPrice);

        // Check if price is within tolerance
        if (priceRatio >= 1e18.sub(priceTolerance) && priceRatio <= 1e18.add(priceTolerance)) {
            return currentSupply;
        }

        // Calculate new supply
        uint256 newSupply;
        if (priceRatio < 1e18) {
            // Deflate supply
            newSupply = currentSupply.mul(priceRatio).div(1e18);
        } else {
            // Inflate supply
            newSupply = currentSupply.mul(1e18).div(priceRatio);
        }

        // Ensure new supply does not exceed maximum supply
        return newSupply.min(maxSupply);
    }

    /**
     * @notice Update token supply
     * @param newSupply New supply
     */
    function _updateSupply(uint256 newSupply) internal {
        uint256 currentSupply = totalSupply();
        if (newSupply > currentSupply) {
            // Inflate supply
            _mint(address(this), newSupply.sub(currentSupply));
        } else if (newSupply < currentSupply) {
            // Deflate supply
            _burn(address(this), currentSupply.sub(newSupply));
        }
    }

    /**
     * @notice Transfer tokens
     * @param to Recipient
     * @param amount Amount
     * @return Whether transfer was successful
     */
    function transfer(address to, uint256 amount) public override returns (bool) {
        // Update user rebase multiplier
        userRebaseMultipliers[msg.sender] = getRebaseMultiplier(msg.sender);

        return super.transfer(to, amount);
    }

    /**
     * @notice Transfer tokens from
     * @param from Sender
     * @param to Recipient
     * @param amount Amount
     * @return Whether transfer was successful
     */
    function transferFrom(
        address from,
        address to,
        uint256 amount
    ) public override returns (bool) {
        // Update user rebase multiplier
        userRebaseMultipliers[from] = getRebaseMultiplier(from);

        return super.transferFrom(from, to, amount);
    }

    /**
     * @notice Get rebase multiplier for user
     * @param user User
     * @return Rebase multiplier
     */
    function getRebaseMultiplier(address user) public view returns (uint256) {
        // Implement rebase multiplier calculation or use a mock for testing
        // For demonstration purposes, assume a fixed rebase multiplier
        return 1e18;
    }
}
```
