import os
import httpx
from dotenv import load_dotenv

load_dotenv()

def get_session():
    ua = os.getenv("USER_AGENT", "inkle-tourism-assignment/1.0 (contact: rpr22ainds@cmrit.ac.in)")
    timeout = httpx.Timeout(10.0, connect=10.0)
    return httpx.Client(timeout=timeout, headers={"User-Agent": ua})
