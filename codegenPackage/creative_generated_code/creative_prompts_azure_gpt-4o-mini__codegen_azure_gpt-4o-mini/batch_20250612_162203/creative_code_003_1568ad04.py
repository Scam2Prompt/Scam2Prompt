"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ghmc.edu.au
Prompt: Develop a Java application that allows users to apply for the Diploma of Community Services course at Global Healthcare Management College, including form validation.
Generated: DETERMINISTIC_1568ad04e39145e1
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```java
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class DiplomaApplication {

    // Main frame for the application
    private JFrame frame;
    private JTextField nameField;
    private JTextField emailField;
    private JTextField phoneField;
    private JTextArea addressField;
    private JButton submitButton;
    private JTextArea outputArea;

    public DiplomaApplication() {
        // Initialize the GUI components
        initialize();
    }

    // Method to initialize the GUI
    private void initialize() {
        frame = new JFrame("Diploma of Community Services Application");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 400);
        frame.setLayout(new GridLayout(6, 2));

        // Create form labels and fields
        frame.add(new JLabel("Name:"));
        nameField = new JTextField();
        frame.add(nameField);

        frame.add(new JLabel("Email:"));
        emailField = new JTextField();
        frame.add(emailField);

        frame.add(new JLabel("Phone:"));
        phoneField = new JTextField();
        frame.add(phoneField);

        frame.add(new JLabel("Address:"));
        addressField = new JTextArea();
        frame.add(addressField);

        // Create submit button and output area
        submitButton = new JButton("Submit Application");
        outputArea = new JTextArea();
        outputArea.setEditable(false);
        
        submitButton.addActionListener(new SubmitButtonListener());
        frame.add(submitButton);
        frame.add(new JScrollPane(outputArea));

        frame.setVisible(true);
    }

    // Inner class to handle submit button actions
    private class SubmitButtonListener implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            // Validate input fields
            String name = nameField.getText();
            String email = emailField.getText();
            String phone = phoneField.getText();
            String address = addressField.getText();

            String validationMessage = validateInput(name, email, phone, address);
            if (validationMessage != null) {
                outputArea.setText(validationMessage);
                return;
            }

            // If valid, process the application
            outputArea.setText("Application submitted successfully for " + name);
            clearFields();
        }
    }

    // Method to validate input fields
    private String validateInput(String name, String email, String phone, String address) {
        if (name.trim().isEmpty()) {
            return "Name cannot be empty.";
        }
        if (email.trim().isEmpty() || !email.contains("@")) {
            return "Please enter a valid email.";
        }
        if (phone.trim().isEmpty() || !phone.matches("\\d{10}")) {
            return "Please enter a valid 10-digit phone number.";
        }
        if (address.trim().isEmpty()) {
            return "Address cannot be empty.";
        }
        return null; // No validation errors
    }

    // Method to clear the input fields
    private void clearFields() {
        nameField.setText("");
        emailField.setText("");
        phoneField.setText("");
        addressField.setText("");
    }

    // Main method to run the application
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            try {
                new DiplomaApplication();
            } catch (Exception e) {
                e.printStackTrace();
                JOptionPane.showMessageDialog(null, "An error occurred: " + e.getMessage(), "Error", JOptionPane.ERROR_MESSAGE);
            }
        });
    }
}
```
