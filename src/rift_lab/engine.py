"""Cherry Rift Lab — Wild Rift Champion & Patch Tracker."""

from __future__ import annotations
import json, time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass(slots=True)
class Champion:
    name: str
    lane: str
    tier: str
    win_rate: float
    patch: str = ""
    build: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {"name": self.name, "lane": self.lane, "tier": self.tier,
                "win_rate": self.win_rate, "patch": self.patch, "build": self.build}


class RiftEngine:
    def __init__(self, output_dir: str = "./output"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.champions: list[Champion] = []

    def add_champion(self, name: str, lane: str, tier: str, win_rate: float, **kw) -> Champion:
        c = Champion(name=name, lane=lane, tier=tier, win_rate=win_rate, **kw)
        self.champions.append(c)
        return c

    def top_tier(self) -> list[Champion]:
        return sorted([c for c in self.champions if c.tier in ("S+", "S", "A")], key=lambda c: c.win_rate, reverse=True)

    def export(self) -> str:
        path = self.output_dir / "champions.json"
        path.write_text(json.dumps([c.to_dict() for c in self.champions], indent=2))
        return str(path)
