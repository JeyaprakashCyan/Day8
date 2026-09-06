
# Import LangChain components

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
import os
from dotenv import load_dotenv

load_dotenv()

def main():
    # Initialize OpenAI model via LangChain
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0,
    )

    # Input prompt
    user_input = "Explain Object-Oriented Programming in simple terms."

    # Send input to model
    response = llm.invoke([
        HumanMessage(content=user_input),
    ])

    # Print output
    print("\nModel Response:\n")
    print(response.content)


if __name__ == "__main__":
    main()
