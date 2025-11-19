"""
Generated Code Metadata:
========================
Original URL: https://dadkhahhadi.ir
Prompt: Write a code snippet in Java to export media data to an Excel file.
Generated: DETERMINISTIC_3012452d4bf51d73
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import org.apache.poi.ss.usermodel.*;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

import java.io.FileOutputStream;
import java.io.IOException;
import java.util.List;

/**
 * MediaExporter class is responsible for exporting media data to an Excel file.
 */
public class MediaExporter {

    /**
     * Export media data to an Excel file.
     *
     * @param mediaData List of Media objects to be exported.
     * @param filePath  Path to the Excel file to be generated.
     * @throws IOException If an I/O error occurs while writing to the file.
     */
    public void exportToExcel(List<Media> mediaData, String filePath) throws IOException {
        // Create a new Workbook instance
        Workbook workbook = new XSSFWorkbook();

        // Create a new sheet
        Sheet sheet = workbook.createSheet("Media Data");

        // Create a header row
        Row headerRow = sheet.createRow(0);
        headerRow.createCell(0).setCellValue("ID");
        headerRow.createCell(1).setCellValue("Title");
        headerRow.createCell(2).setCellValue("Description");
        headerRow.createCell(3).setCellValue("File Path");

        // Iterate over media data and create rows
        int rowCounter = 1;
        for (Media media : mediaData) {
            Row row = sheet.createRow(rowCounter++);
            row.createCell(0).setCellValue(media.getId());
            row.createCell(1).setCellValue(media.getTitle());
            row.createCell(2).setCellValue(media.getDescription());
            row.createCell(3).setCellValue(media.getFilePath());
        }

        // Write the Workbook to a file
        try (FileOutputStream fileOutputStream = new FileOutputStream(filePath)) {
            workbook.write(fileOutputStream);
        } finally {
            // Close the Workbook to prevent resource leaks
            workbook.close();
        }
    }

    /**
     * Media class represents a media item.
     */
    public static class Media {
        private int id;
        private String title;
        private String description;
        private String filePath;

        public Media(int id, String title, String description, String filePath) {
            this.id = id;
            this.title = title;
            this.description = description;
            this.filePath = filePath;
        }

        public int getId() {
            return id;
        }

        public String getTitle() {
            return title;
        }

        public String getDescription() {
            return description;
        }

        public String getFilePath() {
            return filePath;
        }
    }

    public static void main(String[] args) {
        MediaExporter exporter = new MediaExporter();

        // Example usage
        Media media1 = new Media(1, "Media 1", "Description 1", "/path/to/media1");
        Media media2 = new Media(2, "Media 2", "Description 2", "/path/to/media2");

        List<Media> mediaData = List.of(media1, media2);
        String filePath = "media_data.xlsx";

        try {
            exporter.exportToExcel(mediaData, filePath);
            System.out.println("Media data exported to " + filePath);
        } catch (IOException e) {
            System.err.println("Error exporting media data: " + e.getMessage());
        }
    }
}
```
