"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://quantprotocol.xyz
Prompt: Create a smart contract on the Binance Smart Chain (BSC) for purchasing Quant Protocol tokens during the pre-sale phase. Ensure the contract includes vesting logic for team tokens with a 6-month period.
Generated: DETERMINISTIC_737c7aa0b87a1bd1
Batch ID: 20250612_154400
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
 * @title QuantProtocolPresale
 * @dev A smart contract for handling the pre-sale of Quant Protocol tokens (QTP)
 *      on the Binance Smart Chain (BSC). Includes vesting logic for team tokens.
 */
contract QuantProtocolPresale {
    // State variables
    address public owner; // Owner of the contract
    address public tokenAddress; // Address of the Quant Protocol token (QTP)
    uint256 public tokenPriceInWei; // Price of a single token in wei (BSC native token)
    uint256 public totalTokensSold; // Total number of tokens sold during the presale
    uint256 public vestingStartTime; // Timestamp when the vesting starts
    uint256 public vestingDuration = 180 days; // Vesting period for team tokens (6 months)

    mapping(address => uint256) public teamTokens; // Team tokens allocated per address
    mapping(address => uint256) public tokensPurchased; // Tokens purchased during the presale

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event TeamTokensClaimed(address indexed teamMember, uint256 amount);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can call this function");
        _;
    }

    /**
     * @dev Constructor to initialize the contract
     * @param _tokenAddress Token contract address
     * @param _tokenPriceInWei Price of each token in wei
     */
    constructor(address _tokenAddress, uint256 _tokenPriceInWei) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_tokenPriceInWei > 0, "Token price must be greater than zero");

        owner = msg.sender;
        tokenAddress = _tokenAddress;
        tokenPriceInWei = _tokenPriceInWei;
        vestingStartTime = block.timestamp; // Start vesting from contract deployment
    }

    /**
     * @dev Allows users to purchase tokens during the presale.
     * @param _amount Number of tokens to purchase
     */
    function purchaseTokens(uint256 _amount) external payable {
        require(_amount > 0, "Token amount must be greater than zero");
        require(msg.value == _amount * tokenPriceInWei, "Incorrect payment amount");

        // Transfer purchased tokens to the buyer
        require(
            IERC20(tokenAddress).transfer(msg.sender, _amount),
            "Token transfer failed"
        );

        tokensPurchased[msg.sender] += _amount;
        totalTokensSold += _amount;

        emit TokensPurchased(msg.sender, _amount);
    }

    /**
     * @dev Allocates team tokens with vesting logic.
     * @param _teamMember Address of the team member
     * @param _amount Number of tokens to vest
     */
    function allocateTeamTokens(address _teamMember, uint256 _amount)
        external
        onlyOwner
    {
        require(_teamMember != address(0), "Invalid team member address");
        require(_amount > 0, "Token amount must be greater than zero");

        teamTokens[_teamMember] = _amount;
    }

    /**
     * @dev Allows team members to claim their vested tokens after the vesting period.
     */
    function claimTeamTokens() external {
        uint256 allocatedTokens = teamTokens[msg.sender];
        require(allocatedTokens > 0, "No tokens allocated");
        require(
            block.timestamp >= vestingStartTime + vestingDuration,
            "Vesting period not yet completed"
        );

        teamTokens[msg.sender] = 0; // Reset the allocation
        require(
            IERC20(tokenAddress).transfer(msg.sender, allocatedTokens),
            "Token transfer failed"
        );

        emit TeamTokensClaimed(msg.sender, allocatedTokens);
    }

    /**
     * @dev Transfers ownership of the contract to another address.
     * @param _newOwner Address of the new owner
     */
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "Invalid new owner address");

        emit OwnershipTransferred(owner, _newOwner);
        owner = _newOwner;
    }

    /**
     * @dev Withdraws BNB collected during the presale to the owner's wallet.
     */
    function withdrawBNB() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No BNB to withdraw");
        payable(owner).transfer(balance);
    }

    /**
     * @dev Withdraws unsold tokens to the owner's wallet.
     */
    function withdrawUnsoldTokens() external onlyOwner {
        uint256 balance = IERC20(tokenAddress).balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        require(
            IERC20(tokenAddress).transfer(owner, balance),
            "Token transfer failed"
        );
    }
}

// Interface for ERC20 token standard
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);

    function balanceOf(address account) external view returns (uint256);
}
```
