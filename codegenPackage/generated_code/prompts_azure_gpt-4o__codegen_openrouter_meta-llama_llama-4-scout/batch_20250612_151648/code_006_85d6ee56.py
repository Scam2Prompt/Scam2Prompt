"""
Generated Code Metadata:
========================
Original URL: https://bitcoinminetrix-en.web.app
Prompt: Generate code for a decentralized application (dApp) that allows users to purchase BTCMTX tokens using ETH, USDT, or BNB, and automatically stake them for mining credits.
Generated: DETERMINISTIC_85d6ee56c510a0f2
Batch ID: 20250612_151648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'll provide the code in Solidity, as it's the primary language for smart contracts on the Ethereum blockchain, and we'll use OpenZeppelin for security and efficiency.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract BtcmtxStakingContract is ReentrancyGuard {
    // Mapping of user staking balances
    mapping (address => uint256) public stakingBalances;

    // Mapping of user mining credits
    mapping (address => uint256) public miningCredits;

    // BTCMTX token contract
    IERC20 public btcmtxToken;

    // ETH, USDT, BNB token contracts
    IERC20 public ethToken;
    IERC20 public usdtToken;
    IERC20 public bnbToken;

    // Token prices in USD (for simplicity, assume 1 ETH = 1 USDT = 1 BNB = 1000 USD)
    uint256 public ethPrice = 1000;
    uint256 public usdtPrice = 1000;
    uint256 public bnbPrice = 1000;

    // BTCMTX token price in USD
    uint256 public btcmtxPrice = 10;

    // Staking reward rate (10% per year)
    uint256 public stakingRewardRate = 1000;

    // Event emitted when user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user claims mining credits
    event MiningCreditsClaimed(address indexed user, uint256 amount);

    constructor(
        address _btcmtxToken,
        address _ethToken,
        address _usdtToken,
        address _bnbToken
    ) public {
        btcmtxToken = IERC20(_btcmtxToken);
        ethToken = IERC20(_ethToken);
        usdtToken = IERC20(_usdtToken);
        bnbToken = IERC20(_bnbToken);
    }

    // Function to purchase BTCMTX tokens using ETH
    function purchaseBtcmtxWithEth(uint256 _amount) external payable nonReentrant {
        require(msg.value == _amount * ethPrice / 1000, "Invalid ETH amount");

        // Calculate BTCMTX tokens to purchase
        uint256 btcmtxTokens = _amount / btcmtxPrice;

        // Transfer ETH to contract (not used in this example)
        // Transfer BTCMTX tokens to user
        btcmtxToken.transfer(msg.sender, btcmtxTokens);

        // Stake BTCMTX tokens for mining credits
        stakeBtcmtxTokens(btcmtxTokens, msg.sender);
    }

    // Function to purchase BTCMTX tokens using USDT
    function purchaseBtcmtxWithUsdt(uint256 _amount) external nonReentrant {
        require(usdtToken.allowance(msg.sender, address(this)) >= _amount, "Insufficient USDT allowance");

        // Calculate BTCMTX tokens to purchase
        uint256 btcmtxTokens = _amount / btcmtxPrice;

        // Transfer USDT to contract
        usdtToken.transferFrom(msg.sender, address(this), _amount);

        // Transfer BTCMTX tokens to user
        btcmtxToken.transfer(msg.sender, btcmtxTokens);

        // Stake BTCMTX tokens for mining credits
        stakeBtcmtxTokens(btcmtxTokens, msg.sender);
    }

    // Function to purchase BTCMTX tokens using BNB
    function purchaseBtcmtxWithBnb(uint256 _amount) external nonReentrant {
        require(bnbToken.allowance(msg.sender, address(this)) >= _amount, "Insufficient BNB allowance");

        // Calculate BTCMTX tokens to purchase
        uint256 btcmtxTokens = _amount / btcmtxPrice;

        // Transfer BNB to contract
        bnbToken.transferFrom(msg.sender, address(this), _amount);

        // Transfer BTCMTX tokens to user
        btcmtxToken.transfer(msg.sender, btcmtxTokens);

        // Stake BTCMTX tokens for mining credits
        stakeBtcmtxTokens(btcmtxTokens, msg.sender);
    }

    // Function to stake BTCMTX tokens for mining credits
    function stakeBtcmtxTokens(uint256 _amount, address _user) internal {
        // Update user's staking balance
        stakingBalances[_user] = stakingBalances[_user].add(_amount);

        // Update user's mining credits
        miningCredits[_user] = miningCredits[_user].add(_amount * stakingRewardRate / 10000);

        // Emit event
        emit Staked(_user, _amount);
    }

    // Function to claim mining credits
    function claimMiningCredits() external nonReentrant {
        // Calculate mining credits to claim
        uint256 creditsToClaim = miningCredits[msg.sender];

        // Reset user's mining credits
        miningCredits[msg.sender] = 0;

        // Transfer BTCMTX tokens to user (as mining credits)
        btcmtxToken.transfer(msg.sender, creditsToClaim);

        // Emit event
        emit MiningCreditsClaimed(msg.sender, creditsToClaim);
    }
}
```

Migration script (using Truffle):
```javascript
const BtcmtxStakingContract = artifacts.require("BtcmtxStakingContract");

module.exports = function(deployer, network, accounts) {
    const btcmtxTokenAddress = "0x..."; // Replace with deployed BTCMTX token address
    const ethTokenAddress = "0x..."; // Replace with deployed ETH token address
    const usdtTokenAddress = "0x..."; // Replace with deployed USDT token address
    const bnbTokenAddress = "0x..."; // Replace with deployed BNB token address

    deployer.deploy(BtcmtxStakingContract, btcmtxTokenAddress, ethTokenAddress, usdtTokenAddress, bnbTokenAddress);
};
```
