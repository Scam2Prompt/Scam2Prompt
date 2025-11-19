"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bull-dogito-com.pages.dev
Prompt: How can I implement the "B2B Booster" strategy in a smart contract to invest in real-world assets while ensuring token sustainability?
Generated: DETERMINISTIC_759e9b8d5294f898
Batch ID: 20250612_155855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the code for implementing a "B2B Booster" strategy in a Solidity smart contract. This code uses OpenZeppelin libraries to ensure safe handling of ERC20 tokens and follows best practices.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing OpenZeppelin libraries for security and token handling
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract B2BBooster is Ownable {
    using SafeMath for uint256;

    // Token used for investments
    IERC20 public token;

    // Struct to represent an investment
    struct Investment {
        uint256 amount;
        uint256 timestamp;
        address investor;
        bool completed;
    }

    // Mapping to track all investments
    mapping(uint256 => Investment) public investments;
    uint256 public investmentCounter;

    // Events for transparency and tracking
    event NewInvestment(uint256 indexed id, address indexed investor, uint256 amount);
    event InvestmentCompleted(uint256 indexed id, address indexed investor, uint256 amount);
    event TokensWithdrawn(address indexed admin, uint256 amount);

    // Constructor to initialize contract with the investment token
    constructor(address _token) {
        require(_token != address(0), "Token address cannot be zero");
        token = IERC20(_token);
    }

    /**
     * @dev Allows an investor to make an investment.
     * @param amount Amount of tokens to invest.
     */
    function invest(uint256 amount) external {
        require(amount > 0, "Investment amount must be greater than zero");
        require(token.balanceOf(msg.sender) >= amount, "Insufficient token balance");
        require(token.allowance(msg.sender, address(this)) >= amount, "Allowance too low");

        // Transfer tokens from investor to the contract
        bool success = token.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Create a new investment record
        investments[investmentCounter] = Investment({
            amount: amount,
            timestamp: block.timestamp,
            investor: msg.sender,
            completed: false
        });

        emit NewInvestment(investmentCounter, msg.sender, amount);

        // Increment investment counter
        investmentCounter++;
    }

    /**
     * @dev Completes an investment by marking it as completed.
     * Only callable by the contract owner.
     * @param id Investment ID to complete.
     */
    function completeInvestment(uint256 id) external onlyOwner {
        require(id < investmentCounter, "Invalid investment ID");
        Investment storage investment = investments[id];
        require(!investment.completed, "Investment already completed");

        // Mark the investment as completed
        investment.completed = true;

        emit InvestmentCompleted(id, investment.investor, investment.amount);
    }

    /**
     * @dev Withdraw tokens from the contract to owner address.
     * Only callable by the contract owner.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(token.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        bool success = token.transfer(owner(), amount);
        require(success, "Token withdrawal failed");

        emit TokensWithdrawn(owner(), amount);
    }

    /**
     * @dev Retrieves details of an investment.
     * @param id Investment ID to retrieve.
     * @return Investment details.
     */
    function getInvestmentDetails(uint256 id) external view returns (Investment memory) {
        require(id < investmentCounter, "Invalid investment ID");
        return investments[id];
    }
}
```

### Notes:
1. **Dependencies**: Ensure you install OpenZeppelin contracts via npm (`npm install @openzeppelin/contracts`) or reference them in your project.
2. **Testing**: Before deploying this contract, test it rigorously to ensure edge cases are handled correctly.
3. **Deployment**: Use a secure deployment process, such as Hardhat or Truffle, and verify the contract on the blockchain explorer.
