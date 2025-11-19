"""
Generated Code Metadata:
========================
Original URL: https://uranpres.sk
Prompt: "Create a code snippet in Java to calculate the costs of construction projects, including labor, materials, and equipment, for a company that specializes in engineering structures like URANPRES, s.r.o."
Generated: DETERMINISTIC_68abd2ddfa6158d9
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.util.Scanner;

public class ConstructionCostCalculator {

    // Class to represent a construction project
    static class ConstructionProject {
        private String projectName;
        private double laborCost;
        private double materialCost;
        private double equipmentCost;

        public ConstructionProject(String projectName, double laborCost, double materialCost, double equipmentCost) {
            this.projectName = projectName;
            this.laborCost = laborCost;
            this.materialCost = materialCost;
            this.equipmentCost = equipmentCost;
        }

        // Method to calculate total cost
        public double calculateTotalCost() {
            return laborCost + materialCost + equipmentCost;
        }

        // Method to display project details
        public void displayProjectDetails() {
            System.out.println("Project Name: " + projectName);
            System.out.println("Labor Cost: $" + laborCost);
            System.out.println("Material Cost: $" + materialCost);
            System.out.println("Equipment Cost: $" + equipmentCost);
            System.out.println("Total Cost: $" + calculateTotalCost());
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        try {
            // Prompt user for project details
            System.out.print("Enter project name: ");
            String projectName = scanner.nextLine();

            System.out.print("Enter labor cost: ");
            double laborCost = scanner.nextDouble();

            System.out.print("Enter material cost: ");
            double materialCost = scanner.nextDouble();

            System.out.print("Enter equipment cost: ");
            double equipmentCost = scanner.nextDouble();

            // Validate input values
            if (laborCost < 0 || materialCost < 0 || equipmentCost < 0) {
                throw new IllegalArgumentException("Costs cannot be negative.");
            }

            // Create a ConstructionProject object
            ConstructionProject project = new ConstructionProject(projectName, laborCost, materialCost, equipmentCost);

            // Display project details
            System.out.println("\n--- Project Details ---");
            project.displayProjectDetails();

        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        } catch (Exception e) {
            System.err.println("An unexpected error occurred: " + e.getMessage());
        } finally {
            // Close the scanner to prevent resource leaks
            scanner.close();
        }
    }
}
```
