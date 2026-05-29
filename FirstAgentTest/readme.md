## FirstAgentTest

这里是hello-agent的网站：https://hello-agents.datawhale.cc/#/./README

我在hello-agent看到的第一个练习是**第一章的1.3--5分钟实现一个智能体**，虽然说是5分钟，但是我配环境，写代码还是用了挺久的😂

我自己看着网站练习时在vscode写了5个文件，下面是我的文件结构：

---/

-get_weath.py  -放get_weather函数

-get_attra.py  -放get_attraction函数

-agent_prompt.py  -放提示词

-OpenAICompatibleClient.py  -实现一个通用的客户端

-main.py -主函数

### 第一步

先下载下面的库
```py
pip install requests tavily-python openai
```
### 第二步

跟着老师写的把代码粘到对应的文件里，这一步没有什么难度，我把代码放到文件夹里了，因为对python语法还不是很熟悉
所以注释里也有对代码语法的解析，不熟悉python的可以看看

### 第三步
执行行动循环，但是真正执行前，还需要配环境，第一次还不是很熟悉，所以花了一些时间

这里是老师给的配置环境的官方文档：https://github.com/datawhalechina/hello-agents/blob/main/Extra-Chapter/Extra07-%E7%8E%AF%E5%A2%83%E9%85%8D%E7%BD%AE.md

**这里有几个坑：**

1.AIHubmix国内不好访问，我登录试了两个邮箱，都报错

2.ModelScope，这个是国内的，注册方便，支持，**但是注意，在使用的时候记得绑定阿里巴巴，否则无法使用**

3.tavily,这个注册的时候用邮箱注册也是很卡，很难注册，但是用github账号注册就很顺利，**推荐用github账号注册**

因为我用的是ModelScope，所以main.py里的配置代码也要更改，可以参考这个：
```py
API_KEY = "your_ModelScope_api_key"
BASE_URL = "https://api-inference.modelscope.cn/v1/"
MODEL_ID = "deepseek-ai/DeepSeek-V4-Flash" #这里我用的是deepseek的模型
os.environ['TAVILY_API_KEY'] = "YOUR_TAVILY_API_KEY"
```

还有在运行main.py文件前，**最好先测试一下各个api的连通性**，下面是官方给的测试代码：
```py
# 测试天气 API
import requests
response = requests.get("https://wttr.in/Beijing?format=j1")
print("天气API状态:", response.status_code)

# 测试 Tavily API
from tavily import TavilyClient
tavily = TavilyClient(api_key="your_tavily_key")
try:
    result = tavily.search("test", search_depth="basic")
    print("Tavily API 连接成功")
except Exception as e:
    print("Tavily API 错误:", e)

# 测试 LLM API - AIHubmix
from openai import OpenAI
client = OpenAI(
    api_key="your_aihubmix_api_key",
    base_url="https://aihubmix.com/v1"
)
try:
    response = client.chat.completions.create(
        model="coding-glm-4.7-free",
        messages=[{"role": "user", "content": "Hello"}],
        max_tokens=10
    )
    print("LLM API 连接成功:", response.choices[0].message.content)
except Exception as e:
    print("LLM API 错误:", e)

# 测试 LLM API - ModelScope（如果您使用的是 ModelScope，请取消注释并替换配置）
# from openai import OpenAI
# client = OpenAI(
#     api_key="your_modelscope_api_key",
#     base_url="https://api-inference.modelscope.cn/v1/"
# )
# try:
#     response = client.chat.completions.create(
#         model="Qwen/Qwen2.5-72B-Instruct",
#         messages=[{"role": "user", "content": "Hello"}],
#         max_tokens=10
#     )
#     print("LLM API 连接成功:", response.choices[0].message.content)
# except Exception as e:
#     print("LLM API 错误:", e)
```
如果测试了都没有问题，那运行程序大概率也是没有问题的

下面是我运行后的结果：

<img width="1443" height="836" alt="屏幕截图 2026-05-27 201448" src="https://github.com/user-attachments/assets/4c79d3f5-14ce-4d58-bb91-8e2860266707" />
