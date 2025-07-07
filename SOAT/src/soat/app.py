from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled
from dotenv import load_dotenv
import os

load_dotenv()
set_tracing_disabled(True)

api_key = os.getenv("GOOGLE_API_KEY")
base_url = os.getenv("GOOGLE_BASE_URL")
model = os.getenv("GOOGLE_MODEL")

external_client = AsyncOpenAI(
    api_key=api_key,
    base_url=base_url
)

model = OpenAIChatCompletionsModel(
    model=model,
    openai_client=external_client
)

async def main(user_input):
    Agent1 = Agent(
        name="Task Manager Agent",
        instructions="You are a task manager agent. Your job is to help with task management and organization.",
        model=model
    )

    Agent2 = Agent(
        name="Email Assistant Agent",
        instructions="You are an email assistant agent. Your job is to help with email management and responses.",
        model=model
    )

    Agent3 = Agent(
        name="Scheduler Agent",
        instructions="You are a scheduler agent. Your job is to help with scheduling and calendar management.",
        model=model
    )

    Agent4 = Agent(
        name="Summary Agent",
        instructions="You are a summary agent. Your job is to summarize information and provide concise overviews.",
        model=model
    )

    Agent5 = Agent(
        name="Manager Agent",
        instructions="You are a manager agent. Your job is to oversee and coordinate tasks among other agents.",
        handoffs=[
            Agent1,
            Agent2,
            Agent3,
            Agent4
        ],
        model=model
    )

    response = await Runner.run(
        Agent5,
        user_input
    )

    return response.final_output, response.last_agent.name