"""
Generated Code Metadata:
========================
Original URL: https://aethirclaim-ifbf5prj-iamsorryman.4everland.app
Prompt: Write a Solidity contract that includes functionality for tracking deposits and distributing tokens proportionally during a presale, with a cap of 1000 ETH.
Generated: DETERMINISTIC_236efcb260bdb0d2
Batch ID: 20250612_145436
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title PresaleContract
 * @author [Your Name]
 * @notice A contract for tracking deposits and distributing tokens proportionally during a presale.
 */
contract PresaleContract is ReentrancyGuard {
    // Mapping of user deposits
    mapping (address => uint256) public deposits;

    // Total deposited ETH
    uint256 public totalDeposited;

    // Cap for presale in ETH
    uint256 public constant PRESALE_CAP = 1000 ether;

    // Token to be distributed
    ERC20 public token;

    // Token distribution rate (1:1, for example, 1 ETH = 10 tokens)
    uint256 public tokenDistributionRate;

    // Flag to check if presale is active
    bool public isPresaleActive;

    // Event emitted when deposit is made
    event DepositMade(address indexed user, uint256 amount);

    // Event emitted when tokens are distributed
    event TokensDistributed(address indexed user, uint256 amount);

    /**
     * @param _tokenAddress Address of the token to be distributed
     * @param _tokenDistributionRate Rate at which tokens are distributed per ETH
     */
    constructor(address _tokenAddress, uint256 _tokenDistributionRate) {
        require(_tokenAddress != address(0), "Token address cannot be zero");
        require(_tokenDistributionRate > 0, "Token distribution rate must be greater than zero");

        token = ERC20(_tokenAddress);
        tokenDistributionRate = _tokenDistributionRate;

        // Initialize presale as active
        isPresaleActive = true;
    }

    /**
     * @notice Make a deposit
     */
    function makeDeposit() external payable nonReentrant {
        require(msg.value > 0, "Deposit amount must be greater than zero");
        require(totalDeposited + msg.value <= PRESALE_CAP, "Presale cap exceeded");
        require(isPresaleActive, "Presale is not active");

        deposits[msg.sender] += msg.value;
        totalDeposited += msg.value;

        emit DepositMade(msg.sender, msg.value);
    }

    /**
     * @notice Distribute tokens to users
     */
    function distributeTokens() external nonReentrant {
        require(!isPresaleActive, "Presale is still active");
        require(totalDeposited > 0, "No deposits to distribute");

        uint256 tokensToDistribute = totalDeposited * tokenDistributionRate;

        // Ensure token contract has sufficient balance
        require(token.balanceOf(address(this)) >= tokensToDistribute, "Insufficient tokens for distribution");

        for (address user in deposits) {
            uint256 userDeposit = deposits[user];
            uint256 tokensForUser = (userDeposit * tokenDistributionRate);

            // Transfer tokens to user
            require(token.transfer(user, tokensForUser), "Token transfer failed");

            emit TokensDistributed(user, tokensForUser);
        }

        // Reset deposits and total deposited
        for (address user in deposits) {
            deposits[user] = 0;
        }

        totalDeposited = 0;
    }

    /**
     * @notice End presale
     */
    function endPresale() external {
        require(isPresaleActive, "Presale is not active");
        require(msg.sender == owner(), "Only owner can end presale");

        isPresaleActive = false;
    }

    /**
     * @notice Withdraw remaining tokens
     */
    function withdrawTokens() external {
        require(!isPresaleActive, "Presale is still active");
        require(msg.sender == owner(), "Only owner can withdraw tokens");

        uint256 remainingTokens = token.balanceOf(address(this));

        require(token.transfer(msg.sender, remainingTokens), "Token transfer failed");
    }
}
```
