# API-AI-Thailand-Hackathon!ทีมLAWACHICKEN
โปรเจกต์นี้ประกอบด้วยแอปพลิเคชัน FastAPI สองตัว API1 และ API2 โดยวิธีการdeploy มีดังนี้

# สารบัญ

1.สิ่งที่ต้องมี (Prerequisites)
2.เริ่มต้นใช้งาน (Getting Started)
3.การ Deploy (Deployment)
4.การทดสอบ API (Testing the APIs)
5.โครงสร้างโปรเจกต์ (Project Structure)

---------------------------------------

# 1.สิ่งที่ต้องมี (Prerequisites)

1.Docker ดาวน์โหลดผ่าน: https://www.docker.com/
2.Git ดาวน์โหลดผ่าน: https://git-scm.com/

# 2.เริ่มต้นใช้งาน (Getting Started)

1.เข้าไปยังterminal/cmd (windows):
    1.1: win+R
    1.2: พิมพ์cmd+enter
2.clone Repository :
    2.1: พิมพ์คำสั่งในcmd; git clone https://github.com/warakornbiggy1/API-AI-Thailand-Hackathon-
    2.2: พิมพ์คำสั่งในcmd; cd API-AI-Thailand-Hackathon-

# 3.การ Deploy (Deployment)

ใช้ Docker Compose เพื่อให้การ Deploy API ทั้งสองง่ายขึ้น Docker Compose จะสร้าง Docker Image ที่จำเป็นและรัน Services ที่กำหนดไว้ในไฟล์ `docker-compose.yml`

1.Build และรัน Services:
    ต่อจากข้อ2.
    แล้วรันคำสั่งต่อไปนี้: docker-compose up --build -d

      --build: Flag นี้จะช่วยให้มั่นใจว่า Docker Image สำหรับ API1 และ API2 ถูกสร้าง (หรือสร้างใหม่หากตรวจพบการเปลี่ยนแปลงใน Dockerfile หรือ Source code)
      -d: Flag นี้จะรัน Services ในโหมด Detached ซึ่งหมายความว่า Services จะทำงานอยู่เบื้องหลัง ทำให้คุณสามารถใช้งาน Terminal ต่อไปได้

    คำสั่งนี้จะ:

      * Build Docker Image สำหรับ API1 และ API2 โดยอิงตาม Dockerfile ของแต่ละตัว 
      * สร้างและเริ่มต้น Container สำหรับทั้งสอง Services
      * Map Port ภายใน Container ไปยัง Port ของเครื่อง Host ของคุณตามที่กำหนดไว้ใน docker-compose.yml

2.ตรวจสอบว่า Container กำลังทำงาน:

    รันคำสั่งต่อไปนี้: docker-compose ps
    คุณควรเห็นสถานะ Up สำหรับ Services ทั้ง API1 และ API2

# 4.การทดสอบ API (Testing the APIs)

เมื่อ Services เริ่มทำงานแล้ว คุณสามารถทดสอบได้ Endpoint ที่แน่นอนจะขึ้นอยู่กับการใช้งานภายในแอปพลิเคชัน FastAPI แต่ละตัว

สมมติว่า API1 ถูกเปิดใช้งานที่ http://localhost:8000 และ API2 ที่ http://localhost:8001:

1.เข้าถึง API1 :

    เปิดเว็บเบราว์เซอร์ของคุณ หรือใช้เครื่องมืออย่าง curl เพื่อเข้าถึงเอกสารประกอบ (Documentation) หรือ Endpoint ตัวอย่าง

    OpenAPI (Swagger) UI สำหรับ API1:
    โดยทั่วไปจะอยู่ที่ http://localhost:8000/docs

    Redoc สำหรับ API1:
    โดยทั่วไปจะอยู่ที่ http://localhost:8000/redoc

    Endpoint :  curl http://localhost:8000/

2.เข้าถึง API2 :

    เช่นเดียวกันสำหรับ `API2`:

    OpenAPI (Swagger) UI สำหรับ API2:
    โดยทั่วไปจะอยู่ที่ http://localhost:8001/docs

    Redoc สำหรับ API2:
    โดยทั่วไปจะอยู่ที่ http://localhost:8001/redoc

    Endpoint :  curl http://localhost:8001/

# 5.โครงสร้างโปรเจกต์ (Project Structure)

Repository มีโครงสร้างดังนี้:

API-AI-Thailand-Hackathon/
├── API1/
│   ├── Dockerfile             # Dockerfile สำหรับ Build API1
│   └── main.py                # แอปพลิเคชัน FastAPI 
│   └──requirement.txt         # หลักสำหรับ API1
├── API2/
│   ├── Dockerfile             # Dockerfile สำหรับ Build API2
│   └── main.py                # แอปพลิเคชัน FastAPI 
│   └──requirement.txt         # หลักสำหรับ API1
├── docker-compose.yml         # กำหนดและรันแอปพลิเคชัน Docker แบบ Multi-Container
└── README.md                  # ไฟล์ สำหรับอธิบายการdeply
