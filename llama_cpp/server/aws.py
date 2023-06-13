"""AWS Lambda function for llama.cpp.
"""
from mangum import Mangum
from llama_cpp.server.app import create_app

handler = Mangum(create_app())


