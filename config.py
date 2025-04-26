# Loads sensitive environment configs like DB URI and JWT secret
import os
from dotenv import load_dotenv

load_dotenv()

DB_URI = os.getenv("DB_URI")
JWT_SECRET = os.getenv("JWT_SECRET", "default-secret")
