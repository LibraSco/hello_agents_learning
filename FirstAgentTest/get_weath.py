import requests
#city：str表示传入的变量应该是字符串
def get_weather(city:str) ->str:#->str是返回型类型注解，表示返回的是一个字符串,这个名字一定要是已经有的变量名
    """
    通过调用wttr.in api 查询正式的天气信息
    """
    #这里的city会赋值为传入的变量名
    url=f"https://wttr.in/{city}?format=j1"
    try:
        #try放可能出错的代码，一定下面的代码1出现异常，就会跳到相应的except块去处理
        #
        #发起网络请求
        response=requests.get(url)
        response.raise_for_status()
        #它会检查http状态码，不是200就会抛出HTTPERROR异常
        data=response.json() #是字典
        #会把服务器返回的 JSON 格式的字符串自动解析成 Python 的字典或列表，然后赋给 data。
        current_condition=data['current_condition'][0]
        weather_desc=current_condition['weatherDesc'][0]['value']
        temp_c=current_condition['temp_C']

        return f"{city}当前天气:{weather_desc},气温:{temp_c}摄氏度"
    # 捕获try中抛出的异常，把把捕捉的异常赋值给e，后面就可以打印具体错误信息
    #这是 requests 库里所有网络相关异常的基类。用它可以一口气捕捉到超时、连接错误、请求失败等问题
    except requests.exceptions.RequestException as e:
        return f"错误：查询天气出现问题 -{e}"
    #只要出现元组中的任意一个异常，就进到这个except块
    #这两个异常和网络无关，是数据解析失败，大概率是因为城市名无效导致 API 返回了意外的结构。分开捕捉可以给出更精准的报错信息。
    except {KeyError,IndexError} as e:
        #处理数据解析错误
        return f"错误：解析天气数据失败 可能是城市名称无效 - {e}"
