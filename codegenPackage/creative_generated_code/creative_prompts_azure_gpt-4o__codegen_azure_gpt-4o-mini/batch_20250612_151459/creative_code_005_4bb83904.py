"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepeunchained-sale.pages.dev
Prompt: Provide code to implement tokenomics for $PEPU, including allocations for liquidity, project finance, presale, staking, and marketing as outlined in the Pepe Unchained tokenomics section.
Generated: DETERMINISTIC_4bb83904dce3ee40
Batch ID: 20250612_151459
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

// Importing OpenZeppelin's ERC20 implementation for security and standard functionalities
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title Pepe Unchained Token ($PEPU)
 * @dev This contract implements the tokenomics for the $PEPU token, including allocations for liquidity,
 *      project finance, presale, staking, and marketing.
 */
contract PEPU is ERC20, Ownable {
    // Allocation percentages (in basis points)
    uint256 public constant LIQUIDITY_ALLOCATION = 2000;     // 20%
    uint256 public constant PROJECT_FINANCE_ALLOCATION = 3000; // 30%
    uint256 public constant PRESALE_ALLOCATION = 2500;        // 25%
    uint256 public constant STAKING_ALLOCATION = 1500;        // 15%
    uint256 public constant MARKETING_ALLOCATION = 1000;      // 10%

    // Total supply of the token (in tokens)
    uint256 public constant TOTAL_SUPPLY = 1000000000 * 10 ** decimals(); // 1 Billion tokens

    // Addresses for each allocation
    address public liquidityAddress;
    address public projectFinanceAddress;
    address public presaleAddress;
    address public stakingAddress;
    address public marketingAddress;

    // Events for tracking allocations
    event TokensAllocated(address indexed to, uint256 amount);

    /**
     * @dev Constructor that gives msg.sender all of the existing tokens and allocates to specified addresses.
     * @param _liquidityAddress Address for liquidity allocation
     * @param _projectFinanceAddress Address for project finance allocation
     * @param _presaleAddress Address for presale allocation
     * @param _stakingAddress Address for staking allocation
     * @param _marketingAddress Address for marketing allocation
     */
    constructor(
        address _liquidityAddress,
        address _projectFinanceAddress,
        address _presaleAddress,
        address _stakingAddress,
        address _marketingAddress
    ) ERC20("Pepe Unchained", "$PEPU") {
        require(_liquidityAddress != address(0), "Invalid liquidity address");
        require(_projectFinanceAddress != address(0), "Invalid project finance address");
        require(_presaleAddress != address(0), "Invalid presale address");
        require(_stakingAddress != address(0), "Invalid staking address");
        require(_marketingAddress != address(0), "Invalid marketing address");

        liquidityAddress = _liquidityAddress;
        projectFinanceAddress = _projectFinanceAddress;
        presaleAddress = _presaleAddress;
        stakingAddress = _stakingAddress;
        marketingAddress = _marketingAddress;

        // Allocate tokens to each address according to the defined allocations
        _mint(liquidityAddress, (TOTAL_SUPPLY * LIQUIDITY_ALLOCATION) / 10000);
        emit TokensAllocated(liquidityAddress, (TOTAL_SUPPLY * LIQUIDITY_ALLOCATION) / 10000);

        _mint(projectFinanceAddress, (TOTAL_SUPPLY * PROJECT_FINANCE_ALLOCATION) / 10000);
        emit TokensAllocated(projectFinanceAddress, (TOTAL_SUPPLY * PROJECT_FINANCE_ALLOCATION) / 10000);

        _mint(presaleAddress, (TOTAL_SUPPLY * PRESALE_ALLOCATION) / 10000);
        emit TokensAllocated(presaleAddress, (TOTAL_SUPPLY * PRESALE_ALLOCATION) / 10000);

        _mint(stakingAddress, (TOTAL_SUPPLY * STAKING_ALLOCATION) / 10000);
        emit TokensAllocated(stakingAddress, (TOTAL_SUPPLY * STAKING_ALLOCATION) / 10000);

        _mint(marketingAddress, (TOTAL_SUPPLY * MARKETING_ALLOCATION) / 10000);
        emit TokensAllocated(marketingAddress, (TOTAL_SUPPLY * MARKETING_ALLOCATION) / 10000);
    }

    /**
     * @dev Allows the owner to withdraw accidentally sent ERC20 tokens to the contract.
     * @param tokenAddress The address of the token to be withdrawn
     * @param amount The amount of tokens to withdraw
     */
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");
        
        IERC20(tokenAddress).transfer(owner(), amount);
    }
}
```
