from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from app.schemas.chat import ChatRequest
from app.services.llm_service import LLMService

router = APIRouter(prefix="/api/v1/chat", tags=["Chat AI"])

# 싱글톤처럼 사용할 서비스 인스턴스 생성 (스프링 @Autowired 대용)
def get_llm_service() -> LLMService:
    return LLMService()

@router.post("/stream")
async def chat_stream_endpoint(
    request: ChatRequest,
    # FastAPI의 의존성 주입(DI) 방식인 Depends 사용
    llm_service: LLMService = Depends(get_llm_service)
):
    """
    사용자의 질문을 받아 OpenAI GPT 모델의 응답을 실시간 스트리밍으로 전달합니다.
    """
    # StreamingResponse는 비동기 제네레이터(stream_chat)를 인자로 받아
    # 클라이언트에게 HTTP chunked transfer 데이터로 실시간 전송합니다.
    return StreamingResponse(
        llm_service.stream_chat(request.message),
        media_type="text/event-stream"  # SSE 표준 미디어 타입
    )
