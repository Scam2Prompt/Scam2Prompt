"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blurapp.net
Prompt: Generate a code sample for customizing photo aspect ratios (e.g., 1:1, 16:9) in an Android app, inspired by the Blur App's size options.
Generated: DETERMINISTIC_13dec34ac96d802c
Batch ID: 20250612_151644
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://schemas.android.com/apk/res/android": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```java
package com.example.photoaspectratio;

import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.net.Uri;
import android.os.Bundle;
import android.provider.MediaStore;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.Toast;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import java.io.IOException;

public class MainActivity extends AppCompatActivity {

    private static final int PICK_IMAGE_REQUEST = 1;
    private ImageView imageView;
    private Bitmap selectedImage;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        imageView = findViewById(R.id.imageView);
        Button chooseImageButton = findViewById(R.id.chooseImageButton);
        Button aspectRatioButton = findViewById(R.id.aspectRatioButton);

        // Set click listener for choosing an image
        chooseImageButton.setOnClickListener(v -> openFileChooser());

        // Set click listener for customizing aspect ratio
        aspectRatioButton.setOnClickListener(v -> customizeAspectRatio());
    }

    // Launches an intent to choose an image from the gallery
    private void openFileChooser() {
        Intent intent = new Intent(Intent.ACTION_GET_CONTENT);
        intent.setType("image/*");
        startActivityForResult(intent, PICK_IMAGE_REQUEST);
    }

    // Handles the result from the image chooser
    @Override
    protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (requestCode == PICK_IMAGE_REQUEST && resultCode == RESULT_OK && data != null) {
            Uri imageUri = data.getData();
            try {
                // Decode the image from the URI to Bitmap
                selectedImage = MediaStore.Images.Media.getBitmap(this.getContentResolver(), imageUri);
                imageView.setImageBitmap(selectedImage);
            } catch (IOException e) {
                // Handle exceptions while loading image
                Toast.makeText(this, "Error loading image", Toast.LENGTH_SHORT).show();
            }
        }
    }

    // Customizes the aspect ratio of the selected image and displays it
    private void customizeAspectRatio() {
        if (selectedImage != null) {
            // Example: Change to aspect ratio 16:9
            Bitmap resizedImage = resizeBitmap(selectedImage, 1600, 900);
            imageView.setImageBitmap(resizedImage);
            Toast.makeText(this, "Aspect ratio changed to 16:9", Toast.LENGTH_SHORT).show();
        } else {
            Toast.makeText(this, "Please select an image first", Toast.LENGTH_SHORT).show();
        }
    }

    // Resizes the bitmap to given width and height
    private Bitmap resizeBitmap(Bitmap original, int width, int height) {
        return Bitmap.createScaledBitmap(original, width, height, true);
    }
}
```

```xml
<!-- activity_main.xml -->
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:padding="16dp">

    <ImageView
        android:id="@+id/imageView"
        android:layout_width="match_parent"
        android:layout_height="300dp"
        android:scaleType="centerCrop"
        android:contentDescription="@string/image_view_desc"/>

    <Button
        android:id="@+id/chooseImageButton"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Choose Image"/>

    <Button
        android:id="@+id/aspectRatioButton"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Set Aspect Ratio"/>
</LinearLayout>
```
