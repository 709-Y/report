import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def load_users():
    with open(os.path.join(BASE_DIR, 'data/users.json'), 'r', encoding='utf-8') as f:
        return json.load(f)
def load_reports():
    with open(os.path.join(BASE_DIR, 'data/reports.json'), 'r', encoding='utf-8') as f:
        return json.load(f)

def generate_summary(content: str) -> str:
    # 模拟摘要内容，可根据实际情况随机生成或根据规则返回
    simulated_summary = "【模擬摘要】：這是一份投資報告的摘要，涵蓋了資產配置、收益變化與市場趨勢。"

    try:
        # 可選：如果你還想保留 GPT 調用，可以把這段放在 try 裡面
        import openai
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "你是一位財經分析師，請為下列報告內容生成摘要。"},
                {"role": "user", "content": content}
            ],
            temperature=0.7,
            max_tokens=300,
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        print(f"[摘要失敗，使用模擬摘要]: {e}")
        return simulated_summary