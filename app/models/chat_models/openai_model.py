from langchain.chat_models import init_chat_model
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_community.tools.ddg_search.tool import DuckDuckGoSearchRun
from langgraph.prebuilt import create_react_agent


class SimpleChatBot:
    def __init__(self):
        model = init_chat_model("gpt-4o-mini", model_provider="openai")
        workflow = StateGraph(state_schema=MessagesState)
        search = DuckDuckGoSearchRun()
        tools = [search]
        system_prompt_msg = """
        You are a helpful Telegram bot.  
        - Answer user questions clearly and concisely.  
        - Keep responses short, simple, and to the point.  
        - Do not provide or encourage harmful, illegal, explicit, or dangerous content.  
        - If a question is inappropriate (dirty, offensive, violent, or unsafe), politely refuse to answer.  
        - Stay professional, friendly, and respectful at all times.
        """

        # Define the function that calls the model
        def call_model(state: MessagesState):
            system_prompt = system_prompt_msg
            messages = [SystemMessage(content=system_prompt)] + state["messages"]
            response = model.invoke(messages)
            return {"messages": response}

        # Define the node and edge
        workflow.add_node("model", call_model)
        workflow.add_edge(START, "model")

        # Add simple in-memory checkpointer
        memory = MemorySaver()
        self.chatbot = create_react_agent(model, tools, checkpointer=memory)

    def ask(self, msg: str) -> str:
        return self.chatbot.invoke(
            {"messages": [HumanMessage(content=msg)]},
            config={"configurable": {"thread_id": "1"}},
        )["messages"][-1].content
