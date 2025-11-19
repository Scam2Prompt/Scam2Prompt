"""
Generated Code Metadata:
========================
Original URL: https://cryptoallstars-launch.firebaseapp.com
Prompt: Generate code in Solidity to allocate token supply based on the Crypto All-Stars tokenomics breakdown (e.g., presale, staking, marketing, etc.).
Generated: DETERMINISTIC_a16b3d5e367f65ba
Batch ID: 20250612_153722
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

contract CryptoAllStarsToken is ERC20, Ownable {
    // Token allocation percentages (basis points)
    uint256 public constant PRESALE_ALLOCATION = 3000; // 30%
    uint256 public constant STAKING_ALLOCATION = 2500; // 25%
    uint256 public constant MARKETING_ALLOCATION = 1500; // 15%
    uint256 public constant TEAM_ALLOCATION = 1500; // 15%
    uint256 public constant ADVISORS_ALLOCATION = 1000; // 10%
    uint256 public constant LIQUIDITY_ALLOCATION = 500; // 5%

    // Allocation addresses
    address public presaleVault;
    address public stakingVault;
    address public marketingVault;
    address public teamVault;
    address public advisorsVault;
    address public liquidityVault;

    // Total supply (1 billion tokens with 18 decimals)
    uint256 private constant TOTAL_SUPPLY = 1_000_000_000 * 10**18;

    // Track allocated tokens
    bool private allocationsDone = false;

    event AllocationComplete();
    event VaultsSet(
        address presaleVault,
        address stakingVault,
        address marketingVault,
        address teamVault,
        address advisorsVault,
        address liquidityVault
    );

    constructor() ERC20("Crypto All-Stars", "CAS") {
        _mint(address(this), TOTAL_SUPPLY);
    }

    /**
     * @dev Set the vault addresses for token allocations
     * @param _presaleVault Presale allocation address
     * @param _stakingVault Staking rewards address
     * @param _marketingVault Marketing funds address
     * @param _teamVault Team allocation address
     * @param _advisorsVault Advisors allocation address
     * @param _liquidityVault Liquidity pool address
     */
    function setVaults(
        address _presaleVault,
        address _stakingVault,
        address _marketingVault,
        address _teamVault,
        address _advisorsVault,
        address _liquidityVault
    ) external onlyOwner {
        require(!allocationsDone, "Allocations already completed");
        require(
            _presaleVault != address(0) &&
                _stakingVault != address(0) &&
                _marketingVault != address(0) &&
                _teamVault != address(0) &&
                _advisorsVault != address(0) &&
                _liquidityVault != address(0),
            "Invalid vault address"
        );

        presaleVault = _presaleVault;
        stakingVault = _stakingVault;
        marketingVault = _marketingVault;
        teamVault = _teamVault;
        advisorsVault = _advisorsVault;
        liquidityVault = _liquidityVault;

        emit VaultsSet(
            _presaleVault,
            _stakingVault,
            _marketingVault,
            _teamVault,
            _advisorsVault,
            _liquidityVault
        );
    }

    /**
     * @dev Allocate tokens to respective vaults based on tokenomics
     */
    function allocateTokens() external onlyOwner {
        require(!allocationsDone, "Allocations already completed");
        require(
            presaleVault != address(0) &&
                stakingVault != address(0) &&
                marketingVault != address(0) &&
                teamVault != address(0) &&
                advisorsVault != address(0) &&
                liquidityVault != address(0),
            "Vault addresses not set"
        );

        // Calculate allocations
        uint256 presaleAmount = (TOTAL_SUPPLY * PRESALE_ALLOCATION) / 10000;
        uint256 stakingAmount = (TOTAL_SUPPLY * STAKING_ALLOCATION) / 10000;
        uint256 marketingAmount = (TOTAL_SUPPLY * MARKETING_ALLOCATION) / 10000;
        uint256 teamAmount = (TOTAL_SUPPLY * TEAM_ALLOCATION) / 10000;
        uint256 advisorsAmount = (TOTAL_SUPPLY * ADVISORS_ALLOCATION) / 10000;
        uint256 liquidityAmount = (TOTAL_SUPPLY * LIQUIDITY_ALLOCATION) / 10000;

        // Transfer tokens to vaults
        _transfer(address(this), presaleVault, presaleAmount);
        _transfer(address(this), stakingVault, stakingAmount);
        _transfer(address(this), marketingVault, marketingAmount);
        _transfer(address(this), teamVault, teamAmount);
        _transfer(address(this), advisorsVault, advisorsAmount);
        _transfer(address(this), liquidityVault, liquidityAmount);

        allocationsDone = true;
        emit AllocationComplete();
    }

    /**
     * @dev Recover any tokens accidentally sent to this contract
     * @param tokenAddress The token contract address
     * @param to The recipient address
     * @param amount The amount to recover
     */
    function recoverERC20(
        address tokenAddress,
        address to,
        uint256 amount
    ) external onlyOwner {
        IERC20(tokenAddress).transfer(to, amount);
    }
}
```
