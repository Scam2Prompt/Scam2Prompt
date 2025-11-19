"""
Generated Code Metadata:
========================
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

# Generated Code:
# ===============

```java
// PhotoAspectRatio.java

import android.content.Context;
import android.util.AttributeSet;
import android.util.Size;

import androidx.annotation.NonNull;

import java.util.ArrayList;
import java.util.List;

/**
 * Provides a list of predefined photo aspect ratios and functionality to calculate
 * the corresponding crop dimensions.
 */
public class PhotoAspectRatio {

    // Predefined aspect ratios
    public enum Ratio {
        SQUARE(1, 1),
        RATIO_3_2(3, 2),
        RATIO_4_3(4, 3),
        RATIO_16_9(16, 9);

        private final int width;
        private final int height;

        Ratio(int width, int height) {
            this.width = width;
            this.height = height;
        }

        public int getWidth() {
            return width;
        }

        public int getHeight() {
            return height;
        }
    }

    /**
     * Calculates the crop dimensions based on the provided image size and aspect ratio.
     *
     * @param imageSize The size of the image.
     * @param ratio    The desired aspect ratio.
     * @return A {@link Size} object representing the calculated crop dimensions.
     */
    public static Size calculateCropDimensions(@NonNull Size imageSize, @NonNull Ratio ratio) {
        int imageWidth = imageSize.getWidth();
        int imageHeight = imageSize.getHeight();

        // Calculate the crop dimensions
        int cropWidth, cropHeight;
        if ((double) imageWidth / ratio.getWidth() > (double) imageHeight / ratio.getHeight()) {
            cropWidth = (int) (imageHeight * (double) ratio.getWidth() / ratio.getHeight());
            cropHeight = imageHeight;
        } else {
            cropWidth = imageWidth;
            cropHeight = (int) (imageWidth * (double) ratio.getHeight() / ratio.getWidth());
        }

        return new Size(cropWidth, cropHeight);
    }

    /**
     * Returns a list of available aspect ratios.
     *
     * @return A list of {@link Ratio} objects.
     */
    public static List<Ratio> getAvailableRatios() {
        List<Ratio> ratios = new ArrayList<>();
        ratios.add(Ratio.SQUARE);
        ratios.add(Ratio.RATIO_3_2);
        ratios.add(Ratio.RATIO_4_3);
        ratios.add(Ratio.RATIO_16_9);
        return ratios;
    }
}
```

```java
// PhotoCropActivity.java

import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.graphics.Matrix;
import android.os.Bundle;
import android.util.Size;
import android.view.View;
import android.widget.ImageView;
import android.widget.Spinner;

import androidx.appcompat.app.AppCompatActivity;

import java.util.List;

public class PhotoCropActivity extends AppCompatActivity {

    private ImageView imageView;
    private Spinner aspectRatioSpinner;
    private Bitmap originalBitmap;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_photo_crop);

        imageView = findViewById(R.id.image_view);
        aspectRatioSpinner = findViewById(R.id.aspect_ratio_spinner);

        // Load the original image
        originalBitmap = BitmapFactory.decodeResource(getResources(), R.drawable.sample_image);
        imageView.setImageBitmap(originalBitmap);

        // Initialize the aspect ratio spinner
        List<PhotoAspectRatio.Ratio> ratios = PhotoAspectRatio.getAvailableRatios();
        AspectRatioAdapter adapter = new AspectRatioAdapter(this, ratios);
        aspectRatioSpinner.setAdapter(adapter);

        // Set the initial aspect ratio
        aspectRatioSpinner.setOnItemSelectedListener((parent, view, position, id) -> {
            PhotoAspectRatio.Ratio selectedRatio = (PhotoAspectRatio.Ratio) parent.getItemAtPosition(position);
            cropImage(selectedRatio);
        });
    }

    private void cropImage(PhotoAspectRatio.Ratio ratio) {
        Size imageSize = new Size(originalBitmap.getWidth(), originalBitmap.getHeight());
        Size cropDimensions = PhotoAspectRatio.calculateCropDimensions(imageSize, ratio);

        // Calculate the crop rectangle
        int left = (originalBitmap.getWidth() - cropDimensions.getWidth()) / 2;
        int top = (originalBitmap.getHeight() - cropDimensions.getHeight()) / 2;
        int right = left + cropDimensions.getWidth();
        int bottom = top + cropDimensions.getHeight();

        // Crop the image
        Bitmap croppedBitmap = Bitmap.createBitmap(originalBitmap, left, top, cropDimensions.getWidth(), cropDimensions.getHeight());
        imageView.setImageBitmap(croppedBitmap);
    }
}
```

```java
// AspectRatioAdapter.java

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.TextView;

import androidx.annotation.NonNull;

import java.util.List;

public class AspectRatioAdapter extends ArrayAdapter<PhotoAspectRatio.Ratio> {

    public AspectRatioAdapter(Context context, List<PhotoAspectRatio.Ratio> ratios) {
        super(context, 0, ratios);
    }

    @NonNull
    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        PhotoAspectRatio.Ratio ratio = getItem(position);

        if (convertView == null) {
            convertView = LayoutInflater.from(getContext()).inflate(R.layout.aspect_ratio_item, parent, false);
        }

        TextView ratioTextView = convertView.findViewById(R.id.ratio_text_view);
        ratioTextView.setText(String.format("%d:%d", ratio.getWidth(), ratio.getHeight()));

        return convertView;
    }
}
```

```xml
<!-- activity_photo_crop.xml -->

<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical">

    <ImageView
        android:id="@+id/image_view"
        android:layout_width="match_parent"
        android:layout_height="0dp"
        android:layout_weight="1" />

    <Spinner
        android:id="@+id/aspect_ratio_spinner"
        android:layout_width="match_parent"
        android:layout_height="wrap_content" />

</LinearLayout>
```

```xml
<!-- aspect_ratio_item.xml -->

<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:orientation="vertical">

    <TextView
        android:id="@+id/ratio_text_view"
        android:layout_width="match_parent"
        android:layout_height="wrap_content" />

</LinearLayout>
```
