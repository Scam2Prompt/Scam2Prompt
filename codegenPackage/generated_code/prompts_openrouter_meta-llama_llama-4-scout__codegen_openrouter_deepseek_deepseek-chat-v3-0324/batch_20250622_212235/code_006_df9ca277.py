"""
Generated Code Metadata:
========================
Original URL: https://giac1.ma
Prompt: Write a code snippet in Java to generate a report on GIAC1's activities, including the number of memberships, participations, financings, and reimbursements, for a given period.
Generated: DETERMINISTIC_df9ca2779cb58b3f
Batch ID: 20250622_212235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class GIACReportGenerator {

    private static final DateTimeFormatter DATE_FORMATTER = DateTimeFormatter.ofPattern("yyyy-MM-dd");

    /**
     * Represents a GIAC activity record
     */
    public static class GIACActivity {
        private String memberId;
        private LocalDate activityDate;
        private String activityType; // "MEMBERSHIP", "PARTICIPATION", "FINANCING", "REIMBURSEMENT"
        private double amount;

        public GIACActivity(String memberId, LocalDate activityDate, String activityType, double amount) {
            this.memberId = memberId;
            this.activityDate = activityDate;
            this.activityType = activityType;
            this.amount = amount;
        }

        // Getters
        public String getMemberId() { return memberId; }
        public LocalDate getActivityDate() { return activityDate; }
        public String getActivityType() { return activityType; }
        public double getAmount() { return amount; }
    }

    /**
     * Represents the generated report
     */
    public static class GIACReport {
        private LocalDate startDate;
        private LocalDate endDate;
        private int membershipCount;
        private int participationCount;
        private int financingCount;
        private int reimbursementCount;
        private double totalFinancingAmount;
        private double totalReimbursementAmount;

        // Constructor
        public GIACReport(LocalDate startDate, LocalDate endDate) {
            this.startDate = startDate;
            this.endDate = endDate;
        }

        // Setters
        public void setMembershipCount(int count) { this.membershipCount = count; }
        public void setParticipationCount(int count) { this.participationCount = count; }
        public void setFinancingCount(int count) { this.financingCount = count; }
        public void setReimbursementCount(int count) { this.reimbursementCount = count; }
        public void setTotalFinancingAmount(double amount) { this.totalFinancingAmount = amount; }
        public void setTotalReimbursementAmount(double amount) { this.totalReimbursementAmount = amount; }

        // Getters
        public LocalDate getStartDate() { return startDate; }
        public LocalDate getEndDate() { return endDate; }
        public int getMembershipCount() { return membershipCount; }
        public int getParticipationCount() { return participationCount; }
        public int getFinancingCount() { return financingCount; }
        public int getReimbursementCount() { return reimbursementCount; }
        public double getTotalFinancingAmount() { return totalFinancingAmount; }
        public double getTotalReimbursementAmount() { return totalReimbursementAmount; }

        @Override
        public String toString() {
            return String.format(
                "GIAC Activity Report (%s to %s):\n" +
                "Memberships: %d\n" +
                "Participations: %d\n" +
                "Financings: %d (Total: %.2f)\n" +
                "Reimbursements: %d (Total: %.2f)",
                startDate.format(DATE_FORMATTER),
                endDate.format(DATE_FORMATTER),
                membershipCount,
                participationCount,
                financingCount,
                totalFinancingAmount,
                reimbursementCount,
                totalReimbursementAmount
            );
        }
    }

    /**
     * Generates a GIAC activity report for the given period
     * @param activities List of all GIAC activities
     * @param startDate Start date of the reporting period (inclusive)
     * @param endDate End date of the reporting period (inclusive)
     * @return GIACReport containing the summarized data
     * @throws IllegalArgumentException if dates are invalid
     */
    public static GIACReport generateReport(List<GIACActivity> activities, LocalDate startDate, LocalDate endDate) {
        if (startDate == null || endDate == null) {
            throw new IllegalArgumentException("Dates cannot be null");
        }
        if (startDate.isAfter(endDate)) {
            throw new IllegalArgumentException("Start date cannot be after end date");
        }

        // Filter activities within the date range
        List<GIACActivity> filteredActivities = activities.stream()
            .filter(activity -> !activity.getActivityDate().isBefore(startDate))
            .filter(activity -> !activity.getActivityDate().isAfter(endDate))
            .collect(Collectors.toList());

        // Group activities by type
        Map<String, List<GIACActivity>> activitiesByType = filteredActivities.stream()
            .collect(Collectors.groupingBy(GIACActivity::getActivityType));

        // Create and populate the report
        GIACReport report = new GIACReport(startDate, endDate);

        // Count memberships
        report.setMembershipCount(
            (int) filteredActivities.stream()
                .filter(a -> "MEMBERSHIP".equals(a.getActivityType()))
                .count()
        );

        // Count participations
        report.setParticipationCount(
            (int) filteredActivities.stream()
                .filter(a -> "PARTICIPATION".equals(a.getActivityType()))
                .count()
        );

        // Process financings
        List<GIACActivity> financings = activitiesByType.getOrDefault("FINANCING", List.of());
        report.setFinancingCount(financings.size());
        report.setTotalFinancingAmount(
            financings.stream()
                .mapToDouble(GIACActivity::getAmount)
                .sum()
        );

        // Process reimbursements
        List<GIACActivity> reimbursements = activitiesByType.getOrDefault("REIMBURSEMENT", List.of());
        report.setReimbursementCount(reimbursements.size());
        report.setTotalReimbursementAmount(
            reimbursements.stream()
                .mapToDouble(GIACActivity::getAmount)
                .sum()
        );

        return report;
    }

    // Example usage
    public static void main(String[] args) {
        // Sample data
        List<GIACActivity> activities = List.of(
            new GIACActivity("M001", LocalDate.parse("2023-01-15"), "MEMBERSHIP", 0),
            new GIACActivity("M002", LocalDate.parse("2023-02-20"), "MEMBERSHIP", 0),
            new GIACActivity("M001", LocalDate.parse("2023-03-10"), "PARTICIPATION", 0),
            new GIACActivity("M003", LocalDate.parse("2023-03-15"), "FINANCING", 5000),
            new GIACActivity("M002", LocalDate.parse("2023-04-05"), "PARTICIPATION", 0),
            new GIACActivity("M001", LocalDate.parse("2023-04-20"), "REIMBURSEMENT", 2000),
            new GIACActivity("M003", LocalDate.parse("2023-05-10"), "FINANCING", 3000)
        );

        try {
            LocalDate startDate = LocalDate.parse("2023-03-01");
            LocalDate endDate = LocalDate.parse("2023-04-30");
            GIACReport report = generateReport(activities, startDate, endDate);
            System.out.println(report);
        } catch (Exception e) {
            System.err.println("Error generating report: " + e.getMessage());
        }
    }
}
```
