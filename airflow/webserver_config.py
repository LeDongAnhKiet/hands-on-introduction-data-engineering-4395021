from __future__ import annotations
import os
from airflow.www.fab_security.manager import AUTH_DB

basedir = os.path.abspath(os.path.dirname(__file__))

WTF_CSRF_ENABLED = False
WTF_CSRF_TIME_LIMIT = None