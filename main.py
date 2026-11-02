from dotenv import load_dotenv

load_dotenv('.env')
from recipe_agent import agent

result = agent.run_sync("Can I substitute almond milk in the pancakes? The pancake recipe lists 'milk' as an ingredient but says nothing about substitutions")
print(result.output)