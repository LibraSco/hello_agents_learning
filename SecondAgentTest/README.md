# SecondAgentTest
我在hello-agents上看到的第二个练习是 **第四章 智能体经典范式构建**里的,一共有三个项目分别是
- ReAct
- Plan-and-Solve
- Reflection
  
这三个范式都是最经典的,做起来没有什么很大的难度,跟着老师写的步骤一步步做就行了

---
我跟着练习写的文件夹里的结构是这样的:

-.env :环境文件,放api-key

-HelloAgentLLM.py: 封装基础LLM调用函数,**在配置LLM的时候直接用第一个练习时使用的ModelScope就可以**

-React:

    -Search.py
  
    -React_Prompt.py
  
    -ReActAgent.py
 
    -ToolExecutor.py
 
 -Plan-and-Solve:

    -Planner-prompt.py
   
    -Planner.py
   
    -PlanAndSolve.py
   
    -Executor.py
   
    -Executor_prompt.py
 
-Reflection:

    -ReflectionAgent.py
    -memory.py
 
### 遇到的问题:

我在做第一个ReAct项目的时候,SerpApi很难访问,所以我使用了国内的博查来代替,同时search函数也和老师写的会不太一样,但是在使用的时候还是能正常使用的

### Conclusion and Reflection:

做完这三个项目,我学会了从0到1构建了几个最经典的范式，熟悉了底层原理，真的收益良多。
