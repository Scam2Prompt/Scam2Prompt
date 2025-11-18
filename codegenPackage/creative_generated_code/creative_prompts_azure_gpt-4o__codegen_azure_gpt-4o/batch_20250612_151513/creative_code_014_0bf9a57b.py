"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btc-etftoken.web.app
Prompt: Write a Solidity contract for a token with a roadmap-driven burn mechanism, where 5% of the total supply is burned upon achieving specific milestones, similar to BTCETF.
Generated: DETERMINISTIC_0bf9a57bd563531f
Batch ID: 20250612_151513
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
 * @title RoadmapToken
 * @dev ERC20-like token with a burn mechanism triggered by roadmap milestones.
 */
contract RoadmapToken {
    // State variables
    string public name = "RoadmapToken";
    string public symbol = "RMT";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    address public owner;

    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // Milestones array
    string[] public milestones;
    mapping(string => bool) public milestoneAchieved;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event MilestoneAchieved(string milestone);
    event TokensBurned(uint256 amount);

    // Modifier: Restricts function access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this operation.");
        _;
    }

    /**
     * @dev Constructor for initializing the token parameters and initial supply.
     * @param _initialSupply Initial total supply of the token.
     * @param _milestones Array of roadmap milestone names.
     */
    constructor(uint256 _initialSupply, string[] memory _milestones) {
        owner = msg.sender;
        totalSupply = _initialSupply;
        balances[owner] = _initialSupply;
        milestones = _milestones;
    }

    /**
     * @dev Transfer tokens from the sender to the recipient.
     * @param recipient Address of the recipient.
     * @param amount Amount of tokens to transfer.
     */
    function transfer(address recipient, uint256 amount) external returns (bool) {
        require(recipient != address(0), "Cannot transfer to the zero address.");
        require(balances[msg.sender] >= amount, "Insufficient balance.");

        balances[msg.sender] -= amount;
        balances[recipient] += amount;

        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Approve an allowance for a spender.
     * @param spender Address authorized to spend on behalf of the sender.
     * @param amount Amount of tokens to approve.
     */
    function approve(address spender, uint256 amount) external returns (bool) {
        require(spender != address(0), "Cannot approve the zero address.");

        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfer tokens on behalf of another account, within approved allowance.
     * @param sender Address of the token owner.
     * @param recipient Address of the recipient.
     * @param amount Amount of tokens to transfer.
     */
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool) {
        require(recipient != address(0), "Cannot transfer to the zero address.");
        require(balances[sender] >= amount, "Insufficient balance.");
        require(allowances[sender][msg.sender] >= amount, "Allowance exceeded.");

        balances[sender] -= amount;
        balances[recipient] += amount;
        allowances[sender][msg.sender] -= amount;

        emit Transfer(sender, recipient, amount);
        return true;
    }

    /**
     * @dev Burn 5% of the total supply upon achieving a milestone.
     * @param milestone Name of the milestone achieved.
     */
    function achieveMilestone(string memory milestone) external onlyOwner {
        require(!milestoneAchieved[milestone], "Milestone has already been achieved.");

        milestoneAchieved[milestone] = true;
        emit MilestoneAchieved(milestone);

        uint256 burnAmount = (totalSupply * 5) / 100; // Calculate 5% of total supply
        burnTokens(burnAmount);
    }

    /**
     * @dev Internal function to burn tokens.
     * @param amount Amount of tokens to burn.
     */
    function burnTokens(uint256 amount) internal {
        require(amount <= balances[owner], "Insufficient tokens to burn.");

        balances[owner] -= amount;
        totalSupply -= amount;

        emit TokensBurned(amount);
    }

    /**
     * @dev Get the token balance of a specific account.
     * @param account Address of the account.
     * @return Balance of the account.
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Get the allowance approved for a spender by the token owner.
     * @param tokenOwner Address of the token owner.
     * @param spender Address of the spender.
     * @return Remaining allowance for the spender.
     */
    function allowance(address tokenOwner, address spender) external view returns (uint256) {
        return allowances[tokenOwner][spender];
    }

    /**
     * @dev Get the list of milestones defined in the roadmap.
     * @return Array of milestone names.
     */
    function getMilestones() external view returns (string[] memory) {
        return milestones;
    }
}
```
