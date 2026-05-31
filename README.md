# 🔮 Xem Chỉ Tay Bằng AI

Ứng dụng xem chỉ tay tự động sử dụng AI (Groq - LLaMA Vision), phân tích các đường chỉ tay và đưa ra kết quả bằng tiếng Việt.

## 🌐 Link App

👉 **[Chạy app tại đây](https://chitay-app-sumyzstcah6f92ajarsrbk.streamlit.app/)**

## 📋 Tính năng

- Upload ảnh hoặc chụp trực tiếp từ camera
- Phân tích **3 đường chỉ tay chính:**
  - 💗 Đường tình cảm
  - 🧠 Đường trí tuệ  
  - 🌱 Đường sinh mệnh
- Kết quả bằng tiếng Việt theo phong cách huyền bí

## 🛠️ Công nghệ sử dụng

- **Streamlit** — giao diện web
- **Groq API** — AI phân tích ảnh (LLaMA 4 Vision)
- **Python 3.11**

## 📁 Cấu trúc

```
chitay-app/
├── app.py              # Code chính
├── requirements.txt    # Thư viện
└── README.md           # File này
```

## ⚙️ Cài đặt & Chạy local

```bash
git clone https://github.com/thanhle31251024682-a11y/chitay-app
cd chitay-app
pip install -r requirements.txt
streamlit run app.py
```

> Cần thêm `GROQ_API_KEY` vào file `.streamlit/secrets.toml`
