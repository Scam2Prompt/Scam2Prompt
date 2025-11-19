"""
Generated Code Metadata:
========================
Original URL: https://bryantroll.com
Prompt: "Create a simple command-line tool in Java to list directory contents, including for each item: name, last modified date, and size."
Generated: DETERMINISTIC_f66d0bdfcf98a1cc
Batch ID: 20250622_211528
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.io.File;
import java.text.SimpleDateFormat;

public class DirectoryLister {

    public static void main(String[] args) {
        // Check if the user provided a directory path
        if (args.length != 1) {
            System.err.println("Usage: java DirectoryLister <directory-path>");
            System.exit(1);
        }

        // Get the directory path from the command line arguments
        String directoryPath = args[0];
        File directory = new File(directoryPath);

        // Check if the provided path is a valid directory
        if (!directory.isDirectory()) {
            System.err.println("Error: The provided path is not a valid directory.");
            System.exit(1);
        }

        // List the contents of the directory
        listDirectoryContents(directory);
    }

    /**
     * Lists the contents of the specified directory.
     *
     * @param directory The directory to list contents from.
     */
    private static void listDirectoryContents(File directory) {
        // Get all files and directories in the specified directory
        File[] files = directory.listFiles();

        // Check if the directory is empty or an error occurred
        if (files == null) {
            System.err.println("Error: Unable to access the directory contents.");
            return;
        }

        // Print header
        System.out.printf("%-30s %-25s %-10s%n", "Name", "Last Modified", "Size (bytes)");
        System.out.println("---------------------------------------------------------------");

        // Iterate through each file/directory and print its details
        for (File file : files) {
            String name = file.getName();
            String lastModified = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss").format(file.lastModified());
            long size = file.length();

            // Print the file details
            System.out.printf("%-30s %-25s %-10d%n", name, lastModified, size);
        }
    }
}
```
