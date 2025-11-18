"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://9eth.eu
Prompt: Create a guide for integrating a governance token distribution system into an ETH airdrop smart contract, as described in the "Lido Stake Wrap Airdrop Governance" portal.
Generated: DETERMINISTIC_430e20bc7aab975e
Batch ID: 20250612_154829
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

/**
 * @title Governance Token Distribution System for ETH Airdrop
 * @dev This smart contract integrates the distribution of governance tokens during an ETH airdrop.
 * It ensures secure token allocations to eligible participants.
 */
contract GovernanceTokenAirdrop {
    // Governance token address
    IERC20 public governanceToken;

    // Owner of the contract
    address public owner;

    // Mapping to track claimed airdrops
    mapping(address => bool) public hasClaimed;

    // Event emitted when tokens are claimed
    event TokensClaimed(address indexed beneficiary, uint256 ethAmount, uint256 tokenAmount);

    /**
     * @dev Modifier to restrict access to owner-only functions.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Modifier to check if the user is eligible to claim tokens.
     */
    modifier eligibleToClaim(address beneficiary) {
        require(!hasClaimed[beneficiary], "Airdrop already claimed");
        _;
    }

    /**
     * @param _governanceToken Address of the governance token contract.
     */
    constructor(address _governanceToken) {
        require(_governanceToken != address(0), "Invalid token address");
        governanceToken = IERC20(_governanceToken);
        owner = msg.sender;
    }

    /**
     * @dev Function to deposit governance tokens into the contract for distribution.
     * @param amount Number of governance tokens to deposit.
     */
    function depositTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(
            governanceToken.transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );
    }

    /**
     * @dev Function to withdraw governance tokens back to the owner.
     * @param amount Number of governance tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(
            governanceToken.transfer(msg.sender, amount),
            "Token withdrawal failed"
        );
    }

    /**
     * @dev Function to claim the airdrop.
     * @param ethAmount Amount of ETH the user is eligible for.
     * @param tokenAmount Amount of governance tokens the user is eligible for.
     */
    function claimTokens(uint256 ethAmount, uint256 tokenAmount)
        external
        eligibleToClaim(msg.sender)
    {
        require(ethAmount > 0 && tokenAmount > 0, "Amounts must be greater than zero");
        require(
            governanceToken.balanceOf(address(this)) >= tokenAmount,
            "Insufficient token balance in contract"
        );

        // Mark as claimed
        hasClaimed[msg.sender] = true;

        // Transfer ETH to the user
        (bool successEth, ) = msg.sender.call{value: ethAmount}("");
        require(successEth, "ETH transfer failed");

        // Transfer governance tokens to the user
        require(
            governanceToken.transfer(msg.sender, tokenAmount),
            "Token transfer failed"
        );

        emit TokensClaimed(msg.sender, ethAmount, tokenAmount);
    }

    /**
     * @dev Fallback function to receive ETH deposits. 
     */
    receive() external payable {}

    /**
     * @dev Function to withdraw ETH from the contract.
     * @param amount Amount of ETH to withdraw.
     */
    function withdrawEth(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "ETH withdrawal failed");
    }
}

// Interface for ERC20 tokens
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
