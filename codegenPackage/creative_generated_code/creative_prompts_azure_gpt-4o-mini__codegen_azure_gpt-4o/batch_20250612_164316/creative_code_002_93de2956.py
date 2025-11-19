"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greenbitcoin-dapps.pages.dev
Prompt: What are the best practices for creating a presale for a cryptocurrency token, based on the Green Bitcoin model?
Generated: DETERMINISTIC_93de2956c9ff4e52
Batch ID: 20250612_164316
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
 * @title GreenBitcoinPresale
 * @dev Implements a presale contract for a cryptocurrency token based on the Green Bitcoin model.
 */
contract GreenBitcoinPresale {
    // State variables
    address public owner; // Owner of the presale contract
    address public tokenAddress; // Address of the token contract
    uint256 public presaleStartTime; // Start time of the presale
    uint256 public presaleEndTime; // End time of the presale
    uint256 public tokenPriceInWei; // Token price in wei
    uint256 public hardCap; // Maximum amount of ETH that can be raised
    uint256 public totalRaised; // Total ETH raised during presale
    uint256 public minContribution; // Minimum contribution in wei
    uint256 public maxContribution; // Maximum contribution in wei

    mapping(address => uint256) public contributions; // Tracks contributions by each address

    // Events
    event ContributionReceived(address indexed contributor, uint256 amount);
    event TokensClaimed(address indexed claimant, uint256 amount);
    event PresaleEnded(uint256 totalRaised);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Not contract owner");
        _;
    }

    modifier presaleActive() {
        require(block.timestamp >= presaleStartTime, "Presale has not started");
        require(block.timestamp < presaleEndTime, "Presale has ended");
        _;
    }

    modifier presaleEnded() {
        require(block.timestamp >= presaleEndTime, "Presale has not ended yet");
        _;
    }

    // Constructor
    constructor(
        address _tokenAddress,
        uint256 _startTime,
        uint256 _endTime,
        uint256 _tokenPriceInWei,
        uint256 _hardCap,
        uint256 _minContribution,
        uint256 _maxContribution
    ) {
        require(
            _startTime < _endTime,
            "Start time must be before end time"
        );
        require(_tokenPriceInWei > 0, "Token price must be greater than 0");
        require(_hardCap > 0, "Hard cap must be greater than 0");
        require(
            _minContribution <= _maxContribution,
            "Min contribution must be <= max contribution"
        );

        owner = msg.sender;
        tokenAddress = _tokenAddress;
        presaleStartTime = _startTime;
        presaleEndTime = _endTime;
        tokenPriceInWei = _tokenPriceInWei;
        hardCap = _hardCap;
        minContribution = _minContribution;
        maxContribution = _maxContribution;
    }

    /**
     * @dev Function to contribute to the presale
     */
    function contribute() external payable presaleActive {
        require(
            msg.value >= minContribution,
            "Contribution below minimum limit"
        );
        require(
            msg.value <= maxContribution,
            "Contribution above maximum limit"
        );
        require(
            totalRaised + msg.value <= hardCap,
            "Contribution exceeds hard cap"
        );

        contributions[msg.sender] += msg.value;
        totalRaised += msg.value;

        emit ContributionReceived(msg.sender, msg.value);
    }

    /**
     * @dev Function to claim tokens after presale ends
     */
    function claimTokens() external presaleEnded {
        uint256 contribution = contributions[msg.sender];
        require(contribution > 0, "No contributions found");

        uint256 tokenAmount = (contribution * 10**18) / tokenPriceInWei; // Adjust token decimals as needed
        contributions[msg.sender] = 0; // Reset contribution to prevent re-claiming

        // Transfer tokens to the claimant
        (bool success) = IERC20(tokenAddress).transfer(msg.sender, tokenAmount);
        require(success, "Token transfer failed");

        emit TokensClaimed(msg.sender, tokenAmount);
    }

    /**
     * @dev Owner can withdraw raised ETH after presale ends
     */
    function withdrawFunds() external onlyOwner presaleEnded {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "ETH transfer failed");
    }

    /**
     * @dev Ends the presale manually (only owner)
     */
    function endPresale() external onlyOwner {
        presaleEndTime = block.timestamp;
        emit PresaleEnded(totalRaised);
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers
     */
    fallback() external payable {
        revert("Use contribute() to participate in presale");
    }

    receive() external payable {
        revert("Use contribute() to participate in presale");
    }
}

/**
 * @dev Interface for ERC20 token transfers
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount)
        external
        returns (bool);
}
```
