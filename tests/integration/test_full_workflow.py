"""
Full Stack Workflow Test — Cherry Rift Lab
==========================================
Analyze → Build → Play → Record → Improve
"""

import sys
import json
from pathlib import Path

sys.path.insert(0, "src")
sys.path.insert(0, "../mermicorn-commerce-ai/src")
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "mermicorn-commerce-ai" / "src"))

from rift_lab.engine import RiftEngine
from rift_lab.ai_coach import RiftAI
from rift_lab.skills_meta import RiftSkills


def test_full_workflow():
    """Test complete rift workflow: Analyze → Build → Play → Record → Improve."""
    print("⚔️ RIFT LAB FULL WORKFLOW TEST")
    print("=" * 50)
    
    # ═══════════════════════════════════════════════════════════
    # STEP 1: Analyze Champion (AI)
    # ═══════════════════════════════════════════════════════════
    print("\n📌 STEP 1: Analyze Champion")
    ai = RiftAI()
    result = ai.analyze_champion("Ahri", "mid")
    
    assert result.success, f"Analysis failed: {result.reasoning}"
    print(f"   ✅ Champion: {result.data}")
    print(f"   ✅ Confidence: {result.confidence}")
    
    # ═══════════════════════════════════════════════════════════
    # STEP 2: Recommend Build (AI)
    # ═══════════════════════════════════════════════════════════
    print("\n📌 STEP 2: Recommend Build")
    build = ai.recommend_build("Ahri", "vs Zed")
    
    assert build.success, f"Build failed: {build.reasoning}"
    print(f"   ✅ Build: {build.data}")
    
    # ═══════════════════════════════════════════════════════════
    # STEP 3: Analyze Matchup (AI)
    # ═══════════════════════════════════════════════════════════
    print("\n📌 STEP 3: Analyze Matchup")
    matchup = ai.analyze_matchup("Ahri", "Zed", "mid")
    
    assert matchup.success, f"Matchup failed: {matchup.reasoning}"
    print(f"   ✅ Matchup: {matchup.data}")
    
    # ═══════════════════════════════════════════════════════════
    # STEP 4: Analyze Meta (AI)
    # ═══════════════════════════════════════════════════════════
    print("\n📌 STEP 4: Analyze Meta")
    meta = ai.analyze_meta("current")
    
    assert meta.success, f"Meta failed: {meta.reasoning}"
    print(f"   ✅ Meta: {meta.data}")
    
    # ═══════════════════════════════════════════════════════════
    # STEP 5: Update Champion (Skills)
    # ═══════════════════════════════════════════════════════════
    print("\n📌 STEP 5: Update Champion")
    skills = RiftSkills()
    skills.update_champion("Ahri", {"tier": "S+", "win_rate": 54.2, "pick_rate": 15.3})
    skills.update_champion("Zed", {"tier": "S", "win_rate": 52.1, "pick_rate": 12.8})
    skills.update_champion("Yasuo", {"tier": "A", "win_rate": 50.5, "pick_rate": 8.2})
    
    meta_list = skills.get_meta()
    print(f"   ✅ S+: {[c['name'] for c in meta_list.get('S+', [])]}")
    print(f"   ✅ S: {[c['name'] for c in meta_list.get('S', [])]}")
    print(f"   ✅ A: {[c['name'] for c in meta_list.get('A', [])]}")
    
    # ═══════════════════════════════════════════════════════════
    # STEP 6: Record Game
    # ═══════════════════════════════════════════════════════════
    print("\n📌 STEP 6: Record Game")
    game1 = skills.record_game("Ahri", "win", "8/2/5", ["Luden", "Shadowflame", "Rabadon"], "Great rotations")
    game2 = skills.record_game("Ahri", "win", "6/1/8", ["Luden", "Horizon Focus", "Void"], "Early kills")
    game3 = skills.record_game("Ahri", "loss", "3/4/4", ["Luden", "Shadowflame"], "Fell behind early")
    
    stats = skills.get_champion_stats("Ahri")
    print(f"   ✅ Ahri: {stats['wins']}W-{stats['losses']}L ({stats['win_rate']:.0f}%)")
    
    # ═══════════════════════════════════════════════════════════
    # STEP 7: Record Matchups
    # ═══════════════════════════════════════════════════════════
    print("\n📌 STEP 7: Record Matchups")
    skills.record_matchup("Ahri", "Zed", "win", "mid")
    skills.record_matchup("Ahri", "Zed", "win", "mid")
    skills.record_matchup("Ahri", "Zed", "loss", "mid")
    
    matchup_stats = skills.get_matchup_stats("Ahri", "Zed")
    print(f"   ✅ Ahri vs Zed: {matchup_stats['wins']}W-{matchup_stats['losses']}L ({matchup_stats['win_rate']:.0f}%)")
    
    # ═══════════════════════════════════════════════════════════
    # STEP 8: Add to Engine
    # ═══════════════════════════════════════════════════════════
    print("\n📌 STEP 8: Add to Engine")
    engine = RiftEngine()
    engine.add_champion("Ahri", "Mid", "S+", 54.2, patch="5.2")
    engine.add_champion("Zed", "Mid", "S", 52.1, patch="5.2")
    engine.add_champion("Yasuo", "Mid/Baron", "A", 50.5, patch="5.2")
    engine.add_champion("Jinx", "ADC", "A", 51.8, patch="5.2")
    
    top = engine.top_tier()
    print(f"   ✅ Top tier: {[c.name for c in top]}")
    
    # ═══════════════════════════════════════════════════════════
    # STEP 9: Coaching (AI)
    # ═══════════════════════════════════════════════════════════
    print("\n📌 STEP 9: Coaching")
    player_data = {
        "rank": "Platinum II",
        "main": "Ahri",
        "win_rate": 55,
        "games_played": 200,
        "kda": 3.2,
    }
    coaching = ai.coach_improvement(player_data)
    
    assert coaching.success, f"Coaching failed: {coaching.reasoning}"
    print(f"   ✅ Coaching: {coaching.data}")
    
    # ═══════════════════════════════════════════════════════════
    # SUMMARY
    # ═══════════════════════════════════════════════════════════
    print("\n" + "=" * 50)
    print("✅ FULL WORKFLOW COMPLETE")
    print(f"   Champions tracked: {len(skills.champions)}")
    print(f"   Games recorded: {len(skills.games)}")
    print(f"   Matchups: {len(skills.matchups)}")
    print(f"   Ahri stats: {stats['wins']}W-{stats['losses']}L")
    print(f"   Ahri vs Zed: {matchup_stats['win_rate']:.0f}%")
    print("=" * 50)
    
    return True


if __name__ == "__main__":
    success = test_full_workflow()
    sys.exit(0 if success else 1)
