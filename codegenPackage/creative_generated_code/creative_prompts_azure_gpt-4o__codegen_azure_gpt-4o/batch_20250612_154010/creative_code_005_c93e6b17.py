"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimflockerztoken.pages.dev
Prompt: Develop a Solidity contract that allocates $FLOCK tokens according to the tokenomics described (e.g., 20% for early birds, 25% for staking, 25% for the DAO vault).
Generated: DETERMINISTIC_c93e6b17dc492246
Batch ID: 20250612_154010
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
 * @title FLOCK Token Distribution Contract
 * @dev Distributes $FLOCK tokens according to specified tokenomics.
 *      - 20% for early birds
 *      - 25% for staking
 *      - 25% for the DAO vault
 *      - Remaining allocation is reserved for future use/development
 */
contract FLOCKToken {
    // Tokenomics percentages
    uint256 public constant EARLY_BIRDS_ALLOCATION = 20; // 20%
    uint256 public constant STAKING_ALLOCATION = 25; // 25%
    uint256 public constant DAO_VAULT_ALLOCATION = 25; // 25%

    // Total supply of tokens
    uint256 public immutable totalSupply;

    // Addresses for allocations
    address public earlyBirdsAddress;
    address public stakingAddress;
    address public daoVaultAddress;

    // Token balances
    mapping(address => uint256) public balances;

    event TokensAllocated(address indexed recipient, uint256 amount);

    /**
     * @dev Constructor initializes the contract and allocates tokens.
     * @param _totalSupply Total supply of $FLOCK tokens.
     * @param _earlyBirdsAddress Address receiving early birds allocation.
     * @param _stakingAddress Address receiving staking allocation.
     * @param _daoVaultAddress Address receiving DAO vault allocation.
     */
    constructor(
        uint256 _totalSupply,
        address _earlyBirdsAddress,
        address _stakingAddress,
        address _daoVaultAddress
    ) {
        require(_totalSupply > 0, "Total supply must be greater than zero");
        require(
            _earlyBirdsAddress != address(0) &&
                _stakingAddress != address(0) &&
                _daoVaultAddress != address(0),
            "Addresses must be valid"
        );

        totalSupply = _totalSupply;
        earlyBirdsAddress = _earlyBirdsAddress;
        stakingAddress = _stakingAddress;
        daoVaultAddress = _daoVaultAddress;

        // Calculate allocations
        uint256 earlyBirdsTokens = (_totalSupply * EARLY_BIRDS_ALLOCATION) / 100;
        uint256 stakingTokens = (_totalSupply * STAKING_ALLOCATION) / 100;
        uint256 daoVaultTokens = (_totalSupply * DAO_VAULT_ALLOCATION) / 100;

        // Allocate tokens
        balances[_earlyBirdsAddress] = earlyBirdsTokens;
        balances[_stakingAddress] = stakingTokens;
        balances[_daoVaultAddress] = daoVaultTokens;
        balances[address(this)] = _totalSupply - (earlyBirdsTokens + stakingTokens + daoVaultTokens); // Remaining for future use

        emit TokensAllocated(_earlyBirdsAddress, earlyBirdsTokens);
        emit TokensAllocated(_stakingAddress, stakingTokens);
        emit TokensAllocated(_daoVaultAddress, daoVaultTokens);
    }

    /**
     * @dev Function to transfer tokens from the contract to another address.
     * @param _to Address receiving the tokens.
     * @param _amount Number of tokens to transfer.
     */
    function transfer(address _to, uint256 _amount) external {
        require(_to != address(0), "Cannot transfer to zero address");
        require(balances[msg.sender] >= _amount, "Insufficient balance");

        // Perform transfer
        balances[msg.sender] -= _amount;
        balances[_to] += _amount;

        emit TokensAllocated(_to, _amount); // Emit as allocation for transparency
    }

    /**
     * @dev Retrieve the balance of a specific address.
     * @param _account Address to query the balance of.
     * @return Balance of the given account.
     */
    function balanceOf(address _account) external view returns (uint256) {
        return balances[_account];
    }
}
```
