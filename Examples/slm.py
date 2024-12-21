import httpx
import json

ASSISTERR_API_KEY=''
ASSISTERR_BASE_URL='https://api.assisterr.ai'

# Simulating chat history
chat_history_simulation = [
    {"user": "",
     "assistant": "Hey I'm here to help! what are you interested in?"},
]

class AssisterrSLM:
    def __init__(self, model_slug, additional_prompt=''):
        self.model = model_slug
        self.additional_prompt = additional_prompt

    async def get_single_call(self, query):
        """Make a single API call for a quick response."""
        url = f'{ASSISTERR_BASE_URL}/api/v1/slm/{self.model}/chat/'

        async with httpx.AsyncClient() as client:
            response = await client.post(
                url=url,
                headers={'X-Api-Key': ASSISTERR_API_KEY},
                json={'query': query}
            )
            response.raise_for_status()
            return response.json()['message']

    def construct_prompt(self, question, chat_history):
        """Create prompt for the LLM."""
        header = f"<|start_header_id|>system<|end_header_id|>\n{self.additional_prompt}<|eot_id|>\n" if self.additional_prompt else ""
        chat_history_formatted = self.format_chat_history(chat_history)

        msg = f"<|start_header_id|>user<|end_header_id|>\n{question}<|eot_id|>\n<|start_header_id|>assistant<|end_header_id|>\n"
        final_prompt = header + chat_history_formatted + msg

        return final_prompt

    def format_chat_history(self, chat_history):
        """Format the chat history for the LLM."""
        formatted_history = ""
        for entry in chat_history:
            user_input = entry['user']
            assistant_response = entry['assistant']
            formatted_history += f"<|start_header_id|>user<|end_header_id|>\n{user_input}<|eot_id|>\n<|start_header_id|>assistant<|end_header_id|>\n{assistant_response}<|eot_id|>\n"
        return formatted_history

    async def get_response(self, question):
        """Get a response from the LLM."""
        prompt = self.construct_prompt(question, chat_history_simulation)

        request = json.dumps(prompt)

        url = f'{ASSISTERR_BASE_URL}/api/v1/slm/{self.model}/chat/'

        async with httpx.AsyncClient() as client:
            response = await client.post(
                url=url,
                headers={'X-Api-Key': ASSISTERR_API_KEY},
                json={'query': request}
            )
            response.raise_for_status()
            result = response.json()['message']

        # Update chat history
        chat_history_simulation.append({'user': question, 'assistant': result})
        return result
