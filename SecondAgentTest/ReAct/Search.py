import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()
def search(query: str) -> str:
    """
    一个基于博查(Bocha)搜索API的网页搜索引擎工具。
    它会智能地解析搜索结果，优先返回知识图谱等信息，若无则返回前几个网页摘要。
    """
    print(f"🔍 正在执行 [博查] 网页搜索: {query}")
    try:
        # 1. 从环境变量获取API密钥
        api_key = os.getenv("BOCHA_API_KEY")
        if not api_key:
            return "错误: BOCHA_API_KEY 未在 .env 文件中配置。"

        # 2. 准备API请求
        # 使用博查提供的Web Search API端点[reference:3][reference:4][reference:5]
        url = "https://api.bochaai.com/v1/web-search"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "query": query,       # 搜索关键词
            "summary": True,      # 请求返回内容摘要，便于AI理解[reference:6]
            "count": 5,           # 返回结果数量，最多50条[reference:7]
            "page": 1,            # 分页参数
            "freshness": "noLimit" # 默认搜索所有时间的网页[reference:8]
        }

        # 3. 发送POST请求
        response = requests.post(url, headers=headers, data=json.dumps(payload))

        # 4. 处理响应结果
        if response.status_code == 200:
            results = response.json()
            # 博查返回的数据结构通常为 results["data"]["webPages"]["value"][reference:9]
            web_pages = results.get("data", {}).get("webPages", {}).get("value", [])

            if not web_pages:
                return f"对不起，没有找到关于 '{query}' 的信息。"

            # 智能解析：优先返回结构化的模态卡，例如知识图谱等信息
            # 你原有的 SerpApi 代码会检查 knowledge_graph
            # 在博查中，可以通过 'modalCards' 或类似字段获取，具体可查阅官方文档
            # 这里提供一个简化的示例，你后续可以根据官方文档进行定制化解析
            # 如果有模态卡，优先展示模态卡信息
            # if results.get("data", {}).get("modalCards"):
            #     # 处理模态卡信息...
            #     pass

            # 若没有模态卡，则返回前三个网页结果的摘要
            # 博查返回的网页结果中，'summary' 字段包含了长文本摘要[reference:10]
            snippets = []
            for i, page in enumerate(web_pages[:3], 1):
                title = page.get('name', '')        # 网页标题
                summary = page.get('summary', '')    # 网页内容摘要
                snippets.append(f"[{i}] {title}\n{summary}")

            return "\n\n".join(snippets)

        else:
            return f"搜索API请求失败！错误码：{response.status_code}, 详情：{response.text}"

    except Exception as e:
        return f"搜索时发生错误: {e}"