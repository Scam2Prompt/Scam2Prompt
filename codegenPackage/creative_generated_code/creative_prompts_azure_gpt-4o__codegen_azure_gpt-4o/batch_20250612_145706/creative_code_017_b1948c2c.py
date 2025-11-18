"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://popofrog-io.pages.dev
Prompt: Develop a smart contract for a fixed total supply token with allocations for presale, staking, marketing, rewards, and liquidity, based on $FROP’s supply cap of 111,111,111,111 tokens.
Generated: DETERMINISTIC_b1948c2c95934709
Batch ID: 20250612_145706
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
 * @title FROPSmartContract
 * @dev A fixed total supply token contract with allocations for presale, staking, marketing,
 * rewards, and liquidity. The total supply is 111,111,111,111 tokens.
 */
contract FROPToken {
    string public constant name = "FROP Token";
    string public constant symbol = "FROP";
    uint8 public constant decimals = 18;
    uint256 public constant totalSupply = 111_111_111_111 * (10 ** uint256(decimals));

    // Allocation percentages
    uint256 public constant presaleAllocation = (totalSupply * 30) / 100; // 30%
    uint256 public constant stakingAllocation = (totalSupply * 20) / 100; // 20%
    uint256 public constant marketingAllocation = (totalSupply * 15) / 100; // 15%
    uint256 public constant rewardsAllocation = (totalSupply * 25) / 100; // 25%
    uint256 public constant liquidityAllocation = (totalSupply * 10) / 100; // 10%

    // Balances mapping
    mapping(address => uint256) private _balances;

    // Allowances for spending on behalf of others
    mapping(address => mapping(address => uint256)) private _allowances;

    // Address of the owner of the contract
    address public owner;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Modifier for restricted access
    modifier onlyOwner() {
        require(msg.sender == owner, "Access denied: Only owner allowed");
        _;
    }

    /**
     * @dev Constructor to initialize the contract and allocate tokens.
     */
    constructor(
        address presaleWallet,
        address stakingWallet,
        address marketingWallet,
        address rewardsWallet,
        address liquidityWallet
    ) {
        require(presaleWallet != address(0), "Invalid presale wallet address");
        require(stakingWallet != address(0), "Invalid staking wallet address");
        require(marketingWallet != address(0), "Invalid marketing wallet address");
        require(rewardsWallet != address(0), "Invalid rewards wallet address");
        require(liquidityWallet != address(0), "Invalid liquidity wallet address");

        owner = msg.sender;

        // Allocate tokens to respective wallets
        _balances[presaleWallet] = presaleAllocation;
        _balances[stakingWallet] = stakingAllocation;
        _balances[marketingWallet] = marketingAllocation;
        _balances[rewardsWallet] = rewardsAllocation;
        _balances[liquidityWallet] = liquidityAllocation;

        // Emit Transfer events for transparency
        emit Transfer(address(0), presaleWallet, presaleAllocation);
        emit Transfer(address(0), stakingWallet, stakingAllocation);
        emit Transfer(address(0), marketingWallet, marketingAllocation);
        emit Transfer(address(0), rewardsWallet, rewardsAllocation);
        emit Transfer(address(0), liquidityWallet, liquidityAllocation);
    }

    /**
     * @dev Transfers tokens from caller to another address.
     */
    function transfer(address to, uint256 amount) external returns (bool) {
        require(to != address(0), "Transfer to the zero address is not allowed");
        require(_balances[msg.sender] >= amount, "Insufficient balance for transfer");

        _balances[msg.sender] -= amount;
        _balances[to] += amount;
        emit Transfer(msg.sender, to, amount);
        return true;
    }

    /**
     * @dev Approves a spender to spend tokens on behalf of the caller.
     */
    function approve(address spender, uint256 amount) external returns (bool) {
        require(spender != address(0), "Approve to the zero address is not allowed");

        _allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfers tokens on behalf of the owner (requires allowance).
     */
    function transferFrom(address from, address to, uint256 amount) external returns (bool) {
        require(to != address(0), "Transfer to the zero address is not allowed");
        require(_balances[from] >= amount, "Insufficient balance for transfer");
        require(_allowances[from][msg.sender] >= amount, "Transfer amount exceeds allowance");

        _balances[from] -= amount;
        _allowances[from][msg.sender] -= amount;
        _balances[to] += amount;
        emit Transfer(from, to, amount);
        return true;
    }

    /**
     * @dev Returns the balance of a given address.
     */
    function balanceOf(address account) external view returns (uint256) {
        return _balances[account];
    }

    /**
     * @dev Returns the remaining allowance for a spender.
     */
    function allowance(address ownerAddress, address spender) external view returns (uint256) {
        return _allowances[ownerAddress][spender];
    }

    /**
     * @dev Burns tokens from the caller's account, reducing the total supply.
     */
    function burn(uint256 amount) external onlyOwner {
        require(_balances[msg.sender] >= amount, "Insufficient balance to burn");

        _balances[msg.sender] -= amount;
        emit Transfer(msg.sender, address(0), amount);
    }
}
```
