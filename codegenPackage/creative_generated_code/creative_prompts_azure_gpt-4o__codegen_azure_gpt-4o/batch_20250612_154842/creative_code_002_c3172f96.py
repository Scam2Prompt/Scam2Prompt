"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ondofoundaktion.org
Prompt: Generate code to deploy a governance token for a DAO, modeled after the ONDO token, with voting rights tied to decisions about lending protocols like Flux Finance.
Generated: DETERMINISTIC_c3172f9668088154
Batch ID: 20250612_154842
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
 * @title Governance Token for DAO
 * @dev ERC20 token with voting rights tied to DAO decisions on lending protocols.
 * Inspired by ONDO token functionality.
 */
contract GovernanceToken {
    // ERC20 token storage variables
    string public name = "Governance Token";
    string public symbol = "GOV";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping for balances and allowances
    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // Delegation structure for voting rights
    mapping(address => address) public delegates;
    mapping(address => uint256) public voteWeight;

    // Events for transparency
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event DelegateChanged(address indexed delegator, address indexed fromDelegate, address indexed toDelegate);
    event VoteWeightChanged(address indexed delegate, uint256 previousWeight, uint256 newWeight);

    // Modifier to check for sufficient balance
    modifier hasEnoughBalance(address account, uint256 amount) {
        require(balances[account] >= amount, "Insufficient balance");
        _;
    }

    // Constructor initializes the total supply and assigns it to the deployer
    constructor(uint256 _initialSupply) {
        totalSupply = _initialSupply * (10 ** decimals);
        balances[msg.sender] = totalSupply;
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    /**
     * @dev Transfer tokens to a recipient.
     * @param recipient The address to send tokens to.
     * @param amount The amount of tokens to send.
     */
    function transfer(address recipient, uint256 amount) external hasEnoughBalance(msg.sender, amount) returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Approve a spender to use your tokens.
     * @param spender The address to approve.
     * @param amount The amount to approve.
     */
    function approve(address spender, uint256 amount) external returns (bool) {
        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfer tokens on behalf of an owner.
     * @param sender The account to transfer from.
     * @param recipient The account to transfer to.
     * @param amount The amount to transfer.
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external hasEnoughBalance(sender, amount) returns (bool) {
        require(allowances[sender][msg.sender] >= amount, "Allowance exceeded");
        allowances[sender][msg.sender] -= amount;
        _transfer(sender, recipient, amount);
        return true;
    }

    /**
     * @dev Internal function to handle transfers.
     * @param sender The account sending tokens.
     * @param recipient The account receiving tokens.
     * @param amount The amount of tokens to transfer.
     */
    function _transfer(address sender, address recipient, uint256 amount) internal {
        balances[sender] -= amount;
        balances[recipient] += amount;
        emit Transfer(sender, recipient, amount);
        _moveDelegates(sender, recipient, amount);
    }

    /**
     * @dev Delegate voting rights to another address.
     * @param delegatee The address to delegate to.
     */
    function delegate(address delegatee) external {
        address currentDelegate = delegates[msg.sender];
        uint256 delegatorBalance = balances[msg.sender];
        delegates[msg.sender] = delegatee;

        emit DelegateChanged(msg.sender, currentDelegate, delegatee);
        _moveDelegates(currentDelegate, delegatee, delegatorBalance);
    }

    /**
     * @dev Internal function to move voting rights between delegates.
     * @param from The address to move votes from.
     * @param to The address to move votes to.
     * @param amount The amount of votes to move.
     */
    function _moveDelegates(
        address from,
        address to,
        uint256 amount
    ) internal {
        if (from != address(0)) {
            uint256 previousWeight = voteWeight[from];
            voteWeight[from] -= amount;
            emit VoteWeightChanged(from, previousWeight, voteWeight[from]);
        }

        if (to != address(0)) {
            uint256 previousWeight = voteWeight[to];
            voteWeight[to] += amount;
            emit VoteWeightChanged(to, previousWeight, voteWeight[to]);
        }
    }

    /**
     * @dev Returns the balance of an address.
     * @param account The address to query.
     * @return The balance of the address.
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Returns the allowance of a spender for an owner.
     * @param owner The address of the token owner.
     * @param spender The address of the token spender.
     * @return The remaining allowance.
     */
    function allowance(address owner, address spender) external view returns (uint256) {
        return allowances[owner][spender];
    }
}
```
