"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qudefi-ai.pages.dev
Prompt: Create a sample Solidity smart contract for the QuDefi token, ensuring it includes features for automated daily snapshots and eligibility criteria for rewards distribution.
Generated: DETERMINISTIC_5f2729fc9a3ff856
Batch ID: 20250612_163601
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
 * @title QuDefi Token Smart Contract
 * @dev Implements an ERC-20 token with daily snapshot functionality and rewards eligibility criteria.
 */
contract QuDefiToken {
    // ------------------------ ERC-20 Token Details ------------------------
    string public name = "QuDefi Token";
    string public symbol = "QDF";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // ------------------------ State Variables ------------------------
    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // Snapshot structure to record daily balances
    struct Snapshot {
        uint256 timestamp;
        uint256 balance;
    }

    mapping(address => Snapshot[]) private snapshots;

    // ------------------------ Events ------------------------
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event SnapshotRecorded(address indexed account, uint256 balance, uint256 timestamp);

    // ------------------------ Constructor ------------------------
    /**
     * @dev Initializes the total supply and assigns it to the deployer.
     * @param initialSupply The initial supply of the token.
     */
    constructor(uint256 initialSupply) {
        totalSupply = initialSupply;
        balances[msg.sender] = initialSupply;
        emit Transfer(address(0), msg.sender, initialSupply);
    }

    // ------------------------ ERC-20 Methods ------------------------
    /**
     * @dev Returns the balance of the specified account.
     * @param account The address of the account.
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfers tokens to the specified address.
     * @param recipient The address of the recipient.
     * @param amount The amount of tokens to transfer.
     */
    function transfer(address recipient, uint256 amount) public returns (bool) {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        require(recipient != address(0), "Invalid recipient address");

        balances[msg.sender] -= amount;
        balances[recipient] += amount;

        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Approves a spender to transfer up to the specified amount.
     * @param spender The address of the spender.
     * @param amount The amount to approve.
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        require(spender != address(0), "Invalid spender address");

        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfers tokens on behalf of the owner.
     * @param sender The address of the sender.
     * @param recipient The address of the recipient.
     * @param amount The amount of tokens to transfer.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public returns (bool) {
        require(allowances[sender][msg.sender] >= amount, "Allowance exceeded");
        require(balances[sender] >= amount, "Insufficient balance");
        require(recipient != address(0), "Invalid recipient address");

        allowances[sender][msg.sender] -= amount;
        balances[sender] -= amount;
        balances[recipient] += amount;

        emit Transfer(sender, recipient, amount);
        return true;
    }

    /**
     * @dev Returns the allowance of the spender for the specified owner.
     * @param owner The address of the owner.
     * @param spender The address of the spender.
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }

    // ------------------------ Snapshot Functionality ------------------------
    /**
     * @dev Records a daily snapshot of balances.
     * Called by token holders manually or via an automated off-chain process.
     */
    function recordSnapshot() public {
        uint256 currentBalance = balances[msg.sender];
        uint256 currentTime = block.timestamp;

        // Append snapshot data for the caller
        snapshots[msg.sender].push(Snapshot(currentTime, currentBalance));

        emit SnapshotRecorded(msg.sender, currentBalance, currentTime);
    }

    /**
     * @dev Returns all snapshots for a specific account.
     * @param account The address of the account.
     */
    function getSnapshots(address account) public view returns (Snapshot[] memory) {
        return snapshots[account];
    }

    // ------------------------ Rewards Eligibility ------------------------
    /**
     * @dev Determines eligibility for rewards based on account balance and snapshot history.
     * @param account The address of the account.
     */
    function isEligibleForRewards(address account) public view returns (bool) {
        Snapshot[] memory accountSnapshots = snapshots[account];
        if (accountSnapshots.length == 0) {
            return false; // No snapshots available
        }

        // Example criteria: must have at least one snapshot with a balance > 1000 tokens
        for (uint256 i = 0; i < accountSnapshots.length; i++) {
            if (accountSnapshots[i].balance > 1000 * (10 ** decimals)) {
                return true;
            }
        }

        return false;
    }
}
```
