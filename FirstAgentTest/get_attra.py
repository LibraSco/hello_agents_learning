import os
from tavily import TavilyClient
def get_attraction(city:str,weather:str) ->str:
    """
    根据城市和天气，使用Tavily Search API搜索并返回优化后的景点推荐。
    """
    api_key=os.environ.get("TAVILY_API_KEY")
    if not api_key:#如果api_key是None或者空字符串，返回True
        return "错误：未配置TAVILY_API_KEY环境变量。"
    tavily=TavilyClient(api_key=api_key)
    query=f"'{city}' 在'{weather}天气下最值得去的旅游景点推荐及理由"
    try:
        #这里用了关键字参数，调用时，通过 参数名=值来传递参数，更加易读
        response=tavily.search(query=query,search_depth="basic",include_answer=True)
        if response.get("answer"):#用get方法从response字典里取“answer”的值
            return response["answer"]
        formatted_results=[]
        for result in response.get("results",[]):
            formatted_results.append(f"-{result['title']}:{result['content']}")
        if not formatted_results:#列表是空的
            return "抱歉，没有找到相关的旅游景点推荐。"
        return "根据搜索，为您找到以下信息:\n"+ "\n".join(formatted_results)#这个join是把formatted_results列表里的所有字符连接成一个大字符串
    except Exception as e:
        return f"错误:执行Tavily搜索时出现问题 - {e}"
