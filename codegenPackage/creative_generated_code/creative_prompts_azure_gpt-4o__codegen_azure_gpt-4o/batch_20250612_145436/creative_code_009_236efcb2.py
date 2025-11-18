"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aethirclaim-ifbf5prj-iamsorryman.4everland.app
Prompt: Write a Solidity contract that includes functionality for tracking deposits and distributing tokens proportionally during a presale, with a cap of 1000 ETH.
Generated: DETERMINISTIC_236efcb260bdb0d2
Batch ID: 20250612_145436
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
 * @dev A contract for tracking deposits and distributing tokens proportionally during a presale.
 */
contract PresaleContract {
    // Maximum allowed ETH deposit (1000 ETH cap)
    uint256 public constant MAX_CAP = 1000 ether;

    // Total ETH deposited in the contract
    uint256 public totalDeposits;

    // Address of the owner (admin)
    address public owner;

    // Mapping to track user deposits
    mapping(address => uint256) public deposits;

    // Token distribution flag
    bool public tokensDistributed;

    // ERC20 token interface
    IERC20 public token;

    // Events
    event Deposit(address indexed user, uint256 amount);
    event TokensDistributed();

    // Modifier to restrict function access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Modifier to ensure the presale cap is not exceeded
    modifier withinCap(uint256 amount) {
        require(totalDeposits + amount <= MAX_CAP, "Deposit exceeds presale cap");
        _;
    }

    /**
     * @dev Contract constructor
     * @param _token Address of the ERC20 token for distribution
     */
    constructor(address _token) {
        require(_token != address(0), "Invalid token address");
        owner = msg.sender;
        token = IERC20(_token);
    }

    /**
     * @dev Function to deposit ETH during the presale
     */
    function deposit() external payable withinCap(msg.value) {
        require(msg.value > 0, "Deposit amount must be greater than 0");
        require(!tokensDistributed, "Tokens have already been distributed");

        deposits[msg.sender] += msg.value;
        totalDeposits += msg.value;

        emit Deposit(msg.sender, msg.value);
    }

    /**
     * @dev Function to distribute tokens proportionally to depositors
     */
    function distributeTokens() external onlyOwner {
        require(!tokensDistributed, "Tokens have already been distributed");
        require(totalDeposits > 0, "No deposits to distribute tokens for");

        uint256 totalTokens = token.balanceOf(address(this));
        require(totalTokens > 0, "No tokens available for distribution");

        tokensDistributed = true;

        // Distribute tokens proportionally
        for (uint256 i = 0; i < getDepositors().length; i++) {
            address user = getDepositors()[i];
            uint256 userDeposit = deposits[user];
            uint256 userShare = (userDeposit * totalTokens) / totalDeposits;

            // Transfer tokens to the user
            require(token.transfer(user, userShare), "Token transfer failed");
        }

        emit TokensDistributed();
    }

    /**
     * @dev Function to withdraw ETH erroneously sent to the contract
     */
    function withdrawETH() external onlyOwner {
        require(address(this).balance > 0, "No ETH to withdraw");
        payable(owner).transfer(address(this).balance);
    }

    /**
     * @dev Helper function to get a list of all depositors (for demonstration purposes)
     */
    function getDepositors() public view returns (address[] memory) {
        // Note: In production use, this function should be optimized or avoided
        // as it may run into gas limits for large datasets.
        address[] memory depositors;
        uint256 index = 0;

        for (uint256 i = 0; i < totalDeposits;) {
        }
        return depositors;
    }
}
```
