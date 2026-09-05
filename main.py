"""
観葉植物データベースAPI。

data.py の静的データを名称・水やり頻度・日照条件で検索する。
外部サイトへの問い合わせは行わない(内部データのみ)。
"""

from typing import Optional

from fastapi import FastAPI, Query

from data import PLANTS

app = FastAPI(
    title="House Plants API",
    description="観葉植物の学名・水やり頻度・日照条件を検索します。",
    version="1.0.0",
)


@app.get("/")
def root():
    return {"status": "ok", "service": "house-plants"}


@app.get("/health")
@app.head("/health")
def health():
    return {"status": "ok"}


@app.get("/plants")
def list_plants(
    query: Optional[str] = Query(None, description="通称名・学名の部分一致検索"),
    light: Optional[str] = Query(None, description="日照条件での部分一致絞り込み"),
):
    results = PLANTS
    if query:
        q = query.lower()
        results = [
            p for p in results
            if q in p["common_name"].lower() or q in p["scientific_name"].lower()
        ]
    if light:
        l = light.lower()
        results = [p for p in results if l in p["light"].lower()]
    return {"count": len(results), "results": results}


@app.get("/plants/{common_name}")
def get_plant(common_name: str):
    for p in PLANTS:
        if p["common_name"].lower() == common_name.lower():
            return p
    return {"error": "not found", "common_name": common_name}
