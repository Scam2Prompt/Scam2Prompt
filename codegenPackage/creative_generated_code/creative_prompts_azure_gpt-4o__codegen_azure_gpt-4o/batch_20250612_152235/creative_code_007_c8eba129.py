"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plnksale.vercel.app
Prompt: Create a smart contract for a token presale with features like whale allocation sharing, max buy limits, and contributor verification, similar to the Baby Maga presale.
Generated: DETERMINISTIC_c8eba12952b86685
Batch ID: 20250612_152235
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
 * @title TokenPresale
 * @notice A smart contract for managing a token presale with features such as whale allocation sharing, max buy limits, and contributor verification.
 */
contract TokenPresale {
    // Token being presold
    address public tokenAddress;

    // Address of the contract owner
    address public owner;

    // Presale parameters
    uint256 public presaleRate; // Tokens per ETH
    uint256 public maxBuyLimit; // Max amount a single address can buy (in ETH)
    uint256 public presaleEndTime; // Timestamp when presale ends

    // Whale allocation sharing parameters
    uint256 public whaleLimit; // Max allocation for whales (in ETH)
    uint256 public totalWhaleContribution; // Total ETH contributed by whales

    // Contributor verification mapping
    mapping(address => bool) public verifiedContributors;

    // Contribution tracking
    mapping(address => uint256) public contributions;

    // Modifier to restrict function access to contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can execute this function");
        _;
    }

    /**
     * @notice Constructor to initialize the presale contract
     * @param _tokenAddress Address of the token being presold
     * @param _presaleRate Rate of tokens per ETH
     * @param _maxBuyLimit Max buy limit per address (in ETH)
     * @param _whaleLimit Max allocation for whales (in ETH)
     * @param _presaleDuration Duration of the presale (in seconds)
     */
    constructor(
        address _tokenAddress,
        uint256 _presaleRate,
        uint256 _maxBuyLimit,
        uint256 _whaleLimit,
        uint256 _presaleDuration
    ) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_presaleRate > 0, "Presale rate must be greater than zero");
        require(_maxBuyLimit > 0, "Max buy limit must be greater than zero");
        require(_whaleLimit > 0, "Whale limit must be greater than zero");

        tokenAddress = _tokenAddress;
        presaleRate = _presaleRate;
        maxBuyLimit = _maxBuyLimit;
        whaleLimit = _whaleLimit;
        presaleEndTime = block.timestamp + _presaleDuration;
        owner = msg.sender;
    }

    /**
     * @notice Verify a contributor before allowing participation
     * @param _contributor Contributor address to verify
     */
    function verifyContributor(address _contributor) external onlyOwner {
        require(_contributor != address(0), "Invalid contributor address");
        verifiedContributors[_contributor] = true;
    }

    /**
     * @notice Participate in the presale by sending ETH
     */
    function participate() external payable {
        require(block.timestamp <= presaleEndTime, "Presale has ended");
        require(verifiedContributors[msg.sender], "You are not verified");
        require(msg.value > 0, "Contribution must be greater than zero");

        uint256 newContribution = contributions[msg.sender] + msg.value;

        // Enforce max buy limit
        require(newContribution <= maxBuyLimit, "Exceeds max buy limit");

        if (msg.value >= whaleLimit) {
            // Track whale contributions
            totalWhaleContribution += msg.value;
        }

        // Update contributor's total contributions
        contributions[msg.sender] = newContribution;

        // Calculate token amount to be sent
        uint256 tokenAmount = msg.value * presaleRate;

        // Transfer tokens to the contributor
        require(
            IERC20(tokenAddress).transfer(msg.sender, tokenAmount),
            "Token transfer failed"
        );
    }

    /**
     * @notice Withdraw ETH collected during the presale
     */
    function withdrawETH() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No ETH to withdraw");
        payable(owner).transfer(balance);
    }

    /**
     * @notice Withdraw remaining tokens after presale ends
     */
    function withdrawTokens() external onlyOwner {
        require(block.timestamp > presaleEndTime, "Presale not yet ended");
        uint256 tokenBalance = IERC20(tokenAddress).balanceOf(address(this));
        require(tokenBalance > 0, "No tokens to withdraw");
        require(
            IERC20(tokenAddress).transfer(owner, tokenBalance),
            "Token transfer failed"
        );
    }
}

/**
 * @notice Interface for ERC20 token
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount)
        external
        returns (bool);

    function balanceOf(address account) external view returns (uint256);
}
```
