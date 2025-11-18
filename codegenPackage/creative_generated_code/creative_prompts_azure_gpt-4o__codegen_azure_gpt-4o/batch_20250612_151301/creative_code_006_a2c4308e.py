"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multichaingreenbitcoinapp.pages.dev
Prompt: Develop a Solidity contract for managing the presale of $GBTC tokens, including functionality for staking during the presale and claiming tokens post-presale, as outlined on the Green Bitcoin site.
Generated: DETERMINISTIC_a2c4308e37330a4a
Batch ID: 20250612_151301
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
 * @title GBTC Presale Contract
 * @dev A contract to manage the presale of $GBTC tokens including staking during the presale 
 *      and claiming tokens post-presale.
 */
contract GBTCPresale {
    // Token-related details
    string public constant tokenName = "Green Bitcoin Token";
    string public constant tokenSymbol = "GBTC";
    uint256 public constant tokenDecimals = 18;

    // Presale parameters
    uint256 public presaleStartTime;
    uint256 public presaleEndTime;
    uint256 public tokensPerETH; // Conversion rate of ETH to GBTC

    // Contract owner
    address public owner;

    // User balances
    mapping(address => uint256) public stakedETH; // Tracks ETH staked during presale
    mapping(address => uint256) public claimableTokens; // Tracks GBTC tokens claimable post presale

    // Events
    event Staked(address indexed user, uint256 amount);
    event TokensClaimed(address indexed user, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    modifier presaleActive() {
        require(
            block.timestamp >= presaleStartTime && block.timestamp <= presaleEndTime,
            "Presale is not active"
        );
        _;
    }

    modifier presaleEnded() {
        require(block.timestamp > presaleEndTime, "Presale has not ended");
        _;
    }

    /**
     * @dev Constructor to initialize the presale contract.
     * @param _presaleStartTime Start time of the presale (Unix timestamp).
     * @param _presaleEndTime End time of the presale (Unix timestamp).
     * @param _tokensPerETH Number of GBTC tokens per 1 ETH.
     */
    constructor(
        uint256 _presaleStartTime,
        uint256 _presaleEndTime,
        uint256 _tokensPerETH
    ) {
        require(_presaleStartTime < _presaleEndTime, "Start time must be before end time");
        presaleStartTime = _presaleStartTime;
        presaleEndTime = _presaleEndTime;
        tokensPerETH = _tokensPerETH;
        owner = msg.sender;
    }

    /**
     * @dev Allows users to stake ETH during the presale to receive GBTC tokens post-presale.
     */
    function stake() external payable presaleActive {
        require(msg.value > 0, "Stake amount must be greater than zero");

        // Update user's staked ETH balance
        stakedETH[msg.sender] += msg.value;

        // Calculate the number of GBTC tokens the user can claim post-presale
        uint256 tokenAmount = msg.value * tokensPerETH;
        claimableTokens[msg.sender] += tokenAmount;

        // Emit staking event
        emit Staked(msg.sender, msg.value);
    }

    /**
     * @dev Allows users to claim their GBTC tokens after the presale has ended.
     */
    function claimTokens() external presaleEnded {
        uint256 amount = claimableTokens[msg.sender];
        require(amount > 0, "No claimable tokens available");

        // Reset claimable tokens balance
        claimableTokens[msg.sender] = 0;

        // Transfer tokens to the user (mock transfer, replace with actual token logic)
        // In production, this should call the actual ERC20 token contract's transfer function
        // For example: token.transfer(msg.sender, amount);

        // Emit tokens claimed event
        emit TokensClaimed(msg.sender, amount);
    }

    /**
     * @dev Allows the owner to withdraw all ETH collected during the presale.
     */
    function withdrawETH() external onlyOwner presaleEnded {
        uint256 balance = address(this).balance;
        require(balance > 0, "No ETH available for withdrawal");

        payable(owner).transfer(balance);
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers to the contract.
     */
    receive() external payable {
        revert("ETH transfers disabled. Use the stake function.");
    }
}
```
