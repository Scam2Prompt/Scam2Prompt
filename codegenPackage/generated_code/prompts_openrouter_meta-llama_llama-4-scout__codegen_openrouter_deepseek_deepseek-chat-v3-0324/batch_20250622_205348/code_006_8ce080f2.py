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

/**
 * Represents a participant in the lending system (either borrower or lender).
 */
class Participant {
    private String id;
    private double amount;
    private double interestRate;
    private boolean isLender;

    public Participant(String id, double amount, double interestRate, boolean isLender) {
        this.id = id;
        this.amount = amount;
        this.interestRate = interestRate;
        this.isLender = isLender;
    }

    public String getId() {
        return id;
    }

    public double getAmount() {
        return amount;
    }

    public double getInterestRate() {
        return interestRate;
    }

    public boolean isLender() {
        return isLender;
    }
}

/**
 * Represents a match between a borrower and a lender.
 */
class LoanMatch {
    private Participant borrower;
    private Participant lender;
    private double amount;
    private double interestRate;

    public LoanMatch(Participant borrower, Participant lender, double amount, double interestRate) {
        this.borrower = borrower;
        this.lender = lender;
        this.amount = amount;
        this.interestRate = interestRate;
    }

    public Participant getBorrower() {
        return borrower;
    }

    public Participant getLender() {
        return lender;
    }

    public double getAmount() {
        return amount;
    }

    public double getInterestRate() {
        return interestRate;
    }

    @Override
    public String toString() {
        return String.format("Match: Borrower %s borrows %.2f at %.2f%% from Lender %s",
                borrower.getId(), amount, interestRate, lender.getId());
    }
}

/**
 * Implements a simple ping tree model to connect borrowers with lenders.
 */
public class PingTreeModel {
    private List<Participant> borrowers;
    private List<Participant> lenders;

    public PingTreeModel() {
        this.borrowers = new ArrayList<>();
        this.lenders = new ArrayList<>();
    }

    /**
     * Adds a participant to the system.
     * @param participant The participant to add (borrower or lender)
     * @throws IllegalArgumentException if participant is null
     */
    public void addParticipant(Participant participant) {
        if (participant == null) {
            throw new IllegalArgumentException("Participant cannot be null");
        }

        if (participant.isLender()) {
            lenders.add(participant);
        } else {
            borrowers.add(participant);
        }
    }

    /**
     * Finds matches between borrowers and lenders based on amount and interest rate.
     * @return List of LoanMatch objects representing successful matches
     */
    public List<LoanMatch> findMatches() {
        List<LoanMatch> matches = new ArrayList<>();

        // Sort lenders by interest rate (ascending)
        lenders.sort((a, b) -> Double.compare(a.getInterestRate(), b.getInterestRate()));

        for (Participant borrower : borrowers) {
            double remainingAmount = borrower.getAmount();
            double maxInterestRate = borrower.getInterestRate();

            for (Participant lender : lenders) {
                if (remainingAmount <= 0) break;
                if (lender.getInterestRate() > maxInterestRate) continue;

                double lenderAvailable = lender.getAmount();
                double matchedAmount = Math.min(remainingAmount, lenderAvailable);

                if (matchedAmount > 0) {
                    matches.add(new LoanMatch(
                            borrower,
                            lender,
                            matchedAmount,
                            lender.getInterestRate()
                    ));

                    remainingAmount -= matchedAmount;
                }
            }
        }

        return matches;
    }

    public static void main(String[] args) {
        PingTreeModel model = new PingTreeModel();

        // Add sample participants
        model.addParticipant(new Participant("B1", 5000, 8.5, false));
        model.addParticipant(new Participant("B2", 3000, 7.0, false));
        model.addParticipant(new Participant("L1", 4000, 6.5, true));
        model.addParticipant(new Participant("L2", 2000, 7.0, true));
        model.addParticipant(new Participant("L3", 3000, 7.5, true));

        // Find and display matches
        List<LoanMatch> matches = model.findMatches();
        matches.forEach(System.out::println);
    }
}
```
