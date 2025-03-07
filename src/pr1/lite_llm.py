from litellm import completion 
from dotenv import load_dotenv
import os
load_dotenv() 
api_key : str = os.getenv("GEMINI_API_KEY")
def kickoff() -> str:
    if api_key is None:
        return ValueError("GEMINI_API_KEY is not set in the environment variables.")

    response : dict[str, any]= completion(
        model ="gemini/gemini-1.5-flash",
        api_key = api_key,
        messages=[{
            "role": "user",
            "content": "How to become agentic developer?"
        }]
    )
    result : str = response["choices"][0]["message"]["content"]
    return result

    
