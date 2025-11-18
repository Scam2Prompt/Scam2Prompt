"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bibbydivs.com
Prompt: Develop a Solidity smart contract that implements a mechanism for redistributing exit fees to all token holders proportionally, as described on BibbyDivs.com.
Generated: DETERMINISTIC_d517a1b833662c40
Batch ID: 20250612_150316
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// This contract defines a token that redistributes exit fees to all token holders proportionally.
contract BibbyDivs is IERC20, Ownable {
    string public name = "BibbyDivsToken";
    string public symbol = "BDT";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;

    uint256 public exitFeePercentage = 5; // Fee percentage to redistribute
    uint256 private constant FEE_DIVISOR = 100;

    event ExitFeePaid(address indexed from, uint256 amount);
    event ExitFeeRedistributed(uint256 totalFeeCollected);

    constructor(uint256 initialSupply) {
        totalSupply = initialSupply * 10 ** uint256(decimals);
        _balances[msg.sender] = totalSupply;
    }

    // ERC20 functions
    function balanceOf(address account) external view override returns (uint256) {
        return _balances[account];
    }

    function transfer(address recipient, uint256 amount) external override returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    function approve(address spender, uint256 amount) external override returns (bool) {
        _approve(msg.sender, spender, amount);
        return true;
    }

    function transferFrom(address sender, address recipient, uint256 amount) external override returns (bool) {
        _transfer(sender, recipient, amount);
        _approve(sender, msg.sender, _allowances[sender][msg.sender] - amount);
        return true;
    }

    function allowance(address owner, address spender) external view override returns (uint256) {
        return _allowances[owner][spender];
    }

    // Internal functions
    function _transfer(address sender, address recipient, uint256 amount) internal {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");
        require(amount <= _balances[sender], "ERC20: transfer amount exceeds balance");

        // Calculate exit fee
        uint256 exitFee = (amount * exitFeePercentage) / FEE_DIVISOR;
        uint256 amountAfterFee = amount - exitFee;

        // Update balances
        _balances[sender] -= amount;
        _balances[recipient] += amountAfterFee;

        // Redistribute exit fee
        _redistributeExitFee(exitFee);

        emit Transfer(sender, recipient, amountAfterFee);
    }

    function _approve(address owner, address spender, uint256 amount) internal {
        require(owner != address(0), "ERC20: approve from the zero address");
        require(spender != address(0), "ERC20: approve to the zero address");

        _allowances[owner][spender] = amount;
        emit Approval(owner, spender, amount);
    }

    function _redistributeExitFee(uint256 exitFee) internal {
        // Redistribute the exit fee to all token holders
        if (exitFee > 0) {
            uint256 totalHolders = 0;
            address[] memory holders = getAllHolders(); // Function to get all token holders
            for (uint256 i = 0; i < holders.length; i++) {
                totalHolders += _balances[holders[i]];
            }

            for (uint256 j = 0; j < holders.length; j++) {
                if (totalHolders > 0) {
                    uint256 holderShare = (exitFee * _balances[holders[j]]) / totalHolders;
                    _balances[holders[j]] += holderShare; // Distribute fee proportionally
                }
            }

            emit ExitFeeRedistributed(exitFee);
        }
    }

    function getAllHolders() internal view returns (address[] memory) {
        // This is a placeholder function.
        // In practice, you will need a way to track all token holders.
        // This could be implemented with an event log or a separate mapping.
        return new address[](0); // To be implemented
    }

    // Only owner can update exit fee percentage
    function setExitFeePercentage(uint256 newPercentage) external onlyOwner {
        require(newPercentage <= FEE_DIVISOR, "Exit fee must be less than or equal to 100%");
        exitFeePercentage = newPercentage;
    }
}
```
