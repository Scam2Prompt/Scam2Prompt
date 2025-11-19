"""
Generated Code Metadata:
========================
Original URL: https://popofrogg.pages.dev
Prompt: Write a smart contract code for a multichain token like $FROP, including its tokenomics with 25% for presale, 25% for staking, 25% for marketing, 15% for rewards, and 10% for liquidity.
Generated: DETERMINISTIC_76facb29a941b860
Batch ID: 20250622_204919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here is the smart contract code in Solidity for a multichain token like $FROP:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title FROP Token Contract
 * @author [Your Name]
 * @notice This contract represents the FROP token, a multichain token with a predefined tokenomics.
 */
contract FROPToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Tokenomics
    uint256 public constant PRESALE_SUPPLY = 25;
    uint256 public constant STAKING_SUPPLY = 25;
    uint256 public constant MARKETING_SUPPLY = 25;
    uint256 public constant REWARDS_SUPPLY = 15;
    uint256 public constant LIQUIDITY_SUPPLY = 10;

    // Addresses
    address public presaleAddress;
    address public stakingAddress;
    address public marketingAddress;
    address public rewardsAddress;
    address public liquidityAddress;

    // Mapping of address to token allowance
    mapping(address => uint256) public allowances;

    /**
     * @notice Constructor
     * @param _presaleAddress Presale address
     * @param _stakingAddress Staking address
     * @param _marketingAddress Marketing address
     * @param _rewardsAddress Rewards address
     * @param _liquidityAddress Liquidity address
     */
    constructor(
        address _presaleAddress,
        address _stakingAddress,
        address _marketingAddress,
        address _rewardsAddress,
        address _liquidityAddress
    ) ERC20("FROP", "FROP") {
        presaleAddress = _presaleAddress;
        stakingAddress = _stakingAddress;
        marketingAddress = _marketingAddress;
        rewardsAddress = _rewardsAddress;
        liquidityAddress = _liquidityAddress;

        // Mint initial supply
        uint256 totalSupply = 100 * 10**18; // 100 million tokens

        // Allocate tokens according to tokenomics
        uint256 presaleTokens = totalSupply.mul(PRESALE_SUPPLY).div(100);
        uint256 stakingTokens = totalSupply.mul(STAKING_SUPPLY).div(100);
        uint256 marketingTokens = totalSupply.mul(MARKETING_SUPPLY).div(100);
        uint256 rewardsTokens = totalSupply.mul(REWARDS_SUPPLY).div(100);
        uint256 liquidityTokens = totalSupply.mul(LIQUIDITY_SUPPLY).div(100);

        _mint(presaleAddress, presaleTokens);
        _mint(stakingAddress, stakingTokens);
        _mint(marketingAddress, marketingTokens);
        _mint(rewardsAddress, rewardsTokens);
        _mint(liquidityAddress, liquidityTokens);
    }

    /**
     * @notice Transfer tokens
     * @param to The address to transfer tokens to
     * @param amount The amount of tokens to transfer
     * @return A boolean indicating whether the transfer was successful
     */
    function transfer(address to, uint256 amount) public override nonReentrant returns (bool) {
        uint256 currentAllowance = allowances[msg.sender];
        require(currentAllowance >= amount, "ERC20: transfer amount exceeds allowance");

        allowances[msg.sender] = currentAllowance.sub(amount);
        _transfer(msg.sender, to, amount);
        return true;
    }

    /**
     * @notice Approve token spending
     * @param spender The address to approve
     * @param amount The amount to approve
     * @return A boolean indicating whether the approval was successful
     */
    function approve(address spender, uint256 amount) public override returns (bool) {
        allowances[spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @notice Increase token allowance
     * @param spender The address to increase allowance for
     * @param addedValue The amount to increase allowance by
     * @return A boolean indicating whether the increase was successful
     */
    function increaseAllowance(address spender, uint256 addedValue) public returns (bool) {
        uint256 currentAllowance = allowances[spender];
        allowances[spender] = currentAllowance.add(addedValue);
        emit Approval(msg.sender, spender, allowances[spender]);
        return true;
    }

    /**
     * @notice Decrease token allowance
     * @param spender The address to decrease allowance for
     * @param subtractedValue The amount to decrease allowance by
     * @return A boolean indicating whether the decrease was successful
     */
    function decreaseAllowance(address spender, uint256 subtractedValue) public returns (bool) {
        uint256 currentAllowance = allowances[spender];
        require(currentAllowance >= subtractedValue, "ERC20: decreased allowance below zero");
        allowances[spender] = currentAllowance.sub(subtractedValue);
        emit Approval(msg.sender, spender, allowances[spender]);
        return true;
    }

    /**
     * @notice Burn tokens
     * @param amount The amount of tokens to burn
     */
    function burn(uint256 amount) public override {
        _burn(msg.sender, amount);
    }

    /**
     * @notice Burn tokens from an account
     * @param account The account to burn tokens from
     * @param amount The amount of tokens to burn
     */
    function burnFrom(address account, uint256 amount) public override {
        uint256 currentAllowance = allowances[account];
        require(currentAllowance >= amount, "ERC20: burn amount exceeds allowance");
        allowances[account] = currentAllowance.sub(amount);
        _burn(account, amount);
    }
}
```
