# -*- coding: utf-8 -*-

"""
Google Play Store Scraper

A web scraper for the Google Play Android app store.
"""

__version__ = '0.1.11'

from .api import details, details_min, collection, developer, suggestions, search, similar


# Set default logging handler to avoid "No handler found" warnings.
import logging
try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())
