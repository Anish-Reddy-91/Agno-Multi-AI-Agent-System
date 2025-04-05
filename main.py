import os
from agno.agent import Agent
from agno.models.ollama import Ollama
from agno.models.openai import OpenAIChat
from agno.tools.x import XTools
from agno.tools.youtube import YouTubeTools
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.telegram import TelegramTools
from agno.tools.website import WebsiteTools
from agno.tools.yfinance import YFinanceTools
from agno.tools.newspaper4k import Newspaper4kTools
from agno.tools.arxiv import ArxivTools
from agno.tools.email import EmailTools
from dotenv import load_dotenv

# Load environment variables
load_dotenv(dotenv_path="./config/.env")

X_CONSUMER_KEY = os.getenv("X_CONSUMER_KEY")
X_CONSUMER_SECRET = os.getenv("X_CONSUMER_SECRET")
X_ACCESS_TOKEN = os.getenv("X_ACCESS_TOKEN")
X_ACCESS_TOKEN_SECRET = os.getenv("X_ACCESS_TOKEN_SECRET")
X_BEARER_TOKEN = os.getenv("X_BEARER_TOKEN")
receiver_email = os.getenv("receiver_email")
sender_email = os.getenv("sender_email")
sender_name = os.getenv("sender_name")
sender_passkey = os.getenv("sender_passkey")
base_url = os.getenv("base_url")
model_name = os.getenv("model_name")
telegram_token = os.getenv("telegram_token")    
chat_id = os.getenv("chat_id")


# # model = Ollama(id=model_name, host=base_url),
# model=OpenAIChat("gpt-4o-mini"),

# Initialize tools

x_tools = XTools(
    bearer_token=X_BEARER_TOKEN,
    consumer_key=X_CONSUMER_KEY,
    consumer_secret=X_CONSUMER_SECRET,
    access_token=X_ACCESS_TOKEN,
    access_token_secret=X_ACCESS_TOKEN_SECRET
)

email_tools = EmailTools(
    receiver_email=receiver_email,
    sender_email=sender_email,
    sender_name=sender_name,
    sender_passkey=sender_passkey,
)

# Define individual agents
twitter_agent = Agent(
    name="Twitter Agent",
    # model = Ollama(id=model_name, host=base_url),
    model=OpenAIChat("gpt-4o-mini"),
    role="Manages and interacts with Twitter (X) as an authorized user.",
    tools=[x_tools],
    instructions=[
        "Use your tools to interact with X as the authorized user.",
        "When asked to create a tweet, generate appropriate content based on the request.",
        "Do not post tweets unless explicitly instructed to do so.",
        "Respect X's usage policies and rate limits.",
    ],
    show_tool_calls=True,
    debug_mode= True,
    markdown=True
)

email_agent = Agent(
    name="Email Agent",
    # model = Ollama(id=model_name, host=base_url),
    model=OpenAIChat("gpt-4o-mini"),
    role="Collect the data fetched and emails that to specified recipients.",
    tools=[email_tools],
    instructions=[
        "Use the EmailTools to send emails.",
        "Provide a clear and concise response to the user's request.",
    ],
    debug_mode=True,
    show_tool_calls=True,
    markdown=True
)

web_search_agent = Agent(
    name="Web Search and Web Scraper Agent",
    # model = Ollama(id=model_name, host=base_url),
    model=OpenAIChat("gpt-4o-mini"),
    role="Searches the web for real-time data, retrieves relevant information and can also extracts and summarizes information from websites.",
    tools=[DuckDuckGoTools(),WebsiteTools()],
    instructions=[
        "Use DuckDuckGo to search for real-time information.",
        "Use WebsiteTools to extract information only when any URL is given by user, otherwise use DuckDuckGoTools",
        "Summarize findings in a clear and concise manner.",
    ],
    markdown=True,
    debug_mode=True
)

youtube_agent = Agent(
    name="YouTube Agent",
    # model = Ollama(id=model_name, host=base_url),
    model=OpenAIChat("gpt-4o-mini"),
    role="Handles YouTube-related queries, including video summaries and transcript extraction.",
    tools=[YouTubeTools()],
    instructions=[
        "Retrieve YouTube video transcripts and summarize the content.",
        "Provide insightful summaries for requested videos.",
    ],
    debug_mode= True,
    markdown=True
)

telegram_agent = Agent(
    name="Telegram Agent",
    # model = Ollama(id=model_name, host=base_url),
    model=OpenAIChat("gpt-4o-mini"),
    role="Sends messages to telegram.",
    tools=[TelegramTools(token=telegram_token, chat_id=chat_id)],
    debug_mode=True,
    add_history_to_messages=True,
    show_tool_calls=True,
    markdown=True
    )

finance_agent = Agent(
    name="Finance Agent",
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    # model = Ollama(id=model_name, host=base_url),
    model=OpenAIChat("gpt-4o-mini"),
    show_tool_calls=True,
    description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
    instructions=["Format your response using markdown and use tables to display data where possible."],
    debug_mode=True, 
    markdown=True
)

news_agent = Agent(
    name="News Agent",
    tools=[Newspaper4kTools()], 
    # model = Ollama(id=model_name, host=base_url),
    model=OpenAIChat("gpt-4o-mini"),
    debug_mode=True, 
    show_tool_calls=True,
    markdown=True

)

arxiv_agent = Agent(
    name="Arxiv Agent",
    tools=[ArxivTools()], 
    # model = Ollama(id=model_name, host=base_url),
    model=OpenAIChat("gpt-4o-mini"),
    debug_mode=True, 
    show_tool_calls=True,
    markdown=True
)


