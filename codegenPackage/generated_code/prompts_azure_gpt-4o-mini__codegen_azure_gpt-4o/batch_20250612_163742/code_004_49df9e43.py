"""
Generated Code Metadata:
========================
Original URL: https://gummy-b3j.pages.dev
Prompt: Illustrate how to set up a smart contract for $Gummy that incorporates the unique features of its tokenomics, including team and founder allocations.
Generated: DETERMINISTIC_49df9e43586a5d4d
Batch ID: 20250612_163742
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
 * @title GummyToken
 * @dev ERC20 token with custom tokenomics for team and founder allocations.
 */
contract GummyToken {
    // Token details
    string public name = "$Gummy";
    string public symbol = "GUMMY";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Address allocations
    address public teamWallet;
    address public founderWallet;

    // Tokenomics percentages
    uint256 public constant TEAM_ALLOCATION_PERCENT = 20; // 20% of total supply
    uint256 public constant FOUNDER_ALLOCATION_PERCENT = 10; // 10% of total supply

    // Balances mapping
    mapping(address => uint256) private balances;

    // Allowance mapping
    mapping(address => mapping(address => uint256)) private allowances;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    /**
     * @dev Constructor to initialize the token and distribute allocations.
     * @param _totalSupply The total supply of the token.
     * @param _teamWallet The wallet address for the team allocation.
     * @param _founderWallet The wallet address for the founder allocation.
     */
    constructor(
        uint256 _totalSupply,
        address _teamWallet,
        address _founderWallet
    ) {
        require(_teamWallet != address(0), "Team wallet cannot be zero address");
        require(_founderWallet != address(0), "Founder wallet cannot be zero address");

        totalSupply = _totalSupply;
        teamWallet = _teamWallet;
        founderWallet = _founderWallet;

        // Calculate allocations
        uint256 teamAllocation = (_totalSupply * TEAM_ALLOCATION_PERCENT) / 100;
        uint256 founderAllocation = (_totalSupply * FOUNDER_ALLOCATION_PERCENT) / 100;

        // Distribute allocations
        balances[teamWallet] = teamAllocation;
        balances[founderWallet] = founderAllocation;

        // Remaining supply goes to the contract deployer
        balances[msg.sender] = _totalSupply - teamAllocation - founderAllocation;

        emit Transfer(address(0), teamWallet, teamAllocation);
        emit Transfer(address(0), founderWallet, founderAllocation);
        emit Transfer(address(0), msg.sender, balances[msg.sender]);
    }

    /**
     * @dev Returns the balance of a given address.
     * @param account The address to query the balance of.
     * @return The balance of the address.
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfers tokens to a specified address.
     * @param to The address to transfer to.
     * @param amount The amount to transfer.
     * @return True if the transfer is successful.
     */
    function transfer(address to, uint256 amount) public returns (bool) {
        require(to != address(0), "Cannot transfer to zero address");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;
        balances[to] += amount;

        emit Transfer(msg.sender, to, amount);
        return true;
    }

    /**
     * @dev Approves a spender to transfer tokens on behalf of the caller.
     * @param spender The address authorized to spend.
     * @param amount The amount to approve.
     * @return True if the approval is successful.
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        require(spender != address(0), "Cannot approve zero address");

        allowances[msg.sender][spender] = amount;

        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfers tokens from one address to another using allowance.
     * @param from The address to transfer from.
     * @param to The address to transfer to.
     * @param amount The amount to transfer.
     * @return True if the transfer is successful.
     */
    function transferFrom(
        address from,
        address to,
        uint256 amount
    ) public returns (bool) {
        require(to != address(0), "Cannot transfer to zero address");
        require(balances[from] >= amount, "Insufficient balance");
        require(allowances[from][msg.sender] >= amount, "Allowance exceeded");

        balances[from] -= amount;
        balances[to] += amount;
        allowances[from][msg.sender] -= amount;

        emit Transfer(from, to, amount);
        return true;
    }

    /**
     * @dev Returns the remaining allowance for a spender.
     * @param owner The address of the token owner.
     * @param spender The address of the spender.
     * @return The remaining allowance.
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }
}
```
