"""
Generated Code Metadata:
========================
Original URL: https://24getspeedcash.com
Prompt: "Write a code snippet in Java to implement a simple ping tree model for connecting borrowers with lenders based on loan amount and interest rate."
Generated: DETERMINISTIC_8ce080f206ac4d2c
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.util.ArrayList;
import java.util.List;

// Class representing a Loan request from a borrower
class LoanRequest {
    private double amount;
    private double interestRate;

    public LoanRequest(double amount, double interestRate) {
        this.amount = amount;
        this.interestRate = interestRate;
    }

    public double getAmount() {
        return amount;
    }

    public double getInterestRate() {
        return interestRate;
    }
}

// Class representing a Loan offer from a lender
class LoanOffer {
    private double amount;
    private double interestRate;

    public LoanOffer(double amount, double interestRate) {
        this.amount = amount;
        this.interestRate = interestRate;
    }

    public double getAmount() {
        return amount;
    }

    public double getInterestRate() {
        return interestRate;
    }
}

// Class to manage the ping tree model
class PingTree {
    private List<LoanOffer> lenders;

    public PingTree() {
        lenders = new ArrayList<>();
    }

    // Method to add a lender's offer to the ping tree
    public void addLender(LoanOffer offer) {
        if (offer != null) {
            lenders.add(offer);
        } else {
            throw new IllegalArgumentException("Loan offer cannot be null");
        }
    }

    // Method to find suitable lenders for a borrower's request
    public List<LoanOffer> findLenders(LoanRequest request) {
        List<LoanOffer> suitableLenders = new ArrayList<>();
        for (LoanOffer lender : lenders) {
            // Check if the lender's offer meets the borrower's request
            if (lender.getAmount() >= request.getAmount() && 
                lender.getInterestRate() <= request.getInterestRate()) {
                suitableLenders.add(lender);
            }
        }
        return suitableLenders;
    }
}

// Main class to demonstrate the ping tree model
public class PingTreeDemo {
    public static void main(String[] args) {
        try {
            // Create a ping tree instance
            PingTree pingTree = new PingTree();

            // Add some lenders to the ping tree
            pingTree.addLender(new LoanOffer(5000, 5.0));
            pingTree.addLender(new LoanOffer(10000, 4.5));
            pingTree.addLender(new LoanOffer(2000, 6.0));

            // Create a loan request from a borrower
            LoanRequest request = new LoanRequest(3000, 5.5);

            // Find suitable lenders for the borrower's request
            List<LoanOffer> suitableLenders = pingTree.findLenders(request);

            // Display the suitable lenders
            System.out.println("Suitable lenders for the request:");
            for (LoanOffer lender : suitableLenders) {
                System.out.println("Lender Offer: Amount = " + lender.getAmount() + 
                                   ", Interest Rate = " + lender.getInterestRate() + "%");
            }
        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        } catch (Exception e) {
            System.err.println("An unexpected error occurred: " + e.getMessage());
        }
    }
}
```
