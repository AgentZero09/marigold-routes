"""
Vercel Serverless Entry Point for Marigold Routes
This file is required for Vercel's Python runtime
"""
import sys
import os

# Add the backend directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from run import app

# Vercel will use this as the WSGI application
# No need to call app.run() - Vercel handles that
