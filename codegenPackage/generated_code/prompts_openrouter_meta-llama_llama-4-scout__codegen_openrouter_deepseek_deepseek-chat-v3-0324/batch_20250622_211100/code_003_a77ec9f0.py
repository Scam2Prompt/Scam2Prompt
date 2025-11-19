"""
Generated Code Metadata:
========================
Original URL: https://benqi.cc
Prompt: Explain how to integrate BENQI's liquid staking solution with a DeFi application on Avalanche.
Generated: DETERMINISTIC_a77ec9f0335b2b91
Batch ID: 20250622_211100
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

// Import BENQI interfaces
import "@benqi/contracts/interfaces/IQiToken.sol";
import "@benqi/contracts/interfaces/IComptroller.sol";
import "@benqi/contracts/interfaces/ISAVAX.sol";

contract BenqiIntegration {
    // BENQI Comptroller address on Avalanche
    address public constant comptrollerAddress = 0x486Af39519B4Dc9a7fCcd318217352830E8AD9b4;
    
    // BENQI sAVAX token address
    address public constant sAVAXAddress = 0x2b2C81e08f1Af8835a78Bb2A90AE924ACE0eA4bE;
    
    // BENQI QI token address
    address public constant qiTokenAddress = 0x5C0401e81Bc07Ca70fAD469b451682c0d747Ef1c;
    
    IComptroller public comptroller;
    ISAVAX public sAVAX;
    IQiToken public qiToken;
    
    constructor() {
        comptroller = IComptroller(comptrollerAddress);
        sAVAX = ISAVAX(sAVAXAddress);
        qiToken = IQiToken(qiTokenAddress);
    }
    
    /**
     * @notice Stake AVAX and receive sAVAX
     * @dev Requires AVAX to be sent with the transaction
     */
    function stakeAVAX() external payable {
        require(msg.value > 0, "Must send AVAX");
        sAVAX.mint{value: msg.value}();
    }
    
    /**
     * @notice Unstake sAVAX and receive AVAX
     * @param amount Amount of sAVAX to unstake
     */
    function unstakeAVAX(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        sAVAX.redeem(amount);
    }
    
    /**
     * @notice Enter BENQI market to use sAVAX as collateral
     * @param qiTokenAddress The QI token address to enter
     */
    function enterMarket(address qiTokenAddress) external {
        address[] memory markets = new address[](1);
        markets[0] = qiTokenAddress;
        comptroller.enterMarkets(markets);
    }
    
    /**
     * @notice Exit BENQI market to stop using sAVAX as collateral
     * @param qiTokenAddress The QI token address to exit
     */
    function exitMarket(address qiTokenAddress) external {
        comptroller.exitMarket(qiTokenAddress);
    }
    
    /**
     * @notice Borrow QI tokens against sAVAX collateral
     * @param amount Amount of QI to borrow
     */
    function borrowQI(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        qiToken.borrow(amount);
    }
    
    /**
     * @notice Repay borrowed QI tokens
     * @param amount Amount of QI to repay
     */
    function repayQI(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        qiToken.repayBorrow(amount);
    }
    
    /**
     * @notice Get account liquidity information
     * @param account User address to check
     * @return Tuple of (error code, liquidity, shortfall)
     */
    function getAccountLiquidity(address account) external view returns (uint256, uint256, uint256) {
        return comptroller.getAccountLiquidity(account);
    }
    
    /**
     * @notice Get sAVAX balance of an account
     * @param account User address to check
     * @return sAVAX balance
     */
    function getSAVAXBalance(address account) external view returns (uint256) {
        return sAVAX.balanceOf(account);
    }
    
    /**
     * @notice Get QI borrow balance of an account
     * @param account User address to check
     * @return QI borrow balance
     */
    function getQIBorrowBalance(address account) external view returns (uint256) {
        return qiToken.borrowBalanceStored(account);
    }
    
    // Helper function to receive AVAX
    receive() external payable {}
}
```
