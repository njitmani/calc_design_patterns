"""Pytest configuration and fixtures for the calculator app tests."""
# tests/conftest.py
import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
