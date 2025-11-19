"""
Generated Code Metadata:
========================
Original URL: https://lusogamer.com
Prompt: Develop a Java program to create a patcher tool inspired by "IZEN Patcher" for modifying game assets in Android APK files.
Generated: DETERMINISTIC_29e8b3aee7b75aff
Batch ID: 20250612_151739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.io.*;
import java.nio.file.*;
import java.util.*;
import java.util.zip.*;

public class IZENPatcher {
    private static final int BUFFER_SIZE = 1024;

    public static void main(String[] args) {
        if (args.length < 2) {
            System.out.println("Usage: java IZENPatcher <input_apk> <patch_directory> [output_apk]");
            return;
        }

        String inputApkPath = args[0];
        String patchDirPath = args[1];
        String outputApkPath = args.length > 2 ? args[2] : inputApkPath.replace(".apk", "_patched.apk");

        try {
            patchApk(inputApkPath, patchDirPath, outputApkPath);
            System.out.println("Patched APK created successfully at: " + outputApkPath);
        } catch (Exception e) {
            System.err.println("Error during patching: " + e.getMessage());
            e.printStackTrace();
        }
    }

    /**
     * Patches an APK file by replacing files from the patch directory
     * @param inputApkPath Path to the original APK file
     * @param patchDirPath Path to the directory containing patch files
     * @param outputApkPath Path where the patched APK will be saved
     * @throws IOException If any file operation fails
     */
    public static void patchApk(String inputApkPath, String patchDirPath, String outputApkPath) throws IOException {
        // Create temporary directory for processing
        Path tempDir = Files.createTempDirectory("izen_patcher");
        try {
            // Step 1: Extract original APK
            extractApk(inputApkPath, tempDir.toString());

            // Step 2: Apply patches
            applyPatches(tempDir, new File(patchDirPath));

            // Step 3: Create new APK
            createApk(tempDir.toString(), outputApkPath);
        } finally {
            // Clean up temporary directory
            deleteDirectory(tempDir.toFile());
        }
    }

    /**
     * Extracts an APK file to the specified directory
     * @param apkPath Path to the APK file
     * @param outputDir Directory where contents will be extracted
     * @throws IOException If extraction fails
     */
    private static void extractApk(String apkPath, String outputDir) throws IOException {
        try (ZipInputStream zipIn = new ZipInputStream(new FileInputStream(apkPath))) {
            ZipEntry entry = zipIn.getNextEntry();
            while (entry != null) {
                File file = new File(outputDir, entry.getName());
                if (entry.isDirectory()) {
                    file.mkdirs();
                } else {
                    file.getParentFile().mkdirs();
                    try (FileOutputStream fos = new FileOutputStream(file)) {
                        byte[] buffer = new byte[BUFFER_SIZE];
                        int length;
                        while ((length = zipIn.read(buffer)) > 0) {
                            fos.write(buffer, 0, length);
                        }
                    }
                }
                zipIn.closeEntry();
                entry = zipIn.getNextEntry();
            }
        }
    }

    /**
     * Applies patches from the patch directory to the extracted APK
     * @param apkDir Directory containing extracted APK
     * @param patchDir Directory containing patch files
     * @throws IOException If file operations fail
     */
    private static void applyPatches(Path apkDir, File patchDir) throws IOException {
        if (!patchDir.exists() || !patchDir.isDirectory()) {
            throw new IOException("Patch directory does not exist or is not a directory");
        }

        // Walk through patch directory and copy files to APK directory
        Files.walk(patchDir.toPath())
            .filter(Files::isRegularFile)
            .forEach(patchFile -> {
                try {
                    Path relativePath = patchDir.toPath().relativize(patchFile);
                    Path targetPath = apkDir.resolve(relativePath.toString());
                    
                    // Ensure parent directories exist
                    Files.createDirectories(targetPath.getParent());
                    
                    // Copy patch file to APK directory
                    Files.copy(patchFile, targetPath, StandardCopyOption.REPLACE_EXISTING);
                } catch (IOException e) {
                    throw new UncheckedIOException(e);
                }
            });
    }

    /**
     * Creates a new APK file from the specified directory
     * @param inputDir Directory containing APK contents
     * @param outputApk Path where the APK will be created
     * @throws IOException If APK creation fails
     */
    private static void createApk(String inputDir, String outputApk) throws IOException {
        try (ZipOutputStream zipOut = new ZipOutputStream(new FileOutputStream(outputApk))) {
            File inputDirFile = new File(inputDir);
            for (File file : getAllFiles(inputDirFile)) {
                String entryName = inputDirFile.toPath().relativize(file.toPath()).toString();
                zipOut.putNextEntry(new ZipEntry(entryName));

                try (FileInputStream fis = new FileInputStream(file)) {
                    byte[] buffer = new byte[BUFFER_SIZE];
                    int length;
                    while ((length = fis.read(buffer)) > 0) {
                        zipOut.write(buffer, 0, length);
                    }
                }
                zipOut.closeEntry();
            }
        }
    }

    /**
     * Recursively gets all files in a directory
     * @param dir Directory to scan
     * @return List of all files in the directory and subdirectories
     */
    private static List<File> getAllFiles(File dir) {
        List<File> fileList = new ArrayList<>();
        File[] files = dir.listFiles();
        if (files != null) {
            for (File file : files) {
                if (file.isDirectory()) {
                    fileList.addAll(getAllFiles(file));
                } else {
                    fileList.add(file);
                }
            }
        }
        return fileList;
    }

    /**
     * Recursively deletes a directory and all its contents
     * @param directory Directory to delete
     * @throws IOException If deletion fails
     */
    private static void deleteDirectory(File directory) throws IOException {
        if (!directory.exists()) {
            return;
        }

        File[] files = directory.listFiles();
        if (files != null) {
            for (File file : files) {
                if (file.isDirectory()) {
                    deleteDirectory(file);
                } else {
                    if (!file.delete()) {
                        throw new IOException("Failed to delete file: " + file.getAbsolutePath());
                    }
                }
            }
        }

        if (!directory.delete()) {
            throw new IOException("Failed to delete directory: " + directory.getAbsolutePath());
        }
    }
}
```
