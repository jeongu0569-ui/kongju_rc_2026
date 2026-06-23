# 자율주행 자동차 - 기초 수업 사이트

이 저장소는 강의 계획과 예제 파일(`python/`)을 모아둔 간단한 정적 사이트입니다.

빠른 시작

- 로컬에서 확인:

```bash
git clone <your-repo-url>
cd <repo-folder>
# 브라우저로 index.html을 열거나 간단 서버 사용
python3 -m http.server 8000
# 브라우저에서 http://localhost:8000 접속
```

- GitHub Pages 자동 배포
  - `main` 브랜치에 푸시하면 `.github/workflows/pages.yml`에 의해 자동으로 배포됩니다.
  - 저장소 Settings > Pages에서 배포 상태 확인 가능

Slide 링크/자료 추가

- `index.html`의 Slides 부분에 Google Slides URL을 넣어주세요.

RC 폴더

- 향후 RC 폴더에서 실습을 진행하실 경우, `RC/` 폴더를 생성하고 커밋하면 됩니다. 예시:

```bash
mkdir RC
echo "RC 작업 폴더" > RC/README.md
git add RC/README.md
git commit -m "Add RC placeholder"
git push
```

문의나 요청사항 있으면 알려주세요.
