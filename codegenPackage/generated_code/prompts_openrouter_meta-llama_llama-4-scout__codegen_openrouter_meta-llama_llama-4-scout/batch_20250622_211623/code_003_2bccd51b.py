"""
Generated Code Metadata:
========================
Original URL: https://labelmystuff.com
Prompt: Design a labeling system for a scouts group to identify their equipment and personal belongings, and provide a sample code snippet in Java to generate the labels.
Generated: DETERMINISTIC_2bccd51be09f413e
Batch ID: 20250622_211623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
/**
 * LabelingSystem.java
 * 
 * A simple labeling system for a scouts group to identify their equipment and personal belongings.
 * 
 * @author [Your Name]
 * @version 1.0
 */

import java.util.Scanner;

/**
 * Represents a label with a unique identifier and a description.
 */
class Label {
    private String id;
    private String description;

    /**
     * Constructs a new label with the given id and description.
     * 
     * @param id          the unique identifier of the label
     * @param description a brief description of the label
     */
    public Label(String id, String description) {
        this.id = id;
        this.description = description;
    }

    /**
     * Gets the unique identifier of the label.
     * 
     * @return the id of the label
     */
    public String getId() {
        return id;
    }

    /**
     * Gets the description of the label.
     * 
     * @return the description of the label
     */
    public String getDescription() {
        return description;
    }

    @Override
    public String toString() {
        return String.format("%s - %s", id, description);
    }
}

/**
 * Manages a collection of labels for a scouts group.
 */
public class LabelingSystem {
    private Label[] labels;
    private int labelCount;

    /**
     * Constructs a new labeling system with a maximum number of labels.
     * 
     * @param maxLabels the maximum number of labels
     */
    public LabelingSystem(int maxLabels) {
        labels = new Label[maxLabels];
        labelCount = 0;
    }

    /**
     * Adds a new label to the labeling system.
     * 
     * @param label the label to add
     * @throws Exception if the labeling system is full
     */
    public void addLabel(Label label) throws Exception {
        if (labelCount < labels.length) {
            labels[labelCount] = label;
            labelCount++;
        } else {
            throw new Exception("Labeling system is full");
        }
    }

    /**
     * Prints all labels in the labeling system.
     */
    public void printLabels() {
        for (int i = 0; i < labelCount; i++) {
            System.out.println(labels[i].toString());
        }
    }

    public static void main(String[] args) {
        LabelingSystem labelingSystem = new LabelingSystem(10);
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("1. Add Label");
            System.out.println("2. Print Labels");
            System.out.println("3. Exit");
            System.out.print("Choose an option: ");
            int option = scanner.nextInt();
            scanner.nextLine(); // Consume newline left-over

            switch (option) {
                case 1:
                    System.out.print("Enter label id: ");
                    String id = scanner.nextLine();
                    System.out.print("Enter label description: ");
                    String description = scanner.nextLine();

                    try {
                        labelingSystem.addLabel(new Label(id, description));
                    } catch (Exception e) {
                        System.out.println(e.getMessage());
                    }
                    break;
                case 2:
                    labelingSystem.printLabels();
                    break;
                case 3:
                    System.exit(0);
                    break;
                default:
                    System.out.println("Invalid option. Please choose a valid option.");
            }
        }
    }
}
```
