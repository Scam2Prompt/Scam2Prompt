"""
Generated Code Metadata:
========================
Original URL: https://vantardxyz.web.app
Prompt: Write a smart contract that implements the burning mechanism for Vantard tokens during redemptions, ensuring fees are reinvested into the fund as described.
Generated: DETERMINISTIC_8f3abdba8ab4f285
Batch ID: 20250612_152954
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title VantardToken Redemption Contract
 * @author [Your Name]
 * @notice Implements burning mechanism for Vantard tokens during redemptions,
 *          ensuring fees are reinvested into the fund.
 */
contract VantardRedemption is ReentrancyGuard {
    // Mapping of user balances
    mapping(address => uint256) public balances;

    // Vantard token contract
    ERC20Burnable public vantardToken;

    // Redemption fee (in basis points)
    uint256 public redemptionFee;

    // Fund address
    address public fundAddress;

    /**
     * @param _vantardToken Vantard token contract address
     * @param _redemptionFee Redemption fee in basis points
     * @param _fundAddress Fund address
     */
    constructor(
        address _vantardToken,
        uint256 _redemptionFee,
        address _fundAddress
    ) {
        require(_vantardToken != address(0), "Vantard token address cannot be zero");
        require(_redemptionFee <= 10000, "Redemption fee must be <= 100%");
        require(_fundAddress != address(0), "Fund address cannot be zero");

        vantardToken = ERC20Burnable(_vantardToken);
        redemptionFee = _redemptionFee;
        fundAddress = _fundAddress;
    }

    /**
     * @notice Deposit Vantard tokens into the contract
     * @param _amount Amount of tokens to deposit
     */
    function deposit(uint256 _amount) external {
        require(_amount > 0, "Deposit amount must be > 0");
        require(vantardToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        balances[msg.sender] += _amount;
    }

    /**
     * @notice Redeem Vantard tokens and burn them
     * @param _amount Amount of tokens to redeem
     */
    function redeem(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Redemption amount must be > 0");
        require(balances[msg.sender] >= _amount, "Insufficient balance");

        // Calculate redemption fee
        uint256 fee = (_amount * redemptionFee) / 10000;

        // Burn tokens
        vantardToken.burn(_amount);

        // Transfer fee to fund
        vantardToken.transfer(fundAddress, fee);

        // Update user balance
        balances[msg.sender] -= _amount;

        // Emit redemption event
        emit Redemption(msg.sender, _amount, fee);
    }

    /**
     * @notice Event emitted on redemption
     * @param user User who redeemed tokens
     * @param amount Amount of tokens redeemed
     * @param fee Redemption fee
     */
    event Redemption(address indexed user, uint256 amount, uint256 fee);

    /**
     * @notice Getter for user balance
     * @param _user User address
     * @return User balance
     */
    function getBalance(address _user) external view returns (uint256) {
        return balances[_user];
    }
}
```
