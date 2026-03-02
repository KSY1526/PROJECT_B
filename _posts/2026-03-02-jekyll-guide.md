---
layout: post
title: "Jekyll 블로그 글 작성 가이드"
date: 2026-03-02 13:00:00 +0900
tags: [Jekyll, 가이드]
---

블로그에 새 글을 작성하는 방법을 정리합니다.

## 새 글 만들기

`_posts/` 폴더에 아래 형식으로 파일을 만드세요:

```
YYYY-MM-DD-제목.md
```

## Front Matter (머리말)

파일 맨 위에 다음을 포함해야 합니다:

```yaml
---
layout: post
title: "글 제목"
date: 2026-03-02 12:00:00 +0900
tags: [태그1, 태그2]
---
```

## 마크다운 문법

### 코드 블록

```python
def hello():
    print("Hello, World!")
```

### 이미지

```markdown
![대체 텍스트](/assets/images/파일명.png)
```

### 링크

```markdown
[링크 텍스트](https://example.com)
```

이제 글 작성을 시작해보세요!
