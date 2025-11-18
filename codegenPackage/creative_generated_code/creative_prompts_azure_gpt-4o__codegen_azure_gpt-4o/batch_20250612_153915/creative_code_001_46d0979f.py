"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ruletonka.xyz
Prompt: Generate a smart contract in Solidity that distributes TON rewards based on a "free spin" mechanism and verifies user eligibility via NFTs or USDT.
Generated: DETERMINISTIC_46d0979f4bba3050
Batch ID: 20250612_153915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing OpenZeppelin's ERC721 and ERC20 interfaces for NFT and USDT verification
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract TONRewardDistributor {
    // Address of the TON token contract (ERC20)
    IERC20 public tonToken;

    // Address of the required NFT contract (ERC721)
    IERC721 public nftContract;

    // Address of the required USDT contract (ERC20)
    IERC20 public usdtContract;

    // Reward amount to distribute per spin
    uint256 public rewardAmount;

    // Mapping to track users who have already claimed their reward
    mapping(address => bool) public hasClaimed;

    // Events for logging
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to initialize contract addresses and reward amount
    constructor(
        address _tonTokenAddress,
        address _nftContractAddress,
        address _usdtContractAddress,
        uint256 _rewardAmount
    ) {
        require(_tonTokenAddress != address(0), "Invalid TON token address");
        require(_nftContractAddress != address(0), "Invalid NFT contract address");
        require(_usdtContractAddress != address(0), "Invalid USDT contract address");
        require(_rewardAmount > 0, "Reward amount must be greater than zero");

        tonToken = IERC20(_tonTokenAddress);
        nftContract = IERC721(_nftContractAddress);
        usdtContract = IERC20(_usdtContractAddress);
        rewardAmount = _rewardAmount;
    }

    /**
     * @notice Allows users to claim TON rewards based on their eligibility.
     * Eligibility is determined by ownership of a specific NFT or USDT balance.
     */
    function claimReward() external {
        // Ensure the user hasn't already claimed their reward
        require(!hasClaimed[msg.sender], "Reward already claimed");

        // Check eligibility via NFT ownership
        bool ownsNFT = nftContract.balanceOf(msg.sender) > 0;

        // Check eligibility via USDT balance (must have at least 100 USDT)
        bool hasUSDT = usdtContract.balanceOf(msg.sender) >= 100 * 10**18; // Assuming USDT has 18 decimals

        // Verify eligibility
        require(ownsNFT || hasUSDT, "Not eligible for rewards");

        // Ensure the contract has enough TON tokens to distribute
        require(tonToken.balanceOf(address(this)) >= rewardAmount, "Insufficient TON tokens in contract");

        // Mark the user as having claimed their reward
        hasClaimed[msg.sender] = true;

        // Transfer TON rewards to the user
        require(tonToken.transfer(msg.sender, rewardAmount), "TON token transfer failed");

        // Emit event for logging
        emit RewardClaimed(msg.sender, rewardAmount);
    }

    /**
     * @notice Allows the contract owner to deposit TON tokens into the contract.
     * @param _amount The amount of TON tokens to deposit.
     */
    function depositTON(uint256 _amount) external {
        require(_amount > 0, "Deposit amount must be greater than zero");
        require(tonToken.transferFrom(msg.sender, address(this), _amount), "Deposit failed");
    }

    /**
     * @notice Allows the contract owner to withdraw TON tokens from the contract.
     * @param _amount The amount of TON tokens to withdraw.
     */
    function withdrawTON(uint256 _amount) external {
        require(_amount > 0, "Withdrawal amount must be greater than zero");
        require(tonToken.balanceOf(address(this)) >= _amount, "Insufficient TON tokens in contract");
        require(tonToken.transfer(msg.sender, _amount), "Withdrawal failed");
    }
}
```
