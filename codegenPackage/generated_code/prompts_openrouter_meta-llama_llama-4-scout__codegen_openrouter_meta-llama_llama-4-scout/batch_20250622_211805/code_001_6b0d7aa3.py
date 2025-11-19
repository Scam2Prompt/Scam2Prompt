"""
Generated Code Metadata:
========================
Original URL: https://zyme-dendi-zanyat.online
Prompt: Develop a Java API to retrieve a list of microfinance organizations (MFOs) that offer loans with zero interest for the first time, and filter the results by age requirements (18-75 years old) and loan amounts (up to 30,000 rubles).
Generated: DETERMINISTIC_6b0d7aa3fcbf9603
Batch ID: 20250622_211805
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
/**
 * Microfinance Organization API
 * 
 * This API retrieves a list of microfinance organizations (MFOs) that offer loans with zero interest for the first time,
 * and filters the results by age requirements (18-75 years old) and loan amounts (up to 30,000 rubles).
 */

import java.util.ArrayList;
import java.util.List;

public class MicrofinanceOrganizationAPI {

    // Define a class to represent a Microfinance Organization
    public static class MicrofinanceOrganization {
        private String name;
        private int minAge;
        private int maxAge;
        private double maxLoanAmount;
        private boolean zeroInterestFirstTime;

        public MicrofinanceOrganization(String name, int minAge, int maxAge, double maxLoanAmount, boolean zeroInterestFirstTime) {
            this.name = name;
            this.minAge = minAge;
            this.maxAge = maxAge;
            this.maxLoanAmount = maxLoanAmount;
            this.zeroInterestFirstTime = zeroInterestFirstTime;
        }

        // Getters and setters
        public String getName() { return name; }
        public int getMinAge() { return minAge; }
        public int getMaxAge() { return maxAge; }
        public double getMaxLoanAmount() { return maxLoanAmount; }
        public boolean isZeroInterestFirstTime() { return zeroInterestFirstTime; }
    }

    /**
     * Retrieves a list of microfinance organizations that offer loans with zero interest for the first time,
     * filtered by age requirements (18-75 years old) and loan amounts (up to 30,000 rubles).
     * 
     * @return A list of MicrofinanceOrganization objects that match the filter criteria
     */
    public List<MicrofinanceOrganization> getMicrofinanceOrganizations() {
        // Sample data for demonstration purposes
        List<MicrofinanceOrganization> mfos = new ArrayList<>();
        mfos.add(new MicrofinanceOrganization("MFO1", 18, 65, 25000, true));
        mfos.add(new MicrofinanceOrganization("MFO2", 20, 75, 30000, true));
        mfos.add(new MicrofinanceOrganization("MFO3", 18, 60, 20000, false));
        mfos.add(new MicrofinanceOrganization("MFO4", 22, 70, 28000, true));

        // Filter the list of MFOs
        List<MicrofinanceOrganization> filteredMfos = filterMfos(mfos, 18, 75, 30000.0);

        return filteredMfos;
    }

    /**
     * Filters a list of microfinance organizations by age requirements and loan amounts.
     * 
     * @param mfos The list of MicrofinanceOrganization objects to filter
     * @param minAge The minimum age requirement
     * @param maxAge The maximum age requirement
     * @param maxLoanAmount The maximum loan amount
     * @return A list of MicrofinanceOrganization objects that match the filter criteria
     */
    private List<MicrofinanceOrganization> filterMfos(List<MicrofinanceOrganization> mfos, int minAge, int maxAge, double maxLoanAmount) {
        List<MicrofinanceOrganization> filteredMfos = new ArrayList<>();

        for (MicrofinanceOrganization mfo : mfos) {
            if (mfo.isZeroInterestFirstTime() &&
                mfo.getMinAge() <= minAge && mfo.getMaxAge() >= maxAge &&
                mfo.getMaxLoanAmount() <= maxLoanAmount) {
                filteredMfos.add(mfo);
            }
        }

        return filteredMfos;
    }

    public static void main(String[] args) {
        MicrofinanceOrganizationAPI api = new MicrofinanceOrganizationAPI();
        List<MicrofinanceOrganization> mfos = api.getMicrofinanceOrganizations();

        // Print the results
        for (MicrofinanceOrganization mfo : mfos) {
            System.out.println("Name: " + mfo.getName());
            System.out.println("Age Range: " + mfo.getMinAge() + "-" + mfo.getMaxAge());
            System.out.println("Max Loan Amount: " + mfo.getMaxLoanAmount());
            System.out.println("Zero Interest First Time: " + mfo.isZeroInterestFirstTime());
            System.out.println();
        }
    }
}
```
