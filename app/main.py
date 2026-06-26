from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import chat

app = FastAPI(
    title="AI Backend Server", 
    description="Java/Spring 개발자가 빌딩한 FastAPI LangChain 백엔드",
    version="1.0.0"
)

# CORS 미들웨어 설정 (Spring Security의 corsConfigurationSource 역할)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 실무에서는 프론트엔드 도메인만 허용하도록 주소 명시
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 작성한 AI 비즈니스 라우터 등록
app.include_router(chat.router)

@app.get("/health")
async def health_check():
    # Spring Actuator의 health 엔드포인트 역할
    return {"status": "UP"}
