"""
Generated Code Metadata:
========================
Original URL: https://azagros.com
Prompt: Create a mobile app that functions offline for registering visits, taking photos, and mapping areas, with integration to a web-based platform, as seen on Azagros.
Generated: DETERMINISTIC_d6bb7b7d6a2ed05c
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Mobile App Backend (Flask API for Web Integration)
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os
import uuid
from datetime import datetime
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///visits.db'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}
db = SQLAlchemy(app)

class Visit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    visitor_id = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    coordinates = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    notes = db.Column(db.Text)
    photos = db.relationship('Photo', backref='visit', lazy=True)
    synced = db.Column(db.Boolean, default=False)

class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100), nullable=False)
    visit_id = db.Column(db.Integer, db.ForeignKey('visit.id'), nullable=False)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/api/visits', methods=['POST'])
def create_visit():
    try:
        data = request.json
        visit = Visit(
            visitor_id=data['visitor_id'],
            location=data['location'],
            coordinates=data['coordinates'],
            notes=data.get('notes', ''),
            synced=True
        )
        db.session.add(visit)
        db.session.commit()
        return jsonify({'id': visit.id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/visits/<int:visit_id>/photos', methods=['POST'])
def upload_photo(visit_id):
    try:
        if 'photo' not in request.files:
            return jsonify({'error': 'No file part'}), 400
        
        file = request.files['photo']
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400
        
        if file and allowed_file(file.filename):
            filename = secure_filename(f"{uuid.uuid4()}.{file.filename.rsplit('.', 1)[1].lower()}")
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            photo = Photo(filename=filename, visit_id=visit_id)
            db.session.add(photo)
            db.session.commit()
            
            return jsonify({'filename': filename}), 201
        else:
            return jsonify({'error': 'File type not allowed'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/sync', methods=['POST'])
def sync_data():
    try:
        data = request.json
        visits = data.get('visits', [])
        
        for visit_data in visits:
            visit = Visit(
                visitor_id=visit_data['visitor_id'],
                location=visit_data['location'],
                coordinates=visit_data['coordinates'],
                notes=visit_data.get('notes', ''),
                timestamp=datetime.strptime(visit_data['timestamp'], '%Y-%m-%d %H:%M:%S'),
                synced=True
            )
            db.session.add(visit)
            db.session.commit()
            
            for photo_data in visit_data.get('photos', []):
                photo = Photo(
                    filename=photo_data['filename'],
                    visit_id=visit.id
                )
                db.session.add(photo)
        
        db.session.commit()
        return jsonify({'message': 'Sync successful'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    db.create_all()
    app.run(debug=True)
```

```kotlin
// Mobile App (Android - Kotlin)
package com.example.fieldvisits

import android.Manifest
import android.content.Context
import android.content.pm.PackageManager
import android.graphics.Bitmap
import android.location.Location
import android.location.LocationListener
import android.location.LocationManager
import android.os.Bundle
import android.os.Environment
import android.provider.MediaStore
import android.util.Log
import androidx.appcompat.app.AppCompatActivity
import androidx.core.app.ActivityCompat
import androidx.core.content.ContextCompat
import com.google.android.gms.maps.CameraUpdateFactory
import com.google.android.gms.maps.GoogleMap
import com.google.android.gms.maps.OnMapReadyCallback
import com.google.android.gms.maps.SupportMapFragment
import com.google.android.gms.maps.model.LatLng
import com.google.android.gms.maps.model.MarkerOptions
import kotlinx.android.synthetic.main.activity_main.*
import okhttp3.*
import okhttp3.MediaType.Companion.toMediaTypeOrNull
import okhttp3.RequestBody.Companion.toRequestBody
import org.json.JSONObject
import java.io.File
import java.io.FileOutputStream
import java.io.IOException
import java.text.SimpleDateFormat
import java.util.*

class MainActivity : AppCompatActivity(), OnMapReadyCallback, LocationListener {
    private lateinit var mMap: GoogleMap
    private lateinit var locationManager: LocationManager
    private var currentLocation: Location? = null
    private val REQUEST_PERMISSIONS = 1
    private val client = OkHttpClient()
    private val dbHelper = VisitDatabaseHelper(this)
    private var unsyncedVisits = mutableListOf<Visit>()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val mapFragment = supportFragmentManager
            .findFragmentById(R.id.map) as SupportMapFragment
        mapFragment.getMapAsync(this)

        checkPermissions()
        setupLocationManager()

        btnSaveVisit.setOnClickListener { saveVisit() }
        btnTakePhoto.setOnClickListener { takePhoto() }
        btnSync.setOnClickListener { syncData() }

        loadUnsyncedVisits()
    }

    private fun checkPermissions() {
        val permissions = arrayOf(
            Manifest.permission.ACCESS_FINE_LOCATION,
            Manifest.permission.ACCESS_COARSE_LOCATION,
            Manifest.permission.CAMERA,
            Manifest.permission.WRITE_EXTERNAL_STORAGE
        )

        val permissionsToRequest = permissions.filter {
            ContextCompat.checkSelfPermission(this, it) != PackageManager.PERMISSION_GRANTED
        }

        if (permissionsToRequest.isNotEmpty()) {
            ActivityCompat.requestPermissions(this, permissionsToRequest.toTypedArray(), REQUEST_PERMISSIONS)
        }
    }

    private fun setupLocationManager() {
        locationManager = getSystemService(Context.LOCATION_SERVICE) as LocationManager
        if (ActivityCompat.checkSelfPermission(
                this,
                Manifest.permission.ACCESS_FINE_LOCATION
            ) == PackageManager.PERMISSION_GRANTED
        ) {
            locationManager.requestLocationUpdates(
                LocationManager.GPS_PROVIDER,
                5000,
                5f,
                this
            )
        }
    }

    override fun onMapReady(googleMap: GoogleMap) {
        mMap = googleMap
        currentLocation?.let {
            val currentLatLng = LatLng(it.latitude, it.longitude)
            mMap.addMarker(MarkerOptions().position(currentLatLng).title("Current Location"))
            mMap.moveCamera(CameraUpdateFactory.newLatLngZoom(currentLatLng, 15f))
        }
    }

    override fun onLocationChanged(location: Location) {
        currentLocation = location
        val currentLatLng = LatLng(location.latitude, location.longitude)
        mMap.clear()
        mMap.addMarker(MarkerOptions().position(currentLatLng).title("Current Location"))
        mMap.moveCamera(CameraUpdateFactory.newLatLngZoom(currentLatLng, 15f))
    }

    private fun saveVisit() {
        currentLocation?.let { location ->
            val visit = Visit(
                visitorId = "user123", // Replace with actual user ID
                location = etLocation.text.toString(),
                coordinates = "${location.latitude},${location.longitude}",
                notes = etNotes.text.toString(),
                timestamp = SimpleDateFormat("yyyy-MM-dd HH:mm:ss", Locale.getDefault()).format(Date()),
                synced = false
            )

            dbHelper.addVisit(visit)
            unsyncedVisits.add(visit)
            etLocation.text.clear()
            etNotes.text.clear()
        }
    }

    private fun takePhoto() {
        if (currentLocation == null) return

        val lastVisit = dbHelper.getLastVisit()
        if (lastVisit == null || lastVisit.synced) return

        val intent = Intent(MediaStore.ACTION_IMAGE_CAPTURE
