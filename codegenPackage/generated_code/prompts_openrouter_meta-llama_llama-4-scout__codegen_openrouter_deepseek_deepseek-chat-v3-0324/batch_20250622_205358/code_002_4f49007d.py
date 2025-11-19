"""
Generated Code Metadata:
========================
Original URL: https://munshihr.com
Prompt: Generate a code snippet in Java to create a simple background verification system that checks employee credentials and provides a report.
Generated: DETERMINISTIC_4f49007d212affcb
Batch ID: 20250622_205358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.util.HashMap;
import java.util.Map;

/**
 * A simple background verification system for employee credentials.
 */
public class EmployeeVerificationSystem {

    /**
     * Represents an employee with credentials to be verified.
     */
    static class Employee {
        private String id;
        private String name;
        private String education;
        private int yearsOfExperience;
        private boolean criminalRecord;

        public Employee(String id, String name, String education, int yearsOfExperience, boolean criminalRecord) {
            this.id = id;
            this.name = name;
            this.education = education;
            this.yearsOfExperience = yearsOfExperience;
            this.criminalRecord = criminalRecord;
        }

        // Getters
        public String getId() { return id; }
        public String getName() { return name; }
        public String getEducation() { return education; }
        public int getYearsOfExperience() { return yearsOfExperience; }
        public boolean hasCriminalRecord() { return criminalRecord; }
    }

    /**
     * Represents the verification report for an employee.
     */
    static class VerificationReport {
        private String employeeId;
        private String employeeName;
        private boolean educationVerified;
        private boolean experienceVerified;
        private boolean criminalRecordClear;
        private boolean overallStatus;

        public VerificationReport(String employeeId, String employeeName, 
                                boolean educationVerified, boolean experienceVerified, 
                                boolean criminalRecordClear, boolean overallStatus) {
            this.employeeId = employeeId;
            this.employeeName = employeeName;
            this.educationVerified = educationVerified;
            this.experienceVerified = experienceVerified;
            this.criminalRecordClear = criminalRecordClear;
            this.overallStatus = overallStatus;
        }

        @Override
        public String toString() {
            return String.format(
                "Verification Report for %s (ID: %s):%n" +
                "Education Verified: %s%n" +
                "Experience Verified: %s%n" +
                "Criminal Record Clear: %s%n" +
                "Overall Verification Status: %s%n",
                employeeName, employeeId,
                educationVerified ? "Yes" : "No",
                experienceVerified ? "Yes" : "No",
                criminalRecordClear ? "Yes" : "No",
                overallStatus ? "PASSED" : "FAILED"
            );
        }
    }

    /**
     * Database of valid education credentials (simplified for demo).
     */
    private static final Map<String, Boolean> EDUCATION_DATABASE = new HashMap<>();
    static {
        EDUCATION_DATABASE.put("Bachelor's Degree", true);
        EDUCATION_DATABASE.put("Master's Degree", true);
        EDUCATION_DATABASE.put("PhD", true);
    }

    /**
     * Verifies an employee's credentials.
     * @param employee The employee to verify
     * @return VerificationReport containing results
     * @throws IllegalArgumentException if employee is null
     */
    public static VerificationReport verifyEmployee(Employee employee) {
        if (employee == null) {
            throw new IllegalArgumentException("Employee cannot be null");
        }

        boolean educationVerified = verifyEducation(employee.getEducation());
        boolean experienceVerified = verifyExperience(employee.getYearsOfExperience());
        boolean criminalRecordClear = !employee.hasCriminalRecord();
        boolean overallStatus = educationVerified && experienceVerified && criminalRecordClear;

        return new VerificationReport(
            employee.getId(),
            employee.getName(),
            educationVerified,
            experienceVerified,
            criminalRecordClear,
            overallStatus
        );
    }

    /**
     * Verifies education credentials against database.
     * @param education The education level to verify
     * @return true if verified, false otherwise
     */
    private static boolean verifyEducation(String education) {
        return EDUCATION_DATABASE.containsKey(education);
    }

    /**
     * Verifies experience meets minimum requirements.
     * @param yearsOfExperience Years of experience to verify
     * @return true if >= 2 years, false otherwise
     */
    private static boolean verifyExperience(int yearsOfExperience) {
        return yearsOfExperience >= 2;
    }

    public static void main(String[] args) {
        // Example usage
        Employee employee1 = new Employee("EMP001", "John Doe", "Bachelor's Degree", 5, false);
        Employee employee2 = new Employee("EMP002", "Jane Smith", "High School", 1, true);

        System.out.println(verifyEmployee(employee1));
        System.out.println(verifyEmployee(employee2));
    }
}
```
