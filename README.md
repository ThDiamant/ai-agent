# Python Simple AI agent

In this project, a simple AI agent utilizing Google's Gemini is created. The agent is given access to a simple
calculator project and can read what files exist in the project, read the contents of the files, write in the files and
execute them.

This was a simple project that explored on a basic level how AI agents work. Here's the quick breakdown:

* An LLM is chosen which will provide the "AI" in "AI agent".
* A set of functions are defined which correspond to the different actions the agent is allowed to make (like read
  files, write files, execute python code, etc). These functions should always return strings which inform the LLM of
  the result of the function execution.
* A "system prompt" is defined: this instructs the agent on what its role and capabilities are.
* When the agent is run, a user prompt is given. The agent will try to complete the instruction(s) given in the
  user prompt utilizing the system prompt and its available functions.

In order to run this project you will need:
1) An API for Gemini which you should put in a `.env` file. You can create the `.env` file by copying the provided
`.env.dist` file.
2) Run `uv run main.py "<your prompt>"` for example:

```
$ uv run main.py "introduce yourself in the context of this project!"
Hello! I am an AI coding agent. In the context of this project, I can help you by:

*   **Listing files and directories**: I can show you what's inside a specified directory.
*   **Reading file contents**: I can retrieve the content of any file you specify.
*   **Executing Python files**: I can run Python scripts, and pass arguments to them if needed.
*   **Writing files**: I can create new files or overwrite existing ones with content you provide.

How can I assist you today?
```