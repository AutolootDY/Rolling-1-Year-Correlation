# การวิเคราะห์ความสัมพันธ์ระหว่าง Bitcoin และ S&P 500 (Rolling Correlation)

โปรเจกต์นี้ใช้ **Streamlit และ Plotly** เพื่อวิเคราะห์ **Rolling 1-Year Correlation Coefficient** ระหว่าง **Bitcoin (BTC-USD)** และ **S&P 500 (^GSPC)** โดยค่าความสัมพันธ์นี้ช่วยให้เข้าใจว่า Bitcoin มีพฤติกรรมไปในทิศทางเดียวกับตลาดหุ้นหรือไม่

## 📌 คุณสมบัติของโปรแกรม
- **โหลดข้อมูล BTC และ S&P 500 จากไฟล์ CSV อัตโนมัติ** (`btc.csv`, `spx500.csv`)
- **คำนวณ Log Returns** ของ Bitcoin และ S&P 500
- **คำนวณ Rolling 1-Year Correlation** (252 วันทำการ)
- **แสดงผลกราฟด้วย Plotly** และเน้นสีแดงในช่วงที่ Correlation เป็นลบ
- **สร้าง Dashboard เชิงโต้ตอบด้วย Streamlit**

## 🖥 ลิงก์ดูผลงาน
คุณสามารถดูผลงานของแอปที่ถูก Deploy ได้ที่ลิงก์นี้:  
[**Crypto MarketCap Treemap on Streamlit Cloud**](https://rolling-1-year-correlation-jabl8um7xnmvlt2uijiyub.streamlit.app/))



## 📊 วิธีการอ่านกราฟ
- **เส้นสีน้ำเงิน**: ค่าความสัมพันธ์ระหว่าง BTC และ S&P 500 แบบ Rolling
- **พื้นที่สีแดง**: ช่วงที่ความสัมพันธ์ติดลบ (BTC เคลื่อนไหวสวนทางกับ S&P 500)
- **ค่าความสัมพันธ์ใกล้ 1** → BTC มีแนวโน้มเคลื่อนไหวตาม S&P 500
- **ค่าความสัมพันธ์ใกล้ -1** → BTC มีแนวโน้มเคลื่อนไหวสวนทางกับ S&P 500
- **ค่าประมาณ 0** → BTC และ S&P 500 ไม่มีความสัมพันธ์ชัดเจน

## 🛠️ ข้อกำหนดของระบบ
- ต้องใช้ Python 3.8+
- ติดตั้งแพ็กเกจที่จำเป็นโดยใช้คำสั่ง:
```bash
pip install -r requirements.txt
```

## ⚡ ไลบรารีที่ใช้
- `streamlit`
- `pandas`
- `numpy`
- `plotly`
- `yfinance`

## 📌 การพัฒนาในอนาคต
- รองรับสินทรัพย์เพิ่มเติม เช่น ทองคำ, NASDAQ
- อนุญาตให้ผู้ใช้กำหนดช่วง Rolling Window เอง
- จัดเก็บค่าความสัมพันธ์ย้อนหลังในฐานข้อมูล

