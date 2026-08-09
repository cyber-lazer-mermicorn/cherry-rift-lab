"""
Rift Lab — Platform Integration
=================================
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "mermicorn-client"))

from mermicorn_client import MermicornClient


def get_client() -> MermicornClient:
    return MermicornClient(
        api_url=os.environ.get("MERMICORN_API_URL", "http://localhost:8000"),
        api_key=os.environ.get("MERMICORN_API_KEY", ""),
    )


def sync_champions(champions: list[dict]) -> dict:
    """Sync champion data to central platform."""
    client = get_client()
    results = []
    for c in champions:
        result = client.champions.add(
            name=c["name"], tier=c["tier"], win_rate=c["win_rate"],
        )
        results.append(result)
    return {"synced": len(results), "results": results}
