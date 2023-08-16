
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.chat_models import ChatOpenAI
from tools.speech_to_text import record_audio
from tools.text_to_speech import play_generated_audio
from tools.tools import tools_name
from config import OPNEIA_API_BASE,OPNEIA_API_KEY,interactive_mode
from langchain.prompts import MessagesPlaceholder
from langchain.memory import ConversationBufferMemory
from memory.memory import memory,agent_kwargs
output_filename = "recorded_audio.wav"
recording_duration = 5  # in seconds


llm=ChatOpenAI(temperature=0.5,model="gpt-3.5-turbo-16k-0613",openai_api_base=OPNEIA_API_BASE, openai_api_key=OPNEIA_API_KEY)

agent = initialize_agent(
    tools=tools_name,
    llm=llm,
    memory=memory,
    verbose=True,
    agent_kwargs=agent_kwargs,
    agent=AgentType.OPENAI_MULTI_FUNCTIONS,
)


while True:
    if interactive_mode == "speech":
        question = record_audio(output_filename,recording_duration)
        text = agent.run(question)
        play_generated_audio(text=text)

    elif interactive_mode == "terminal":
        question = input("> ")
        agent.run(input=question)
