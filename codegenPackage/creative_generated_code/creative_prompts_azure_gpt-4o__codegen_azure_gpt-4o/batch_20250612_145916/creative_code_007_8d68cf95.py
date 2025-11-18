"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tokenscreatorethpro.pages.dev
Prompt: Create a Solidity function that calculates and deducts a tax fee during token transactions, ensuring compatibility with the token creation process described on the Tokens Creator site.
Generated: DETERMINISTIC_8d68cf952efd29cd
Batch ID: 20250612_145916
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
 * @title TaxableToken
 * @dev A token contract that calculates and deducts a tax fee during token transactions.
 */
contract TaxableToken {
    // ERC20-like state variables
    string public name = "TaxableToken";
    string public symbol = "TAX";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping to store balances
    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;

    // Tax fee percentage (e.g., 2%)
    uint256 public taxFeePercentage = 2;

    // Address to collect tax fees
    address public taxCollector;

    // Events for token transfers and approvals
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    /**
     * @dev Constructor to initialize the token supply and tax collector address.
     */
    constructor(uint256 _initialSupply, address _taxCollector) {
        require(_taxCollector != address(0), "Tax collector address cannot be zero");
        totalSupply = _initialSupply * (10**uint256(decimals));
        balanceOf[msg.sender] = totalSupply;
        taxCollector = _taxCollector;
    }

    /**
     * @dev Internal function to handle transfers and deduct tax fees.
     */
    function _transfer(address _from, address _to, uint256 _value) internal {
        require(_from != address(0), "Sender address cannot be zero");
        require(_to != address(0), "Recipient address cannot be zero");
        require(balanceOf[_from] >= _value, "Insufficient balance");

        // Calculate the tax fee
        uint256 taxFee = (_value * taxFeePercentage) / 100;
        uint256 amountToRecipient = _value - taxFee;

        // Deduct balances
        balanceOf[_from] -= _value;
        balanceOf[_to] += amountToRecipient;
        balanceOf[taxCollector] += taxFee;

        // Emit the transfer event
        emit Transfer(_from, _to, amountToRecipient);
        emit Transfer(_from, taxCollector, taxFee);
    }

    /**
     * @dev Public function to transfer tokens with tax fee deduction.
     */
    function transfer(address _to, uint256 _value) public returns (bool success) {
        _transfer(msg.sender, _to, _value);
        return true;
    }

    /**
     * @dev Public function to approve allowance for a spender.
     */
    function approve(address _spender, uint256 _value) public returns (bool success) {
        allowance[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    /**
     * @dev Public function to transfer tokens from an approved allowance.
     */
    function transferFrom(
        address _from,
        address _to,
        uint256 _value
    ) public returns (bool success) {
        require(allowance[_from][msg.sender] >= _value, "Allowance exceeded");
        allowance[_from][msg.sender] -= _value;
        _transfer(_from, _to, _value);
        return true;
    }
}
```
