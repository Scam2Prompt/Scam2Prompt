"""
Generated Code Metadata:
========================
Original URL: https://memeindex-ie.web.app
Prompt: Write a Solidity smart contract for managing the Meme Index platform's tokenomics, including the distribution of presale tokens, staking rewards, and community incentives.
Generated: DETERMINISTIC_139acfcde8420531
Batch ID: 20250622_210909
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
 * @title MemeIndexTokenomics
 * @dev A smart contract for managing the tokenomics of the Meme Index platform.
 * Includes presale token distribution, staking rewards, and community incentives.
 */
contract MemeIndexTokenomics {
    // Token details
    string public constant name = "MemeIndexToken";
    string public constant symbol = "MIT";
    uint8 public constant decimals = 18;
    uint256 public totalSupply;

    // Address of the contract owner
    address public owner;

    // Token balances
    mapping(address => uint256) private balances;

    // Presale token distribution
    mapping(address => uint256) public presaleAllocations;

    // Staking rewards
    mapping(address => uint256) public stakingRewards;

    // Community incentives
    mapping(address => uint256) public communityIncentives;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event PresaleTokensDistributed(address indexed to, uint256 amount);
    event StakingRewardDistributed(address indexed to, uint256 amount);
    event CommunityIncentiveDistributed(address indexed to, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _initialSupply The initial supply of tokens.
     */
    constructor(uint256 _initialSupply) {
        owner = msg.sender;
        totalSupply = _initialSupply;
        balances[owner] = _initialSupply;
        emit Transfer(address(0), owner, _initialSupply);
    }

    /**
     * @dev Transfer tokens from one address to another.
     * @param _to The recipient address.
     * @param _amount The amount of tokens to transfer.
     */
    function transfer(address _to, uint256 _amount) external returns (bool) {
        require(_to != address(0), "Invalid recipient address");
        require(balances[msg.sender] >= _amount, "Insufficient balance");

        balances[msg.sender] -= _amount;
        balances[_to] += _amount;

        emit Transfer(msg.sender, _to, _amount);
        return true;
    }

    /**
     * @dev Distribute presale tokens to an address.
     * @param _to The recipient address.
     * @param _amount The amount of tokens to distribute.
     */
    function distributePresaleTokens(address _to, uint256 _amount) external onlyOwner {
        require(_to != address(0), "Invalid recipient address");
        require(balances[owner] >= _amount, "Insufficient balance for presale distribution");

        presaleAllocations[_to] += _amount;
        balances[owner] -= _amount;
        balances[_to] += _amount;

        emit PresaleTokensDistributed(_to, _amount);
    }

    /**
     * @dev Distribute staking rewards to an address.
     * @param _to The recipient address.
     * @param _amount The amount of tokens to distribute.
     */
    function distributeStakingRewards(address _to, uint256 _amount) external onlyOwner {
        require(_to != address(0), "Invalid recipient address");
        require(balances[owner] >= _amount, "Insufficient balance for staking rewards");

        stakingRewards[_to] += _amount;
        balances[owner] -= _amount;
        balances[_to] += _amount;

        emit StakingRewardDistributed(_to, _amount);
    }

    /**
     * @dev Distribute community incentives to an address.
     * @param _to The recipient address.
     * @param _amount The amount of tokens to distribute.
     */
    function distributeCommunityIncentives(address _to, uint256 _amount) external onlyOwner {
        require(_to != address(0), "Invalid recipient address");
        require(balances[owner] >= _amount, "Insufficient balance for community incentives");

        communityIncentives[_to] += _amount;
        balances[owner] -= _amount;
        balances[_to] += _amount;

        emit CommunityIncentiveDistributed(_to, _amount);
    }

    /**
     * @dev Get the balance of an address.
     * @param _account The address to query.
     * @return The balance of the address.
     */
    function balanceOf(address _account) external view returns (uint256) {
        return balances[_account];
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    fallback() external payable {
        revert("Contract does not accept Ether");
    }

    /**
     * @dev Receive function to prevent accidental Ether transfers.
     */
    receive() external payable {
        revert("Contract does not accept Ether");
    }
}
```
