"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kelexocrypto.pages.dev
Prompt: Write a Solidity smart contract for a token with the specified tokenomics of KoalaKash: 70% presale, 10% exchange listing, 10% staking rewards, 5% rewards, 3% team tokens, and 2% collaborations.
Generated: DETERMINISTIC_39cfe3d5b9d12c23
Batch ID: 20250612_151310
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
 * @title KoalaKash Token
 * @dev ERC20-compliant token implementation with predefined tokenomics.
 */
contract KoalaKash {
    // ERC20 token parameters
    string public constant name = "KoalaKash";
    string public constant symbol = "KKASH";
    uint8 public constant decimals = 18;

    // Total supply of tokens
    uint256 public constant totalSupply = 10_000_000 * 10**decimals;

    // Tokenomics breakdown
    uint256 public constant presaleAllocation = (totalSupply * 70) / 100; // 70% for presale
    uint256 public constant exchangeListingAllocation = (totalSupply * 10) / 100; // 10% for exchange listing
    uint256 public constant stakingRewardsAllocation = (totalSupply * 10) / 100; // 10% for staking rewards
    uint256 public constant rewardsAllocation = (totalSupply * 5) / 100; // 5% for rewards
    uint256 public constant teamAllocation = (totalSupply * 3) / 100; // 3% for team
    uint256 public constant collaborationsAllocation = (totalSupply * 2) / 100; // 2% for collaborations

    // Balances mapping
    mapping(address => uint256) private balances;

    // Allowances mapping for ERC20 transfers
    mapping(address => mapping(address => uint256)) private allowances;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Owner of the contract
    address public owner;

    // Distribution addresses
    address public presaleAddress;
    address public exchangeListingAddress;
    address public stakingRewardsAddress;
    address public rewardsAddress;
    address public teamAddress;
    address public collaborationsAddress;

    /**
     * @dev Constructor to set the owner and distribute tokens according to tokenomics.
     * @param _presaleAddress Address for presale allocation
     * @param _exchangeListingAddress Address for exchange listing allocation
     * @param _stakingRewardsAddress Address for staking rewards allocation
     * @param _rewardsAddress Address for rewards allocation
     * @param _teamAddress Address for team allocation
     * @param _collaborationsAddress Address for collaborations allocation
     */
    constructor(
        address _presaleAddress,
        address _exchangeListingAddress,
        address _stakingRewardsAddress,
        address _rewardsAddress,
        address _teamAddress,
        address _collaborationsAddress
    ) {
        require(
            _presaleAddress != address(0) &&
            _exchangeListingAddress != address(0) &&
            _stakingRewardsAddress != address(0) &&
            _rewardsAddress != address(0) &&
            _teamAddress != address(0) &&
            _collaborationsAddress != address(0),
            "Invalid address provided"
        );

        owner = msg.sender;

        // Assign tokenomics allocations
        presaleAddress = _presaleAddress;
        exchangeListingAddress = _exchangeListingAddress;
        stakingRewardsAddress = _stakingRewardsAddress;
        rewardsAddress = _rewardsAddress;
        teamAddress = _teamAddress;
        collaborationsAddress = _collaborationsAddress;

        // Distribute tokens
        balances[presaleAddress] = presaleAllocation;
        balances[exchangeListingAddress] = exchangeListingAllocation;
        balances[stakingRewardsAddress] = stakingRewardsAllocation;
        balances[rewardsAddress] = rewardsAllocation;
        balances[teamAddress] = teamAllocation;
        balances[collaborationsAddress] = collaborationsAllocation;

        emit Transfer(address(0), presaleAddress, presaleAllocation);
        emit Transfer(address(0), exchangeListingAddress, exchangeListingAllocation);
        emit Transfer(address(0), stakingRewardsAddress, stakingRewardsAllocation);
        emit Transfer(address(0), rewardsAddress, rewardsAllocation);
        emit Transfer(address(0), teamAddress, teamAllocation);
        emit Transfer(address(0), collaborationsAddress, collaborationsAllocation);
    }

    /**
     * @dev Returns the balance of a specific account.
     * @param account Address to query the balance
     * @return uint256 Balance of the account
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfer tokens from the caller's account to another account.
     * @param recipient Address of the recipient
     * @param amount Amount of tokens to transfer
     * @return bool True if transfer was successful
     */
    function transfer(address recipient, uint256 amount) public returns (bool) {
        require(recipient != address(0), "Transfer to the zero address");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;
        balances[recipient] += amount;

        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Approve an address to spend tokens on the caller's behalf.
     * @param spender Address of the spender
     * @param amount Amount of tokens to approve
     * @return bool True if approval was successful
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        require(spender != address(0), "Approve to the zero address");

        allowances[msg.sender][spender] = amount;

        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfer tokens on behalf of an account, following approval.
     * @param sender Address of the sender
     * @param recipient Address of the recipient
     * @param amount Amount of tokens to transfer
     * @return bool True if transfer was successful
     */
    function transferFrom(address sender, address recipient, uint256 amount) public returns (bool) {
        require(sender != address(0), "Transfer from the zero address");
        require(recipient != address(0), "Transfer to the zero address");
        require(balances[sender] >= amount, "Insufficient balance");
        require(allowances[sender][msg.sender] >= amount, "Allowance exceeded");

        balances[sender] -= amount;
        balances[recipient] += amount;
        allowances[sender][msg.sender] -= amount;

        emit Transfer(sender, recipient, amount);
        return true;
    }

    /**
     * @dev Returns the allowance of a spender for a specific owner.
     * @param owner Address of the token owner
     * @param spender Address of the spender
     * @return uint256 Remaining allowance
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }
}
```
