import os
from openai import OpenAI
from dotenv import load_dotenv #从dotenv库导入load_dotenv函数，用于加载 .env 文件中的环境变量
from typing import List,Dict

load_dotenv()#调用 load_dotenv() 函数，它会读取当前目录（或父目录）下的 .env 文件，把里面的键值对设置为环境变量。之后 os.getenv 就能获取到这些值。

class HelloAgentsLLM:
     """
    为本书 "Hello Agents" 定制的LLM客户端。
    它用于调用任何兼容OpenAI接口的服务，并默认使用流式响应。
    """
     def __init__(self,model:str=None,api_key:str=None,base_url:str=None,timeout:int=None):
          """
        初始化客户端。优先使用传入参数，如果未提供，则从环境变量加载。
        """
          self.model=model or os.getenv("LLM_MODEL_ID")#os.getenv()如果 model 不为 None 且不是假值（如空字符串），则取 model 的值。
                                                       #否则取 os.getenv("LLM_MODEL_ID") 的值（从环境变量读取，若不存在返回 None）。
          api_key=api_key or os.getenv("LLM_API_KEY")
          base_url=base_url or os.getenv("LLM_BASE_URL")
          timeout=timeout or os.getenv("LLM_TIMEOUT",60)

          if not all([self.model,api_key,base_url]):
               return ValueError("模型ID、API密钥和服务地址必须被提供或在.env文件中定义。")
          self.client=OpenAI(api_key=api_key,base_url=base_url,timeout=timeout)

     def think(self,messages:List[Dict[str,str]],temperature:float=0)->str:
        """
        调用大语言模型进行思考，并返回其响应。
        """
        print(f"🧠正在调用{self.model}模型...")
        try:
             response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=temperature,
                stream=True,
            )
              # 处理流式响应
             print("✅ 大语言模型响应成功:")
             collected_content = []
             for chunk in response:#这个是流式响应，一个一个输出
                if not chunk.choices:
                    continue
                content = chunk.choices[0].delta.content or ""
                print(content, end="", flush=True)
                collected_content.append(content)
             print()  # 在流式输出结束后换行
             return "".join(collected_content)
             
        except Exception as e:
            print(f"❌调用LLM API时发生错误:{e}")
            return None
        
if __name__ == '__main__':
     try:
          llmClient = HelloAgentsLLM()
          exampleMessages = [
               {"role": "system", "content": "You are a helpful assistant that writes Python code."},
               {"role": "user", "content": "写一个快速排序算法"}
          ]
          
          print("--- 调用LLM ---")
          responseText = llmClient.think(exampleMessages)
          if responseText:
               print("\n\n--- 完整模型响应 ---")
               print(responseText)
     except ValueError as e:
          print(e)  