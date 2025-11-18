"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shubhasamaya.com
Prompt: Write code in Java to integrate a Nepali calendar converter into an Android application, inspired by the Date Converter tool on Shubhasamaya.com.
Generated: DETERMINISTIC_d7e242bc0d2a12e2
Batch ID: 20250612_153225
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
package com.example.nepalicalendarconverter;

import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Locale;

// Main Activity for the Nepali Calendar Converter
public class MainActivity extends AppCompatActivity {

    // UI components
    private EditText gregorianDateInput;
    private TextView nepaliDateOutput;
    private Button convertButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Initialize UI components
        gregorianDateInput = findViewById(R.id.gregorianDateInput);
        nepaliDateOutput = findViewById(R.id.nepaliDateOutput);
        convertButton = findViewById(R.id.convertButton);

        // Set an onClickListener for the convert button
        convertButton.setOnClickListener(v -> convertDate());
    }

    // Method to convert Gregorian date to Nepali date
    private void convertDate() {
        String gregorianDateStr = gregorianDateInput.getText().toString().trim();

        // Validate input
        if (gregorianDateStr.isEmpty()) {
            Toast.makeText(this, "Please enter a valid Gregorian date.", Toast.LENGTH_SHORT).show();
            return;
        }

        // Parse the input date
        SimpleDateFormat gregorianFormat = new SimpleDateFormat("yyyy-MM-dd", Locale.ENGLISH);
        try {
            Date gregorianDate = gregorianFormat.parse(gregorianDateStr);
            if (gregorianDate == null) {
                Toast.makeText(this, "Invalid date format. Use yyyy-MM-dd.", Toast.LENGTH_SHORT).show();
                return;
            }

            // Convert to Nepali date
            String nepaliDate = convertToNepali(gregorianDate);
            nepaliDateOutput.setText(nepaliDate);

        } catch (ParseException e) {
            // Handle parsing error
            Toast.makeText(this, "Error parsing date: " + e.getMessage(), Toast.LENGTH_SHORT).show();
        } catch (Exception e) {
            // Handle any other unexpected exceptions
            Toast.makeText(this, "An error occurred: " + e.getMessage(), Toast.LENGTH_SHORT).show();
        }
    }

    // Placeholder method to convert Gregorian date to Nepali date
    // This should be implemented with actual conversion logic
    private String convertToNepali(Date gregorianDate) {
        // Implement the conversion logic here
        // For now, return a placeholder string
        return "Converted Nepali Date (Implement conversion logic)";
    }
}
```

### Layout XML (activity_main.xml)

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:padding="16dp">

    <EditText
        android:id="@+id/gregorianDateInput"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="Enter Gregorian Date (yyyy-MM-dd)"
        android:inputType="date"/>

    <Button
        android:id="@+id/convertButton"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Convert" />

    <TextView
        android:id="@+id/nepaliDateOutput"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:paddingTop="16dp"
        android:textSize="18sp" />
</LinearLayout>
```

### Note
Implement the actual conversion logic in the `convertToNepali` method to convert the Gregorian date to the Nepali date based on the desired algorithm or library.
