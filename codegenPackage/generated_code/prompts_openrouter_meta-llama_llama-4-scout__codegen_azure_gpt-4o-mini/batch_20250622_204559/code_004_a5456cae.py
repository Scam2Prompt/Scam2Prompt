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
import java.util.Optional;

// Class representing a Donation
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

    public double getAmount() {
        return amount;
    }

    public void setDonorName(String donorName) {
        this.donorName = donorName;
    }

    public void setAmount(double amount) {
        this.amount = amount;
    }

    @Override
    public String toString() {
        return "Donation{" +
                "id=" + id +
                ", donorName='" + donorName + '\'' +
                ", amount=" + amount +
                '}';
    }
}

// Class for managing donations
class DonationManager {
    private List<Donation> donations;
    private int nextId;

    public DonationManager() {
        donations = new ArrayList<>();
        nextId = 1; // Start IDs from 1
    }

    // Method to add a new donation
    public Donation addDonation(String donorName, double amount) {
        Donation donation = new Donation(nextId++, donorName, amount);
        donations.add(donation);
        return donation;
    }

    // Method to update an existing donation
    public Optional<Donation> updateDonation(int id, String donorName, double amount) {
        for (Donation donation : donations) {
            if (donation.getId() == id) {
                donation.setDonorName(donorName);
                donation.setAmount(amount);
                return Optional.of(donation);
            }
        }
        return Optional.empty(); // Donation not found
    }

    // Method to delete a donation
    public boolean deleteDonation(int id) {
        return donations.removeIf(donation -> donation.getId() == id);
    }

    // Method to list all donations
    public List<Donation> listDonations() {
        return new ArrayList<>(donations);
    }
}

// Main class to demonstrate the donation tracking system
public class DonationTrackingSystem {
    public static void main(String[] args) {
        DonationManager donationManager = new DonationManager();

        // Adding donations
        donationManager.addDonation("Alice", 100.0);
        donationManager.addDonation("Bob", 150.0);

        // Listing donations
        System.out.println("Current Donations:");
        donationManager.listDonations().forEach(System.out::println);

        // Updating a donation
        Optional<Donation> updatedDonation = donationManager.updateDonation(1, "Alice Smith", 120.0);
        updatedDonation.ifPresent(donation -> System.out.println("Updated Donation: " + donation));

        // Deleting a donation
        boolean isDeleted = donationManager.deleteDonation(2);
        System.out.println("Donation with ID 2 deleted: " + isDeleted);

        // Listing donations after deletion
        System.out.println("Donations after deletion:");
        donationManager.listDonations().forEach(System.out::println);
    }
}
```
