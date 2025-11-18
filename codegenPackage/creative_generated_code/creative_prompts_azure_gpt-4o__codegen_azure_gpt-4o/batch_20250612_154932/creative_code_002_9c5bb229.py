"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://whatthefluff.lol
Prompt: Create a script to track screen time usage across multiple apps on a smartphone using Android or iOS APIs. Include recommendations for libraries to visualize the data.
Generated: DETERMINISTIC_9c5bb229092f3cbd
Batch ID: 20250612_154932
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/PhilJay/MPAndroidChart": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/danielgindi/Charts": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Here is the production-ready code for Android that uses the `UsageStatsManager` API to track screen time across multiple apps and stores the data for visualization. 

```java
package com.example.screentimetracker;

import android.app.usage.UsageStats;
import android.app.usage.UsageStatsManager;
import android.content.Context;
import android.os.Build;
import android.util.Log;

import androidx.annotation.RequiresApi;

import java.util.Calendar;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;

/**
 * ScreenTimeTracker - A utility class to track screen time usage across multiple apps.
 */
public class ScreenTimeTracker {

    private static final String TAG = "ScreenTimeTracker";

    /**
     * Retrieves app usage statistics for the current day.
     *
     * @param context The application context.
     * @return A map containing package names and their respective usage times in milliseconds.
     */
    @RequiresApi(api = Build.VERSION_CODES.LOLLIPOP)
    public static Map<String, Long> getDailyUsageStats(Context context) {
        UsageStatsManager usageStatsManager = 
            (UsageStatsManager) context.getSystemService(Context.USAGE_STATS_SERVICE);

        if (usageStatsManager == null) {
            Log.e(TAG, "UsageStatsManager is unavailable.");
            return null;
        }

        // Define the time range to fetch usage stats (midnight to current time today)
        Calendar calendar = Calendar.getInstance();
        long endTime = calendar.getTimeInMillis();
        calendar.set(Calendar.HOUR_OF_DAY, 0);
        calendar.set(Calendar.MINUTE, 0);
        calendar.set(Calendar.SECOND, 0);
        long startTime = calendar.getTimeInMillis();

        // Fetch usage stats for the specified time range
        List<UsageStats> usageStatsList = usageStatsManager.queryUsageStats(
                UsageStatsManager.INTERVAL_DAILY, startTime, endTime);

        if (usageStatsList == null || usageStatsList.isEmpty()) {
            Log.e(TAG, "No usage statistics available. Ensure permission is granted.");
            return null;
        }

        // Aggregate usage times by app package name
        Map<String, Long> usageStatsMap = new TreeMap<>();
        for (UsageStats usageStats : usageStatsList) {
            long totalTimeInForeground = usageStats.getTotalTimeInForeground();
            if (totalTimeInForeground > 0) {
                usageStatsMap.put(usageStats.getPackageName(), totalTimeInForeground);
            }
        }

        return usageStatsMap;
    }
}
```

---

Below is an example of how you might visualize this data using a popular library like MPAndroidChart:

```java
package com.example.screentimetracker;

import android.content.Context;
import android.graphics.Color;
import android.os.Build;
import android.os.Bundle;

import androidx.annotation.RequiresApi;
import androidx.appcompat.app.AppCompatActivity;

import com.github.mikephil.charting.charts.PieChart;
import com.github.mikephil.charting.components.Legend;
import com.github.mikephil.charting.data.PieData;
import com.github.mikephil.charting.data.PieDataSet;
import com.github.mikephil.charting.data.PieEntry;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

/**
 * MainActivity - Displays the screen time usage in a pie chart.
 */
public class MainActivity extends AppCompatActivity {

    private PieChart pieChart;

    @RequiresApi(api = Build.VERSION_CODES.LOLLIPOP)
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        pieChart = findViewById(R.id.pieChart);

        // Fetch usage stats and visualize them
        Map<String, Long> usageStatsMap = ScreenTimeTracker.getDailyUsageStats(this);
        if (usageStatsMap != null) {
            setupPieChart(usageStatsMap);
        }
    }

    /**
     * Configures and populates the pie chart with usage stats data.
     *
     * @param usageStatsMap A map of app package names and their usage times.
     */
    private void setupPieChart(Map<String, Long> usageStatsMap) {
        List<PieEntry> entries = new ArrayList<>();
        for (Map.Entry<String, Long> entry : usageStatsMap.entrySet()) {
            String appName = entry.getKey();
            float screenTimeMinutes = entry.getValue() / 60000f; // Convert milliseconds to minutes
            entries.add(new PieEntry(screenTimeMinutes, appName));
        }

        PieDataSet dataSet = new PieDataSet(entries, "Screen Time Usage");
        dataSet.setColors(ColorTemplate.MATERIAL_COLORS);
        dataSet.setSliceSpace(2f);
        dataSet.setValueTextSize(12f);
        dataSet.setValueTextColor(Color.BLACK);

        PieData pieData = new PieData(dataSet);

        pieChart.setData(pieData);
        pieChart.setCenterText("Screen Time");
        pieChart.setCenterTextSize(16f);
        pieChart.setEntryLabelTextSize(12f);
        pieChart.setEntryLabelColor(Color.BLACK);
        pieChart.setUsePercentValues(true);

        Legend legend = pieChart.getLegend();
        legend.setVerticalAlignment(Legend.LegendVerticalAlignment.BOTTOM);
        legend.setHorizontalAlignment(Legend.LegendHorizontalAlignment.CENTER);
        legend.setOrientation(Legend.LegendOrientation.HORIZONTAL);
        legend.setTextSize(12f);
        legend.setTextColor(Color.BLACK);

        pieChart.invalidate(); // Refresh chart
    }
}
```

---

### Recommendations for Libraries to Visualize Data:
1. **MPAndroidChart** (for Android): A powerful library for creating charts such as bar charts, pie charts, line charts, etc.
   - [GitHub Repository](https://github.com/PhilJay/MPAndroidChart)

2. **Charts** (for iOS): A highly customizable chart library for iOS built using Swift.
   - [GitHub Repository](https://github.com/danielgindi/Charts)

Make sure the proper permissions (`PACKAGE_USAGE_STATS`) are granted in Android settings for the app to access usage stats.
