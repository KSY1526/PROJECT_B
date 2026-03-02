import os
from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT

# 클로드 API 클라이언트 초기화
_api_key = os.environ.get("ANTHROPIC_API_KEY")
client = Anthropic(api_key=_api_key)


def generate_response(prompt: str, model: str = "claude-2-1") -> str:
    """Claude에게 프롬프트를 보내고 응답을 반환합니다.

    Args:
        prompt: 사용자 프롬프트 문자열
        model: 사용할 Claude 모델 이름
    Returns:
        Claude가 생성한 텍스트
    """
    response = client.completions.create(
        model=model,
        prompt=f"{HUMAN_PROMPT}{prompt}{AI_PROMPT}",
        max_tokens=300,
        temperature=0.7,
    )
    return response.completion
