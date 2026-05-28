import streamlit as st
from google import genai
from google.genai import types
import os
from PIL import Image
import io

st.set_page_config(page_title="Xem Chỉ Tay AI", page_icon="🔮")

st.title("🔮 Xem Chỉ Tay Bằng AI")
st.markdown("### Khám phá bí mật từ những đường chỉ tay của bạn ✨")

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

uploaded = st.camera_input("📷 Chụp ảnh lòng bàn tay") or st.file_uploader(
    "hoặc upload ảnh", type=["jpg", "jpeg", "png"]
)

if uploaded:
    image = Image.open(uploaded)
    st.image(image, caption="Ảnh bàn tay của bạn", width=350)

    if st.button("🔮 Xem Chỉ Tay", type="primary", use_container_width=True):
        with st.spinner("Đang xem chỉ tay..."):
            buffer = io.BytesIO()
            image.save(buffer, format="JPEG")
            img_bytes = buffer.getvalue()

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
                response = client.models.generate_content(
                    model="gemini-2.0-flash",
                    contents=[
                        types.Part.from_bytes(data=img_bytes, mime_type="image/jpeg"),
                        prompt
                    ]
                )
                st.markdown("---")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Lỗi: {str(e)}")

st.markdown("---")
st.markdown("""
**💡 Mẹo chụp ảnh:**
- Xòe bàn tay ra, **ngửa lòng bàn tay** lên
- Chụp **đủ sáng**, tránh bóng tối  
- Giữ tay **thẳng**, không cong ngón
""")
