from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    # 자바의 @NotNull, @Size 같은 유효성 검증을 Field로 수행
    message: str = Field(..., min_length=1, description="AI에게 보낼 유저 프롬프트")
