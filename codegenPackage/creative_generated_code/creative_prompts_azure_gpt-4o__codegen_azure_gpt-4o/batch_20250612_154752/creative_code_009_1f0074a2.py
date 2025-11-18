"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yetiouro.co
Prompt: Write a Solidity smart contract for token creation that includes mechanisms for community rewards and Play-to-Earn opportunities, as outlined in Yeti Ouro's tokenomics.
Generated: DETERMINISTIC_1f0074a2ee13f3f6
Batch ID: 20250612_154752
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
 * @title YetiOuroToken
 * @dev An ERC20 token with community rewards and Play-to-Earn mechanisms.
 */
contract YetiOuroToken {
    // ERC20 token variables
    string public name = "YetiOuroToken";
    string public symbol = "YOT";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping of account balances
    mapping(address => uint256) private balances;

    // Mapping for allowance tracking
    mapping(address => mapping(address => uint256)) private allowances;

    // Addresses for reward allocation
    address public communityRewardsPool;
    address public playToEarnPool;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Modifier for valid addresses
    modifier validAddress(address _address) {
        require(_address != address(0), "Invalid address");
        _;
    }

    /**
     * @dev Constructor sets the initial supply and allocates tokens to pools.
     * @param _initialSupply Total supply of the token.
     * @param _communityRewardsPool Address for community rewards allocation.
     * @param _playToEarnPool Address for Play-to-Earn allocation.
     */
    constructor(
        uint256 _initialSupply,
        address _communityRewardsPool,
        address _playToEarnPool
    ) validAddress(_communityRewardsPool) validAddress(_playToEarnPool) {
        totalSupply = _initialSupply;
        communityRewardsPool = _communityRewardsPool;
        playToEarnPool = _playToEarnPool;

        // Allocate 50% of the supply to community rewards
        uint256 communityAllocation = (_initialSupply * 50) / 100;
        balances[communityRewardsPool] = communityAllocation;

        // Allocate 50% of the supply to Play-to-Earn pool
        uint256 playToEarnAllocation = _initialSupply - communityAllocation;
        balances[playToEarnPool] = playToEarnAllocation;

        emit Transfer(address(0), communityRewardsPool, communityAllocation);
        emit Transfer(address(0), playToEarnPool, playToEarnAllocation);
    }

    /**
     * @dev Returns the balance of the given account.
     * @param account Address of the account.
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfers tokens to a specified address.
     * @param recipient Recipient address.
     * @param amount Amount to transfer.
     */
    function transfer(address recipient, uint256 amount) public validAddress(recipient) returns (bool) {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Transfers tokens internally (helper function).
     * @param sender Sender address.
     * @param recipient Recipient address.
     * @param amount Amount to transfer.
     */
    function _transfer(address sender, address recipient, uint256 amount) private {
        balances[sender] -= amount;
        balances[recipient] += amount;
        emit Transfer(sender, recipient, amount);
    }

    /**
     * @dev Approves a spender to transfer tokens on behalf of the sender.
     * @param spender Spender address.
     * @param amount Amount to approve.
     */
    function approve(address spender, uint256 amount) public validAddress(spender) returns (bool) {
        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfers tokens from one account to another on behalf of the owner.
     * @param sender Sender address.
     * @param recipient Recipient address.
     * @param amount Amount to transfer.
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public validAddress(recipient) returns (bool) {
        require(balances[sender] >= amount, "Insufficient balance");
        require(allowances[sender][msg.sender] >= amount, "Allowance exceeded");

        allowances[sender][msg.sender] -= amount;
        _transfer(sender, recipient, amount);
        return true;
    }

    /**
     * @dev Returns the remaining amount that a spender is allowed to spend on behalf of the owner.
     * @param owner Owner address.
     * @param spender Spender address.
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }
}
```
