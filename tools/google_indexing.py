#!/usr/bin/env python3
"""구글 Indexing API — 구글에 URL 변경을 직접 통보한다(구글은 IndexNow 미참여).

주의: 구글 Indexing API는 공식적으로 JobPosting/BroadcastEvent 구조화 데이터 페이지를
대상으로 합니다. 일반 페이지에도 대체로 동작하지만 보장되지는 않으며, 본 사이트의
일상적인 색인은 Search Console 사이트맵 제출이 기본입니다. 빠른 통보 수단으로 함께
사용하세요.

사전 준비:
  1) Google Cloud 프로젝트에서 "Indexing API" 사용 설정
  2) 서비스 계정 생성 후 JSON 키 발급
  3) Search Console 속성에 그 서비스 계정 이메일을 "소유자"로 추가
  4) pip install google-auth

사용법:
    export GOOGLE_APPLICATION_CREDENTIALS=/path/service-account.json
    python3 tools/google_indexing.py                # urls.txt 전체
    python3 tools/google_indexing.py https://.../a/  # 특정 URL만
"""
import json
import os
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from content.site import BASE_URL  # noqa: E402

ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"
SCOPES = ["https://www.googleapis.com/auth/indexing"]
BASE = BASE_URL.rstrip("/")


def get_token() -> str:
    try:
        from google.oauth2 import service_account
        from google.auth.transport.requests import Request
    except ImportError:
        sys.exit("google-auth 가 필요합니다:  pip install google-auth")
    cred_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    if not cred_path or not os.path.exists(cred_path):
        sys.exit("GOOGLE_APPLICATION_CREDENTIALS 에 서비스 계정 JSON 경로를 지정하세요.")
    creds = service_account.Credentials.from_service_account_file(cred_path, scopes=SCOPES)
    creds.refresh(Request())
    return creds.token


def load_urls() -> list:
    args = [a for a in sys.argv[1:] if a.startswith("http")]
    if args:
        return args
    path = os.path.join(ROOT, "urls.txt")
    if not os.path.exists(path):
        sys.exit("urls.txt 가 없습니다. 먼저 `python3 build.py` 를 실행하세요.")
    with open(path, encoding="utf-8") as f:
        return [ln.strip() for ln in f if ln.strip()]


def main() -> None:
    token = get_token()
    urls = load_urls()
    ok = 0
    for url in urls:
        body = json.dumps({"url": url, "type": "URL_UPDATED"}).encode("utf-8")
        req = urllib.request.Request(
            ENDPOINT, data=body, method="POST",
            headers={"Authorization": f"Bearer {token}",
                     "Content-Type": "application/json"},
        )
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                if resp.status == 200:
                    ok += 1
                    print(f"  OK  {url}")
        except urllib.error.HTTPError as e:
            print(f"  ERR {e.code} {url}\n      {e.read().decode('utf-8', 'replace')[:200]}")
    print(f"\n{ok}/{len(urls)} URLs published to Google Indexing API.")


if __name__ == "__main__":
    main()
