"""
Generated Code Metadata:
========================
Original URL: https://moonwell.site
Prompt: Develop a Solidity contract to test Moonwell's interoperability features, focusing on cross-chain asset transfers between Moonbeam and Moonriver.
Generated: DETERMINISTIC_548b3b136f4ff885
Batch ID: 20250612_145616
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title MoonwellInteroperabilityTest
 * @author [Your Name]
 * @notice This contract tests Moonwell's interoperability features, specifically cross-chain asset transfers between Moonbeam and Moonriver.
 */
contract MoonwellInteroperabilityTest {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of supported tokens
    mapping(address => bool) public supportedTokens;

    // Mapping of token balances for testing purposes
    mapping(address => mapping(address => uint256)) public tokenBalances;

    /**
     * @param _token Address of the token to be supported
     */
    function addSupportedToken(address _token) public {
        require(_token != address(0), "Token address cannot be zero");
        supportedTokens[_token] = true;
    }

    /**
     * @param _token Address of the token to be removed
     */
    function removeSupportedToken(address _token) public {
        require(_token != address(0), "Token address cannot be zero");
        supportedTokens[_token] = false;
    }

    /**
     * @param _token Address of the token to transfer
     * @param _amount Amount of tokens to transfer
     * @param _recipient Address of the recipient on the other chain
     */
    function transferTokensCrossChain(address _token, uint256 _amount, address _recipient) public {
        require(supportedTokens[_token], "Token is not supported");
        require(_amount > 0, "Transfer amount must be greater than zero");

        // Simulate token transfer from Moonbeam to Moonriver or vice versa
        // Replace with actual cross-chain transfer logic
        tokenBalances[msg.sender][_token] = tokenBalances[msg.sender][_token].sub(_amount);
        tokenBalances[_recipient][_token] = tokenBalances[_recipient][_token].add(_amount);

        IERC20(_token).safeTransferFrom(msg.sender, address(this), _amount);
        IERC20(_token).safeTransfer(_recipient, _amount);
    }

    /**
     * @param _token Address of the token
     * @param _amount Amount of tokens to deposit
     */
    function depositTokens(address _token, uint256 _amount) public {
        require(supportedTokens[_token], "Token is not supported");
        require(_amount > 0, "Deposit amount must be greater than zero");

        IERC20(_token).safeTransferFrom(msg.sender, address(this), _amount);
        tokenBalances[msg.sender][_token] = tokenBalances[msg.sender][_token].add(_amount);
    }

    /**
     * @param _token Address of the token
     * @param _amount Amount of tokens to withdraw
     */
    function withdrawTokens(address _token, uint256 _amount) public {
        require(supportedTokens[_token], "Token is not supported");
        require(_amount > 0, "Withdrawal amount must be greater than zero");
        require(tokenBalances[msg.sender][_token] >= _amount, "Insufficient balance");

        tokenBalances[msg.sender][_token] = tokenBalances[msg.sender][_token].sub(_amount);
        IERC20(_token).safeTransfer(msg.sender, _amount);
    }

    /**
     * @param _token Address of the token
     */
    function getTokenBalance(address _token, address _user) public view returns (uint256) {
        return tokenBalances[_user][_token];
    }
}
```
