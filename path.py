import os

# путь к текущей папке
PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
# путь к папке с файлами
File_PATH = os.path.join(PROJECT_ROOT_PATH, "file")
ListFiles = os.listdir(File_PATH)
RESOURCES_PATH = (os.path.join(PROJECT_ROOT_PATH, "resources"))
