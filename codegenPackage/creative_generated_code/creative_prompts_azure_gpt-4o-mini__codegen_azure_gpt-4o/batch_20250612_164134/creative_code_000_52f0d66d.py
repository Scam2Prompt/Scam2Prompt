"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mpeppe-ca.web.app
Prompt: Generate a smart contract for the $MPEPE token that includes a mechanism for burning tokens after each transaction, as described in the Mpeppe project details.
Generated: DETERMINISTIC_52f0d66d3a7cf17e
Batch ID: 20250612_164134
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
 * @title $MPEPE Token Contract
 * @dev ERC20 token with burn mechanism after every transaction.
 */
contract MPEPE {
    // Token details
    string public name = "$MPEPE";
    string public symbol = "MPEPE";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping to track balances
    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // Events for transparency
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Burn(address indexed from, uint256 value);

    // Owner address
    address public owner;

    // Burn percentage (e.g., 1% = 100 basis points)
    uint256 public burnPercentageBasisPoints = 100; // Default: 1%

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    // Constructor to initialize the contract
    constructor(uint256 _initialSupply) {
        owner = msg.sender;
        totalSupply = _initialSupply * 10 ** uint256(decimals);
        balances[owner] = totalSupply;

        emit Transfer(address(0), owner, totalSupply);
    }

    /**
     * @dev Get the balance of an account.
     * @param _account The address of the account.
     * @return The balance of the account.
     */
    function balanceOf(address _account) public view returns (uint256) {
        return balances[_account];
    }

    /**
     * @dev Transfer tokens to another account.
     * @param _to Recipient address.
     * @param _value Amount of tokens to transfer.
     * @return True if transfer was successful.
     */
    function transfer(address _to, uint256 _value) public returns (bool) {
        require(_to != address(0), "Cannot transfer to the zero address");
        require(balances[msg.sender] >= _value, "Insufficient balance");

        uint256 burnAmount = (_value * burnPercentageBasisPoints) / 10000; // Calculate burn amount
        uint256 transferAmount = _value - burnAmount; // Calculate transfer amount

        // Update balances
        balances[msg.sender] -= _value;
        balances[_to] += transferAmount;
        totalSupply -= burnAmount; // Reduce total supply

        // Emit events for transparency
        emit Transfer(msg.sender, _to, transferAmount);
        emit Burn(msg.sender, burnAmount);

        return true;
    }

    /**
     * @dev Approve another address to spend tokens on your behalf.
     * @param _spender Address allowed to spend.
     * @param _value Amount of tokens to approve.
     * @return True if approval was successful.
     */
    function approve(address _spender, uint256 _value) public returns (bool) {
        require(_spender != address(0), "Cannot approve the zero address");

        allowances[msg.sender][_spender] = _value;

        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    /**
     * @dev Transfer tokens via an approved allowance mechanism.
     * @param _from Address spending the tokens.
     * @param _to Recipient address.
     * @param _value Amount of tokens to transfer.
     * @return True if transfer was successful.
     */
    function transferFrom(
        address _from,
        address _to,
        uint256 _value
    ) public returns (bool) {
        require(_to != address(0), "Cannot transfer to the zero address");
        require(balances[_from] >= _value, "Insufficient balance");
        require(allowances[_from][msg.sender] >= _value, "Allowance exceeded");

        uint256 burnAmount = (_value * burnPercentageBasisPoints) / 10000; // Calculate burn amount
        uint256 transferAmount = _value - burnAmount; // Calculate transfer amount

        // Update balances and allowances
        balances[_from] -= _value;
        balances[_to] += transferAmount;
        allowances[_from][msg.sender] -= _value;
        totalSupply -= burnAmount; // Reduce total supply

        // Emit events for transparency
        emit Transfer(_from, _to, transferAmount);
        emit Burn(_from, burnAmount);

        return true;
    }

    /**
     * @dev Get the remaining allowance for a spender.
     * @param _owner Token owner address.
     * @param _spender Spender address.
     * @return Remaining allowance.
     */
    function allowance(address _owner, address _spender)
        public
        view
        returns (uint256)
    {
        return allowances[_owner][_spender];
    }

    /**
     * @dev Update the burn percentage (only owner).
     * @param _burnPercentageBasisPoints New burn percentage (basis points).
     */
    function setBurnPercentage(uint256 _burnPercentageBasisPoints)
        public
        onlyOwner
    {
        require(
            _burnPercentageBasisPoints <= 1000,
            "Burn percentage cannot exceed 10%"
        );
        burnPercentageBasisPoints = _burnPercentageBasisPoints;
    }
}
```
