"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appparax.pages.dev
Prompt: Write a smart contract for NFT collateralization and lending based on the risk parameters outlined in ParaX's documentation, using Chainlink oracles for floor price estimation.
Generated: DETERMINISTIC_0f83719931fd4a9b
Batch ID: 20250612_151255
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

// Import Chainlink interfaces for price feeds
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

// A simple NFT collateralization and lending smart contract
contract NFTCollateralLending {
    // Struct representing a loan
    struct Loan {
        address borrower;
        address nftContract;
        uint256 tokenId;
        uint256 loanAmount;
        uint256 collateralValue;
        uint256 floorPrice;
        uint256 interestRate;
        uint256 duration; // Duration of the loan in seconds
        uint256 startTimestamp;
        bool isActive;
    }

    // Mapping of loan IDs to Loan structs
    mapping(uint256 => Loan) public loans;

    // Counter for loan IDs
    uint256 private loanCounter;

    // Address of Chainlink floor price oracle
    AggregatorV3Interface private floorPriceOracle;

    // Event emitted when a loan is created
    event LoanCreated(
        uint256 loanId,
        address borrower,
        address nftContract,
        uint256 tokenId,
        uint256 loanAmount,
        uint256 collateralValue,
        uint256 interestRate,
        uint256 duration
    );

    // Event emitted when a loan is repaid
    event LoanRepaid(uint256 loanId);

    constructor(address _floorPriceOracle) {
        require(_floorPriceOracle != address(0), "Invalid oracle address");
        floorPriceOracle = AggregatorV3Interface(_floorPriceOracle);
    }

    /**
     * @dev Fetch the current floor price of the NFT from Chainlink oracle
     * @return floorPrice Current floor price of the NFT
     */
    function getFloorPrice() public view returns (uint256) {
        (, int256 price, , , ) = floorPriceOracle.latestRoundData();
        require(price > 0, "Invalid floor price from oracle");
        return uint256(price);
    }

    /**
     * @dev Create a loan using an NFT as collateral
     * @param nftContract Address of the NFT contract
     * @param tokenId ID of the NFT being used as collateral
     * @param loanAmount Amount of loan being requested
     * @param interestRate Interest rate for the loan
     * @param duration Duration of the loan in seconds
     */
    function createLoan(
        address nftContract,
        uint256 tokenId,
        uint256 loanAmount,
        uint256 interestRate,
        uint256 duration
    ) external {
        require(nftContract != address(0), "Invalid NFT contract address");
        require(loanAmount > 0, "Loan amount must be greater than zero");
        require(interestRate > 0, "Interest rate must be greater than zero");
        require(duration > 0, "Duration must be greater than zero");

        // Fetch floor price from the oracle
        uint256 floorPrice = getFloorPrice();

        // Calculate collateral value based on risk parameters (e.g., 80% of floor price)
        uint256 collateralValue = (floorPrice * 80) / 100;

        require(
            collateralValue >= loanAmount,
            "Loan amount exceeds collateral value"
        );

        // Transfer the NFT to the contract as collateral
        IERC721(nftContract).transferFrom(msg.sender, address(this), tokenId);

        // Create the loan
        loanCounter++;
        loans[loanCounter] = Loan({
            borrower: msg.sender,
            nftContract: nftContract,
            tokenId: tokenId,
            loanAmount: loanAmount,
            collateralValue: collateralValue,
            floorPrice: floorPrice,
            interestRate: interestRate,
            duration: duration,
            startTimestamp: block.timestamp,
            isActive: true
        });

        // Transfer loan amount to the borrower
        payable(msg.sender).transfer(loanAmount);

        emit LoanCreated(
            loanCounter,
            msg.sender,
            nftContract,
            tokenId,
            loanAmount,
            collateralValue,
            interestRate,
            duration
        );
    }

    /**
     * @dev Repay the loan and retrieve the NFT collateral
     * @param loanId ID of the loan to be repaid
     */
    function repayLoan(uint256 loanId) external payable {
        Loan storage loan = loans[loanId];

        require(loan.isActive, "Loan is not active");
        require(
            loan.borrower == msg.sender,
            "Only borrower can repay the loan"
        );

        // Calculate total repayment amount (principal + interest)
        uint256 interest = (loan.loanAmount * loan.interestRate * loan.duration) /
            (365 * 24 * 60 * 60 * 100); // Interest calculation based on annual rate
        uint256 totalRepayment = loan.loanAmount + interest;

        require(msg.value >= totalRepayment, "Insufficient repayment amount");

        // Mark the loan as repaid
        loan.isActive = false;

        // Return the NFT collateral to the borrower
        IERC721(loan.nftContract).transferFrom(
            address(this),
            loan.borrower,
            loan.tokenId
        );

        emit LoanRepaid(loanId);
    }

    /**
     * @dev Fallback function to receive Ether
     */
    receive() external payable {}

    /**
     * @dev Withdraw function to allow the contract owner to withdraw excess Ether
     */
    function withdraw(uint256 amount) external {
        require(msg.sender == address(this), "Only owner can withdraw");
        payable(msg.sender).transfer(amount);
    }
}

// Interface for ERC721 contract
interface IERC721 {
    function transferFrom(
        address from,
        address to,
        uint256 tokenId
    ) external;
}
```
