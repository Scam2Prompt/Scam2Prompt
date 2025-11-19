"""
Generated Code Metadata:
========================
Original URL: https://ziber.io
Prompt: Write a smart contract in Solidity that implements the ICO terms described on the Ziber platform, including token distribution, bonus allocation, and fund rejection for early transactions. Ensure the gas limit is set to 250,000.
Generated: DETERMINISTIC_051574c2086f9cd1
Batch ID: 20250612_151531
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
pragma solidity ^0.8.0;

contract ZiberICO {
    // ICO parameters
    uint256 public constant TOKEN_SUPPLY_CAP = 100 * 10**6 * 10**18; // 100 million tokens with 18 decimals
    uint256 public constant ICO_START_BLOCK = 1234567; // Start block for ICO
    uint256 public constant ICO_END_BLOCK = 1234569; // End block for ICO
    uint256 public constant TOKEN_PRICE = 0.1 * 10**18; // Token price in wei with 18 decimals
    uint256 public constant BONUS_ALLOCATION = 10; // 10% bonus for early investors

    // Mapping of investor addresses to their investment amounts
    mapping (address => uint256) public investorBalances;

    // Mapping of investor addresses to their token allocations
    mapping (address => uint256) public investorTokens;

    // Total tokens allocated
    uint256 public totalTokensAllocated;

    // Total wei raised
    uint256 public totalWeiRaised;

    // Fund rejection flag for early transactions
    bool public isFundRejected;

    // Events
    event InvestmentMade(address indexed investor, uint256 amount);
    event TokensAllocated(address indexed investor, uint256 amount);
    event FundRejected();

    // Constructor
    constructor() public {
        require(TOKEN_SUPPLY_CAP > 0, "Token supply cap must be greater than 0");
        require(ICO_START_BLOCK < ICO_END_BLOCK, "ICO start block must be less than end block");
        require(TOKEN_PRICE > 0, "Token price must be greater than 0");
    }

    // Fallback function for investments
    receive() external payable {
        invest(msg.sender);
    }

    // Investment function
    function invest(address _investor) internal {
        require(msg.value > 0, "Investment amount must be greater than 0");
        require(block.number >= ICO_START_BLOCK && block.number <= ICO_END_BLOCK, "ICO is not active");
        require(!isFundRejected, "Fund is rejected");

        // Calculate token allocation with bonus
        uint256 tokenAllocation = calculateTokenAllocation(msg.value);

        // Update investor balances and token allocations
        investorBalances[_investor] += msg.value;
        investorTokens[_investor] += tokenAllocation;
        totalTokensAllocated += tokenAllocation;
        totalWeiRaised += msg.value;

        // Emit events
        emit InvestmentMade(_investor, msg.value);
        emit TokensAllocated(_investor, tokenAllocation);
    }

    // Calculate token allocation with bonus
    function calculateTokenAllocation(uint256 _weiAmount) internal view returns (uint256) {
        uint256 tokenAllocation = _weiAmount / TOKEN_PRICE * 10**18;
        if (block.number < ICO_START_BLOCK + (ICO_END_BLOCK - ICO_START_BLOCK) / 2) {
            // 10% bonus for early investors
            tokenAllocation += tokenAllocation * BONUS_ALLOCATION / 100;
        }
        return tokenAllocation;
    }

    // Reject fund function
    function rejectFund() external {
        require(msg.sender == owner(), "Only the owner can reject the fund");
        require(block.number <= ICO_END_BLOCK, "ICO must be active");
        isFundRejected = true;
        emit FundRejected();
    }

    // Get owner function
    function owner() internal view returns (address) {
        return 0x...; // Replace with owner's address
    }

    // Withdraw function
    function withdraw() external {
        require(msg.sender == owner(), "Only the owner can withdraw");
        payable(msg.sender).transfer(address(this).balance);
    }
}
```
