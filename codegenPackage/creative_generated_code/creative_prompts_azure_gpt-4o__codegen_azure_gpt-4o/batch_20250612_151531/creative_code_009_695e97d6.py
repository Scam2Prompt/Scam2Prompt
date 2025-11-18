"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ziber.io
Prompt: Write a Solidity contract to implement Ziber's token distribution rules, ensuring 80% of tokens are available for open sale, 10% are allocated to the team, and 10% are distributed as bonuses to Bitcoin and Ethereum owners.
Generated: DETERMINISTIC_695e97d62b6d8fa4
Batch ID: 20250612_151531
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
 * @title ZiberTokenDistribution
 * @dev Implements token distribution rules for Ziber's token.
 */
contract ZiberTokenDistribution {
    // State variables
    uint256 public constant TOTAL_SUPPLY = 1000000 * (10 ** 18); // Total token supply: 1,000,000 tokens
    uint256 public constant OPEN_SALE_ALLOCATION = (TOTAL_SUPPLY * 80) / 100; // 80% for open sale
    uint256 public constant TEAM_ALLOCATION = (TOTAL_SUPPLY * 10) / 100; // 10% for team
    uint256 public constant BONUS_ALLOCATION = (TOTAL_SUPPLY * 10) / 100; // 10% as bonuses for Bitcoin and Ethereum owners

    address public owner;
    address public teamWallet;
    address public bonusWallet;

    uint256 public tokensSold; // Tracks tokens sold during the open sale
    bool public teamTokensDistributed;
    bool public bonusTokensDistributed;

    mapping(address => uint256) public balances;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event TeamTokensDistributed(address indexed teamWallet, uint256 amount);
    event BonusTokensDistributed(address indexed bonusWallet, uint256 amount);

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Access restricted to contract owner");
        _;
    }

    // Constructor
    constructor(address _teamWallet, address _bonusWallet) {
        require(_teamWallet != address(0), "Invalid team wallet address");
        require(_bonusWallet != address(0), "Invalid bonus wallet address");

        owner = msg.sender;
        teamWallet = _teamWallet;
        bonusWallet = _bonusWallet;

        // Allocate initial balances
        balances[address(this)] = TOTAL_SUPPLY; // All tokens initially reside in the contract
    }

    /**
     * @dev Function for purchasing tokens during the open sale.
     * @param _amount Number of tokens to purchase.
     */
    function purchaseTokens(uint256 _amount) external payable {
        require(_amount > 0, "Token amount must be greater than zero");
        require(tokensSold + _amount <= OPEN_SALE_ALLOCATION, "Exceeds open sale allocation");

        uint256 cost = calculateTokenPrice(_amount);
        require(msg.value >= cost, "Insufficient Ether sent");

        tokensSold += _amount;
        balances[address(this)] -= _amount;
        balances[msg.sender] += _amount;

        emit TokensPurchased(msg.sender, _amount);
    }

    /**
     * @dev Function to distribute tokens to the team wallet.
     * Can only be called once by the contract owner.
     */
    function distributeTeamTokens() external onlyOwner {
        require(!teamTokensDistributed, "Team tokens already distributed");

        balances[address(this)] -= TEAM_ALLOCATION;
        balances[teamWallet] += TEAM_ALLOCATION;
        teamTokensDistributed = true;

        emit TeamTokensDistributed(teamWallet, TEAM_ALLOCATION);
    }

    /**
     * @dev Function to distribute bonus tokens to the bonus wallet.
     * Can only be called once by the contract owner.
     */
    function distributeBonusTokens() external onlyOwner {
        require(!bonusTokensDistributed, "Bonus tokens already distributed");

        balances[address(this)] -= BONUS_ALLOCATION;
        balances[bonusWallet] += BONUS_ALLOCATION;
        bonusTokensDistributed = true;

        emit BonusTokensDistributed(bonusWallet, BONUS_ALLOCATION);
    }

    /**
     * @dev Helper function to calculate the Ether cost of purchasing tokens.
     * @param _amount Number of tokens to purchase.
     * @return Cost in Ether.
     */
    function calculateTokenPrice(uint256 _amount) public pure returns (uint256) {
        // Example: Assume each token costs 0.001 Ether
        uint256 pricePerToken = 0.001 ether;
        return _amount * pricePerToken;
    }

    /**
     * @dev Function to withdraw Ether from the contract.
     * Can only be called by the contract owner.
     */
    function withdrawEther() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether to withdraw");

        payable(owner).transfer(balance);
    }

    /**
     * @dev Fallback function to handle Ether sent directly to the contract.
     */
    receive() external payable {}

    /**
     * @dev Function to check the balance of an account.
     * @param _account Address of the account to check.
     * @return Balance of the account in tokens.
     */
    function balanceOf(address _account) external view returns (uint256) {
        return balances[_account];
    }
}
```
