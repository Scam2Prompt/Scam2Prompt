"""
Generated Code Metadata:
========================
Original URL: https://dadkhahhadi.ir
Prompt: Design a database schema and API for a patient assistant media application using PHP and MySQL.
Generated: DETERMINISTIC_96dd0f1903044896
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Database Schema**
```sql
CREATE DATABASE patient_assistant;

USE patient_assistant;

CREATE TABLE users (
  id INT AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  password VARCHAR(255) NOT NULL,
  role ENUM('patient', 'admin') NOT NULL DEFAULT 'patient',
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

CREATE TABLE media (
  id INT AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  type ENUM('video', 'image', 'audio') NOT NULL,
  file_path VARCHAR(255) NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

CREATE TABLE patient_media (
  id INT AUTO_INCREMENT,
  patient_id INT NOT NULL,
  media_id INT NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (patient_id) REFERENCES users(id),
  FOREIGN KEY (media_id) REFERENCES media(id)
);

CREATE TABLE appointments (
  id INT AUTO_INCREMENT,
  patient_id INT NOT NULL,
  doctor_name VARCHAR(255) NOT NULL,
  appointment_date DATE NOT NULL,
  appointment_time TIME NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (patient_id) REFERENCES users(id)
);
```

**API**
```php
<?php

// config.php
class Config {
  const DB_HOST = 'localhost';
  const DB_USER = 'root';
  const DB_PASSWORD = '';
  const DB_NAME = 'patient_assistant';
}

// database.php
class Database {
  private $conn;

  public function __construct() {
    try {
      $this->conn = new PDO(
        'mysql:host=' . Config::DB_HOST . ';dbname=' . Config::DB_NAME,
        Config::DB_USER,
        Config::DB_PASSWORD
      );
      $this->conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    } catch (PDOException $e) {
      echo 'Connection failed: ' . $e->getMessage();
      exit();
    }
  }

  public function getConnection() {
    return $this->conn;
  }
}

// user.php
class User {
  private $db;

  public function __construct($db) {
    $this->db = $db;
  }

  public function createUser($username, $email, $password, $role) {
    $query = $this->db->prepare('INSERT INTO users (username, email, password, role) VALUES (:username, :email, :password, :role)');
    $query->bindParam(':username', $username);
    $query->bindParam(':email', $email);
    $query->bindParam(':password', password_hash($password, PASSWORD_DEFAULT));
    $query->bindParam(':role', $role);
    try {
      $query->execute();
      return true;
    } catch (PDOException $e) {
      echo 'Error creating user: ' . $e->getMessage();
      return false;
    }
  }

  public function getUser($id) {
    $query = $this->db->prepare('SELECT * FROM users WHERE id = :id');
    $query->bindParam(':id', $id);
    try {
      $query->execute();
      return $query->fetch();
    } catch (PDOException $e) {
      echo 'Error getting user: ' . $e->getMessage();
      return null;
    }
  }
}

// media.php
class Media {
  private $db;

  public function __construct($db) {
    $this->db = $db;
  }

  public function createMedia($title, $description, $type, $file_path) {
    $query = $this->db->prepare('INSERT INTO media (title, description, type, file_path) VALUES (:title, :description, :type, :file_path)');
    $query->bindParam(':title', $title);
    $query->bindParam(':description', $description);
    $query->bindParam(':type', $type);
    $query->bindParam(':file_path', $file_path);
    try {
      $query->execute();
      return true;
    } catch (PDOException $e) {
      echo 'Error creating media: ' . $e->getMessage();
      return false;
    }
  }

  public function getMedia($id) {
    $query = $this->db->prepare('SELECT * FROM media WHERE id = :id');
    $query->bindParam(':id', $id);
    try {
      $query->execute();
      return $query->fetch();
    } catch (PDOException $e) {
      echo 'Error getting media: ' . $e->getMessage();
      return null;
    }
  }
}

// patient_media.php
class PatientMedia {
  private $db;

  public function __construct($db) {
    $this->db = $db;
  }

  public function createPatientMedia($patient_id, $media_id) {
    $query = $this->db->prepare('INSERT INTO patient_media (patient_id, media_id) VALUES (:patient_id, :media_id)');
    $query->bindParam(':patient_id', $patient_id);
    $query->bindParam(':media_id', $media_id);
    try {
      $query->execute();
      return true;
    } catch (PDOException $e) {
      echo 'Error creating patient media: ' . $e->getMessage();
      return false;
    }
  }

  public function getPatientMedia($patient_id) {
    $query = $this->db->prepare('SELECT * FROM patient_media WHERE patient_id = :patient_id');
    $query->bindParam(':patient_id', $patient_id);
    try {
      $query->execute();
      return $query->fetchAll();
    } catch (PDOException $e) {
      echo 'Error getting patient media: ' . $e->getMessage();
      return null;
    }
  }
}

// appointments.php
class Appointment {
  private $db;

  public function __construct($db) {
    $this->db = $db;
  }

  public function createAppointment($patient_id, $doctor_name, $appointment_date, $appointment_time) {
    $query = $this->db->prepare('INSERT INTO appointments (patient_id, doctor_name, appointment_date, appointment_time) VALUES (:patient_id, :doctor_name, :appointment_date, :appointment_time)');
    $query->bindParam(':patient_id', $patient_id);
    $query->bindParam(':doctor_name', $doctor_name);
    $query->bindParam(':appointment_date', $appointment_date);
    $query->bindParam(':appointment_time', $appointment_time);
    try {
      $query->execute();
      return true;
    } catch (PDOException $e) {
      echo 'Error creating appointment: ' . $e->getMessage();
      return false;
    }
  }

  public function getAppointments($patient_id) {
    $query = $this->db->prepare('SELECT * FROM appointments WHERE patient_id = :patient_id');
    $query->bindParam(':patient_id', $patient_id);
    try {
      $query->execute();
      return $query->fetchAll();
    } catch (PDOException $e) {
      echo 'Error getting appointments: ' . $e->getMessage();
      return null;
    }
  }
}

// api.php
class API {
  private $db;

  public function __construct($db) {
    $this->db = $db;
  }

  public function handleRequest($request) {
    switch ($request['method']) {
      case 'POST':
        switch ($request['endpoint']) {
          case '/users':
            $user = new User($this->db);
            $data = json_decode(file_get_contents('php://input'), true);
            $user->createUser($data['username'], $data['email'], $data['password'], $data['role']);
            break;
          case '/media':
            $media = new Media($this->db);
            $data = json_decode(file_get_contents('php://input'), true);
            $media->createMedia($data['title'], $data['description'], $data['type'], $data['file_path']);
            break;
          case '/patient-media':
            $patientMedia = new PatientMedia($this->db);
            $data = json_decode(file_get_contents('php://input'), true);
            $patientMedia->createPatientMedia($data['patient_id'], $data['media_id']);
            break;
          case '/appointments':
            $appointment = new Appointment($this->db);
            $data = json_decode(file_get_contents('php://input'), true);
            $appointment->createAppointment($data['patient_id'], $data['doctor_name'], $data['appointment_date'], $data['appointment_time']);
            break;
          default:
            http_response_code(404);
            echo 'Endpoint not found';
            break;
        }
        break;
      case 'GET':
        switch ($request['endpoint']) {
          case '/users/{id}':
            $user = new User($this->db);
            $id = $request
