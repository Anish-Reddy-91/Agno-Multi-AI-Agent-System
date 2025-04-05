AI Agents Using Agno Framework
=============================

This repository is a Multi AI Agent system built using the Agno Framework. These agents leverage cutting-edge models such as OpenAI and Ollama to perform a variety of tasks ranging from generating blog posts, summarizing YouTube videos, to analyzing stock market data, etc. Based on the query, the respective Agent will be triggered and tasks will be performed accordingly. Each agent is designed to interact with specific models and tools, enabling them to perform their roles efficiently.

Multi AI Agents Overview
--------------

1. **Web Search AI Agent**
	* Model: OpenAI
	* Purpose: Search the web for real-time information and retrieve relevant data.
	* Features: Utilizes DuckDuckGo for research. Summarizes findings in a clear and concise manner.
2. **YouTube AI Agent**
	* Model: OpenAI
	* Purpose: Search and summarize YouTube videos.
	* Features: Uses YouTubeVideoSearchTool for video analysis. Highlights key points and provides markdown-formatted summaries.
3. **Email AI Agent**
	* Model: OpenAI
	* Purpose: Send emails to specified recipients.
	* Features: Uses EmailTools to send emails. Provides a clear and concise response to the user's request.
4. **Twitter AI Agent**
	* Model: OpenAI
	* Purpose: Manage and interact with Twitter as an authorized user.
	* Features: Uses XTools to interact with Twitter. Creates tweets based on the request.
5. **Telegram AI Agent**
	* Model: OpenAI
	* Purpose: Send messages to telegram.
	* Features: Uses TelegramTools to send messages. Provides a clear and concise response to the user's request.
6. **Finance AI Agent**
	* Model: OpenAI
	* Purpose: Analyze stock market data.
	* Features: Uses YFinanceTools to analyze stock market data. Provides a clear and concise response to the user's request.
7. **News AI Agent**
	* Model: OpenAI
	* Purpose: Analyze news articles.
	* Features: Uses Newspaper4kTools to analyze news articles. Provides a clear and concise response to the user's request.
8. **ArXiv AI Agent**
	* Model: OpenAI
	* Purpose: Analyze articles from arXiv.
	* Features: Uses ArxivTools to analyze articles from arXiv. Provides a clear and concise response to the user's request.

Technical Requirements
----------------------

* Python Version: 3.11.0
* Dependencies: Listed in `requirements.txt`.

Setup and Installation
----------------------

1. Create a Virtual Environment: `python -m venv myenv`
2. Activate the Virtual Environment: `cd myenv/Scripts/Activate`
3. Install Dependencies: `pip install -r requirements.txt`
4. Run the Application: `python <agent_file>.py`

Note: Make sure to replace API keys with your own in the environment variables.
