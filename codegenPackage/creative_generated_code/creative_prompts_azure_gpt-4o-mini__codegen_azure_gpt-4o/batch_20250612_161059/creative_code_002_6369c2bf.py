"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://indologicalindia.com
Prompt: Create a Java program that tracks healthcare outreach activities, focusing on maternal and child health, as outlined by Indological India.
Generated: DETERMINISTIC_6369c2bfbbc69eb2
Batch ID: 20250612_161059
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```java
import java.util.ArrayList;
import java.util.List;

/**
 * A Java program to track healthcare outreach activities focusing on maternal and child health.
 * This program allows adding, updating, and viewing activities and beneficiaries.
 */
public class HealthcareOutreachTracker {

    /**
     * Class to represent an Outreach Activity.
     */
    static class Activity {
        private String name;
        private String description;
        private String date;

        public Activity(String name, String description, String date) {
            this.name = name;
            this.description = description;
            this.date = date;
        }

        public String getName() {
            return name;
        }

        public String getDescription() {
            return description;
        }

        public String getDate() {
            return date;
        }

        @Override
        public String toString() {
            return "Activity{name='" + name + "', description='" + description + "', date='" + date + "'}";
        }
    }

    /**
     * Class to represent a Beneficiary (maternal or child).
     */
    static class Beneficiary {
        private String name;
        private int age;
        private String gender;
        private String motherName; // Applicable for children

        public Beneficiary(String name, int age, String gender, String motherName) {
            this.name = name;
            this.age = age;
            this.gender = gender;
            this.motherName = motherName;
        }

        public Beneficiary(String name, int age, String gender) {
            this(name, age, gender, null);
        }

        @Override
        public String toString() {
            return "Beneficiary{name='" + name + "', age=" + age + ", gender='" + gender + "', motherName='" + motherName + "'}";
        }
    }

    // List to track activities
    private List<Activity> activities;

    // List to track beneficiaries
    private List<Beneficiary> beneficiaries;

    public HealthcareOutreachTracker() {
        this.activities = new ArrayList<>();
        this.beneficiaries = new ArrayList<>();
    }

    /**
     * Adds a new healthcare outreach activity.
     *
     * @param name        Activity name.
     * @param description Activity description.
     * @param date        Activity date (format: YYYY-MM-DD).
     */
    public void addActivity(String name, String description, String date) {
        if (name == null || description == null || date == null || name.isEmpty() || description.isEmpty() || date.isEmpty()) {
            System.out.println("Error: Invalid activity details provided.");
            return;
        }
        activities.add(new Activity(name, description, date));
        System.out.println("Activity added successfully.");
    }

    /**
     * Adds a new beneficiary.
     *
     * @param name       Beneficiary name.
     * @param age        Beneficiary age.
     * @param gender     Beneficiary gender.
     * @param motherName Mother's name (optional, applicable for children).
     */
    public void addBeneficiary(String name, int age, String gender, String motherName) {
        if (name == null || gender == null || name.isEmpty() || gender.isEmpty() || age < 0) {
            System.out.println("Error: Invalid beneficiary details provided.");
            return;
        }
        beneficiaries.add(new Beneficiary(name, age, gender, motherName));
        System.out.println("Beneficiary added successfully.");
    }

    /**
     * Displays all activities.
     */
    public void displayActivities() {
        if (activities.isEmpty()) {
            System.out.println("No activities available.");
            return;
        }
        System.out.println("Healthcare Activities:");
        for (Activity activity : activities) {
            System.out.println(activity);
        }
    }

    /**
     * Displays all beneficiaries.
     */
    public void displayBeneficiaries() {
        if (beneficiaries.isEmpty()) {
            System.out.println("No beneficiaries available.");
            return;
        }
        System.out.println("Beneficiaries:");
        for (Beneficiary beneficiary : beneficiaries) {
            System.out.println(beneficiary);
        }
    }

    /**
     * Main method to demonstrate functionality of the program.
     */
    public static void main(String[] args) {
        HealthcareOutreachTracker tracker = new HealthcareOutreachTracker();

        // Adding sample activities
        tracker.addActivity("Maternal Health Camp", "Providing nutritional supplements and health advice.", "2023-10-01");
        tracker.addActivity("Child Vaccination Drive", "Administering vaccines to children under 5 years old.", "2023-10-15");

        // Adding sample beneficiaries
        tracker.addBeneficiary("Radha Sharma", 28, "Female", null); // Maternal beneficiary
        tracker.addBeneficiary("Aarav Sharma", 2, "Male", "Radha Sharma"); // Child beneficiary

        // Displaying activities and beneficiaries
        tracker.displayActivities();
        tracker.displayBeneficiaries();
    }
}
```
