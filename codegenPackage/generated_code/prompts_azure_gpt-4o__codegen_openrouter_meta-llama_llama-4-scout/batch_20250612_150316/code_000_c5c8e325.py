"""
Generated Code Metadata:
========================
Original URL: https://bibbydivs.com
Prompt: Write a smart contract in Solidity that implements a token investment system with a 2% entry fee, a 2% exit fee, and a dividend redistribution mechanism similar to the $BIBBY ecosystem described on BibbyDivs.com.
Generated: DETERMINISTIC_c5c8e32559171f7f
Batch ID: 20250612_150316
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
 * @title BibbyToken
 * @author [Your Name]
 * @notice A token investment system with entry and exit fees, and dividend redistribution.
 */
contract BibbyToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of addresses to their investment balances
    mapping(address => uint256) private _balances;
    // Mapping of addresses to their dividend shares
    mapping(address => uint256) private _dividendShares;
    // Total dividend pool
    uint256 private _dividendPool;
    // Total investment balance
    uint256 private _totalInvestment;
    // Entry fee (2%)
    uint256 private constant _entryFee = 200;
    // Exit fee (2%)
    uint256 private constant _exitFee = 200;
    // Dividend share per investment unit
    uint256 private _dividendSharePerUnit;

    /**
     * @notice Constructor
     * @param name Token name
     * @param symbol Token symbol
     */
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {
        _dividendSharePerUnit = 0;
        _totalInvestment = 0;
        _dividendPool = 0;
    }

    /**
     * @notice Invests in the token, deducting entry fee
     * @param amount Investment amount
     */
    function invest(uint256 amount) external nonReentrant {
        require(amount > 0, "Invalid investment amount");

        // Calculate entry fee
        uint256 entryFeeAmount = amount.mul(_entryFee).div(10000);
        uint256 netAmount = amount.sub(entryFeeAmount);

        // Update total investment and dividend shares
        _totalInvestment = _totalInvestment.add(netAmount);
        _balances[msg.sender] = _balances[msg.sender].add(netAmount);
        _dividendShares[msg.sender] = _dividendShares[msg.sender].add(netAmount);

        // Mint tokens to the investor
        _mint(msg.sender, netAmount);
    }

    /**
     * @notice Redeems tokens, deducting exit fee and redistributing dividend
     * @param amount Redemption amount
     */
    function redeem(uint256 amount) external nonReentrant {
        require(amount > 0, "Invalid redemption amount");
        require(_balances[msg.sender] >= amount, "Insufficient balance");

        // Calculate exit fee
        uint256 exitFeeAmount = amount.mul(_exitFee).div(10000);
        uint256 netAmount = amount.sub(exitFeeAmount);

        // Update total investment and dividend shares
        _totalInvestment = _totalInvestment.sub(amount);
        _balances[msg.sender] = _balances[msg.sender].sub(amount);
        _dividendShares[msg.sender] = _dividendShares[msg.sender].sub(amount);

        // Burn tokens from the redeemer
        _burn(msg.sender, amount);

        // Redistribute dividend
        uint256 dividend = _dividendPool.mul(_dividendShares[msg.sender]).div(_totalInvestment);
        _dividendPool = _dividendPool.sub(dividend);
        _balances[msg.sender] = _balances[msg.sender].add(netAmount.add(dividend));

        // Transfer net amount to the redeemer
        payable(msg.sender).transfer(netAmount.add(dividend));
    }

    /**
     * @notice Adds dividend to the pool
     * @param amount Dividend amount
     */
    function addDividend(uint256 amount) external {
        require(amount > 0, "Invalid dividend amount");

        // Update dividend pool
        _dividendPool = _dividendPool.add(amount);
    }

    /**
     * @notice Calculates dividend share per unit
     */
    function updateDividendSharePerUnit() internal {
        if (_totalInvestment > 0) {
            _dividendSharePerUnit = _dividendPool.div(_totalInvestment);
        } else {
            _dividendSharePerUnit = 0;
        }
    }

    /**
     * @notice Returns total investment balance
     * @return Total investment balance
     */
    function totalInvestment() external view returns (uint256) {
        return _totalInvestment;
    }

    /**
     * @notice Returns dividend pool
     * @return Dividend pool
     */
    function dividendPool() external view returns (uint256) {
        return _dividendPool;
    }

    /**
     * @notice Returns dividend share per unit
     * @return Dividend share per unit
     */
    function dividendSharePerUnit() external view returns (uint256) {
        return _dividendSharePerUnit;
    }
}
```
