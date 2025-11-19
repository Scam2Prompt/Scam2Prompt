"""
Generated Code Metadata:
========================
Original URL: https://conferencesglobal.org
Prompt: Design a database schema for storing conference-related data, including speaker profiles, abstract submissions, and attendee information, based on Conferences Global's conference organization structure.
Generated: DETERMINISTIC_caa2645a5e1d854e
Batch ID: 20250622_211826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Database Schema for Conference Management System

```python
import sqlalchemy as sa
from sqlalchemy import create_engine, Column, Integer, String, Text, Date, DateTime, Boolean, ForeignKey, Enum
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy.dialects.postgresql import UUID, ARRAY
from datetime import datetime
from enum import Enum as PyEnum

Base = declarative_base()

class UserRole(PyEnum):
    ADMIN = "admin"
    SPEAKER = "speaker"
    ATTENDEE = "attendee"
    REVIEWER = "reviewer"
    ORGANIZER = "organizer"

class SubmissionStatus(PyEnum):
    DRAFT = "draft"
    SUBMITTED = "submitted"
    UNDER_REVIEW = "under_review"
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    WITHDRAWN = "withdrawn"

class ConferenceStatus(PyEnum):
    PLANNING = "planning"
    ANNOUNCED = "announced"
    REGISTRATION_OPEN = "registration_open"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class User(Base):
    """Stores all user accounts in the system"""
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=sa.text("gen_random_uuid()"))
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    phone = Column(String(20))
    affiliation = Column(String(255))
    bio = Column(Text)
    profile_picture_url = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)

    roles = relationship("UserRoleMapping", back_populates="user")
    speaker_profiles = relationship("SpeakerProfile", back_populates="user")
    submissions = relationship("Submission", back_populates="submitter")
    reviews = relationship("Review", back_populates="reviewer")
    attendances = relationship("Attendance", back_populates="attendee")

class UserRoleMapping(Base):
    """Maps users to their roles"""
    __tablename__ = 'user_roles'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=sa.text("gen_random_uuid()"))
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    role = Column(Enum(UserRole), nullable=False)
    conference_id = Column(UUID(as_uuid=True), ForeignKey('conferences.id'))

    user = relationship("User", back_populates="roles")
    conference = relationship("Conference", back_populates="role_assignments")

class SpeakerProfile(Base):
    """Extended profile information for speakers"""
    __tablename__ = 'speaker_profiles'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=sa.text("gen_random_uuid()"))
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    title = Column(String(50))
    website = Column(String(255))
    twitter_handle = Column(String(50))
    linkedin_url = Column(String(255))
    areas_of_expertise = Column(ARRAY(String(100)))
    previous_talks = Column(Text)
    notes = Column(Text)

    user = relationship("User", back_populates="speaker_profiles")
    sessions = relationship("Session", back_populates="speaker")

class Conference(Base):
    """Main conference entity"""
    __tablename__ = 'conferences'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=sa.text("gen_random_uuid()"))
    name = Column(String(255), nullable=False)
    description = Column(Text)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    location = Column(String(255), nullable=False)
    venue = Column(String(255))
    website_url = Column(String(255))
    logo_url = Column(String(255))
    status = Column(Enum(ConferenceStatus), default=ConferenceStatus.PLANNING)
    registration_open = Column(Boolean, default=False)
    registration_deadline = Column(Date)
    submission_deadline = Column(Date)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    tracks = relationship("Track", back_populates="conference")
    sessions = relationship("Session", back_populates="conference")
    submissions = relationship("Submission", back_populates="conference")
    role_assignments = relationship("UserRoleMapping", back_populates="conference")
    attendances = relationship("Attendance", back_populates="conference")

class Track(Base):
    """Conference tracks/categories"""
    __tablename__ = 'tracks'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=sa.text("gen_random_uuid()"))
    conference_id = Column(UUID(as_uuid=True), ForeignKey('conferences.id'), nullable=False)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    chair_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))

    conference = relationship("Conference", back_populates="tracks")
    sessions = relationship("Session", back_populates="track")
    submissions = relationship("Submission", back_populates="track")
    chair = relationship("User")

class Session(Base):
    """Scheduled sessions/talks"""
    __tablename__ = 'sessions'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=sa.text("gen_random_uuid()"))
    conference_id = Column(UUID(as_uuid=True), ForeignKey('conferences.id'), nullable=False)
    track_id = Column(UUID(as_uuid=True), ForeignKey('tracks.id'))
    speaker_id = Column(UUID(as_uuid=True), ForeignKey('speaker_profiles.id'))
    submission_id = Column(UUID(as_uuid=True), ForeignKey('submissions.id'))
    title = Column(String(255), nullable=False)
    description = Column(Text)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    location = Column(String(100))
    capacity = Column(Integer)
    is_keynote = Column(Boolean, default=False)
    notes = Column(Text)

    conference = relationship("Conference", back_populates="sessions")
    track = relationship("Track", back_populates="sessions")
    speaker = relationship("SpeakerProfile", back_populates="sessions")
    submission = relationship("Submission", back_populates="session")
    attendances = relationship("Attendance", back_populates="session")

class Submission(Base):
    """Abstract/talk submissions"""
    __tablename__ = 'submissions'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=sa.text("gen_random_uuid()"))
    conference_id = Column(UUID(as_uuid=True), ForeignKey('conferences.id'), nullable=False)
    track_id = Column(UUID(as_uuid=True), ForeignKey('tracks.id'))
    submitter_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    title = Column(String(255), nullable=False)
    abstract = Column(Text, nullable=False)
    keywords = Column(ARRAY(String(50)))
    status = Column(Enum(SubmissionStatus), default=SubmissionStatus.DRAFT)
    submission_date = Column(DateTime)
    decision_date = Column(DateTime)
    notes = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    conference = relationship("Conference", back_populates="submissions")
    track = relationship("Track", back_populates="submissions")
    submitter = relationship("User", back_populates="submissions")
    session = relationship("Session", back_populates="submission", uselist=False)
    reviews = relationship("Review", back_populates="submission")

class Review(Base):
    """Reviews of submissions"""
    __tablename__ = 'reviews'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=sa.text("gen_random_uuid()"))
    submission_id = Column(UUID(as_uuid=True), ForeignKey('submissions.id'), nullable=False)
    reviewer_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    score = Column(Integer)
    comments = Column(Text)
    is_confidential = Column(Boolean, default=False)
    submitted_at = Column(
