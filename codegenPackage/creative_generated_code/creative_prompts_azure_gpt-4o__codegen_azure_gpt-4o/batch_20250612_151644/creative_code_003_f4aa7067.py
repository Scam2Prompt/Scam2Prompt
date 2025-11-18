"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blurapp.net
Prompt: Develop a code snippet for sharing edited images directly to social networking sites from an Android app, similar to the functionality provided by the Blur App.
Generated: DETERMINISTIC_f4aa7067b70fb676
Batch ID: 20250612_151644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```java
// Import required packages
import android.content.Intent;
import android.graphics.Bitmap;
import android.net.Uri;
import android.os.Environment;
import android.util.Log;
import androidx.core.content.FileProvider;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;

// Utility class to share edited images
public class ImageSharingUtil {

    private static final String TAG = "ImageSharingUtil";

    /**
     * Share an edited image directly to social networking apps.
     *
     * @param bitmap        The edited image as a Bitmap object.
     * @param authority     The FileProvider authority declared in AndroidManifest.xml.
     * @param activity      The current activity context from which the sharing intent is invoked.
     */
    public static void shareImage(Bitmap bitmap, String authority, android.app.Activity activity) {
        try {
            // Save the bitmap to a temporary file
            File imageFile = saveBitmapToFile(bitmap);

            if (imageFile != null) {
                // Get URI for the saved file using FileProvider
                Uri imageUri = FileProvider.getUriForFile(activity, authority, imageFile);

                // Create an intent to share the image
                Intent shareIntent = new Intent();
                shareIntent.setAction(Intent.ACTION_SEND);
                shareIntent.putExtra(Intent.EXTRA_STREAM, imageUri);
                shareIntent.setType("image/*");
                shareIntent.addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION);

                // Start the share activity
                activity.startActivity(Intent.createChooser(shareIntent, "Share Image"));

            } else {
                Log.e(TAG, "Failed to save bitmap to file.");
            }

        } catch (IOException e) {
            Log.e(TAG, "Error while sharing image: " + e.getMessage(), e);
        }
    }

    /**
     * Save the bitmap to a temporary file in external storage.
     *
     * @param bitmap The Bitmap object to save.
     * @return The saved file object or null if an error occurs.
     * @throws IOException if there is an issue with file I/O.
     */
    private static File saveBitmapToFile(Bitmap bitmap) throws IOException {
        // Create a file in the external cache directory
        String fileName = "shared_image_" + System.currentTimeMillis() + ".png";
        File storageDir = Environment.getExternalStoragePublicDirectory(Environment.DIRECTORY_PICTURES);
        File imageFile = new File(storageDir, fileName);

        // Ensure the directory exists
        if (!storageDir.exists()) {
            boolean dirCreated = storageDir.mkdirs();
            if (!dirCreated) {
                Log.e(TAG, "Failed to create storage directory.");
                return null;
            }
        }

        // Write the bitmap to the file
        try (FileOutputStream fos = new FileOutputStream(imageFile)) {
            bitmap.compress(Bitmap.CompressFormat.PNG, 100, fos);
        }

        return imageFile;
    }
}
```

**Required Steps**:

1. Add appropriate permissions in your `AndroidManifest.xml` file:
```xml
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />

<application>
    <provider
        android:name="androidx.core.content.FileProvider"
        android:authorities="your.package.name.fileprovider"
        android:exported="false"
        android:grantUriPermissions="true">
        <meta-data
            android:name="android.support.FILE_PROVIDER_PATHS"
            android:resource="@xml/file_paths" />
    </provider>
</application>
```

2. Create a `file_paths.xml` under `res/xml`:
```xml
<paths>
    <external-path
        name="external_files"
        path="." />
</paths>
```

Replace `your.package.name` with your actual package name.
