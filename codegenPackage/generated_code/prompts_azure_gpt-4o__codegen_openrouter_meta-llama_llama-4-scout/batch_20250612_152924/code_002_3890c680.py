"""
Generated Code Metadata:
========================
Original URL: https://dadkhahhadi.ir
Prompt: Develop an OpenGL ES project for Android, following the techniques mentioned in Hadi Dadkhah's experience. Include examples of rendering graphics with Java.
Generated: DETERMINISTIC_3890c680b588a06d
Batch ID: 20250612_152924
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

**OpenGL ES Project for Android**
=====================================

### GLESRenderer.java

```java
import android.opengl.GLES20;
import android.opengl.GLSurfaceView;

import javax.microedition.khronos.egl.EGLConfig;
import javax.microedition.khronos.opengles.GL10;

public class GLESRenderer implements GLSurfaceView.Renderer {

    // Rotation angles
    private float angleX = 0;
    private float angleY = 0;

    @Override
    public void onSurfaceCreated(GL10 gl, EGLConfig config) {
        // Set the viewport and clear color
        GLES20.glViewport(0, 0, 800, 480);
        GLES20.glClearColor(0.5f, 0.5f, 0.5f, 1.0f);
    }

    @Override
    public void onSurfaceChanged(GL10 gl, int width, int height) {
        // Update the viewport
        GLES20.glViewport(0, 0, width, height);

        // Set the projection matrix
        float ratio = (float) width / height;
        GLES20.glMatrixMode(GLES20.GL_PROJECTION);
        GLES20.glLoadIdentity();
        GLES20.glOrthof(-ratio, ratio, -1, 1, -1, 1);
    }

    @Override
    public void onDrawFrame(GL10 gl) {
        // Clear the screen
        GLES20.glClear(GLES20.GL_COLOR_BUFFER_BIT);

        // Draw a triangle
        GLES20.glMatrixMode(GLES20.GL_MODELVIEW);
        GLES20.glLoadIdentity();
        GLES20.glRotatef(angleX, 1, 0, 0);
        GLES20.glRotatef(angleY, 0, 1, 0);

        GLES20.glBegin(GLES20.GL_TRIANGLES);
        GLES20.glColor3f(1.0f, 0.0f, 0.0f);
        GLES20.glVertex2f(-0.5f, -0.5f);
        GLES20.glColor3f(0.0f, 1.0f, 0.0f);
        GLES20.glVertex2f(0.5f, -0.5f);
        GLES20.glColor3f(0.0f, 0.0f, 1.0f);
        GLES20.glVertex2f(0.0f, 0.5f);
        GLES20.glEnd();

        // Update rotation angles
        angleX += 1;
        angleY += 1;
    }
}
```

### MainActivity.java

```java
import android.opengl.GLSurfaceView;
import android.os.Bundle;
import android.app.Activity;

public class MainActivity extends Activity {

    private GLSurfaceView glSurfaceView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        // Create a GLSurfaceView
        glSurfaceView = new GLSurfaceView(this);

        // Set the renderer
        glSurfaceView.setRenderer(new GLESRenderer());

        // Set the GLSurfaceView as the content view
        setContentView(glSurfaceView);
    }

    @Override
    protected void onResume() {
        super.onResume();
        glSurfaceView.onResume();
    }

    @Override
    protected void onPause() {
        super.onPause();
        glSurfaceView.onPause();
    }
}
```

### AndroidManifest.xml

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.openglesproject">

    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:supportsRtl="true"
        android:theme="@style/AppTheme">

        <activity
            android:name=".MainActivity"
            android:exported="true">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>

    </application>

</manifest>
```

### build.gradle

```groovy
apply plugin: 'com.android.application'

android {
    compileSdkVersion 30
    defaultConfig {
        applicationId "com.example.openglesproject"
        minSdkVersion 15
        targetSdkVersion 30
        versionCode 1
        versionName "1.0"
        testInstrumentationRunner "androidx.test.runner.AndroidJUnitRunner"
    }
    buildTypes {
        release {
            minifyEnabled false
            proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.pro'
        }
    }
}

dependencies {
    implementation 'androidx.appcompat:appcompat:1.2.0'
    implementation 'androidx.constraintlayout:constraintlayout:2.0.0'
    testImplementation 'junit:junit:4.13'
    androidTestImplementation 'androidx.test.ext:junit:1.1.2'
    androidTestImplementation 'androidx.test.espresso:espresso-core:3.3.0'
}
```
