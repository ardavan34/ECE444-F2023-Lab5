from pathlib import Path
import sys
sys.path.append("/home/ardavan/Desktop/ECE444/ECE444-F2023-Lab5")
from project.app import app, init_db


def test_index():
    tester = app.test_client()
    response = tester.get("/", content_type="html/text")

    assert response.status_code == 200
    assert response.data == b"Hello, World!"


def test_database():
    init_db()
    assert Path("flaskr.db").is_file()