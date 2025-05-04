from exa_py import Exa
from crewai.tools import tool
import os

from dotenv import load_dotenv

load_dotenv()

class ExaSearchTool:
	@tool
	def search(query: str):
		"""Search for a webpage based on the query."""
		return ExaSearchTool._exa().search(f"{query}", use_autoprompt=True, num_results=10)

	@tool
	def find_similar(url: str):
		"""Search for webpages similar to a given URL.
		The url passed in should be a URL returned from `search`.
		"""
		return ExaSearchTool._exa().find_similar(url,num_results=10)

	@tool
	def get_contents(urls: str):
		"""Get the contents of a webpage

		The list of urls as string must be passed as input, and the output will be a string.
		"""
		contents = ExaSearchTool._exa().get_contents(urls)
		contents = [r.text for r in contents.results]
		return "\n\n".join(contents)

	def tools():
		return [ExaSearchTool.search, ExaSearchTool.find_similar, ExaSearchTool.get_contents]

	def _exa():
		return Exa(api_key=os.getenv("EXA_API_KEY"))


