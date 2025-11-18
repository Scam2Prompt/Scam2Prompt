"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stakestoneclaim.pages.dev
Prompt: Develop a lending protocol smart contract that allows users to borrow against their STONE tokens and optimize looping yields.
Generated: DETERMINISTIC_69b4b6f6a4f99eaf
Batch ID: 20250612_151057
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

// Importing the necessary libraries and interfaces
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title LendingProtocol
 * @dev Smart contract for lending against STONE tokens with yield optimization
 */
contract LendingProtocol is ReentrancyGuard, Ownable {
    // Defining state variables
    IERC20 public stoneToken; // STONE token contract
    mapping(address => uint256) public collateral; // Collateral mapping for each user
    uint256 public totalBorrowed; // Total amount borrowed in the protocol

    // Events for logging
    event CollateralDeposited(address indexed user, uint256 amount);
    event Borrowed(address indexed user, uint256 amount);
    event Repaid(address indexed user, uint256 amount);
    event CollateralWithdrawn(address indexed user, uint256 amount);

    // Constructor to set the STONE token address
    constructor(address _stoneToken) {
        require(_stoneToken != address(0), "Invalid token address");
        stoneToken = IERC20(_stoneToken);
    }

    /**
     * @dev Deposit STONE tokens as collateral
     * @param amount The amount of STONE tokens to deposit
     */
    function depositCollateral(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(stoneToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        collateral[msg.sender] += amount;
        emit CollateralDeposited(msg.sender, amount);
    }

    /**
     * @dev Borrow against the deposited collateral
     * @param amount The amount to borrow
     */
    function borrow(uint256 amount) external nonReentrant {
        require(amount > 0, "Borrow amount must be greater than zero");
        require(collateral[msg.sender] > 0, "No collateral deposited");
        require(totalBorrowed + amount <= getAvailableLiquidity(), "Not enough liquidity");

        totalBorrowed += amount;
        require(stoneToken.transfer(msg.sender, amount), "Transfer failed");
        emit Borrowed(msg.sender, amount);
    }

    /**
     * @dev Repay a borrowed amount
     * @param amount The amount to repay
     */
    function repay(uint256 amount) external nonReentrant {
        require(amount > 0, "Repayment amount must be greater than zero");
        require(stoneToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        totalBorrowed -= amount;
        emit Repaid(msg.sender, amount);
    }

    /**
     * @dev Withdraw collateral after repaying
     * Only the collateral can be withdrawn if there are no outstanding loans
     */
    function withdrawCollateral(uint256 amount) external nonReentrant {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(collateral[msg.sender] >= amount, "Insufficient collateral");
        require(totalBorrowed == 0, "Outstanding loans must be repaid before withdrawal");

        collateral[msg.sender] -= amount;
        require(stoneToken.transfer(msg.sender, amount), "Transfer failed");
        emit CollateralWithdrawn(msg.sender, amount);
    }

    /**
     * @dev Get available liquidity in the contract
     * @return available liquidity in the protocol
     */
    function getAvailableLiquidity() public view returns (uint256) {
        return stoneToken.balanceOf(address(this)) - totalBorrowed;
    }

    /**
     * @dev Set new STONE token address (only owner)
     * @param _stoneToken New STONE token address
     */
    function setStoneToken(address _stoneToken) external onlyOwner {
        require(_stoneToken != address(0), "Invalid token address");
        stoneToken = IERC20(_stoneToken);
    }

    // Fallback function to prevent accidental ETH transfers
    receive() external payable {
        revert("Contract does not accept ETH");
    }
}
```
