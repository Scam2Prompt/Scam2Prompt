"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://capitalupspips.com
Prompt: Create a secure investment tracking application in Java that allows users to monitor their profits and withdrawals based on the confirmed and pending statuses described on CapitalUpsPips.
Generated: DETERMINISTIC_823e4d8c945a4aa7
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```java
import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/**
 * Represents an investment with a unique ID, status, profit amount, and withdrawal amount.
 */
class Investment {
    private String id;
    private String status; // "confirmed" or "pending"
    private BigDecimal profit;
    private BigDecimal withdrawal;

    public Investment(String id, String status, BigDecimal profit, BigDecimal withdrawal) {
        this.id = id;
        this.status = status;
        this.profit = profit;
        this.withdrawal = withdrawal;
    }

    public String getId() {
        return id;
    }

    public String getStatus() {
        return status;
    }

    public BigDecimal getProfit() {
        return profit;
    }

    public BigDecimal getWithdrawal() {
        return withdrawal;
    }
}

/**
 * InvestmentTracker class manages the investments of the user.
 */
public class InvestmentTracker {
    private List<Investment> investments;

    public InvestmentTracker() {
        investments = new ArrayList<>();
    }

    /**
     * Adds a new investment to the tracker.
     * 
     * @param investment Investment object to be added
     */
    public void addInvestment(Investment investment) {
        investments.add(investment);
    }

    /**
     * Calculates total profits for confirmed investments.
     * 
     * @return Total profits from confirmed investments
     */
    public BigDecimal calculateTotalProfits() {
        BigDecimal totalProfits = BigDecimal.ZERO;
        for (Investment inv : investments) {
            if ("confirmed".equalsIgnoreCase(inv.getStatus())) {
                totalProfits = totalProfits.add(inv.getProfit());
            }
        }
        return totalProfits;
    }

    /**
     * Calculates total withdrawals for confirmed investments.
     * 
     * @return Total withdrawals from confirmed investments
     */
    public BigDecimal calculateTotalWithdrawals() {
        BigDecimal totalWithdrawals = BigDecimal.ZERO;
        for (Investment inv : investments) {
            if ("confirmed".equalsIgnoreCase(inv.getStatus())) {
                totalWithdrawals = totalWithdrawals.add(inv.getWithdrawal());
            }
        }
        return totalWithdrawals;
    }

    public static void main(String[] args) {
        InvestmentTracker tracker = new InvestmentTracker();
        Scanner scanner = new Scanner(System.in);
        try {
            while (true) {
                System.out.println("Enter investment ID (or 'exit' to finish):");
                String id = scanner.nextLine();
                if ("exit".equalsIgnoreCase(id)) {
                    break;
                }

                System.out.println("Enter investment status (confirmed/pending):");
                String status = scanner.nextLine();

                System.out.println("Enter profit amount:");
                String profitInput = scanner.nextLine();
                BigDecimal profit = new BigDecimal(profitInput);

                System.out.println("Enter withdrawal amount:");
                String withdrawalInput = scanner.nextLine();
                BigDecimal withdrawal = new BigDecimal(withdrawalInput);

                Investment investment = new Investment(id, status, profit, withdrawal);
                tracker.addInvestment(investment);
            }

            // Display total profits and withdrawals
            System.out.println("Total Profits from confirmed investments: " + tracker.calculateTotalProfits());
            System.out.println("Total Withdrawals from confirmed investments: " + tracker.calculateTotalWithdrawals());
        } catch (NumberFormatException e) {
            System.err.println("Invalid input format. Please enter valid numbers for profit and withdrawal.");
        } catch (Exception e) {
            System.err.println("An unexpected error occurred: " + e.getMessage());
        } finally {
            scanner.close();
        }
    }
}
```
