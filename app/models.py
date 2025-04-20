"""
Database models for the application.
"""
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy.sql import func

db = SQLAlchemy()

class User(db.Model, UserMixin):
    """User model for authentication and role management."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    type = db.Column(db.String(50), nullable=False, default='User')  # 'Admin' or 'User'

class MetricLogs(db.Model):
    """Model to store detailed metrics per Netdata API and project spec."""
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime(timezone=True), server_default=func.now(), nullable=False)
    ip = db.Column(db.String(64), nullable=False)  # Formerly machine_name

    cpu_user = db.Column(db.Float, nullable=True)
    cpu_system = db.Column(db.Float, nullable=True)

    ram_used = db.Column(db.Float, nullable=True)

    disk_reads = db.Column(db.Float, nullable=True)
    disk_writes = db.Column(db.Float, nullable=True)

    net_in = db.Column(db.Float, nullable=True)
    net_out = db.Column(db.Float, nullable=True)

