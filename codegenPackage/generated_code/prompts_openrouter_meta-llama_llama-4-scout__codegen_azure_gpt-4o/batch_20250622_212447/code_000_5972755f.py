"""
Generated Code Metadata:
========================
Original URL: https://phantom237.com
Prompt: Write a Solidity smart contract for a horror-themed meme coin with a playable game feature, similar to PHANTOM237.
Generated: DETERMINISTIC_5972755fedc46a19
Batch ID: 20250622_212447
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
 * @title HorrorMemeCoin
 * @dev A horror-themed meme coin with a playable game feature.
 */
contract HorrorMemeCoin {
    // Token details
    string public name = "HorrorMemeCoin";
    string public symbol = "HORROR";
    uint8 public decimals = 18;
    uint256 public totalSupply = 1_000_000 * (10 ** uint256(decimals));

    // Balances mapping
    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event GamePlayed(address indexed player, uint256 score, bool won);

    // Game variables
    uint256 public gameFee = 0.01 ether; // Fee to play the game
    uint256 public gameReward = 100 * (10 ** uint256(decimals)); // Reward for winning the game
    address public owner;

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    modifier hasEnoughBalance(uint256 amount) {
        require(balanceOf[msg.sender] >= amount, "Insufficient balance");
        _;
    }

    modifier hasEnoughAllowance(address spender, uint256 amount) {
        require(allowance[msg.sender][spender] >= amount, "Allowance exceeded");
        _;
    }

    constructor() {
        owner = msg.sender;
        balanceOf[owner] = totalSupply; // Assign all tokens to the contract owner
    }

    /**
     * @dev Transfer tokens from sender to recipient.
     * @param recipient Address of the recipient.
     * @param amount Amount of tokens to transfer.
     */
    function transfer(address recipient, uint256 amount) public hasEnoughBalance(amount) returns (bool) {
        require(recipient != address(0), "Invalid recipient address");

        balanceOf[msg.sender] -= amount;
        balanceOf[recipient] += amount;

        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Approve a spender to spend tokens on behalf of the sender.
     * @param spender Address of the spender.
     * @param amount Amount of tokens to approve.
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        require(spender != address(0), "Invalid spender address");

        allowance[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfer tokens from one address to another using allowance.
     * @param sender Address of the sender.
     * @param recipient Address of the recipient.
     * @param amount Amount of tokens to transfer.
     */
    function transferFrom(address sender, address recipient, uint256 amount)
        public
        hasEnoughAllowance(sender, amount)
        returns (bool)
    {
        require(sender != address(0), "Invalid sender address");
        require(recipient != address(0), "Invalid recipient address");

        balanceOf[sender] -= amount;
        balanceOf[recipient] += amount;
        allowance[sender][msg.sender] -= amount;

        emit Transfer(sender, recipient, amount);
        return true;
    }

    /**
     * @dev Play the horror-themed game.
     * Players pay a fee to play, and if they win, they receive a reward.
     */
    function playGame() public payable {
        require(msg.value == gameFee, "Incorrect game fee");

        // Simulate game logic (randomized win/lose)
        bool won = (block.timestamp % 2 == 0); // Simple pseudo-random logic
        uint256 score = block.timestamp % 100; // Generate a pseudo-random score

        if (won) {
            require(balanceOf[owner] >= gameReward, "Insufficient reward balance");
            balanceOf[owner] -= gameReward;
            balanceOf[msg.sender] += gameReward;
        }

        emit GamePlayed(msg.sender, score, won);
    }

    /**
     * @dev Withdraw collected game fees to the owner's address.
     */
    function withdrawFees() public onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No fees to withdraw");

        (bool success, ) = owner.call{value: contractBalance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Fallback function to accept Ether.
     */
    receive() external payable {}
}
```
