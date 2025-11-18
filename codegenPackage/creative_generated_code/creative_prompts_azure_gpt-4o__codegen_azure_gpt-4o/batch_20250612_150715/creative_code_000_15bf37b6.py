"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moxie.social
Prompt: Write a smart contract using the Moxie Protocol to create a Fan Token for a Farcaster channel, including programmatic rewards for followers' actions.
Generated: DETERMINISTIC_15bf37b6c864aa17
Batch ID: 20250612_150715
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
 * @title FanToken Contract for Farcaster Channel
 * @dev This contract uses the Moxie Protocol to create a Fan Token associated with a Farcaster channel.
 * Followers can earn programmatic rewards based on their actions, such as liking or reposting content.
 */
contract FanToken {
    // Token details
    string public constant name = "Farcaster Fan Token";
    string public constant symbol = "FFT";
    uint8 public constant decimals = 18;

    // Total supply of the token
    uint256 public totalSupply;

    // Mapping to track balances of each holder
    mapping(address => uint256) private balances;

    // Mapping to track authorized spenders
    mapping(address => mapping(address => uint256)) private allowances;

    // Address of the Farcaster channel owner
    address public immutable channelOwner;

    // Event emitted when tokens are transferred
    event Transfer(address indexed from, address indexed to, uint256 value);

    // Event emitted when allowances are updated
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Event emitted when a reward is granted to a follower
    event RewardGranted(address indexed follower, uint256 value, string action);

    // Modifier to restrict access to the channel owner
    modifier onlyChannelOwner() {
        require(msg.sender == channelOwner, "Only the channel owner can perform this action");
        _;
    }

    /**
     * @dev Constructor to initialize the token and set the channel owner.
     * @param _initialSupply Initial supply of the Fan Token.
     */
    constructor(uint256 _initialSupply) {
        channelOwner = msg.sender;
        totalSupply = _initialSupply;
        balances[channelOwner] = _initialSupply;

        emit Transfer(address(0), channelOwner, _initialSupply);
    }

    /**
     * @dev Gets the balance of a specific account.
     * @param account Address of the account.
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfers tokens from the sender to a recipient.
     * @param recipient Address of the recipient.
     * @param amount Amount of tokens to transfer.
     */
    function transfer(address recipient, uint256 amount) external returns (bool) {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        require(recipient != address(0), "Invalid recipient address");

        balances[msg.sender] -= amount;
        balances[recipient] += amount;

        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Approves a spender to transfer tokens on behalf of the sender.
     * @param spender Address of the spender.
     * @param amount Amount of tokens to approve.
     */
    function approve(address spender, uint256 amount) external returns (bool) {
        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfers tokens from one account to another on behalf of the sender.
     * @param sender Address of the sender.
     * @param recipient Address of the recipient.
     * @param amount Amount of tokens to transfer.
     */
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool) {
        require(balances[sender] >= amount, "Insufficient balance");
        require(allowances[sender][msg.sender] >= amount, "Allowance exceeded");
        require(recipient != address(0), "Invalid recipient address");

        balances[sender] -= amount;
        balances[recipient] += amount;
        allowances[sender][msg.sender] -= amount;

        emit Transfer(sender, recipient, amount);
        return true;
    }

    /**
     * @dev Grants a reward to a follower based on their action.
     * @param follower Address of the follower.
     * @param action Description of the action (e.g., "liked", "reposted").
     * @param rewardAmount Amount of tokens to reward.
     */
    function grantReward(address follower, string memory action, uint256 rewardAmount) external onlyChannelOwner {
        require(follower != address(0), "Invalid follower address");
        require(balances[channelOwner] >= rewardAmount, "Insufficient tokens for reward");

        balances[channelOwner] -= rewardAmount;
        balances[follower] += rewardAmount;

        emit RewardGranted(follower, rewardAmount, action);
        emit Transfer(channelOwner, follower, rewardAmount);
    }

    /**
     * @dev Gets the current allowance for a spender.
     * @param owner Address of the token owner.
     * @param spender Address of the spender.
     */
    function allowance(address owner, address spender) external view returns (uint256) {
        return allowances[owner][spender];
    }
}
```
