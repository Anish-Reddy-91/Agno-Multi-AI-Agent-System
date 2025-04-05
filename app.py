import streamlit as st
from datetime import datetime
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.storage.agent.sqlite import SqliteAgentStorage
from agno.utils.log import logger
from main import (
    web_search_agent, youtube_agent, 
    email_agent, twitter_agent, telegram_agent, 
    finance_agent, news_agent, arxiv_agent
)
from agno.team.team import Team


# Custom CSS for enhanced styling
CUSTOM_CSS = """
<style>
.main-title {
    font-size: 2.5rem;
    color: #2c3e50;
    text-align: center;
    margin-bottom: 0.5rem;
}
.subtitle {
    font-size: 1.2rem;
    color: #7f8c8d;
    text-align: center;
    margin-bottom: 1.5rem;
}
.stChatInput > div > div > input {
    background-color: #f1f2f6;
    border: 1.5px solid #a4b0be;
    border-radius: 10px;
}
</style>
"""

def add_message(role, content, tool_calls=None):
    """Add a message to the session state messages."""
    if 'messages' not in st.session_state:
        st.session_state['messages'] = []
    
    message = {"role": role, "content": content}
    if tool_calls:
        message["tool_calls"] = tool_calls
    
    st.session_state['messages'].append(message)

def main():
    # Page configuration
    st.set_page_config(
        page_title="🤖 Multi-Agent Chat System", 
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Load custom CSS
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

    # App header
    st.markdown("<h1 class='main-title'>🤖 Multi-Agent Chat System</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Intelligent Multi-Agent Problem Solver</p>", unsafe_allow_html=True)

    # Initialize session ID if not exists
    if 'session_id' not in st.session_state:
        st.session_state.session_id = str(datetime.now().strftime("%Y%m%d%H%M%S%f"))[:16]

    # Sidebar
    with st.sidebar:
        if st.button("🆕 Start New Chat"):
            st.session_state.session_id = str(datetime.now().strftime("%Y%m%d%H%M%S%f"))[:16]
            st.session_state['messages'] = []
            st.toast("New chat started", icon="🎉")
            
        st.divider()
        
        
        st.header("🛠️ Available Tools")
        tools = [
            "Web Search", "YouTube", "Email", 
            "Twitter", "Telegram", "Finance", "News", "ArXiv"
        ]
        for tool in tools:
            st.markdown(f"- {tool}")




    # Define the multi-agent team
    knowledge_retrieval_team = Team(
        name="Knowledge Retrieval Team",
        model=OpenAIChat("gpt-4o-mini"),
        members=[
            web_search_agent, youtube_agent, 
            email_agent, twitter_agent, telegram_agent, 
            finance_agent, news_agent, arxiv_agent
        ],
        instructions=[
            "You are a multi-agent team designed to handle complex user queries by leveraging the appropriate tools and agents.",
            "Follow these steps to process any user query:",
            "1. Analyze the user's query to determine the required tasks.",
            "2. For multi-step workflows:",
            "   a. FIRST use the appropriate agent to gather information",
            "   b. THEN pass that information to the action agent as a separate step",
            "3. Always follow this sequence for tasks requiring multiple agents",
            "4. Never try to handle multiple distinct tasks in a single agent call",
            "5. Provide a clear and concise response to the user"
        ],
        show_tool_calls=True,
        markdown=True,
        debug_mode=True,
        enable_agentic_context=True,
        share_member_interactions=True,
        num_of_interactions_from_history=5,
        enable_team_history=True,
        session_id=st.session_state.session_id
    )

    # Display chat history
    for message in st.session_state.get('messages', []):
        with st.chat_message(message['role']):
            st.markdown(message['content'])

    # User input
    if prompt := st.chat_input("Enter your query"):
        # Add user message to chat history
        add_message("user", prompt)

        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate response
        with st.chat_message("assistant"):
            response_container = st.empty()
            
            response_content = ""
            full_response = ""
            
            with st.spinner("Processing your query..."):
                try:
                    # Run the agent with streaming
                    for resp_chunk in knowledge_retrieval_team.run(prompt.strip(), stream=True):


                        # Stream response content
                        if resp_chunk.content is not None:
                            response_content += resp_chunk.content
                            response_container.markdown(response_content)
                            full_response = response_content

                    # Add assistant message to chat history
                    add_message("assistant", full_response, knowledge_retrieval_team.run_response.tools)

                except Exception as e:
                    error_msg = f"An error occurred: {str(e)}"
                    st.error(error_msg)
                    add_message("assistant", error_msg)

if __name__ == "__main__":
    main()