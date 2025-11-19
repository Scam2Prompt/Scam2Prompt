"""
Generated Code Metadata:
========================
Original URL: https://btceftoken.pages.dev
Prompt: Generate a smart contract in Solidity for an ERC-20 token with a burn mechanism similar to the one described for BTCETF, where 5% of the token supply is burned at specific milestones.
Generated: DETERMINISTIC_5b121bf26a129b7b
Batch ID: 20250622_204830
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

/**
 * @title ERC-20 Token with Burn Mechanism
 * @dev Implementation of an ERC-20 token with a burn mechanism that burns 5% of the total supply at specific milestones.
 */
contract BurnableToken {
    // Token details
    string public name = "BurnableToken";
    string public symbol = "BURN";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping to track balances
    mapping(address => uint256) public balanceOf;

    // Mapping to track allowances
    mapping(address => mapping(address => uint256)) public allowance;

    // Milestones for burning
    uint256[] public burnMilestones;
    uint256 public nextMilestoneIndex = 0;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Burn(uint256 amount);

    // Constructor to initialize the token
    constructor(uint256 _initialSupply, uint256[] memory _burnMilestones) {
        require(_initialSupply > 0, "Initial supply must be greater than zero");
        require(_burnMilestones.length > 0, "Burn milestones must be provided");

        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balanceOf[msg.sender] = totalSupply;
        burnMilestones = _burnMilestones;

        emit Transfer(address(0), msg.sender, totalSupply);
    }

    /**
     * @dev Transfer tokens from sender to recipient.
     * @param _to Recipient address.
     * @param _value Amount to transfer.
     */
    function transfer(address _to, uint256 _value) external returns (bool) {
        require(_to != address(0), "Cannot transfer to the zero address");
        require(balanceOf[msg.sender] >= _value, "Insufficient balance");

        _checkAndBurn();

        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += _value;

        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    /**
     * @dev Approve a spender to spend tokens on behalf of the sender.
     * @param _spender Spender address.
     * @param _value Amount to approve.
     */
    function approve(address _spender, uint256 _value) external returns (bool) {
        require(_spender != address(0), "Cannot approve the zero address");

        allowance[msg.sender][_spender] = _value;

        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    /**
     * @dev Transfer tokens from one address to another using allowance.
     * @param _from Sender address.
     * @param _to Recipient address.
     * @param _value Amount to transfer.
     */
    function transferFrom(
        address _from,
        address _to,
        uint256 _value
    ) external returns (bool) {
        require(_to != address(0), "Cannot transfer to the zero address");
        require(balanceOf[_from] >= _value, "Insufficient balance");
        require(allowance[_from][msg.sender] >= _value, "Allowance exceeded");

        _checkAndBurn();

        balanceOf[_from] -= _value;
        balanceOf[_to] += _value;
        allowance[_from][msg.sender] -= _value;

        emit Transfer(_from, _to, _value);
        return true;
    }

    /**
     * @dev Internal function to check and burn tokens at milestones.
     */
    function _checkAndBurn() internal {
        if (
            nextMilestoneIndex < burnMilestones.length &&
            totalSupply <= burnMilestones[nextMilestoneIndex]
        ) {
            uint256 burnAmount = (totalSupply * 5) / 100; // Calculate 5% of total supply
            totalSupply -= burnAmount;

            emit Burn(burnAmount);

            nextMilestoneIndex++;
        }
    }
}
```
