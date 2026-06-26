# my-ai-backend


```text
my-ai-backend/
├── pyproject.toml         # Gradle의 build.gradle 역할 (의존성 관리)
├── uv.lock                # Gradle의 lock 파일 역할 (의존성 고정)
└── app/                   # 소스코드 메인 디렉토리 (src/main/java 역할)
    ├── __init__.py
    ├── main.py            # SpringBootApplication 메인 클래스 역할
    ├── config.py          # application.yml 설정 파일 역할
    ├── schemas/           # DTO (Data Transfer Object) 패키지
    │   └── chat.py
    ├── routers/           # Controller 패키지 (엔드포인트 라우팅)
    │   └── chat.py
    └── services/          # Service 비즈니스 로직 패키지
        └── llm_service.py


# fastapi
uv run uvicorn app.main:app --reload

http://127.0.0.1:8000/docs
http://127.0.0.1:8000/health

kill -9 $(lsof -t -i:8000)

```