"""
Generated Code Metadata:
========================
Original URL: https://pepe20-io.web.app
Prompt: "Generate a Solidity contract for a token similar to Pepe 2.0 with a dev fee."
Generated: DETERMINISTIC_5ce529d2e46b3359
Batch ID: 20250622_205025
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
 * @title Pepe2.0 Token Contract
 * @author [Your Name]
 * @notice A token contract similar to Pepe2.0 with a dev fee.
 */
contract Pepe2Token is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of addresses to their respective balances
    mapping(address => uint256) private _balances;

    // Mapping of addresses to their respective allowances
    mapping(address => mapping(address => uint256)) private _allowances;

    // Total supply of the token
    uint256 private _totalSupply;

    // Development fee (5% by default)
    uint256 public devFee;

    // Address of the developer
    address public devAddress;

    /**
     * @notice Constructor for the Pepe2Token contract
     * @param name_ Name of the token
     * @param symbol_ Symbol of the token
     * @param totalSupply_ Total supply of the token
     * @param devAddress_ Address of the developer
     * @param devFee_ Development fee (in percent)
     */
    constructor(
        string memory name_,
        string memory symbol_,
        uint256 totalSupply_,
        address devAddress_,
        uint256 devFee_
    ) ERC20(name_, symbol_) {
        require(devAddress_ != address(0), "Dev address cannot be zero");
        require(devFee_ >= 0 && devFee_ <= 100, "Dev fee must be between 0 and 100");

        _totalSupply = totalSupply_;
        _balances[msg.sender] = totalSupply_;

        devAddress = devAddress_;
        devFee = devFee_;
    }

    /**
     * @notice Returns the total supply of the token
     * @return uint256 Total supply
     */
    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
    }

    /**
     * @notice Returns the balance of an address
     * @param account Address to check
     * @return uint256 Balance of the address
     */
    function balanceOf(address account) public view override returns (uint256) {
        return _balances[account];
    }

    /**
     * @notice Transfers tokens from one address to another
     * @param recipient Address to transfer to
     * @param amount Amount to transfer
     * @return bool Success
     */
    function transfer(address recipient, uint256 amount) public override nonReentrant returns (bool) {
        uint256 fee = amount.mul(devFee).div(100);
        uint256 sendAmount = amount.sub(fee);

        _balances[msg.sender] = _balances[msg.sender].sub(amount);
        _balances[recipient] = _balances[recipient].add(sendAmount);
        _balances[devAddress] = _balances[devAddress].add(fee);

        emit Transfer(msg.sender, recipient, sendAmount);
        emit Transfer(msg.sender, devAddress, fee);

        return true;
    }

    /**
     * @notice Approves an address to spend tokens on behalf of another
     * @param spender Address to approve
     * @param amount Amount to approve
     * @return bool Success
     */
    function approve(address spender, uint256 amount) public override returns (bool) {
        _allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @notice Transfers tokens from one address to another on behalf of another
     * @param sender Address to transfer from
     * @param recipient Address to transfer to
     * @param amount Amount to transfer
     * @return bool Success
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override nonReentrant returns (bool) {
        uint256 currentAllowance = _allowances[sender][msg.sender];
        require(currentAllowance >= amount, "ERC20: transfer amount exceeds allowance");

        uint256 fee = amount.mul(devFee).div(100);
        uint256 sendAmount = amount.sub(fee);

        _balances[sender] = _balances[sender].sub(amount);
        _balances[recipient] = _balances[recipient].add(sendAmount);
        _balances[devAddress] = _balances[devAddress].add(fee);

        _allowances[sender][msg.sender] = currentAllowance.sub(amount);

        emit Transfer(sender, recipient, sendAmount);
        emit Transfer(sender, devAddress, fee);

        return true;
    }

    /**
     * @notice Burns tokens
     * @param amount Amount to burn
     */
    function burn(uint256 amount) public override {
        _balances[msg.sender] = _balances[msg.sender].sub(amount);
        _totalSupply = _totalSupply.sub(amount);

        emit Transfer(msg.sender, address(0), amount);
    }
}
```
