"""
Generated Code Metadata:
========================
Original URL: https://myantispyware.com
Prompt: Write code to detect and remove adware from an Android phone.
Generated: DETERMINISTIC_6497c32db74646f1
Batch ID: 20250622_211951
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import android.content.Context;
import android.content.pm.ApplicationInfo;
import android.content.pm.PackageInfo;
import android.content.pm.PackageManager;
import android.os.AsyncTask;
import android.util.Log;
import java.util.ArrayList;
import java.util.List;

public class AdwareDetector {

    private static final String TAG = "AdwareDetector";
    private Context context;
    private AdwareDetectionListener listener;

    public interface AdwareDetectionListener {
        void onAdwareDetected(List<PackageInfo> adwareApps);
        void onAdwareRemovalComplete(boolean success);
        void onError(String errorMessage);
    }

    public AdwareDetector(Context context, AdwareDetectionListener listener) {
        this.context = context;
        this.listener = listener;
    }

    public void scanForAdware() {
        new DetectAdwareTask().execute();
    }

    public void removeAdware(List<PackageInfo> adwareApps) {
        new RemoveAdwareTask().execute(adwareApps);
    }

    private class DetectAdwareTask extends AsyncTask<Void, Void, List<PackageInfo>> {
        @Override
        protected List<PackageInfo> doInBackground(Void... voids) {
            List<PackageInfo> adwareApps = new ArrayList<>();
            PackageManager pm = context.getPackageManager();
            List<PackageInfo> installedPackages = pm.getInstalledPackages(PackageManager.GET_META_DATA);

            for (PackageInfo packageInfo : installedPackages) {
                try {
                    ApplicationInfo appInfo = pm.getApplicationInfo(packageInfo.packageName, 0);
                    
                    // Check for common adware indicators
                    if ((appInfo.flags & ApplicationInfo.FLAG_SYSTEM) == 0 &&  // Not system app
                        packageInfo.packageName.toLowerCase().contains("ad") || // Package name contains 'ad'
                        (appInfo.metaData != null && appInfo.metaData.getString("com.google.android.gms.ads.APPLICATION_ID") != null) || // Contains AdMob ID
                        packageInfo.requestedPermissions != null && containsAdPermissions(packageInfo.requestedPermissions)) { // Has ad-related permissions
                        
                        adwareApps.add(packageInfo);
                    }
                } catch (PackageManager.NameNotFoundException e) {
                    Log.e(TAG, "Package not found: " + packageInfo.packageName, e);
                }
            }
            return adwareApps;
        }

        @Override
        protected void onPostExecute(List<PackageInfo> adwareApps) {
            if (adwareApps != null && !adwareApps.isEmpty()) {
                listener.onAdwareDetected(adwareApps);
            } else {
                listener.onError("No adware detected");
            }
        }
    }

    private boolean containsAdPermissions(String[] permissions) {
        String[] adPermissions = {
            "com.google.android.gms.permission.AD_ID",
            "android.permission.ACCESS_COARSE_LOCATION",
            "android.permission.ACCESS_FINE_LOCATION"
        };

        for (String perm : permissions) {
            for (String adPerm : adPermissions) {
                if (perm.equals(adPerm)) {
                    return true;
                }
            }
        }
        return false;
    }

    private class RemoveAdwareTask extends AsyncTask<List<PackageInfo>, Void, Boolean> {
        @Override
        protected Boolean doInBackground(List<PackageInfo>... lists) {
            List<PackageInfo> adwareApps = lists[0];
            PackageManager pm = context.getPackageManager();

            for (PackageInfo packageInfo : adwareApps) {
                try {
                    pm.getPackageInfo(packageInfo.packageName, 0);
                    pm.deletePackage(packageInfo.packageName, null, PackageManager.DELETE_SYSTEM_APP);
                } catch (PackageManager.NameNotFoundException e) {
                    Log.e(TAG, "Failed to remove package: " + packageInfo.packageName, e);
                    return false;
                } catch (SecurityException e) {
                    Log.e(TAG, "Permission denied to remove package: " + packageInfo.packageName, e);
                    return false;
                }
            }
            return true;
        }

        @Override
        protected void onPostExecute(Boolean success) {
            listener.onAdwareRemovalComplete(success);
        }
    }
}
```
