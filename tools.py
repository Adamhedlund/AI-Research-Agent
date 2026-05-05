from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import tool
from datetime import datetime
import warnings
from bs4 import GuessedAtParserWarning

warnings.filterwarnings("ignore", category=GuessedAtParserWarning)

duckduckgo = DuckDuckGoSearchRun()

wiki_api = WikipediaAPIWrapper()
wiki = WikipediaQueryRun(api_wrapper=wiki_api)

@tool
def duckduckgo_search(query: str)-> str:
    """Search the web for current information."""
    try:
        return duckduckgo.run(query)
    except Exception as e:
        return f"DuckDuckGo failed: {e}"
    
@tool
def wikipedia_search(query: str) -> str:
    """Search Wikipedia for bachground information"""
    try:
        return wiki.run(query)
    except Exception as e:
        return f"Wikipedia has failed: {e}"


tools = [duckduckgo_search, wikipedia_search]