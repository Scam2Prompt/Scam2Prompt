"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20claim-now.pages.dev
Prompt: Develop a smart contract in Solidity that implements fixed tokenomics similar to DOGE20, including allocations for presale, marketing, treasury, staking rewards, and liquidity.
Generated: DETERMINISTIC_07ba91af08487c17
Batch ID: 20250612_150552
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
 * @title Fixed Tokenomics Smart Contract
 * @dev Implements allocations for presale, marketing, treasury, staking rewards, and liquidity.
 */
contract FixedTokenomics {
    // Token details
    string public constant name = "Doge20Token";
    string public constant symbol = "DOGE20";
    uint8 public constant decimals = 18;
    uint256 public constant totalSupply = 1_000_000_000 * (10 ** uint256(decimals)); // 1 billion tokens

    // Allocation percentages (in basis points, e.g., 1000 = 10%)
    uint256 public constant presaleAllocation = 3000;  // 30%
    uint256 public constant marketingAllocation = 2000; // 20%
    uint256 public constant treasuryAllocation = 2000;  // 20%
    uint256 public constant stakingRewardsAllocation = 2000; // 20%
    uint256 public constant liquidityAllocation = 1000; // 10%

    // Addresses for allocations
    address public presaleWallet;
    address public marketingWallet;
    address public treasuryWallet;
    address public stakingRewardsWallet;
    address public liquidityWallet;

    // Balances mapping
    mapping(address => uint256) private _balances;

    // Allowance mapping
    mapping(address => mapping(address => uint256)) private _allowances;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    /**
     * @dev Constructor to initialize allocations and mint tokens.
     * @param _presaleWallet Address for presale allocation
     * @param _marketingWallet Address for marketing allocation
     * @param _treasuryWallet Address for treasury allocation
     * @param _stakingRewardsWallet Address for staking rewards allocation
     * @param _liquidityWallet Address for liquidity allocation
     */
    constructor(
        address _presaleWallet,
        address _marketingWallet,
        address _treasuryWallet,
        address _stakingRewardsWallet,
        address _liquidityWallet
    ) {
        require(_presaleWallet != address(0), "Invalid presale wallet address");
        require(_marketingWallet != address(0), "Invalid marketing wallet address");
        require(_treasuryWallet != address(0), "Invalid treasury wallet address");
        require(_stakingRewardsWallet != address(0), "Invalid staking rewards wallet address");
        require(_liquidityWallet != address(0), "Invalid liquidity wallet address");

        // Assign wallet addresses
        presaleWallet = _presaleWallet;
        marketingWallet = _marketingWallet;
        treasuryWallet = _treasuryWallet;
        stakingRewardsWallet = _stakingRewardsWallet;
        liquidityWallet = _liquidityWallet;

        // Mint and distribute tokens
        _mint(presaleWallet, (totalSupply * presaleAllocation) / 10000);
        _mint(marketingWallet, (totalSupply * marketingAllocation) / 10000);
        _mint(treasuryWallet, (totalSupply * treasuryAllocation) / 10000);
        _mint(stakingRewardsWallet, (totalSupply * stakingRewardsAllocation) / 10000);
        _mint(liquidityWallet, (totalSupply * liquidityAllocation) / 10000);
    }

    /**
     * @dev Returns the balance of a specific address.
     * @param account The address to query the balance of.
     * @return The balance of the specified address.
     */
    function balanceOf(address account) public view returns (uint256) {
        return _balances[account];
    }

    /**
     * @dev Transfers tokens to a specified address.
     * @param to The address to transfer to.
     * @param amount The amount to be transferred.
     * @return True if the operation was successful.
     */
    function transfer(address to, uint256 amount) public returns (bool) {
        require(to != address(0), "Transfer to the zero address");
        require(_balances[msg.sender] >= amount, "Insufficient balance");

        _balances[msg.sender] -= amount;
        _balances[to] += amount;

        emit Transfer(msg.sender, to, amount);
        return true;
    }

    /**
     * @dev Approves an address to spend the specified amount of tokens on behalf of the caller.
     * @param spender The address authorized to spend.
     * @param amount The amount to be spent.
     * @return True if the operation was successful.
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        require(spender != address(0), "Approve to the zero address");

        _allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Returns the remaining number of tokens that `spender` is allowed to spend on behalf of `owner`.
     * @param owner The address which owns the funds.
     * @param spender The address authorized to spend.
     * @return The remaining allowance.
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return _allowances[owner][spender];
    }

    /**
     * @dev Transfers tokens on behalf of another address.
     * @param from The address to transfer from.
     * @param to The address to transfer to.
     * @param amount The amount to be transferred.
     * @return True if the operation was successful.
     */
    function transferFrom(address from, address to, uint256 amount) public returns (bool) {
        require(from != address(0), "Transfer from the zero address");
        require(to != address(0), "Transfer to the zero address");
        require(_balances[from] >= amount, "Insufficient balance");
        require(_allowances[from][msg.sender] >= amount, "Transfer amount exceeds allowance");

        _balances[from] -= amount;
        _balances[to] += amount;
        _allowances[from][msg.sender] -= amount;

        emit Transfer(from, to, amount);
        return true;
    }

    /**
     * @dev Internal function to mint tokens.
     * @param account The address to mint the tokens to.
     * @param amount The amount of tokens to be minted.
     */
    function _mint(address account, uint256 amount) internal {
        require(account != address(0), "Mint to the zero address");

        _balances[account] += amount;
        emit Transfer(address(0), account, amount);
    }
}
```
