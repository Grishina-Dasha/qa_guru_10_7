import os
import pytest
from zipfile import ZipFile
from path import File_PATH, RESOURCES_PATH, ListFiles
import shutil


@pytest.fixture(scope='function', autouse=True)
def check_file():
    if not os.path.exists(RESOURCES_PATH):
        os.mkdir(RESOURCES_PATH)
    with ZipFile(os.path.join(RESOURCES_PATH, "archive.zip"), "w") as myzip:
        for f in ListFiles:
            filepath = os.path.join(File_PATH, f)
            myzip.write(filepath, os.path.basename(filepath))
    with ZipFile(os.path.join(RESOURCES_PATH, "archive.zip"), "r") as zp:
        zp.extractall(RESOURCES_PATH)
    yield
    shutil.rmtree(RESOURCES_PATH)
