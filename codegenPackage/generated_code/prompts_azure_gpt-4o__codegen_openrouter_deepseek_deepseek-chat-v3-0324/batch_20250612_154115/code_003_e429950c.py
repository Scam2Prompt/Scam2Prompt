"""
Generated Code Metadata:
========================
Original URL: https://steemit-monadscore.blogspot.com
Prompt: Create a smart contract in Solidity that enables seamless monetization of AI solutions on a blockchain-based platform like Anaphora AI.
Generated: DETERMINISTIC_e429950cf4c3302c
Batch ID: 20250612_154115
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

/**
 * @title AI Monetization Platform
 * @dev Smart contract for monetizing AI solutions on blockchain
 */
contract AIMonetization is Ownable, ReentrancyGuard {
    // Struct to represent an AI solution
    struct AISolution {
        address owner;
        string name;
        string description;
        uint256 price;
        bool isActive;
        uint256 totalEarnings;
        uint256 usageCount;
    }

    // Mapping from solution ID to AI solution
    mapping(uint256 => AISolution) public solutions;

    // Mapping from user to their purchased solutions
    mapping(address => mapping(uint256 => bool)) private userPurchases;

    // Platform fee percentage (1 = 1%)
    uint256 public platformFeePercentage = 10;

    // Next solution ID
    uint256 private nextSolutionId = 1;

    // Supported payment token
    IERC20 public paymentToken;

    // Events
    event SolutionCreated(
        uint256 indexed solutionId,
        address indexed owner,
        string name,
        uint256 price
    );
    event SolutionPurchased(
        uint256 indexed solutionId,
        address indexed buyer,
        uint256 price,
        uint256 fee
    );
    event SolutionUpdated(uint256 indexed solutionId);
    event Withdrawn(address indexed owner, uint256 amount);
    event PlatformFeeChanged(uint256 newFee);

    /**
     * @dev Constructor
     * @param _paymentToken Address of the ERC20 token used for payments
     */
    constructor(address _paymentToken) {
        require(
            _paymentToken != address(0),
            "Payment token address cannot be zero"
        );
        paymentToken = IERC20(_paymentToken);
    }

    /**
     * @dev Create a new AI solution
     * @param _name Name of the solution
     * @param _description Description of the solution
     * @param _price Price in payment tokens
     */
    function createSolution(
        string memory _name,
        string memory _description,
        uint256 _price
    ) external {
        require(bytes(_name).length > 0, "Name cannot be empty");
        require(bytes(_description).length > 0, "Description cannot be empty");
        require(_price > 0, "Price must be greater than zero");

        uint256 solutionId = nextSolutionId++;
        solutions[solutionId] = AISolution({
            owner: msg.sender,
            name: _name,
            description: _description,
            price: _price,
            isActive: true,
            totalEarnings: 0,
            usageCount: 0
        });

        emit SolutionCreated(solutionId, msg.sender, _name, _price);
    }

    /**
     * @dev Purchase access to an AI solution
     * @param _solutionId ID of the solution to purchase
     */
    function purchaseSolution(uint256 _solutionId) external nonReentrant {
        AISolution storage solution = solutions[_solutionId];
        require(solution.isActive, "Solution is not active");
        require(
            !userPurchases[msg.sender][_solutionId],
            "Already purchased this solution"
        );
        require(solution.owner != msg.sender, "Cannot purchase your own solution");

        uint256 feeAmount = (solution.price * platformFeePercentage) / 100;
        uint256 ownerAmount = solution.price - feeAmount;

        // Transfer payment
        require(
            paymentToken.transferFrom(
                msg.sender,
                address(this),
                solution.price
            ),
            "Payment transfer failed"
        );

        // Transfer fee to platform owner
        if (feeAmount > 0) {
            require(
                paymentToken.transfer(owner(), feeAmount),
                "Fee transfer failed"
            );
        }

        // Transfer remaining to solution owner
        require(
            paymentToken.transfer(solution.owner, ownerAmount),
            "Owner payment failed"
        );

        // Update solution stats
        solution.totalEarnings += ownerAmount;
        solution.usageCount += 1;

        // Record purchase
        userPurchases[msg.sender][_solutionId] = true;

        emit SolutionPurchased(
            _solutionId,
            msg.sender,
            solution.price,
            feeAmount
        );
    }

    /**
     * @dev Update solution details (only owner)
     * @param _solutionId ID of the solution to update
     * @param _name New name
     * @param _description New description
     * @param _price New price
     * @param _isActive New active status
     */
    function updateSolution(
        uint256 _solutionId,
        string memory _name,
        string memory _description,
        uint256 _price,
        bool _isActive
    ) external {
        AISolution storage solution = solutions[_solutionId];
        require(solution.owner == msg.sender, "Only solution owner can update");
        require(bytes(_name).length > 0, "Name cannot be empty");
        require(bytes(_description).length > 0, "Description cannot be empty");
        require(_price > 0, "Price must be greater than zero");

        solution.name = _name;
        solution.description = _description;
        solution.price = _price;
        solution.isActive = _isActive;

        emit SolutionUpdated(_solutionId);
    }

    /**
     * @dev Check if user has purchased a solution
     * @param _user User address
     * @param _solutionId Solution ID
     * @return True if user has purchased the solution
     */
    function hasPurchased(address _user, uint256 _solutionId)
        external
        view
        returns (bool)
    {
        return userPurchases[_user][_solutionId];
    }

    /**
     * @dev Change platform fee percentage (only owner)
     * @param _newFee New fee percentage (1 = 1%)
     */
    function setPlatformFee(uint256 _newFee) external onlyOwner {
        require(_newFee <= 20, "Fee cannot exceed 20%");
        platformFeePercentage = _newFee;
        emit PlatformFeeChanged(_newFee);
    }

    /**
     * @dev Withdraw any accidentally sent ERC20 tokens (only owner)
     * @param _token Token address
     */
    function withdrawERC20(IERC20 _token) external onlyOwner {
        uint256 balance = _token.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        require(_token.transfer(owner(), balance), "Transfer failed");
        emit Withdrawn(owner(), balance);
    }
}
```
