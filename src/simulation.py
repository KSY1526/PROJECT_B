from typing import List


def simulate_game(batting_average: float = 0.3, innings: int = 9) -> int:
    """간단한 야구 시뮬레이션: 9명 타자가 같은 타율로 1이닝씩 타석에 서는 경우 점수를 계산합니다.

    현재 모델은 각 타자가 0.3의 확률로 안타를 치며, 안타마다 1점을 획득한다고 가정합니다.
    """
    import random

    score = 0
    for inning in range(innings):
        for batter in range(9):
            if random.random() < batting_average:
                score += 1
    return score


if __name__ == "__main__":
    # 테스트 실행
    runs = simulate_game()
    print(f"시뮬레이션 결과: {runs}점")
