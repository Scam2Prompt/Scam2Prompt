"""
Generated Code Metadata:
========================
Original URL: https://nftcap.pages.dev
Prompt: Write a Solidity function for bundling multiple NFTs as collateral for a single loan, inspired by the "Get a loan on multiple NFTs" feature on NFTfi.com.
Generated: DETERMINISTIC_7cdf43d0bd34faa4
Batch ID: 20250612_151329
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

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/structs/EnumerableSet.sol";

contract NFTBundledLoan is ReentrancyGuard {
    using EnumerableSet for EnumerableSet.UintSet;
    using EnumerableSet for EnumerableSet.AddressSet;

    struct Loan {
        address borrower;
        address lender;
        uint256 loanAmount;
        uint256 interestRate;
        uint256 duration;
        uint256 startTime;
        bool isActive;
        EnumerableSet.AddressSet nftContracts;
        mapping(address => EnumerableSet.UintSet) tokenIds; // nftContract => tokenIds
    }

    uint256 public loanIdCounter;
    mapping(uint256 => Loan) public loans;

    event LoanCreated(
        uint256 indexed loanId,
        address indexed borrower,
        uint256 loanAmount,
        uint256 interestRate,
        uint256 duration,
        address[] nftContracts,
        uint256[][] tokenIds
    );

    event LoanRepaid(uint256 indexed loanId);
    event LoanLiquidated(uint256 indexed loanId);

    modifier onlyLoanParticipant(uint256 loanId) {
        require(
            msg.sender == loans[loanId].borrower || msg.sender == loans[loanId].lender,
            "Not a loan participant"
        );
        _;
    }

    function createLoan(
        uint256 loanAmount,
        uint256 interestRate,
        uint256 duration,
        address[] calldata nftContracts,
        uint256[][] calldata tokenIds
    ) external nonReentrant {
        require(nftContracts.length > 0, "No NFTs provided");
        require(nftContracts.length == tokenIds.length, "Array length mismatch");

        uint256 loanId = loanIdCounter++;
        Loan storage loan = loans[loanId];
        loan.borrower = msg.sender;
        loan.loanAmount = loanAmount;
        loan.interestRate = interestRate;
        loan.duration = duration;
        loan.isActive = true;

        for (uint256 i = 0; i < nftContracts.length; i++) {
            require(tokenIds[i].length > 0, "No token IDs for NFT contract");
            loan.nftContracts.add(nftContracts[i]);

            for (uint256 j = 0; j < tokenIds[i].length; j++) {
                require(
                    IERC721(nftContracts[i]).ownerOf(tokenIds[i][j]) == msg.sender,
                    "Not NFT owner"
                );
                IERC721(nftContracts[i]).transferFrom(
                    msg.sender,
                    address(this),
                    tokenIds[i][j]
                );
                loan.tokenIds[nftContracts[i]].add(tokenIds[i][j]);
            }
        }

        emit LoanCreated(
            loanId,
            msg.sender,
            loanAmount,
            interestRate,
            duration,
            nftContracts,
            tokenIds
        );
    }

    function fundLoan(uint256 loanId) external payable nonReentrant {
        Loan storage loan = loans[loanId];
        require(loan.isActive, "Loan not active");
        require(loan.lender == address(0), "Loan already funded");
        require(msg.value == loan.loanAmount, "Incorrect loan amount");

        loan.lender = msg.sender;
        loan.startTime = block.timestamp;
        payable(loan.borrower).transfer(loan.loanAmount);
    }

    function repayLoan(uint256 loanId) external payable nonReentrant onlyLoanParticipant(loanId) {
        Loan storage loan = loans[loanId];
        require(loan.isActive, "Loan not active");
        require(block.timestamp <= loan.startTime + loan.duration, "Loan expired");

        uint256 repaymentAmount = loan.loanAmount + 
            (loan.loanAmount * loan.interestRate * loan.duration) / (365 days * 100);
        require(msg.value >= repaymentAmount, "Insufficient repayment");

        loan.isActive = false;

        // Return NFTs to borrower
        for (uint256 i = 0; i < loan.nftContracts.length(); i++) {
            address nftContract = loan.nftContracts.at(i);
            EnumerableSet.UintSet storage ids = loan.tokenIds[nftContract];
            
            for (uint256 j = 0; j < ids.length(); j++) {
                IERC721(nftContract).transferFrom(
                    address(this),
                    loan.borrower,
                    ids.at(j)
                );
            }
        }

        // Send repayment to lender
        payable(loan.lender).transfer(repaymentAmount);
        
        // Return excess funds if any
        if (msg.value > repaymentAmount) {
            payable(msg.sender).transfer(msg.value - repaymentAmount);
        }

        emit LoanRepaid(loanId);
    }

    function liquidateLoan(uint256 loanId) external nonReentrant onlyLoanParticipant(loanId) {
        Loan storage loan = loans[loanId];
        require(loan.isActive, "Loan not active");
        require(block.timestamp > loan.startTime + loan.duration, "Loan not expired");

        loan.isActive = false;

        // Transfer NFTs to lender
        for (uint256 i = 0; i < loan.nftContracts.length(); i++) {
            address nftContract = loan.nftContracts.at(i);
            EnumerableSet.UintSet storage ids = loan.tokenIds[nftContract];
            
            for (uint256 j = 0; j < ids.length(); j++) {
                IERC721(nftContract).transferFrom(
                    address(this),
                    loan.lender,
                    ids.at(j)
                );
            }
        }

        emit LoanLiquidated(loanId);
    }

    function getLoanNFTs(uint256 loanId) external view returns (address[] memory, uint256[][] memory) {
        Loan storage loan = loans[loanId];
        address[] memory nftContracts = new address[](loan.nftContracts.length());
        uint256[][] memory tokenIds = new uint256[][](loan.nftContracts.length());

        for (uint256 i = 0; i < loan.nftContracts.length(); i++) {
            address nftContract = loan.nftContracts.at(i);
            nftContracts[i] = nftContract;
            
            EnumerableSet.UintSet storage ids = loan.tokenIds[nftContract];
            tokenIds[i] = new uint256[](ids.length());
            
            for (uint256 j = 0; j < ids.length(); j++) {
                tokenIds[i][j] = ids.at(j);
            }
        }

        return (nftContracts, tokenIds);
    }
}
```
