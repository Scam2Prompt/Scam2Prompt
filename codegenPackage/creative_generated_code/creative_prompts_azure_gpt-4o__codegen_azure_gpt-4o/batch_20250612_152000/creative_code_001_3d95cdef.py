"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-beefmeme.pages.dev
Prompt: Using the BEEF Coin tokenomics model, write a Solidity function that implements a deflationary mechanism by burning a percentage of tokens during each transaction.
Generated: DETERMINISTIC_3d95cdef260a687a
Batch ID: 20250612_152000
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
 * @title BEEF Coin Token Contract
 * @dev Implements a deflationary mechanism by burning a percentage of tokens during each transfer.
 */
contract BeefCoin {
    string public name = "BeefCoin";
    string public symbol = "BEEF";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // Percentage of tokens to burn on each transfer (e.g., 2% burn mechanism)
    uint256 public burnRate = 2;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    /**
     * @dev Sets the initial supply and assigns it to the deployer.
     * @param _initialSupply The initial supply of tokens.
     */
    constructor(uint256 _initialSupply) {
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balances[msg.sender] = totalSupply;
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    /**
     * @dev Returns the balance of a specific address.
     * @param _account The address to query the balance of.
     */
    function balanceOf(address _account) public view returns (uint256) {
        return balances[_account];
    }

    /**
     * @dev Transfers tokens to a specified address with deflationary burning.
     * @param _to The recipient address.
     * @param _amount The amount of tokens to transfer.
     */
    function transfer(address _to, uint256 _amount) public returns (bool) {
        require(_to != address(0), "Cannot transfer to the zero address");
        require(balances[msg.sender] >= _amount, "Insufficient balance");

        // Calculate the burn amount
        uint256 burnAmount = (_amount * burnRate) / 100;
        uint256 transferAmount = _amount - burnAmount;

        // Update balances
        balances[msg.sender] -= _amount;
        balances[_to] += transferAmount;
        totalSupply -= burnAmount; // Reduce total supply by burn amount

        emit Transfer(msg.sender, _to, transferAmount);
        emit Transfer(msg.sender, address(0), burnAmount); // Burn event

        return true;
    }

    /**
     * @dev Approves an address to spend tokens on behalf of the caller.
     * @param _spender The address authorized to spend.
     * @param _amount The maximum amount they can spend.
     */
    function approve(address _spender, uint256 _amount) public returns (bool) {
        require(_spender != address(0), "Cannot approve to the zero address");

        allowances[msg.sender][_spender] = _amount;
        emit Approval(msg.sender, _spender, _amount);

        return true;
    }

    /**
     * @dev Transfers tokens on behalf of the owner with deflationary burning.
     * @param _from The address to transfer tokens from.
     * @param _to The recipient address.
     * @param _amount The amount of tokens to transfer.
     */
    function transferFrom(
        address _from,
        address _to,
        uint256 _amount
    ) public returns (bool) {
        require(_to != address(0), "Cannot transfer to the zero address");
        require(balances[_from] >= _amount, "Insufficient balance");
        require(allowances[_from][msg.sender] >= _amount, "Allowance exceeded");

        // Calculate the burn amount
        uint256 burnAmount = (_amount * burnRate) / 100;
        uint256 transferAmount = _amount - burnAmount;

        // Update balances and allowance
        balances[_from] -= _amount;
        balances[_to] += transferAmount;
        allowances[_from][msg.sender] -= _amount;
        totalSupply -= burnAmount; // Reduce total supply by burn amount

        emit Transfer(_from, _to, transferAmount);
        emit Transfer(_from, address(0), burnAmount); // Burn event

        return true;
    }

    /**
     * @dev Returns the remaining amount that a spender is allowed to transfer on behalf of the owner.
     * @param _owner The owner address.
     * @param _spender The spender's address.
     */
    function allowance(address _owner, address _spender) public view returns (uint256) {
        return allowances[_owner][_spender];
    }
}
```
