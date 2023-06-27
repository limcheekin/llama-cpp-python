"""AWS Lambda function for llama.cpp.
"""
from mangum import Mangum
from llama_cpp.server.app import create_app, Settings
import os

print("os.cpu_count()", os.cpu_count())
handler = Mangum(create_app(
    Settings(n_threads=os.cpu_count(), embedding=False)))
