"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iqratechpoint.pages.dev
Prompt: Create a Solidity smart contract that integrates gamification features for educational milestones, allowing users to earn IQRA Tokens upon completing specific tasks or quizzes.
Generated: DETERMINISTIC_cee9cd50cb5ad4c3
Batch ID: 20250612_151246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

/**
 * @title IQRA Token Gamification Contract
 * @dev A smart contract to reward users with IQRA Tokens for achieving educational milestones.
 */
contract IQRATokenGamification {
    // Token-related variables
    string public constant name = "IQRA Token";
    string public constant symbol = "IQRA";
    uint8 public constant decimals = 18;
    uint256 public totalSupply;

    // Owner of the contract
    address public owner;
    
    // Mapping of user addresses to their balances
    mapping(address => uint256) public balances;

    // Mapping to track completed milestones for each user
    mapping(address => mapping(string => bool)) public completedMilestones;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event MilestoneCompleted(address indexed user, string milestoneName, uint256 rewardAmount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function.");
        _;
    }

    modifier validAddress(address _addr) {
        require(_addr != address(0), "Invalid address.");
        _;
    }
    
    constructor(uint256 _initialSupply) {
        owner = msg.sender;
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balances[owner] = totalSupply; // Assign all tokens to the owner initially
    }

    /**
     * @dev Transfer IQRA Tokens between users.
     * @param _to The recipient address.
     * @param _amount The amount to transfer.
     */
    function transfer(address _to, uint256 _amount) public validAddress(_to) returns (bool) {
        require(balances[msg.sender] >= _amount, "Insufficient token balance.");
        balances[msg.sender] -= _amount;
        balances[_to] += _amount;
        emit Transfer(msg.sender, _to, _amount);
        return true;
    }

    /**
     * @dev Reward tokens for completing a milestone.
     * @param _user The user address to reward.
     * @param _milestoneName The name of the milestone completed.
     * @param _rewardAmount The amount of tokens to reward.
     */
    function rewardMilestone(address _user, string memory _milestoneName, uint256 _rewardAmount) 
        public 
        onlyOwner 
        validAddress(_user) 
    {
        require(!completedMilestones[_user][_milestoneName], "Milestone already completed.");
        require(balances[owner] >= _rewardAmount, "Insufficient reward tokens.");

        // Mark milestone as completed
        completedMilestones[_user][_milestoneName] = true;

        // Transfer reward tokens to the user
        balances[owner] -= _rewardAmount;
        balances[_user] += _rewardAmount;

        emit MilestoneCompleted(_user, _milestoneName, _rewardAmount);
    }

    /**
     * @dev Check if a user has completed a specific milestone.
     * @param _user The user address.
     * @param _milestoneName The name of the milestone.
     * @return True if the milestone is completed, false otherwise.
     */
    function isMilestoneCompleted(address _user, string memory _milestoneName) 
        public 
        view 
        validAddress(_user) 
        returns (bool) 
    {
        return completedMilestones[_user][_milestoneName];
    }

    /**
     * @dev Get the balance of a specific user.
     * @param _user The user's address.
     * @return The balance of IQRA Tokens.
     */
    function balanceOf(address _user) public view validAddress(_user) returns (uint256) {
        return balances[_user];
    }
}
```
