"""
Generated Code Metadata:
========================
Original URL: https://vivalalibertadproject.com
Prompt: Develop a Solidity function to handle token transactions and funding allocation for a project like Viva La Libertad Project, ensuring secure and transparent financial operations.
Generated: DETERMINISTIC_2d0edf10dd6d59a8
Batch ID: 20250622_211853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract VivaLaLibertadFunding is Ownable, ReentrancyGuard {
    IERC20 public token;
    uint256 public fundingGoal;
    uint256 public totalFundsRaised;
    uint256 public allocationPercentage; // Percentage of funds allocated to project (e.g., 70%)
    uint256 public allocationReserve; // Percentage of funds reserved (e.g., 30%)
    bool public fundingClosed = false;
    address public projectWallet;
    address public reserveWallet;

    mapping(address => uint256) public contributions;

    event FundsContributed(address contributor, uint256 amount);
    event FundsAllocated(uint256 projectAmount, uint256 reserveAmount);
    event FundingClosed();

    /**
     * @dev Constructor to initialize the contract
     * @param _tokenAddress Address of the ERC20 token used for funding
     * @param _fundingGoal Total funding goal in token units
     * @param _allocationPercentage Percentage of funds allocated to project (0-100)
     * @param _projectWallet Address where project funds will be sent
     * @param _reserveWallet Address where reserve funds will be sent
     */
    constructor(
        address _tokenAddress,
        uint256 _fundingGoal,
        uint256 _allocationPercentage,
        address _projectWallet,
        address _reserveWallet
    ) {
        require(_tokenAddress != address(0), "Token address cannot be zero");
        require(_projectWallet != address(0), "Project wallet cannot be zero");
        require(_reserveWallet != address(0), "Reserve wallet cannot be zero");
        require(_allocationPercentage <= 100, "Allocation percentage must be <= 100");

        token = IERC20(_tokenAddress);
        fundingGoal = _fundingGoal;
        allocationPercentage = _allocationPercentage;
        allocationReserve = 100 - allocationPercentage;
        projectWallet = _projectWallet;
        reserveWallet = _reserveWallet;
    }

    /**
     * @dev Contribute tokens to the funding
     * @param amount Amount of tokens to contribute
     */
    function contribute(uint256 amount) external nonReentrant {
        require(!fundingClosed, "Funding is closed");
        require(amount > 0, "Amount must be greater than zero");
        require(token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        contributions[msg.sender] += amount;
        totalFundsRaised += amount;

        emit FundsContributed(msg.sender, amount);
    }

    /**
     * @dev Allocate funds to project and reserve wallets
     */
    function allocateFunds() external onlyOwner nonReentrant {
        require(!fundingClosed, "Funding is already closed");
        require(totalFundsRaised > 0, "No funds to allocate");

        uint256 projectAmount = (totalFundsRaised * allocationPercentage) / 100;
        uint256 reserveAmount = totalFundsRaised - projectAmount;

        require(token.transfer(projectWallet, projectAmount), "Project transfer failed");
        require(token.transfer(reserveWallet, reserveAmount), "Reserve transfer failed");

        fundingClosed = true;

        emit FundsAllocated(projectAmount, reserveAmount);
        emit FundingClosed();
    }

    /**
     * @dev Emergency function to return funds to contributors
     */
    function emergencyRefund() external onlyOwner nonReentrant {
        require(!fundingClosed, "Funding is already closed");

        fundingClosed = true;
        emit FundingClosed();
    }

    /**
     * @dev Withdraw tokens accidentally sent to this contract (non-funding tokens)
     * @param _token Address of the token to withdraw
     * @param _to Address to send the tokens to
     * @param _amount Amount of tokens to withdraw
     */
    function recoverTokens(address _token, address _to, uint256 _amount) external onlyOwner {
        require(_token != address(token), "Cannot withdraw funding token");
        require(_to != address(0), "Cannot send to zero address");
        IERC20(_token).transfer(_to, _amount);
    }
}
```
