"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-ea.pages.dev
Prompt: Provide Solidity code for a fixed-supply ERC-20 token similar to DOGE20, including tokenomics features such as allocating percentages for presale, marketing, treasury, staking rewards, and liquidity.
Generated: DETERMINISTIC_fb62650fad6fa552
Batch ID: 20250612_152710
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
 * @title FixedSupplyToken
 * @dev Implementation of a fixed-supply ERC-20 token with allocations for various purposes.
 */
contract FixedSupplyToken {
    // ERC-20 token standard variables
    string public name = "DOGE20 Token";
    string public symbol = "DOGE20";
    uint8 public decimals = 18;

    uint256 public totalSupply = 1_000_000_000 * (10**decimals); // 1 billion tokens

    // Balances mapping
    mapping(address => uint256) public balanceOf;

    // Allowance mapping (for ERC-20 transfers)
    mapping(address => mapping(address => uint256)) public allowance;

    // Events required by ERC-20 standard
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Allocations
    address public presaleWallet;
    address public marketingWallet;
    address public treasuryWallet;
    address public stakingRewardsWallet;
    address public liquidityWallet;

    uint256 public presaleAllocation = (totalSupply * 20) / 100; // 20%
    uint256 public marketingAllocation = (totalSupply * 10) / 100; // 10%
    uint256 public treasuryAllocation = (totalSupply * 30) / 100; // 30%
    uint256 public stakingRewardsAllocation = (totalSupply * 25) / 100; // 25%
    uint256 public liquidityAllocation = (totalSupply * 15) / 100; // 15%

    // Constructor to initialize wallets and distribute tokens
    constructor(
        address _presaleWallet,
        address _marketingWallet,
        address _treasuryWallet,
        address _stakingRewardsWallet,
        address _liquidityWallet
    ) {
        require(_presaleWallet != address(0), "Presale wallet cannot be zero address");
        require(_marketingWallet != address(0), "Marketing wallet cannot be zero address");
        require(_treasuryWallet != address(0), "Treasury wallet cannot be zero address");
        require(_stakingRewardsWallet != address(0), "Staking Rewards wallet cannot be zero address");
        require(_liquidityWallet != address(0), "Liquidity wallet cannot be zero address");

        presaleWallet = _presaleWallet;
        marketingWallet = _marketingWallet;
        treasuryWallet = _treasuryWallet;
        stakingRewardsWallet = _stakingRewardsWallet;
        liquidityWallet = _liquidityWallet;

        // Allocate tokens to wallets
        _mint(presaleWallet, presaleAllocation);
        _mint(marketingWallet, marketingAllocation);
        _mint(treasuryWallet, treasuryAllocation);
        _mint(stakingRewardsWallet, stakingRewardsAllocation);
        _mint(liquidityWallet, liquidityAllocation);
    }

    /**
     * @dev Internal function to mint tokens.
     * @param to The address to receive the tokens.
     * @param amount The amount of tokens to mint.
     */
    function _mint(address to, uint256 amount) internal {
        balanceOf[to] += amount;
        emit Transfer(address(0), to, amount);
    }

    /**
     * @dev Transfer tokens from sender to recipient.
     * @param to Recipient address.
     * @param amount Amount of tokens to transfer.
     * @return success True if transfer succeeds.
     */
    function transfer(address to, uint256 amount) external returns (bool success) {
        require(balanceOf[msg.sender] >= amount, "Insufficient balance");
        require(to != address(0), "Cannot transfer to the zero address");

        balanceOf[msg.sender] -= amount;
        balanceOf[to] += amount;
        emit Transfer(msg.sender, to, amount);

        return true;
    }

    /**
     * @dev Approve a spender to transfer tokens on behalf of the sender.
     * @param spender Address of the spender.
     * @param amount Amount of tokens to approve.
     * @return success True if approval succeeds.
     */
    function approve(address spender, uint256 amount) external returns (bool success) {
        require(spender != address(0), "Cannot approve the zero address");

        allowance[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);

        return true;
    }

    /**
     * @dev Transfer tokens from one address to another using allowance.
     * @param from Address to send tokens from.
     * @param to Address to send tokens to.
     * @param amount Amount of tokens to transfer.
     * @return success True if transfer succeeds.
     */
    function transferFrom(
        address from,
        address to,
        uint256 amount
    ) external returns (bool success) {
        require(balanceOf[from] >= amount, "Insufficient balance");
        require(allowance[from][msg.sender] >= amount, "Allowance exceeded");
        require(to != address(0), "Cannot transfer to the zero address");

        balanceOf[from] -= amount;
        allowance[from][msg.sender] -= amount;
        balanceOf[to] += amount;
        emit Transfer(from, to, amount);

        return true;
    }
}
```
