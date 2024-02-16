import llama_index
from llama_index.llm import OpenAI
from llama_index.readers import SimpleWebPageReader
from llama_index import VectorStoreIndex
import os
from dotenv import load_dotenv