"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mogcoin2.pages.dev
Prompt: Generate Solidity code for an ERC-20 token contract that mimics the features of $MOG, including tokenized winning and cultural branding.
Generated: DETERMINISTIC_5f1f651f405a3c37
Batch ID: 20250612_153648
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
 * @title MOGToken
 * @dev ERC-20 Token Implementation with cultural branding and tokenized winning
 */
contract MOGToken {
    // Token details
    string public constant name = "MOGToken";
    string public constant symbol = "MOG";
    uint8 public constant decimals = 18;
    uint256 public totalSupply;

    // Mapping to store balances of addresses
    mapping(address => uint256) private balances;

    // Mapping to store allowances
    mapping(address => mapping(address => uint256)) private allowances;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Cultural branding and winning logic
    address public culturalTreasury; // Address of the cultural treasury

    // Modifier to restrict access to culturalTreasury
    modifier onlyCulturalTreasury() {
        require(msg.sender == culturalTreasury, "Caller is not the cultural treasury");
        _;
    }

    /**
     * @dev Constructor to initialize token supply and cultural treasury
     * @param _initialSupply Initial supply of tokens
     * @param _culturalTreasury Address of the cultural treasury
     */
    constructor(uint256 _initialSupply, address _culturalTreasury) {
        require(_culturalTreasury != address(0), "Invalid cultural treasury address");

        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balances[msg.sender] = totalSupply;
        culturalTreasury = _culturalTreasury;

        emit Transfer(address(0), msg.sender, totalSupply);
    }

    /**
     * @dev Function to check balance of an address
     * @param _owner Address to fetch balance for
     * @return Balance of the address
     */
    function balanceOf(address _owner) public view returns (uint256) {
        return balances[_owner];
    }

    /**
     * @dev Function to transfer tokens
     * @param _to Recipient address
     * @param _value Amount to transfer
     * @return Success status
     */
    function transfer(address _to, uint256 _value) public returns (bool) {
        require(_to != address(0), "Transfer to zero address");
        require(balances[msg.sender] >= _value, "Insufficient balance");

        balances[msg.sender] -= _value;
        balances[_to] += _value;

        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    /**
     * @dev Function to approve tokens for spending by another address
     * @param _spender Address allowed to spend the tokens
     * @param _value Amount to approve
     * @return Success status
     */
    function approve(address _spender, uint256 _value) public returns (bool) {
        require(_spender != address(0), "Approve to zero address");

        allowances[msg.sender][_spender] = _value;

        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    /**
     * @dev Function to check allowance of a spender
     * @param _owner Owner of the tokens
     * @param _spender Address allowed to spend the tokens
     * @return Remaining allowance
     */
    function allowance(address _owner, address _spender) public view returns (uint256) {
        return allowances[_owner][_spender];
    }

    /**
     * @dev Function to transfer tokens on behalf of another address
     * @param _from Address to send tokens from
     * @param _to Recipient address
     * @param _value Amount to transfer
     * @return Success status
     */
    function transferFrom(address _from, address _to, uint256 _value) public returns (bool) {
        require(_to != address(0), "Transfer to zero address");
        require(balances[_from] >= _value, "Insufficient balance");
        require(allowances[_from][msg.sender] >= _value, "Allowance exceeded");

        balances[_from] -= _value;
        balances[_to] += _value;
        allowances[_from][msg.sender] -= _value;

        emit Transfer(_from, _to, _value);
        return true;
    }

    /**
     * @dev Function to distribute rewards to cultural branding initiatives
     * @param _recipient Address to receive rewards
     * @param _value Amount of rewards to distribute
     * @return Success status
     */
    function distributeRewards(address _recipient, uint256 _value) public onlyCulturalTreasury returns (bool) {
        require(_recipient != address(0), "Distribute to zero address");
        require(balances[culturalTreasury] >= _value, "Insufficient treasury balance");

        balances[culturalTreasury] -= _value;
        balances[_recipient] += _value;

        emit Transfer(culturalTreasury, _recipient, _value);
        return true;
    }
}
```
