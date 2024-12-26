from volcenginesdkarkruntime import Ark

client = Ark(base_url="https://ark.cn-beijing.volces.com/api/v3",
             api_key="")

resp = client.chat.completions.create(
    model="ep-20241226174827-9tzkc",
    messages=[{
        "role": "user",
        "content": [
            {"type": "text", "text": "朋友来成都，推荐他去哪里吃，哪里玩呢"},
        ],
    }]
)

print(resp.choices[0].message.content)