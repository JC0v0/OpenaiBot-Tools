from langchain.memory import ConversationBufferMemory
from config import memory
from langchain.prompts import MessagesPlaceholder

agent_kwargs = {
    "extra_prompt_messages": [MessagesPlaceholder(variable_name="memory")],
}

if memory == 'ConversationBufferMemory':

    memory = ConversationBufferMemory(memory_key="memory", return_messages=True)


