"""
Rift Skills — Gaming Intelligence
==================================
Specialized skills for Wild Rift analysis.
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).parent.parent.parent / "mermicorn-commerce-ai" / "src"))
from commerce_ai.skills import MermicornSkills


class RiftSkills:
    """
    Specialized Wild Rift skills.
    
    Provides:
    - Champion meta tracking
    - Build optimization
    - Matchup database
    - Performance analytics
    - Patch impact analysis
    """
    
    def __init__(self, storage_dir: str = "./rift_data"):
        self.skills = MermicornSkills(storage_dir)
        self.champions: dict[str, dict] = {}
        self.matchups: dict[str, dict] = {}
        self.games: list[dict] = []
    
    def update_champion(self, name: str, data: dict[str, Any]) -> None:
        """Update champion data."""
        self.champions[name] = data
        self.skills.memory.remember(f"champion:{name}", data, category="champions")
        
        # Track win rate
        if "win_rate" in data:
            self.skills.data.add_point(f"wr:{name}", data["win_rate"])
    
    def get_meta(self) -> dict[str, Any]:
        """Get current meta tier list."""
        tier_list = {"S+": [], "S": [], "A": [], "B": [], "C": [], "D": []}
        
        for name, data in self.champions.items():
            tier = data.get("tier", "C")
            if tier in tier_list:
                tier_list[tier].append({
                    "name": name,
                    "win_rate": data.get("win_rate", 50),
                    "pick_rate": data.get("pick_rate", 0),
                })
        
        # Sort each tier by win rate
        for tier in tier_list:
            tier_list[tier].sort(key=lambda c: c["win_rate"], reverse=True)
        
        return tier_list
    
    def record_game(self, champion: str, result: str, kda: str,
                   items: list[str], notes: str = "") -> dict[str, Any]:
        """Record a game."""
        game = {
            "champion": champion, "result": result, "kda": kda,
            "items": items, "notes": notes, "timestamp": time.time(),
        }
        self.games.append(game)
        
        # Update champion stats
        if champion in self.champions:
            games_on = sum(1 for g in self.games if g["champion"] == champion)
            wins = sum(1 for g in self.games if g["champion"] == champion and g["result"] == "win")
            self.champions[champion]["games_played"] = games_on
            self.champions[champion]["win_rate"] = wins / max(games_on, 1) * 100
        
        return game
    
    def get_champion_stats(self, champion: str) -> dict[str, Any]:
        """Get stats for a champion."""
        games = [g for g in self.games if g["champion"] == champion]
        wins = sum(1 for g in games if g["result"] == "win")
        
        return {
            "champion": champion,
            "games_played": len(games),
            "wins": wins,
            "losses": len(games) - wins,
            "win_rate": wins / max(len(games), 1) * 100,
            "recent_games": games[-5:],
            "meta_data": self.champions.get(champion, {}),
        }
    
    def record_matchup(self, champion: str, opponent: str, result: str,
                      lane: str = "mid") -> None:
        """Record a matchup result."""
        key = f"{champion}:{opponent}"
        if key not in self.matchups:
            self.matchups[key] = {"wins": 0, "losses": 0, "games": []}
        
        self.matchups[key]["games"].append({"result": result, "lane": lane, "timestamp": time.time()})
        if result == "win":
            self.matchups[key]["wins"] += 1
        else:
            self.matchups[key]["losses"] += 1
    
    def get_matchup_stats(self, champion: str, opponent: str) -> dict[str, Any]:
        """Get matchup stats."""
        key = f"{champion}:{opponent}"
        data = self.matchups.get(key, {"wins": 0, "losses": 0, "games": []})
        total = data["wins"] + data["losses"]
        
        return {
            "champion": champion,
            "opponent": opponent,
            "games": total,
            "wins": data["wins"],
            "losses": data["losses"],
            "win_rate": data["wins"] / max(total, 1) * 100,
        }
    
    def get_stats(self) -> dict[str, Any]:
        return {
            "skills": self.skills.get_stats(),
            "champions_tracked": len(self.champions),
            "matchups_recorded": len(self.matchups),
            "games_recorded": len(self.games),
        }
