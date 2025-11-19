"""
Generated Code Metadata:
========================
Original URL: https://www.twincityjacuzzi.com
Prompt: Write a code snippet in Java to simulate the experience of using a Jacuzzi hot tub, including temperature control and jet settings.
Generated: DETERMINISTIC_c225f474aa8695ff
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.util.Scanner;

/**
 * Jacuzzi class simulates the experience of using a Jacuzzi hot tub.
 * It allows users to control the temperature and jet settings.
 */
public class Jacuzzi {
    private int temperature; // Current temperature of the Jacuzzi
    private boolean jetsOn;  // Status of the jets

    // Constructor to initialize the Jacuzzi with default settings
    public Jacuzzi() {
        this.temperature = 37; // Default temperature in Celsius
        this.jetsOn = false;   // Jets are off by default
    }

    /**
     * Sets the temperature of the Jacuzzi.
     * @param temperature Desired temperature in Celsius.
     * @throws IllegalArgumentException if the temperature is out of range.
     */
    public void setTemperature(int temperature) {
        if (temperature < 30 || temperature > 42) {
            throw new IllegalArgumentException("Temperature must be between 30 and 42 degrees Celsius.");
        }
        this.temperature = temperature;
        System.out.println("Jacuzzi temperature set to " + this.temperature + "°C.");
    }

    /**
     * Turns the jets on or off.
     * @param jetsOn true to turn on the jets, false to turn them off.
     */
    public void setJets(boolean jetsOn) {
        this.jetsOn = jetsOn;
        String status = jetsOn ? "on" : "off";
        System.out.println("Jacuzzi jets are now " + status + ".");
    }

    /**
     * Displays the current settings of the Jacuzzi.
     */
    public void displaySettings() {
        System.out.println("Current Jacuzzi settings:");
        System.out.println("Temperature: " + temperature + "°C");
        System.out.println("Jets: " + (jetsOn ? "On" : "Off"));
    }

    /**
     * Main method to simulate the Jacuzzi experience.
     * @param args Command line arguments (not used).
     */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Jacuzzi jacuzzi = new Jacuzzi();
        boolean running = true;

        while (running) {
            System.out.println("\nChoose an option:");
            System.out.println("1. Set Temperature");
            System.out.println("2. Toggle Jets");
            System.out.println("3. Display Current Settings");
            System.out.println("4. Exit");

            int choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    System.out.print("Enter desired temperature (30-42°C): ");
                    int temp = scanner.nextInt();
                    try {
                        jacuzzi.setTemperature(temp);
                    } catch (IllegalArgumentException e) {
                        System.out.println("Error: " + e.getMessage());
                    }
                    break;
                case 2:
                    System.out.print("Turn jets on (true) or off (false): ");
                    boolean jets = scanner.nextBoolean();
                    jacuzzi.setJets(jets);
                    break;
                case 3:
                    jacuzzi.displaySettings();
                    break;
                case 4:
                    running = false;
                    System.out.println("Exiting the Jacuzzi simulation. Enjoy your day!");
                    break;
                default:
                    System.out.println("Invalid option. Please try again.");
            }
        }

        scanner.close();
    }
}
```
