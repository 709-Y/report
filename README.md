# 📊 Report API - 線上筆試題目（Django 版本）

本專案實作一組符合 RESTful 規範的 API，使用 Django 架設，模擬報告查詢與摘要功能。


## ✅ 功能說明

| 路徑                                | 方法 | 說明                 |
|-------------------------------------|------|----------------------|
| `/login`                            | POST | 模擬用戶登入         |
| `/reports?user_id=<user_id>`        | GET  | 查詢該使用者的報告清單 |
| `/report/<int:report_id>`           | GET  | 查詢單一報告內容     |
| `/report/<int:report_id>/summary`   | POST | 模擬 AI 生成摘要     |

---

## 🛠 技術棧

- Python 
- Django 
- RESTful 架構（使用  DRF ）
- JSON 資料模擬（`users.json`、`reports.json`）
- ## 🧪 API 测试说明

本项目包含 Postman 测试集合，位于
Report API.postman_collection.json
