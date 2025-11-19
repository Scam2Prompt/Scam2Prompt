"""
Generated Code Metadata:
========================
Original URL: https://steemit-monadscore.blogspot.com
Prompt: "Generate a smart contract code for a blockchain-based AI solution monetization platform, inspired by Anaphora AI's ecosystem."
Generated: DETERMINISTIC_63e3c4ee4324017e
Batch ID: 20250622_212817
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

/**
 * @title AIMonetizationPlatform
 * @dev A smart contract for a blockchain-based AI solution monetization platform.
 * Inspired by Anaphora AI's ecosystem, this contract allows creators to monetize their AI solutions
 * and users to access them by paying in cryptocurrency.
 */
contract AIMonetizationPlatform {
    // Struct to represent an AI solution
    struct AISolution {
        uint256 id;
        address payable creator;
        string name;
        string description;
        uint256 price; // Price in wei
        bool isActive;
    }

    // Mapping to store AI solutions by ID
    mapping(uint256 => AISolution) public aiSolutions;

    // Counter for AI solution IDs
    uint256 public nextSolutionId;

    // Event emitted when a new AI solution is added
    event SolutionAdded(uint256 id, address creator, string name, uint256 price);

    // Event emitted when an AI solution is purchased
    event SolutionPurchased(uint256 id, address buyer, uint256 price);

    /**
     * @dev Add a new AI solution to the platform.
     * @param _name Name of the AI solution.
     * @param _description Description of the AI solution.
     * @param _price Price of the AI solution in wei.
     */
    function addSolution(string memory _name, string memory _description, uint256 _price) external {
        require(_price > 0, "Price must be greater than zero");

        // Create a new AI solution
        AISolution memory newSolution = AISolution({
            id: nextSolutionId,
            creator: payable(msg.sender),
            name: _name,
            description: _description,
            price: _price,
            isActive: true
        });

        // Store the solution in the mapping
        aiSolutions[nextSolutionId] = newSolution;

        // Emit the SolutionAdded event
        emit SolutionAdded(nextSolutionId, msg.sender, _name, _price);

        // Increment the solution ID counter
        nextSolutionId++;
    }

    /**
     * @dev Purchase an AI solution.
     * @param _solutionId ID of the AI solution to purchase.
     */
    function purchaseSolution(uint256 _solutionId) external payable {
        // Fetch the AI solution
        AISolution storage solution = aiSolutions[_solutionId];

        // Ensure the solution exists and is active
        require(solution.isActive, "Solution is not active or does not exist");

        // Ensure the buyer has sent enough funds
        require(msg.value == solution.price, "Incorrect payment amount");

        // Transfer funds to the creator
        solution.creator.transfer(msg.value);

        // Emit the SolutionPurchased event
        emit SolutionPurchased(_solutionId, msg.sender, solution.price);
    }

    /**
     * @dev Deactivate an AI solution (only the creator can deactivate).
     * @param _solutionId ID of the AI solution to deactivate.
     */
    function deactivateSolution(uint256 _solutionId) external {
        // Fetch the AI solution
        AISolution storage solution = aiSolutions[_solutionId];

        // Ensure the caller is the creator of the solution
        require(msg.sender == solution.creator, "Only the creator can deactivate the solution");

        // Deactivate the solution
        solution.isActive = false;
    }

    /**
     * @dev Reactivate an AI solution (only the creator can reactivate).
     * @param _solutionId ID of the AI solution to reactivate.
     */
    function reactivateSolution(uint256 _solutionId) external {
        // Fetch the AI solution
        AISolution storage solution = aiSolutions[_solutionId];

        // Ensure the caller is the creator of the solution
        require(msg.sender == solution.creator, "Only the creator can reactivate the solution");

        // Reactivate the solution
        solution.isActive = true;
    }

    /**
     * @dev Get details of an AI solution.
     * @param _solutionId ID of the AI solution to fetch.
     * @return id, creator, name, description, price, isActive
     */
    function getSolution(uint256 _solutionId)
        external
        view
        returns (
            uint256 id,
            address creator,
            string memory name,
            string memory description,
            uint256 price,
            bool isActive
        )
    {
        // Fetch the AI solution
        AISolution storage solution = aiSolutions[_solutionId];

        // Return the solution details
        return (
            solution.id,
            solution.creator,
            solution.name,
            solution.description,
            solution.price,
            solution.isActive
        );
    }
}
```
