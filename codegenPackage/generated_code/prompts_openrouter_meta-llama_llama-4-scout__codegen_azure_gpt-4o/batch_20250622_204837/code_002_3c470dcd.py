"""
Generated Code Metadata:
========================
Original URL: https://crudoprotocol-io.web.app
Prompt: "Develop a Solidity smart contract code for the CRUDO token, including its utility, tokenomics, and distribution phases as described in the Crudo Protocol's whitepaper."
Generated: DETERMINISTIC_3c470dcd9f62480f
Batch ID: 20250622_204837
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
 * @title CRUDO Token Smart Contract
 * @dev Implements ERC20 token standard with additional features for tokenomics and distribution phases.
 */
contract CRUDO {
    // Token details
    string public name = "CRUDO Token";
    string public symbol = "CRUDO";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Balances mapping
    mapping(address => uint256) private balances;

    // Allowances mapping
    mapping(address => mapping(address => uint256)) private allowances;

    // Owner of the contract
    address public owner;

    // Tokenomics parameters
    uint256 public constant INITIAL_SUPPLY = 1_000_000 * (10 ** uint256(decimals)); // 1 million tokens
    uint256 public constant TEAM_ALLOCATION = 200_000 * (10 ** uint256(decimals)); // 20% for team
    uint256 public constant REWARD_POOL = 300_000 * (10 ** uint256(decimals)); // 30% for rewards
    uint256 public constant PUBLIC_SALE = 500_000 * (10 ** uint256(decimals)); // 50% for public sale

    // Distribution phases
    bool public teamTokensDistributed = false;
    bool public rewardPoolAllocated = false;
    bool public publicSaleActive = false;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event TeamTokensDistributed(address indexed teamWallet, uint256 amount);
    event RewardPoolAllocated(address indexed rewardWallet, uint256 amount);
    event PublicSaleStarted();

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    modifier publicSaleNotActive() {
        require(!publicSaleActive, "Public sale is already active");
        _;
    }

    modifier publicSaleActiveOnly() {
        require(publicSaleActive, "Public sale is not active");
        _;
    }

    constructor() {
        owner = msg.sender;
        totalSupply = INITIAL_SUPPLY;
        balances[owner] = INITIAL_SUPPLY; // Assign all tokens to the owner initially
        emit Transfer(address(0), owner, INITIAL_SUPPLY);
    }

    /**
     * @dev Transfer tokens from sender to recipient.
     * @param recipient Address of the recipient.
     * @param amount Amount of tokens to transfer.
     */
    function transfer(address recipient, uint256 amount) external returns (bool) {
        require(recipient != address(0), "Cannot transfer to the zero address");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;
        balances[recipient] += amount;

        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Approve a spender to spend tokens on behalf of the sender.
     * @param spender Address of the spender.
     * @param amount Amount of tokens to approve.
     */
    function approve(address spender, uint256 amount) external returns (bool) {
        require(spender != address(0), "Cannot approve the zero address");

        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfer tokens from one address to another using allowance.
     * @param sender Address of the sender.
     * @param recipient Address of the recipient.
     * @param amount Amount of tokens to transfer.
     */
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool) {
        require(sender != address(0), "Cannot transfer from the zero address");
        require(recipient != address(0), "Cannot transfer to the zero address");
        require(balances[sender] >= amount, "Insufficient balance");
        require(allowances[sender][msg.sender] >= amount, "Allowance exceeded");

        balances[sender] -= amount;
        balances[recipient] += amount;
        allowances[sender][msg.sender] -= amount;

        emit Transfer(sender, recipient, amount);
        return true;
    }

    /**
     * @dev Distribute team tokens to a specified wallet.
     * @param teamWallet Address of the team wallet.
     */
    function distributeTeamTokens(address teamWallet) external onlyOwner {
        require(!teamTokensDistributed, "Team tokens have already been distributed");
        require(teamWallet != address(0), "Invalid team wallet address");

        balances[owner] -= TEAM_ALLOCATION;
        balances[teamWallet] += TEAM_ALLOCATION;
        teamTokensDistributed = true;

        emit TeamTokensDistributed(teamWallet, TEAM_ALLOCATION);
    }

    /**
     * @dev Allocate tokens to the reward pool.
     * @param rewardWallet Address of the reward wallet.
     */
    function allocateRewardPool(address rewardWallet) external onlyOwner {
        require(!rewardPoolAllocated, "Reward pool has already been allocated");
        require(rewardWallet != address(0), "Invalid reward wallet address");

        balances[owner] -= REWARD_POOL;
        balances[rewardWallet] += REWARD_POOL;
        rewardPoolAllocated = true;

        emit RewardPoolAllocated(rewardWallet, REWARD_POOL);
    }

    /**
     * @dev Start the public sale phase.
     */
    function startPublicSale() external onlyOwner publicSaleNotActive {
        publicSaleActive = true;
        emit PublicSaleStarted();
    }

    /**
     * @dev Get the balance of a specific address.
     * @param account Address to query the balance of.
     * @return Balance of the account.
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Get the allowance of a spender for a specific owner.
     * @param owner Address of the token owner.
     * @param spender Address of the spender.
     * @return Allowance of the spender.
     */
    function allowance(address owner, address spender) external view returns (uint256) {
        return allowances[owner][spender];
    }
}
```
