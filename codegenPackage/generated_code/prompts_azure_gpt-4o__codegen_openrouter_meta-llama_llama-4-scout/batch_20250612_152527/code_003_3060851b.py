"""
Generated Code Metadata:
========================
Original URL: https://yooshi-io.pages.dev
Prompt: Generate a smart contract on Binance Smart Chain that implements a burning mechanism similar to YooShi's Black Hole algorithm, where a percentage of transaction fees is sent to a burn address.
Generated: DETERMINISTIC_3060851b89782dde
Batch ID: 20250612_152527
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
 * @title BlackHoleToken
 * @author [Your Name]
 * @notice A token with a burning mechanism similar to YooShi's Black Hole algorithm.
 */
contract BlackHoleToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Burn address
    address public constant BURN_ADDRESS = 0x0000000000000000000000000000000000000000;

    // Percentage of transaction fees to be burned
    uint256 public burnFeePercentage;

    /**
     * @notice Constructor
     * @param name Token name
     * @param symbol Token symbol
     * @param burnFeePercentage_ Percentage of transaction fees to be burned
     */
    constructor(string memory name, string memory symbol, uint256 burnFeePercentage_) ERC20(name, symbol) {
        burnFeePercentage = burnFeePercentage_;
    }

    /**
     * @notice Transfer function with burning mechanism
     * @param from Sender address
     * @param to Receiver address
     * @param amount Amount to transfer
     * @return bool Success
     */
    function transferFrom(address from, address to, uint256 amount) public override nonReentrant returns (bool) {
        uint256 fee = amount.mul(burnFeePercentage).div(100);
        uint256 netAmount = amount.sub(fee);

        _transfer(from, to, netAmount);

        // Burn fee
        _burn(from, fee);

        return true;
    }

    /**
     * @notice Transfer function with burning mechanism
     * @param to Receiver address
     * @param amount Amount to transfer
     * @return bool Success
     */
    function transfer(address to, uint256 amount) public override nonReentrant returns (bool) {
        uint256 fee = amount.mul(burnFeePercentage).div(100);
        uint256 netAmount = amount.sub(fee);

        _transfer(_msgSender(), to, netAmount);

        // Burn fee
        _burn(_msgSender(), fee);

        return true;
    }

    /**
     * @notice Approve function with no change
     */
    function approve(address spender, uint256 amount) public override returns (bool) {
        return super.approve(spender, amount);
    }

    /**
     * @notice Increase approval
     */
    function increaseAllowance(address spender, uint256 addedValue) public override returns (bool) {
        return super.increaseAllowance(spender, addedValue);
    }

    /**
     * @notice Decrease approval
     */
    function decreaseAllowance(address spender, uint256 subtractedValue) public override returns (bool) {
        return super.decreaseAllowance(spender, subtractedValue);
    }

    /**
     * @notice Allow a trusted operator to burn tokens on behalf of an owner.
     * @param account The account whose tokens are to be burned.
     * @param amount The amount of tokens to burn.
     */
    function burnFrom(address account, uint256 amount) public override {
        super.burnFrom(account, amount);
    }

    /**
     * @notice Internal transfer function
     * @param from Sender address
     * @param to Receiver address
     * @param amount Amount to transfer
     */
    function _transfer(address from, address to, uint256 amount) internal override {
        if (from == BURN_ADDRESS || to == BURN_ADDRESS) {
            // Prevent transferring to/from burn address
            revert("Invalid transfer address");
        }

        super._transfer(from, to, amount);
    }

    /**
     * @notice Internal burn function
     * @param account Account to burn from
     * @param amount Amount to burn
     */
    function _burn(address account, uint256 amount) internal override {
        super._burn(account, amount);

        // Send burned tokens to burn address
        _transfer(account, BURN_ADDRESS, amount);
    }
}
```
