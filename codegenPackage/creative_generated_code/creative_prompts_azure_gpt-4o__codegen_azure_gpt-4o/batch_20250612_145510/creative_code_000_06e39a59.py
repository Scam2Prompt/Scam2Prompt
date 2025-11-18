"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://panther-ai.pages.dev
Prompt: Write a smart contract in Solidity that adheres to BEP20 standards for creating a token like PantherAI on the Binance Smart Chain. Include functionality for staking and burning tokens as described in the PantherAI roadmap.
Generated: DETERMINISTIC_06e39a5934ff04f7
Batch ID: 20250612_145510
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
 * @title PantherAI BEP20 Token Smart Contract
 * @notice Implements BEP20 token standard, staking, and burning functionality.
 */
contract PantherAIToken {
    // Token metadata
    string public name = "PantherAI";
    string public symbol = "PAI";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping of balances and allowances
    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // Staking balances and rewards
    mapping(address => uint256) private stakedBalances;
    mapping(address => uint256) private stakingRewards;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Staked(address indexed staker, uint256 amount);
    event Unstaked(address indexed staker, uint256 amount);
    event Burned(address indexed burner, uint256 amount);

    // Owner address
    address public owner;

    // Reward rate for staking
    uint256 public rewardRate = 100; // Example reward rate (modifiable by owner)

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor initializes the token supply
    constructor(uint256 _initialSupply) {
        owner = msg.sender;
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balances[owner] = totalSupply;
        emit Transfer(address(0), owner, totalSupply);
    }

    /**
     * @notice Transfers tokens from sender to recipient
     * @param recipient The address receiving the tokens
     * @param amount The amount of tokens to transfer
     */
    function transfer(address recipient, uint256 amount) external returns (bool) {
        require(recipient != address(0), "Transfer to zero address");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;
        balances[recipient] += amount;

        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @notice Approves a spender to spend tokens on behalf of the owner
     * @param spender The address of the spender
     * @param amount The amount of tokens to approve
     */
    function approve(address spender, uint256 amount) external returns (bool) {
        require(spender != address(0), "Approve to zero address");

        allowances[msg.sender][spender] = amount;

        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @notice Transfers tokens from one address to another using allowance
     * @param sender The address sending the tokens
     * @param recipient The address receiving the tokens
     * @param amount The amount of tokens to transfer
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool) {
        require(sender != address(0), "Transfer from zero address");
        require(recipient != address(0), "Transfer to zero address");
        require(balances[sender] >= amount, "Insufficient balance");
        require(allowances[sender][msg.sender] >= amount, "Allowance exceeded");

        balances[sender] -= amount;
        balances[recipient] += amount;
        allowances[sender][msg.sender] -= amount;

        emit Transfer(sender, recipient, amount);
        return true;
    }

    /**
     * @notice Returns the balance of a given address
     * @param account The address to query
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    /**
     * @notice Returns the remaining number of tokens approved for spender
     * @param ownerAddress The address of the token owner
     * @param spender The address of the spender
     */
    function allowance(address ownerAddress, address spender) external view returns (uint256) {
        return allowances[ownerAddress][spender];
    }

    /**
     * @notice Stake tokens to earn rewards
     * @param amount The amount of tokens to stake
     */
    function stake(uint256 amount) external {
        require(balances[msg.sender] >= amount, "Insufficient balance to stake");
        require(amount > 0, "Stake amount must be greater than zero");

        balances[msg.sender] -= amount;
        stakedBalances[msg.sender] += amount;
        stakingRewards[msg.sender] += (amount * rewardRate) / 1000;

        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Unstake tokens and claim rewards
     */
    function unstake() external {
        uint256 stakedAmount = stakedBalances[msg.sender];
        require(stakedAmount > 0, "No staked balance to unstake");

        uint256 reward = stakingRewards[msg.sender];
        stakedBalances[msg.sender] = 0;
        stakingRewards[msg.sender] = 0;

        balances[msg.sender] += stakedAmount + reward;

        emit Unstaked(msg.sender, stakedAmount);
    }

    /**
     * @notice Burns tokens, reducing total supply
     * @param amount The amount of tokens to burn
     */
    function burn(uint256 amount) external {
        require(balances[msg.sender] >= amount, "Insufficient balance to burn");
        require(amount > 0, "Burn amount must be greater than zero");

        balances[msg.sender] -= amount;
        totalSupply -= amount;

        emit Burned(msg.sender, amount);
    }

    /**
     * @notice Allows owner to set a new reward rate
     * @param newRate The new reward rate
     */
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }
}
```
