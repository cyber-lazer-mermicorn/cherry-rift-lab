"""
Rift Vision — See Screenshots, Analyze Gameplay
================================================
Screenshot-based game analysis.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).parent.parent.parent / "mermicorn-commerce-ai" / "src"))
from commerce_ai.vision import MermicornVision, VisionResult


class RiftVision:
    """
    Vision-powered gaming analysis.
    
    See a screenshot → Analyze gameplay → Provide coaching
    """
    
    def __init__(self, api_key: str | None = None):
        self.vision = MermicornVision(api_key=api_key)
    
    def analyze_screenshot(self, image_path: str) -> VisionResult:
        """Analyze a Wild Rift screenshot."""
        prompt = """Analyze this Wild Rift gameplay screenshot.

Identify:
- Champions visible (both teams)
- Game state (early/mid/late)
- Score and timer
- Items visible
- Map position
- Team fight or laning

Provide JSON with:
- champions_visible: {allies: [], enemies: []}
- game_state: {phase, score, timer}
- items_visible: list
- map_position: location on map
- situation: what's happening
- tactical_analysis: assessment
- improvement_tips: list
- confidence: 0-1"""
        
        return self.vision.analyze_image(image_path, task="identify")
    
    def analyze_build_screenshot(self, image_path: str) -> VisionResult:
        """Analyze a build screen screenshot."""
        prompt = """Analyze this Wild Rift build/item screen.

Identify:
- Champion being built
- Items purchased
- Gold spent
- Build order
- Rune choices

Provide JSON with:
- champion: name
- items: list of items
- total_gold: amount spent
- build_quality: assessment
- optimization_suggestions: list
- alternative_builds: list
- confidence: 0-1"""
        
        return self.vision.analyze_image(image_path, task="identify")
    
    def get_stats(self) -> dict[str, Any]:
        return {"vision_stats": self.vision.get_stats()}
