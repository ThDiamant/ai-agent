import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

from functions.call_function import call_function
from functions.get_file_content import schema_get_file_content
from functions.get_files_info import schema_get_files_info
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file
from prompts import system_prompt

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

user_prompt = args.user_prompt
messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError('API key not set')

client = genai.Client(api_key=api_key)

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file
    ],
)

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=messages,
    config = types.GenerateContentConfig(
        tools = [available_functions],
        system_instruction = system_prompt
    )
)

if not response.usage_metadata:
    raise RuntimeError('No usage metadata found')

if response.function_calls:
    function_results = []
    for function_call in response.function_calls:
        function_call_result = call_function(function_call)
        if not function_call_result.parts:
            raise Exception("Function call did not return any result")

        if not function_call_result.parts[0].function_response:
            raise Exception("Function call did not return any response")

        if not function_call_result.parts[0].function_response.response:
            raise Exception("Function call did not return any response")

        function_results.append(function_call_result.parts[0])
        if args.verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")
else:
    print(response.text)

if args.verbose:
    prompt_token_count = response.usage_metadata.prompt_token_count
    response_token_count = response.usage_metadata.candidates_token_count
    print(f"User prompt: {user_prompt}")
    print(f"Prompt tokens: {prompt_token_count}")
    print(f"Response tokens: {response_token_count}")
