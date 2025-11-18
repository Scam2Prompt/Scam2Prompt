"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeifqb523rma32dtbtz2yeebyhpqrdvv7pt4basdjhn2uhdzoyvslai.ipfs.dweb.link
Prompt: Write a Solidity contract that allows users to lend $DAI, $USDC, or $WETH and earn yield, replicating the Vault functionality described in the Gains Network ecosystem.
Generated: DETERMINISTIC_1917720317c53e38
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title YieldVault
 * @dev A contract that allows users to lend ERC20 tokens ($DAI, $USDC, $WETH)
 *      and earn yield, replicating Vault functionality similar to Gains Network.
 */
 
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract YieldVault is Ownable, ReentrancyGuard {
    // Supported tokens for lending
    IERC20 public dai;
    IERC20 public usdc;
    IERC20 public weth;

    // Tracks deposits of each user for each token
    mapping(address => mapping(IERC20 => uint256)) public deposits;

    // Yield balances for each user
    mapping(address => uint256) public yieldBalance;

    // Total tokens lent in the vault
    mapping(IERC20 => uint256) public totalLent;

    // Yield rate per token (in basis points, e.g., 100 = 1%)
    mapping(IERC20 => uint256) public yieldRate;

    // Event declarations
    event Deposited(address indexed user, IERC20 token, uint256 amount);
    event Withdrawn(address indexed user, IERC20 token, uint256 amount);
    event YieldClaimed(address indexed user, uint256 amount);
    event YieldRateUpdated(IERC20 token, uint256 newRate);

    /**
     * @dev Initialize the contract with supported tokens.
     * @param _dai Address of the $DAI token contract.
     * @param _usdc Address of the $USDC token contract.
     * @param _weth Address of the $WETH token contract.
     */
    constructor(IERC20 _dai, IERC20 _usdc, IERC20 _weth) {
        dai = _dai;
        usdc = _usdc;
        weth = _weth;
    }

    /**
     * @dev Deposit tokens into the vault to start earning yield.
     * @param token The ERC20 token to deposit ($DAI, $USDC, $WETH).
     * @param amount The amount of tokens to deposit.
     */
    function deposit(IERC20 token, uint256 amount) external nonReentrant {
        require(isSupportedToken(token), "Unsupported token");
        require(amount > 0, "Amount must be greater than zero");

        // Transfer tokens from user to the contract
        token.transferFrom(msg.sender, address(this), amount);

        // Update deposits and total lent
        deposits[msg.sender][token] += amount;
        totalLent[token] += amount;

        emit Deposited(msg.sender, token, amount);
    }

    /**
     * @dev Withdraw tokens from the vault.
     * @param token The ERC20 token to withdraw ($DAI, $USDC, $WETH).
     * @param amount The amount of tokens to withdraw.
     */
    function withdraw(IERC20 token, uint256 amount) external nonReentrant {
        require(isSupportedToken(token), "Unsupported token");
        require(deposits[msg.sender][token] >= amount, "Insufficient balance");

        // Update deposits and total lent
        deposits[msg.sender][token] -= amount;
        totalLent[token] -= amount;

        // Transfer tokens back to the user
        token.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, token, amount);
    }

    /**
     * @dev Claim accumulated yield.
     */
    function claimYield() external nonReentrant {
        uint256 yield = calculateYield(msg.sender);
        require(yield > 0, "No yield available");

        // Reset yield balance
        yieldBalance[msg.sender] = 0;

        // Transfer yield (in a stablecoin, e.g., $DAI)
        dai.transfer(msg.sender, yield);

        emit YieldClaimed(msg.sender, yield);
    }

    /**
     * @dev Update the yield rate for a specific token.
     * @param token The ERC20 token ($DAI, $USDC, $WETH).
     * @param rate The new yield rate in basis points (e.g., 100 = 1%).
     */
    function updateYieldRate(IERC20 token, uint256 rate) external onlyOwner {
        require(isSupportedToken(token), "Unsupported token");
        yieldRate[token] = rate;

        emit YieldRateUpdated(token, rate);
    }

    /**
     * @dev Calculate the yield for a user based on their deposits.
     * @param user The address of the user.
     * @return The amount of yield available for the user.
     */
    function calculateYield(address user) public view returns (uint256) {
        uint256 totalYield = 0;

        // Iterate over supported tokens
        if (deposits[user][dai] > 0) {
            totalYield += (deposits[user][dai] * yieldRate[dai]) / 10000;
        }
        if (deposits[user][usdc] > 0) {
            totalYield += (deposits[user][usdc] * yieldRate[usdc]) / 10000;
        }
        if (deposits[user][weth] > 0) {
            totalYield += (deposits[user][weth] * yieldRate[weth]) / 10000;
        }

        return totalYield;
    }

    /**
     * @dev Helper function to check if a token is supported.
     * @param token The ERC20 token to check.
     * @return True if the token is supported, false otherwise.
     */
    function isSupportedToken(IERC20 token) internal view returns (bool) {
        return (token == dai || token == usdc || token == weth);
    }
}
```
