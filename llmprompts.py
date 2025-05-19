from langchain_ollama import OllamaLLM
from langchain_community.utilities import GoogleSerperAPIWrapper
from dotenv import load_dotenv
import json

load_dotenv()

# Result 
search = GoogleSerperAPIWrapper(k=15, type="news")
llm = OllamaLLM(model='llama3.2', format='json')

def get_web_deets(
        news_start_date: str, news_end_date: str, coin_name: str = None
) -> str:
    """Search the web for news about a security at a specific date."""
    if coin_name:
        return search.run(
            f"{coin_name} price before: {news_end_date} after {news_start_date}"
        )
    else:
        return search.run(
            f"BTC price before: {news_end_date} after {news_start_date}"
        )
    
def prompt_template(web_deets: str) -> str:
    """Parses results from a web search into a formatted prompt"""
    return f"""You are a helpful financial assistant, provide helpful, harmless and honest answers.
            Using the news below, respond as to whether the sentiment in the news is either ['positive', 'negative']
            and give a score of how strong the sentiment is between 0 and 1. Respond using the keys sentiment, score.

            Example of result:
            'sentiment': 'positive',
            'score': 0.2

            Do not reply with neutral sentiment or mixed.

            News: {web_deets}"""

def direct_recommendation(web_deets: str) -> str:
    """Parses results from a web search into a formatted prompt"""
    return f"""You are a helpful financial assistant, provide helpful, harmless and honest answers.
            Using the news below, respond as to whether an investor should you buy, sell or hold
            and give a score of how strong the signal is between 0 and 1. 
            Respond using the format of recommendation and score.

            Example of result:
            'recommendation': 'hold',
            'score': 0.2

            News: {web_deets}"""