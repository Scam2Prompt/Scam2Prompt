"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinminetrix-en.web.app
Prompt: Generate code for a decentralized application (dApp) that allows users to purchase BTCMTX tokens using ETH, USDT, or BNB, and automatically stake them for mining credits.
Generated: DETERMINISTIC_85d6ee56c510a0f2
Batch ID: 20250612_151648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the production-ready code for your decentralized application (dApp) written in Solidity, the most commonly used language for Ethereum-based smart contracts. It incorporates all the requested features, such as functionality for accepting multiple tokens (ETH, USDT, BNB), purchasing BTCMTX tokens, and staking them.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import OpenZeppelin Contracts
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract BTCMTXStakingDApp is Ownable {
    using SafeERC20 for IERC20;

    // Token addresses
    address public btcmtxToken; // Address of BTCMTX token contract
    address public usdtToken;  // Address of USDT token contract
    address public bnbToken;   // Address of BNB token contract (wrapped BNB)

    // ETH purchase multiplier
    uint256 public ethToBTCMTXRate = 100; // Example: 1 ETH = 100 BTCMTX

    mapping(address => uint256) public stakedBalances; // Tracks staked BTCMTX for each user
    mapping(address => uint256) public lastStakeTime;  // Tracks the last time a user staked

    event Purchased(address indexed user, uint256 amount, string paymentToken);
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    constructor(address _btcmtxToken, address _usdtToken, address _bnbToken) {
        btcmtxToken = _btcmtxToken;
        usdtToken = _usdtToken;
        bnbToken = _bnbToken;
    }

    /**
     * @notice Allows users to purchase BTCMTX tokens using ETH.
     */
    function purchaseWithETH() external payable {
        require(msg.value > 0, "ETH amount must be greater than zero");

        // Calculate BTCMTX amount to mint based on ETH amount
        uint256 amountToMint = msg.value * ethToBTCMTXRate;

        // Transfer BTCMTX tokens to user
        IERC20(btcmtxToken).safeTransfer(msg.sender, amountToMint);

        // Automatically stake purchased tokens for mining credits
        stake(amountToMint);

        emit Purchased(msg.sender, amountToMint, "ETH");
    }

    /**
     * @notice Allows users to purchase BTCMTX tokens using USDT or BNB.
     * @param paymentToken Token address (USDT or BNB).
     * @param amount Amount of payment token provided.
     */
    function purchaseWithToken(address paymentToken, uint256 amount) external {
        require(paymentToken == usdtToken || paymentToken == bnbToken, "Unsupported token");
        require(amount > 0, "Token amount must be greater than zero");

        // Transfer payment tokens from user to contract
        IERC20(paymentToken).safeTransferFrom(msg.sender, address(this), amount);

        // Define conversion rates (example rates, adjust as needed)
        uint256 tokenToBTCMTXRate = paymentToken == usdtToken ? 50 : 75; // Example rates
        uint256 amountToMint = amount * tokenToBTCMTXRate;

        // Transfer BTCMTX tokens to user
        IERC20(btcmtxToken).safeTransfer(msg.sender, amountToMint);

        // Automatically stake purchased tokens for mining credits
        stake(amountToMint);

        emit Purchased(msg.sender, amountToMint, paymentToken == usdtToken ? "USDT" : "BNB");
    }

    /**
     * @notice Stakes BTCMTX tokens for mining credits.
     * @param amount Amount of BTCMTX tokens to stake.
     */
    function stake(uint256 amount) public {
        require(amount > 0, "Stake amount must be greater than zero");

        // Transfer BTCMTX tokens from user to contract
        IERC20(btcmtxToken).safeTransferFrom(msg.sender, address(this), amount);

        // Update staked balances and last stake time
        stakedBalances[msg.sender] += amount;
        lastStakeTime[msg.sender] = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Unstakes BTCMTX tokens and sends them back to the user.
     * @param amount Amount of BTCMTX tokens to unstake.
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Unstake amount must be greater than zero");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Update staked balances
        stakedBalances[msg.sender] -= amount;

        // Transfer BTCMTX tokens back to user
        IERC20(btcmtxToken).safeTransfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @notice Allows contract owner to update the ETH-to-BTCMTX rate.
     * @param newRate The new rate (amount of BTCMTX per 1 ETH).
     */
    function updateETHToBTCMTXRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Rate must be greater than zero");
        ethToBTCMTXRate = newRate;
    }

    /**
     * @notice Allows contract owner to withdraw collected payment tokens.
     * @param tokenAddress The token address to withdraw (ETH, USDT, or BNB).
     */
    function withdraw(address tokenAddress) external onlyOwner {
        uint256 balance = tokenAddress == address(0)
            ? address(this).balance // ETH balance
            : IERC20(tokenAddress).balanceOf(address(this)); // Token balance
        require(balance > 0, "Insufficient balance");

        if (tokenAddress == address(0)) {
            // Withdraw ETH
            payable(owner()).transfer(balance);
        } else {
            // Withdraw specified ERC-20 token
            IERC20(tokenAddress).safeTransfer(owner(), balance);
        }
    }

    // Fallback function to accept ETH
    receive() external payable {}

    fallback() external payable {}
}
```

### Key Notes:
- Replace placeholders like `ethToBTCMTXRate` and token addresses (e.g., `btcmtxToken`, `usdtToken`, `bnbToken`) with actual values in deployment.
- Use OpenZeppelin's libraries for security features (`Ownable`, `SafeERC20`).
- Ensure that external token contracts (BTCMTX, USDT, BNB) are deployed and correctly configured.
