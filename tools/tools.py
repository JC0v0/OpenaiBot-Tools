from langchain.tools.python.tool import PythonREPLTool
from langchain.tools import Tool,ShellTool
from langchain.tools.ddg_search.tool import DuckDuckGoSearchResults
from langchain.utilities import TextRequestsWrapper
from langchain.tools.file_management.write import WriteFileTool
from langchain.tools.file_management.read import ReadFileTool
from langchain.tools.file_management.copy import CopyFileTool
from langchain.tools.file_management.delete import DeleteFileTool
from langchain.tools.file_management.move import MoveFileTool
from langchain.tools.file_management.list_dir import ListDirectoryTool
from langchain.tools import WikipediaQueryRun
from langchain.utilities import WikipediaAPIWrapper
from tools.tool.zaobao import zaobao
from tools.tool.comment import comment
from tools.tool.weather import get_weather 
from tools.tool.joke import get_joke
from tools.tool.qinghua import get_qinghua
from tools.tool.check_express import kd
python = PythonREPLTool()
requests = TextRequestsWrapper()
shell_tool = ShellTool()
ddg_search = DuckDuckGoSearchResults()
wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())

tools_name = [
    Tool.from_function(
        func=ddg_search.run,
        name="ddg_search",
        description="useful for when you need to answer questions about current events",
        handle_tool_error=True,
    ),
    Tool.from_function(
        func=python.run,
        name="Python",
        description="You can run Python code using",
        handle_tool_error=True,
    ),
    Tool.from_function(
        func=requests.get,
        name="Requests",
        description="Use it when you need to visit a link",
        handle_tool_error=True,
    ),
    Tool.from_function(
        func=shell_tool.run,
        name="Shell",
        description="It allows you to execute shell commands and interact with local system files",
        handle_tool_error=True,
        #适用于linux系统
    ),
    Tool.from_function(
        func=wikipedia.run,
        name="Wiki",
        description="Wikipedia knowledge base, you can search for some useful knowledge",
        handle_tool_error=True,
    ),
    zaobao,
    comment,
    get_weather,
    get_joke,
    get_qinghua,
    kd,
]
