"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pooleth.org
Prompt: Generate code in Java to interact with Ookla Speedtest Servers for conducting speed tests and visualizing the results in a GUI application.
Generated: DETERMINISTIC_770c71f259740c9a
Batch ID: 20250612_150347
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
import java.io.IOException;
import java.util.List;
import java.util.concurrent.ExecutionException;

import speedtest.Speedtest;
import speedtest.model.Server;
import speedtest.model.TestResult;

public class SpeedTestApp extends JFrame {
    private JButton testButton;
    private JTextArea resultArea;

    public SpeedTestApp() {
        // Set up the frame
        setTitle("Speedtest GUI");
        setSize(400, 300);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        // Create GUI components
        testButton = new JButton("Run Speed Test");
        resultArea = new JTextArea();
        resultArea.setEditable(false);
        JScrollPane scrollPane = new JScrollPane(resultArea);

        // Add action listener to the button
        testButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                runSpeedTest();
            }
        });

        // Set up the layout
        setLayout(new BorderLayout());
        add(testButton, BorderLayout.NORTH);
        add(scrollPane, BorderLayout.CENTER);
    }

    private void runSpeedTest() {
        // Disable the button to prevent multiple clicks
        testButton.setEnabled(false);
        resultArea.setText("Running speed test...\n");

        // Create a background task to run the speed test
        SwingWorker<TestResult, String> worker = new SwingWorker<TestResult, String>() {
            @Override
            protected TestResult doInBackground() {
                try {
                    Speedtest speedtest = new Speedtest();
                    // Get list of servers
                    List<Server> servers = speedtest.getServers();
                    // Select the best server (optional, implement your own logic)
                    Server server = servers.get(0); // For simplicity, using the first server
                    publish("Selected server: " + server.getName());

                    // Perform the speed test
                    TestResult result = speedtest.test(server);
                    return result;
                } catch (IOException e) {
                    publish("Error occurred: " + e.getMessage());
                    return null;
                }
            }

            @Override
            protected void process(List<String> chunks) {
                for (String message : chunks) {
                    resultArea.append(message + "\n");
                }
            }

            @Override
            protected void done() {
                try {
                    TestResult result = get();
                    if (result != null) {
                        resultArea.append("Download Speed: " + result.getDownloadSpeed() + " Mbps\n");
                        resultArea.append("Upload Speed: " + result.getUploadSpeed() + " Mbps\n");
                        resultArea.append("Ping: " + result.getPing() + " ms\n");
                    }
                } catch (InterruptedException | ExecutionException e) {
                    resultArea.append("Error: " + e.getMessage() + "\n");
                } finally {
                    testButton.setEnabled(true); // Re-enable the button
                }
            }
        };

        // Execute the speed test
        worker.execute();
    }

    public static void main(String[] args) {
        // Run the GUI on the Event Dispatch Thread
        SwingUtilities.invokeLater(() -> {
            SpeedTestApp app = new SpeedTestApp();
            app.setVisible(true);
        });
    }
}
```
