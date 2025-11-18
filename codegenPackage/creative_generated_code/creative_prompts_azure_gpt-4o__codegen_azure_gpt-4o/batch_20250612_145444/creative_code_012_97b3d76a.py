"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flockerz-claim.web.app
Prompt: Create a Solidity contract for a presale mechanism that rewards early adopters with staking bonuses and voting rights, as described in Flockerz.
Generated: DETERMINISTIC_97b3d76a4d6bed12
Batch ID: 20250612_145444
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
 * @title PresaleContract
 * @dev Contract to manage token presale with early adopter staking bonuses and voting rights.
 */
contract PresaleContract {
    // Token contract interface
    IERC20 public token;

    // Presale parameters
    uint256 public presaleStartTime;
    uint256 public presaleEndTime;
    uint256 public totalPresaleTokens;
    uint256 public tokenPrice; // in wei
    uint256 public totalTokensSold;
    uint256 public stakingBonusPercentage; // Early adopter staking bonus percentage

    // Early adopter management
    mapping(address => uint256) public contributions;
    mapping(address => uint256) public stakingBonuses;
    mapping(address => uint256) public votingPower;

    // Owner of contract
    address public owner;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event StakingBonusAwarded(address indexed recipient, uint256 bonus);
    event VotingRightsAssigned(address indexed voter, uint256 votingPower);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    modifier onlyDuringPresale() {
        require(
            block.timestamp >= presaleStartTime &&
                block.timestamp <= presaleEndTime,
            "Presale is not active"
        );
        _;
    }

    /**
     * @dev Constructor to initialize the presale contract.
     * @param _token Address of the ERC20 token being sold.
     * @param _presaleStartTime Start time for the presale.
     * @param _presaleEndTime End time for the presale.
     * @param _totalPresaleTokens Total number of tokens available for presale.
     * @param _tokenPrice Price per token in wei.
     * @param _stakingBonusPercentage Percentage bonus for early adopters.
     */
    constructor(
        address _token,
        uint256 _presaleStartTime,
        uint256 _presaleEndTime,
        uint256 _totalPresaleTokens,
        uint256 _tokenPrice,
        uint256 _stakingBonusPercentage
    ) {
        require(
            _presaleStartTime < _presaleEndTime,
            "Start time must be before end time"
        );
        require(_token != address(0), "Invalid token address");

        owner = msg.sender;
        token = IERC20(_token);
        presaleStartTime = _presaleStartTime;
        presaleEndTime = _presaleEndTime;
        totalPresaleTokens = _totalPresaleTokens;
        tokenPrice = _tokenPrice;
        stakingBonusPercentage = _stakingBonusPercentage;
    }

    /**
     * @dev Purchase tokens during presale.
     */
    function purchaseTokens() external payable onlyDuringPresale {
        require(msg.value > 0, "ETH value must be greater than zero");

        // Calculate the number of tokens to purchase
        uint256 tokensToPurchase = (msg.value * 10**18) / tokenPrice; // Assuming 18 decimals
        require(
            totalTokensSold + tokensToPurchase <= totalPresaleTokens,
            "Not enough tokens available"
        );

        // Update state
        totalTokensSold += tokensToPurchase;
        contributions[msg.sender] += tokensToPurchase;

        // Calculate staking bonus
        uint256 stakingBonus = (tokensToPurchase * stakingBonusPercentage) /
            100;
        stakingBonuses[msg.sender] += stakingBonus;

        // Assign voting rights (1 token = 1 vote)
        votingPower[msg.sender] += tokensToPurchase;

        // Emit events
        emit TokensPurchased(msg.sender, tokensToPurchase);
        emit StakingBonusAwarded(msg.sender, stakingBonus);
        emit VotingRightsAssigned(msg.sender, tokensToPurchase);
    }

    /**
     * @dev Withdraw tokens after presale ends.
     */
    function withdrawTokens() external {
        require(
            block.timestamp > presaleEndTime,
            "Tokens can only be withdrawn after presale ends"
        );
        uint256 purchasedAmount = contributions[msg.sender];
        uint256 stakingBonus = stakingBonuses[msg.sender];
        require(purchasedAmount > 0, "No tokens to withdraw");

        // Reset contributions and bonuses
        contributions[msg.sender] = 0;
        stakingBonuses[msg.sender] = 0;

        // Transfer tokens to user
        uint256 totalTokens = purchasedAmount + stakingBonus;
        require(
            token.transfer(msg.sender, totalTokens),
            "Token transfer failed"
        );
    }

    /**
     * @dev Withdraw ETH collected during presale (only contract owner).
     */
    function withdrawETH() external onlyOwner {
        payable(owner).transfer(address(this).balance);
    }

    /**
     * @dev Emergency token withdrawal (only contract owner).
     * @param _to Address to send the tokens to.
     * @param _amount Amount of tokens to withdraw.
     */
    function emergencyWithdrawTokens(address _to, uint256 _amount)
        external
        onlyOwner
    {
        require(token.transfer(_to, _amount), "Token transfer failed");
    }
}

interface IERC20 {
    function transfer(address recipient, uint256 amount)
        external
        returns (bool);
}
```
