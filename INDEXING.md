# 색인(인덱싱) 가이드 — 네이버·구글·빙 빠른 등록

도메인: **https://bucheon-massage-88.pages.dev/**

빌드(`python3 build.py`) 시 자동 생성되는 색인 자산:

| 파일 | 용도 |
|------|------|
| `sitemap.xml` | 색인 페이지 46개 (lastmod·changefreq·priority 포함) |
| `feed.xml` | RSS 2.0 피드 (네이버 RSS 제출용) |
| `robots.txt` | 크롤 허용 + 사이트맵 위치 |
| `e9b782a229a61379a7c0a9b2ee1604c5.txt` | IndexNow 키 파일 (사이트 루트) |
| `urls.txt` | 색인 통보 스크립트가 읽는 전체 URL 목록 |
| 메인 `<head>` | 네이버 사이트 인증 메타 태그 |

---

## 1. 네이버 서치어드바이저 (가장 중요)

1. https://searchadvisor.naver.com → **웹마스터 도구**에 사이트 등록
   `https://bucheon-massage-88.pages.dev/`
2. **소유확인**: 「HTML 태그」 방식 선택 → 메인 페이지에 이미 아래 태그가 들어 있습니다.
   ```html
   <meta name="naver-site-verification" content="d72b9347bb45636527b3fc7a291a8c7fe69e5925" />
   ```
   → 배포 확인 후 "소유확인" 버튼만 누르면 됩니다.
3. **요청 → 사이트맵 제출**: `sitemap.xml`
4. **요청 → RSS 제출**: `feed.xml`
5. **검증 → robots.txt** 확인 후, 주요 페이지는 **웹페이지 수집** 요청으로 직접 등록.

## 2. 구글 서치 콘솔

1. https://search.google.com/search-console 에서 **URL 접두어** 속성으로
   `https://bucheon-massage-88.pages.dev/` 추가.
2. 소유확인: 「HTML 태그」 방식의 `google-site-verification` 메타를 받으면
   `content/main.py` 의 `_JSONLD` 상단(네이버 태그 옆)에 한 줄 추가 후 `python3 build.py` →
   재배포 → 확인.
3. **Sitemaps** 메뉴에 `sitemap.xml` 제출.
4. 급한 페이지는 상단 **URL 검사 → 색인 생성 요청**.

## 3. IndexNow (빙·네이버 즉시 통보) — 키 설정 완료

- 키: `e9b782a229a61379a7c0a9b2ee1604c5`
- 키 파일이 사이트 루트(`/e9b782a229a61379a7c0a9b2ee1604c5.txt`)에 배포됩니다.
- **배포가 끝난 뒤** 아래를 실행하면 한 번에 빙·네이버 등 IndexNow 참여 엔진에 통보됩니다.
  ```bash
  python3 build.py                      # urls.txt 갱신
  python3 tools/indexnow_submit.py      # 전체 URL 통보
  python3 tools/indexnow_submit.py https://bucheon-massage-88.pages.dev/bucheon/wonmi/jung-dong-chuljangmassage/  # 특정 URL만
  ```
- 응답 200/202 = 정상 접수. 403 = 키 파일 미배포(배포 후 재시도).

## 4. 구글 Indexing API (선택 — 구글은 IndexNow 미참여)

구글 Indexing API는 공식적으로 채용공고/방송 일정 페이지용이며 일반 페이지는 보장되지
않습니다. 그래도 빠른 통보 수단으로 쓰려면:

1. Google Cloud 프로젝트에서 **Indexing API** 사용 설정
2. **서비스 계정** 생성 → JSON 키 발급
3. 서치 콘솔 속성에 그 서비스 계정 이메일을 **소유자**로 추가
4. 실행:
   ```bash
   pip install google-auth
   export GOOGLE_APPLICATION_CREDENTIALS=/path/service-account.json
   python3 tools/google_indexing.py
   ```

## 5. 자동화 — 글 올릴 때마다 즉시 통보

`.github/workflows/indexing.yml` 이 **main 브랜치 push** 시(또는 수동 실행 시):
`build.py` 실행 → 배포 대기(90초) → IndexNow 통보 → (Secret `GCP_SA_KEY` 가 있으면)
구글 Indexing API 통보를 자동 수행합니다.

- 구글 Indexing API 자동화를 켜려면 리포지토리
  **Settings → Secrets → Actions** 에 `GCP_SA_KEY`(서비스 계정 JSON 전체)를 등록하세요.
- Cloudflare Pages 배포 시간이 90초보다 길면 워크플로의 `sleep` 값을 늘리세요.

## 참고

- 구글·빙의 옛 `sitemap ping` GET 엔드포인트는 2023년에 폐지되었습니다. 그래서 구글은
  **서치 콘솔 사이트맵 제출**, 빙·네이버는 **IndexNow** 를 기본 통보 수단으로 사용합니다.
- 색인 키나 도메인이 바뀌면 `content/site.py` 의 `BASE_URL` / `INDEXNOW_KEY` 만 고치고
  다시 빌드하면 전체 자산에 반영됩니다.
