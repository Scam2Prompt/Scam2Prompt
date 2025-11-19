"""
Generated Code Metadata:
========================
Original URL: https://bibbydivs.com
Prompt: Develop a Solidity smart contract that implements a mechanism for redistributing exit fees to all token holders proportionally, as described on BibbyDivs.com.
Generated: DETERMINISTIC_d517a1b833662c40
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
 * @title BibbyDivs Token Contract
 * @author [Your Name]
 * @notice A token contract that redistributes exit fees to all token holders proportionally.
 */
contract BibbyDivsToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user balances and their corresponding dividend shares
    mapping(address => uint256) private _balances;
    mapping(address => uint256) private _dividendShares;

    // Total dividend shares
    uint256 private _totalDividendShares;

    // Exit fee percentage (in basis points)
    uint256 public exitFeePercentage;

    // Total exit fees collected
    uint256 private _totalExitFees;

    /**
     * @notice Constructor
     * @param name Token name
     * @param symbol Token symbol
     * @param initialSupply Initial token supply
     * @param exitFeePercentage Exit fee percentage (in basis points)
     */
    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply,
        uint256 exitFeePercentage_
    ) ERC20(name, symbol) {
        _mint(msg.sender, initialSupply);
        exitFeePercentage = exitFeePercentage_;
        _totalDividendShares = initialSupply;
        _balances[msg.sender] = initialSupply;
        _dividendShares[msg.sender] = initialSupply;
    }

    /**
     * @notice Transfer tokens and update dividend shares
     * @param to Recipient address
     * @param amount Amount to transfer
     * @return bool Success
     */
    override function transfer(address to, uint256 amount) public override nonReentrant returns (bool) {
        uint256 fee = amount.mul(exitFeePercentage).div(10000);
        uint256 netAmount = amount.sub(fee);

        // Update total exit fees
        _totalExitFees = _totalExitFees.add(fee);

        // Update dividend shares
        _updateDividendShares(msg.sender, _balances[msg.sender].sub(amount));
        _updateDividendShares(to, _balances[to].add(netAmount));

        // Perform transfer
        return super.transfer(to, netAmount);
    }

    /**
     * @notice Transfer tokens from one address to another and update dividend shares
     * @param from Sender address
     * @param to Recipient address
     * @param amount Amount to transfer
     * @return bool Success
     */
    override function transferFrom(
        address from,
        address to,
        uint256 amount
    ) public override nonReentrant returns (bool) {
        uint256 fee = amount.mul(exitFeePercentage).div(10000);
        uint256 netAmount = amount.sub(fee);

        // Update total exit fees
        _totalExitFees = _totalExitFees.add(fee);

        // Update dividend shares
        _updateDividendShares(from, _balances[from].sub(amount));
        _updateDividendShares(to, _balances[to].add(netAmount));

        // Perform transfer
        return super.transferFrom(from, to, netAmount);
    }

    /**
     * @notice Burn tokens and update dividend shares
     * @param amount Amount to burn
     */
    override function burn(uint256 amount) public override nonReentrant {
        // Update dividend shares
        _updateDividendShares(msg.sender, _balances[msg.sender].sub(amount));

        // Perform burn
        super.burn(amount);
    }

    /**
     * @notice Update dividend shares for an address
     * @param account Address to update
     * @param newBalance New balance
     */
    private function _updateDividendShares(address account, uint256 newBalance) internal {
        _totalDividendShares = _totalDividendShares.sub(_dividendShares[account]);
        _dividendShares[account] = newBalance;
        _totalDividendShares = _totalDividendShares.add(newBalance);
    }

    /**
     * @notice Get dividend share for an address
     * @param account Address to get dividend share for
     * @return uint256 Dividend share
     */
    function getDividendShare(address account) public view returns (uint256) {
        return _dividendShares[account];
    }

    /**
     * @notice Get total dividend shares
     * @return uint256 Total dividend shares
     */
    function getTotalDividendShares() public view returns (uint256) {
        return _totalDividendShares;
    }

    /**
     * @notice Get total exit fees collected
     * @return uint256 Total exit fees
     */
    function getTotalExitFees() public view returns (uint256) {
        return _totalExitFees;
    }

    /**
     * @notice Claim exit fees
     */
    function claimExitFees() public nonReentrant {
        uint256 claimableAmount = _totalExitFees.mul(_dividendShares[msg.sender]).div(_totalDividendShares);
        _totalExitFees = _totalExitFees.sub(claimableAmount);
        _balances[msg.sender] = _balances[msg.sender].add(claimableAmount);
        emit Transfer(address(this), msg.sender, claimableAmount);
    }
}
```
