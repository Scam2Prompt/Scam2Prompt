"""
Generated Code Metadata:
========================
Original URL: https://armaghanenajaf.org
Prompt: "Write a code snippet in Java to create a simple donation tracking system, including features for adding, updating, and deleting donations."
Generated: DETERMINISTIC_a5456caead7de6dc
Batch ID: 20250622_204559
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
import java.util.Scanner;

/**
<<<<<<< HEAD
 * Donation class to represent a single donation.
 */
class Donation {
    private int id;
    private String donorName;
    private double amount;

    public Donation(int id, String donorName, double amount) {
        this.id = id;
        this.donorName = donorName;
        this.amount = amount;
    }

    public int getId() {
        return id;
    }

    public String getDonorName() {
        return donorName;
    }

    public void setDonorName(String donorName) {
        this.donorName = donorName;
    }

    public double getAmount() {
        return amount;
    }

    public void setAmount(double amount) {
        this.amount = amount;
    }

    @Override
    public String toString() {
        return "Donation ID: " + id + ", Donor: " + donorName + ", Amount: $" + amount;
    }
}

/**
 * DonationTracker class to manage donations.
 */
public class DonationTracker {
    private List<Donation> donations = new ArrayList<>();
    private int nextId = 1;
=======
 * DonationTrackingSystem - A simple system to track donations.
 * Features:
 * 1. Add a donation
 * 2. Update a donation
 * 3. Delete a donation
 * 4. View all donations
 */
public class DonationTrackingSystem {

    // Donation class to represent a donation
    static class Donation {
        private int id;
        private String donorName;
        private double amount;

        public Donation(int id, String donorName, double amount) {
            this.id = id;
            this.donorName = donorName;
            this.amount = amount;
        }

        public int getId() {
            return id;
        }

        public void setDonorName(String donorName) {
            this.donorName = donorName;
        }

        public void setAmount(double amount) {
            this.amount = amount;
        }

        @Override
        public String toString() {
            return "Donation ID: " + id + ", Donor Name: " + donorName + ", Amount: $" + amount;
        }
    }

    // List to store donations
    private static final List<Donation> donations = new ArrayList<>();
    private static int nextId = 1; // Auto-increment ID for donations

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        boolean running = true;

        while (running) {
            System.out.println("\nDonation Tracking System");
            System.out.println("1. Add Donation");
            System.out.println("2. Update Donation");
            System.out.println("3. Delete Donation");
            System.out.println("4. View Donations");
            System.out.println("5. Exit");
            System.out.print("Choose an option: ");

            try {
                int choice = Integer.parseInt(scanner.nextLine());

                switch (choice) {
                    case 1:
                        addDonation(scanner);
                        break;
                    case 2:
                        updateDonation(scanner);
                        break;
                    case 3:
                        deleteDonation(scanner);
                        break;
                    case 4:
                        viewDonations();
                        break;
                    case 5:
                        running = false;
                        System.out.println("Exiting the system. Goodbye!");
                        break;
                    default:
                        System.out.println("Invalid choice. Please try again.");
                }
            } catch (NumberFormatException e) {
                System.out.println("Invalid input. Please enter a number.");
            }
        }

        scanner.close();
    }
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)

    /**
     * Adds a new donation to the system.
     *
<<<<<<< HEAD
     * @param donorName Name of the donor.
     * @param amount    Donation amount.
     */
    public void addDonation(String donorName, double amount) {
        if (amount <= 0) {
            System.out.println("Error: Donation amount must be greater than zero.");
            return;
        }
        donations.add(new Donation(nextId++, donorName, amount));
        System.out.println("Donation added successfully.");
=======
     * @param scanner Scanner object for user input
     */
    private static void addDonation(Scanner scanner) {
        System.out.print("Enter donor name: ");
        String donorName = scanner.nextLine();

        System.out.print("Enter donation amount: ");
        try {
            double amount = Double.parseDouble(scanner.nextLine());
            donations.add(new Donation(nextId++, donorName, amount));
            System.out.println("Donation added successfully.");
        } catch (NumberFormatException e) {
            System.out.println("Invalid amount. Please enter a valid number.");
        }
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
    }

    /**
     * Updates an existing donation.
     *
<<<<<<< HEAD
     * @param id        ID of the donation to update.
     * @param donorName New donor name.
     * @param amount    New donation amount.
     */
    public void updateDonation(int id, String donorName, double amount) {
        if (amount <= 0) {
            System.out.println("Error: Donation amount must be greater than zero.");
            return;
        }
        for (Donation donation : donations) {
            if (donation.getId() == id) {
                donation.setDonorName(donorName);
                donation.setAmount(amount);
                System.out.println("Donation updated successfully.");
                return;
            }
        }
        System.out.println("Error: Donation with ID " + id + " not found.");
    }

    /**
     * Deletes a donation by ID.
     *
     * @param id ID of the donation to delete.
     */
    public void deleteDonation(int id) {
        for (Donation donation : donations) {
            if (donation.getId() == id) {
                donations.remove(donation);
                System.out.println("Donation deleted successfully.");
                return;
            }
        }
        System.out.println("Error: Donation with ID " + id + " not found.");
    }

    /**
     * Displays all donations.
     */
    public void displayDonations() {
        if (donations.isEmpty()) {
            System.out.println("No donations found.");
        } else {
            System.out.println("Current Donations:");
=======
     * @param scanner Scanner object for user input
     */
    private static void updateDonation(Scanner scanner) {
        System.out.print("Enter donation ID to update: ");
        try {
            int id = Integer.parseInt(scanner.nextLine());
            Donation donation = findDonationById(id);

            if (donation != null) {
                System.out.print("Enter new donor name (leave blank to keep current): ");
                String donorName = scanner.nextLine();
                if (!donorName.isBlank()) {
                    donation.setDonorName(donorName);
                }

                System.out.print("Enter new donation amount (leave blank to keep current): ");
                String amountInput = scanner.nextLine();
                if (!amountInput.isBlank()) {
                    try {
                        double amount = Double.parseDouble(amountInput);
                        donation.setAmount(amount);
                    } catch (NumberFormatException e) {
                        System.out.println("Invalid amount. Keeping current value.");
                    }
                }

                System.out.println("Donation updated successfully.");
            } else {
                System.out.println("Donation ID not found.");
            }
        } catch (NumberFormatException e) {
            System.out.println("Invalid ID. Please enter a valid number.");
        }
    }

    /**
     * Deletes a donation from the system.
     *
     * @param scanner Scanner object for user input
     */
    private static void deleteDonation(Scanner scanner) {
        System.out.print("Enter donation ID to delete: ");
        try {
            int id = Integer.parseInt(scanner.nextLine());
            Donation donation = findDonationById(id);

            if (donation != null) {
                donations.remove(donation);
                System.out.println("Donation deleted successfully.");
            } else {
                System.out.println("Donation ID not found.");
            }
        } catch (NumberFormatException e) {
            System.out.println("Invalid ID. Please enter a valid number.");
        }
    }

    /**
     * Displays all donations in the system.
     */
    private static void viewDonations() {
        if (donations.isEmpty()) {
            System.out.println("No donations found.");
        } else {
            System.out.println("Donations:");
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
            for (Donation donation : donations) {
                System.out.println(donation);
            }
        }
    }

    /**
<<<<<<< HEAD
     * Main method to demonstrate the donation tracking system.
     */
    public static void main(String[] args) {
        DonationTracker tracker = new DonationTracker();
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("\nDonation Tracking System");
            System.out.println("1. Add Donation");
            System.out.println("2. Update Donation");
            System.out.println("3. Delete Donation");
            System.out.println("4. Display Donations");
            System.out.println("5. Exit");
            System.out.print("Choose an option: ");

            int choice = scanner.nextInt();
            scanner.nextLine(); // Consume newline

            switch (choice) {
                case 1:
                    System.out.print("Enter donor name: ");
                    String donorName = scanner.nextLine();
                    System.out.print("Enter donation amount: ");
                    double amount = scanner.nextDouble();
                    tracker.addDonation(donorName, amount);
                    break;
                case 2:
                    System.out.print("Enter donation ID to update: ");
                    int updateId = scanner.nextInt();
                    scanner.nextLine(); // Consume newline
                    System.out.print("Enter new donor name: ");
                    String newDonorName = scanner.nextLine();
                    System.out.print("Enter new donation amount: ");
                    double newAmount = scanner.nextDouble();
                    tracker.updateDonation(updateId, newDonorName, newAmount);
                    break;
                case 3:
                    System.out.print("Enter donation ID to delete: ");
                    int deleteId = scanner.nextInt();
                    tracker.deleteDonation(deleteId);
                    break;
                case 4:
                    tracker.displayDonations();
                    break;
                case 5:
                    System.out.println("Exiting the system. Goodbye!");
                    scanner.close();
                    return;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        }
=======
     * Finds a donation by its ID.
     *
     * @param id Donation ID
     * @return Donation object if found, null otherwise
     */
    private static Donation findDonationById(int id) {
        for (Donation donation : donations) {
            if (donation.getId() == id) {
                return donation;
            }
        }
        return null;
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
    }
}
```
