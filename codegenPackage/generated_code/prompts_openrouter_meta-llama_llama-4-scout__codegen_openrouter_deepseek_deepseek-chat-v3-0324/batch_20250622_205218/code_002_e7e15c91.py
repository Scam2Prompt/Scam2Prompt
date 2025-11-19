"""
Generated Code Metadata:
========================
Original URL: https://arbitrum-token-bridge-mtrh5hnjn-offchain-labs.vercel.app
Prompt: How can I implement a decentralized application (dApp) on Arbitrum L2 that utilizes the CCTP for direct USDC transfers with Ethereum, and what are the benefits of doing so?
Generated: DETERMINISTIC_e7e15c91b43b2db4
Batch ID: 20250622_205218
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/Address.sol";

/**
 * @title CrossChainUSDCTokenBridge
 * @dev A contract for bridging USDC between Ethereum and Arbitrum using CCTP
 */
contract CrossChainUSDCTokenBridge is ReentrancyGuard {
    using Address for address;

    // CCTP contract addresses (example addresses - replace with actual)
    address public constant CCTP_ETHEREUM = 0x123...;
    address public constant CCTP_ARBITRUM = 0x456...;
    
    // USDC token addresses
    address public immutable usdcEthereum;
    address public immutable usdcArbitrum;

    // Events
    event DepositInitiated(
        address indexed sender,
        address indexed recipient,
        uint256 amount,
        uint256 timestamp
    );
    event WithdrawalCompleted(
        address indexed recipient,
        uint256 amount,
        uint256 timestamp
    );

    /**
     * @dev Constructor
     * @param _usdcEthereum USDC address on Ethereum
     * @param _usdcArbitrum USDC address on Arbitrum
     */
    constructor(address _usdcEthereum, address _usdcArbitrum) {
        require(
            _usdcEthereum != address(0) && _usdcArbitrum != address(0),
            "Invalid token address"
        );
        usdcEthereum = _usdcEthereum;
        usdcArbitrum = _usdcArbitrum;
    }

    /**
     * @dev Deposit USDC to be bridged to Arbitrum
     * @param amount Amount of USDC to bridge
     * @param recipient Address to receive funds on Arbitrum
     */
    function depositToArbitrum(uint256 amount, address recipient) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(recipient != address(0), "Invalid recipient address");

        IERC20 usdc = IERC20(usdcEthereum);
        require(
            usdc.transferFrom(msg.sender, address(this), amount),
            "Transfer failed"
        );

        // Approve CCTP to spend USDC
        usdc.approve(CCTP_ETHEREUM, amount);

        // Call CCTP bridge function (implementation depends on CCTP interface)
        // This is a placeholder - actual implementation will depend on CCTP's API
        (bool success, ) = CCTP_ETHEREUM.call(
            abi.encodeWithSignature(
                "depositFor(address,uint256,address)",
                recipient,
                amount,
                usdcArbitrum
            )
        );
        require(success, "CCTP deposit failed");

        emit DepositInitiated(msg.sender, recipient, amount, block.timestamp);
    }

    /**
     * @dev Complete withdrawal from Arbitrum (called by CCTP)
     * @param recipient Address to receive funds
     * @param amount Amount of USDC to withdraw
     */
    function completeWithdrawal(address recipient, uint256 amount) external nonReentrant {
        require(msg.sender == CCTP_ARBITRUM, "Unauthorized");
        require(amount > 0, "Amount must be greater than 0");
        require(recipient != address(0), "Invalid recipient address");

        IERC20 usdc = IERC20(usdcArbitrum);
        require(usdc.transfer(recipient, amount), "Transfer failed");

        emit WithdrawalCompleted(recipient, amount, block.timestamp);
    }

    /**
     * @dev Emergency function to withdraw stuck tokens
     * @param tokenAddress Address of the token to withdraw
     * @param amount Amount to withdraw
     */
    function emergencyWithdraw(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than 0");
        
        IERC20 token = IERC20(tokenAddress);
        require(token.transfer(msg.sender, amount), "Transfer failed");
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Not owner");
        _;
    }

    address public owner;

    /**
     * @dev Transfer ownership
     * @param newOwner Address of new owner
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid owner address");
        owner = newOwner;
    }
}
```
