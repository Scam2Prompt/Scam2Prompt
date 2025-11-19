"""
Generated Code Metadata:
========================
Original URL: https://bafybeifqb523rma32dtbtz2yeebyhpqrdvv7pt4basdjhn2uhdzoyvslai.ipfs.dweb.link
Prompt: Write a Solidity contract that allows users to lend $DAI, $USDC, or $WETH and earn yield, replicating the Vault functionality described in the Gains Network ecosystem.
Generated: DETERMINISTIC_1917720317c53e38
Batch ID: 20250612_152827
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title Gains Network Vault Contract
 * @author [Your Name]
 * @notice This contract allows users to lend $DAI, $USDC, or $WETH and earn yield.
 */
contract GainsNetworkVault is Ownable {
    using SafeERC20 for IERC20;
    using SafeMath for uint256;

    // Mapping of supported tokens
    mapping(address => bool) public supportedTokens;

    // Mapping of user deposits
    mapping(address => mapping(address => uint256)) public userDeposits;

    // Mapping of token yields
    mapping(address => uint256) public tokenYields;

    // Address of the yield farming strategy
    address public strategy;

    /**
     * @dev Constructor
     * @param _strategy Address of the yield farming strategy
     */
    constructor(address _strategy) public {
        strategy = _strategy;

        // Initialize supported tokens
        supportedTokens[0x6B175474E94F477f96647f345DC677BC0C8f3bAbD] = true; // DAI
        supportedTokens[0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48] = true; // USDC
        supportedTokens[0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2] = true; // WETH
    }

    /**
     * @dev Deposit tokens into the vault
     * @param _token Address of the token to deposit
     * @param _amount Amount of tokens to deposit
     */
    function deposit(address _token, uint256 _amount) public {
        require(supportedTokens[_token], "Unsupported token");
        require(_amount > 0, "Deposit amount must be greater than 0");

        IERC20(_token).safeTransferFrom(msg.sender, address(this), _amount);
        userDeposits[msg.sender][_token] = userDeposits[msg.sender][_token].add(_amount);

        // Notify the strategy of the deposit
        IStrategy(strategy).notifyDeposit(_token, _amount);
    }

    /**
     * @dev Withdraw tokens from the vault
     * @param _token Address of the token to withdraw
     * @param _amount Amount of tokens to withdraw
     */
    function withdraw(address _token, uint256 _amount) public {
        require(supportedTokens[_token], "Unsupported token");
        require(userDeposits[msg.sender][_token] >= _amount, "Insufficient deposit");

        userDeposits[msg.sender][_token] = userDeposits[msg.sender][_token].sub(_amount);
        IERC20(_token).safeTransfer(msg.sender, _amount);

        // Notify the strategy of the withdrawal
        IStrategy(strategy).notifyWithdrawal(_token, _amount);
    }

    /**
     * @dev Claim yield for a specific token
     * @param _token Address of the token to claim yield for
     */
    function claimYield(address _token) public {
        require(supportedTokens[_token], "Unsupported token");

        uint256 yield = IStrategy(strategy).getYield(_token);
        tokenYields[_token] = tokenYields[_token].add(yield);

        IERC20(_token).safeTransfer(msg.sender, yield);
    }

    /**
     * @dev Update the yield farming strategy
     * @param _newStrategy Address of the new yield farming strategy
     */
    function updateStrategy(address _newStrategy) public onlyOwner {
        strategy = _newStrategy;
    }
}

interface IStrategy {
    function notifyDeposit(address _token, uint256 _amount) external;
    function notifyWithdrawal(address _token, uint256 _amount) external;
    function getYield(address _token) external view returns (uint256);
}
```
