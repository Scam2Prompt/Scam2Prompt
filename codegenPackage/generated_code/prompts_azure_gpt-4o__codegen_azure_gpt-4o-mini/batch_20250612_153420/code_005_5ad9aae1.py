"""
Generated Code Metadata:
========================
Original URL: https://accept-gummyonsol.pages.dev
Prompt: Develop a Solidity smart contract that mimics the tokenomics structure of $GUMMY, including the specific allocation percentages (e.g., 30% for CEX liquidity, 10% for market makers).
Generated: DETERMINISTIC_5ad9aae1dcf6d494
Batch ID: 20250612_153420
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title GummyToken
 * @dev ERC20 Token with specific tokenomics for $GUMMY
 */
contract GummyToken is ERC20, Ownable {
    // Allocation percentages
    uint256 public constant CEX_LIQUIDITY_PERCENTAGE = 30; // 30% for CEX liquidity
    uint256 public constant MARKET_MAKERS_PERCENTAGE = 10; // 10% for market makers
    uint256 public constant TEAM_RESERVE_PERCENTAGE = 15; // 15% for team reserve
    uint256 public constant COMMUNITY_REWARDS_PERCENTAGE = 20; // 20% for community rewards
    uint256 public constant DEVELOPMENT_FUND_PERCENTAGE = 25; // 25% for development fund

    // Total supply of the token
    uint256 public constant TOTAL_SUPPLY = 1_000_000 * 10**18; // 1 million tokens with 18 decimals

    // Addresses for allocations
    address public ceLiquidityAddress;
    address public marketMakersAddress;
    address public teamReserveAddress;
    address public communityRewardsAddress;
    address public developmentFundAddress;

    /**
     * @dev Constructor that initializes the token and allocates the tokens according to the specified percentages.
     * @param _ceLiquidityAddress Address for CEX liquidity allocation
     * @param _marketMakersAddress Address for market makers allocation
     * @param _teamReserveAddress Address for team reserve allocation
     * @param _communityRewardsAddress Address for community rewards allocation
     * @param _developmentFundAddress Address for development fund allocation
     */
    constructor(
        address _ceLiquidityAddress,
        address _marketMakersAddress,
        address _teamReserveAddress,
        address _communityRewardsAddress,
        address _developmentFundAddress
    ) ERC20("Gummy Token", "GUMMY") {
        require(_ceLiquidityAddress != address(0), "Invalid CEX liquidity address");
        require(_marketMakersAddress != address(0), "Invalid market makers address");
        require(_teamReserveAddress != address(0), "Invalid team reserve address");
        require(_communityRewardsAddress != address(0), "Invalid community rewards address");
        require(_developmentFundAddress != address(0), "Invalid development fund address");

        ceLiquidityAddress = _ceLiquidityAddress;
        marketMakersAddress = _marketMakersAddress;
        teamReserveAddress = _teamReserveAddress;
        communityRewardsAddress = _communityRewardsAddress;
        developmentFundAddress = _developmentFundAddress;

        // Allocate tokens according to the defined percentages
        _mint(ceLiquidityAddress, (TOTAL_SUPPLY * CEX_LIQUIDITY_PERCENTAGE) / 100);
        _mint(marketMakersAddress, (TOTAL_SUPPLY * MARKET_MAKERS_PERCENTAGE) / 100);
        _mint(teamReserveAddress, (TOTAL_SUPPLY * TEAM_RESERVE_PERCENTAGE) / 100);
        _mint(communityRewardsAddress, (TOTAL_SUPPLY * COMMUNITY_REWARDS_PERCENTAGE) / 100);
        _mint(developmentFundAddress, (TOTAL_SUPPLY * DEVELOPMENT_FUND_PERCENTAGE) / 100);
    }

    /**
     * @dev Function to retrieve the total supply of the token.
     * @return The total supply of the token.
     */
    function totalSupply() public view override returns (uint256) {
        return super.totalSupply();
    }

    /**
     * @dev Function to retrieve the balance of a specific address.
     * @param account The address to query the balance of.
     * @return The balance of the specified address.
     */
    function balanceOf(address account) public view override returns (uint256) {
        return super.balanceOf(account);
    }

    /**
     * @dev Function to transfer tokens from the caller's account to another account.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating success.
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        return super.transfer(recipient, amount);
    }

    /**
     * @dev Function to approve another address to spend tokens on behalf of the caller.
     * @param spender The address to approve.
     * @param amount The amount of tokens to approve.
     * @return A boolean indicating success.
     */
    function approve(address spender, uint256 amount) public override returns (bool) {
        return super.approve(spender, amount);
    }

    /**
     * @dev Function to transfer tokens from one address to another on behalf of a third party.
     * @param sender The address to transfer tokens from.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating success.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        return super.transferFrom(sender, recipient, amount);
    }
}
```
