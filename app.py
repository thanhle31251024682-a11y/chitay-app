import streamlit as st
from groq import Groq
import base64
import os
from PIL import Image
import io

st.set_page_config(page_title="Xem Chỉ Tay AI", page_icon="🔮")
st.title("🔮 Xem Chỉ Tay Bằng AI")
st.markdown("### Khám phá bí mật từ những đường chỉ tay của bạn ✨")

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

uploaded = st.camera_input("📷 Chụp ảnh lòng bàn tay") or st.file_uploader(
    "hoặc upload ảnh", type=["jpg", "jpeg", "png"]
)

if uploaded:
    image = Image.open(uploaded)
    st.image(image, caption="Ảnh bàn tay của bạn", width=350)

    if st.button("🔮 Xem Chỉ Tay", type="primary", use_container_width=True):
        with st.spinner("Đang xem chỉ tay..."):
            buffer = io.BytesIO()
            image.convert("RGB").save(buffer, format="JPEG")
            img_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")

            prompt = """Bạn là một thầy xem chỉ tay người Việt Nam có 30 năm kinh nghiệm.
Hãy xem bàn tay trong ảnh và đưa ra kết quả xem chỉ tay chi tiết bằng tiếng Việt.

Phân tích theo thứ tự:
1. 💗 **Đường tình cảm** (đường trên cùng): tình yêu, hôn nhân, cảm xúc
2. 🧠 **Đường trí tuệ** (đường giữa): tư duy, học vấn, sự nghiệp trí óc
3. 🌱 **Đường sinh mệnh** (đường cong quanh ngón cái): sức khỏe, tuổi thọ, năng lượng
4. 🍀 **Nhận xét tổng thể** và lời khuyên

Viết theo phong cách huyền bí, thú vị, tích cực nhưng thực tế.
Mỗi mục khoảng 2-3 câu. Kết thúc bằng 1 câu chúc may mắn."""

            try:
                response = client.chat.completions.create(
                    model="meta-llama/llama-4-scout-17b-16e-instruct",
                    messages=[
                        {
                            "role": "user",
                            "content": [
                                {
                                    "type": "image_url",
                                    "image_url": {
                                        "url": f"data:image/jpeg;base64,{img_base64}"
                                    }
                                },
                                {"type": "text", "text": prompt}
                            ]
                        }
                    ],
                    max_tokens=1000,
                )
                st.markdown("---")
                st.markdown(response.choices[0].message.content)
            except Exception as e:
                st.error(f"Lỗi: {str(e)}")

st.markdown("---")
st.markdown("""
**💡 Mẹo chụp ảnh:**
- Xòe bàn tay ra, **ngửa lòng bàn tay** lên
- Chụp **đủ sáng**, tránh bóng tối
- Giữ tay **thẳng**, không cong ngón
""")
