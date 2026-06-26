from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from app.config import settings
from typing import AsyncGenerator

class LLMService:
    def __init__(self):
        # 1. LangChain LLM 클라이언트 빈(Bean) 초기화 효과
        self.model = ChatOpenAI(
            model="gpt-4o-mini", 
            api_key=settings.OPENAI_API_KEY,
            streaming=True  # 스트리밍 활성화 필수
        )
        # 2. 프롬프트 템플릿 정의
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", "당신은 친절한 백엔드 개발 전문가 AI 가이드입니다. 한국어로 답변하세요."),
            ("user", "{user_input}")
        ])
        # 3. LangChain 표현식(LCEL) 체인 연결 (파이프라인 구축)
        self.chain = self.prompt | self.model

    async def stream_chat(self, message: str) -> AsyncGenerator[str, None]:
        """
        비동기로 LLM 스트리밍 데이터를 받아 chunk 단위로 yield(반환)하는 제네레이터
        """
        # 자바의 WebFlux Flux와 유사한 개념입니다.
        async for chunk in self.chain.astream({"user_input": message}):
            # LLM이 뱉어내는 한 조각(chunk)의 텍스트만 추출하여 전달
            if chunk.content:
                yield chunk.content
