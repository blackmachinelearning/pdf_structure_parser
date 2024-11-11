import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DATA_PATH = os.getenv("DATA_PATH")
    EXTRACTED_DATA_PATH = os.getenv("EXTRACTED_DATA_PATH")
    FILE_NAME = os.getenv("FILE_NAME")

