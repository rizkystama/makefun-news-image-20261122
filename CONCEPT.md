# news-image-20261122 — Concept

**Concept A: editorial broadsheet** (ChatGPT concept review 22 Nov 18:01 WIB:
A wins; 5 conditions: date prominent, event recognition, regional breadth,
factual integrity, 300px legibility test). Rizky 18:02 picked the dense
32–33 story version. Top-8 leaderboard entries studied before building
(ranks 1, 2, 5, 8 read in full): all use masthead + number strip + region
bar + UTC timeline + 3 illustrated leads + small cards + map + ALSO list +
DATE CHECK box. This entry follows that proven structure with its own
verified story set.

**Stories: 32 image items** from 30 verified research stories + 3 new
parent-supplementary stories (S1 Bahrain claim, S3 Sparta II, S4
Wembanyama; S2 barrage figures frame story A4, not a separate item),
minus 2 dropped (A13 Bessent partisan item, A24 Hazlewood minor item),
with A2 (COP31 plenary) folded into lead 1, and 2 splits (COP31 → lead +
finance item; India Test → card + centuries item).
Regions: Asia-Pacific 12 · Middle East 7 · Americas 5 · Global 4 ·
Europe 3 · Africa 1.

**Leads:** 1 COP31 final text (ADOPTION PENDING — text released, plenary
delayed, adoption not confirmed as of ~11:00 UTC); 2 Bahrain radar claim
vs denial (CLAIM — IRGC claim Sat night, Bahrain answer + wide reporting
Sunday); 3 Russia fires 186 drones, Kyiv-region block destroyed (161
downed/suppressed, Ukrainian Air Force).

**Honesty devices:** DATE CHECK box (left-out other-days news, included
Sunday items, not-yet-decided: COP31 adoption, ATP final, Liverpool v
Man Utd); certainty tags REPORTED / CLAIM / ADOPTION PENDING with footer
legend; "Sources read to ~11:00 UTC" line.

**Build:** render.py (deterministic PIL, no randomness/time) → entry.png
1024x1024, 182,265 bytes. main.ts copies the pinned render after sha256
verification. v2 fixed card caption spacing (both caption lines fit).
300px thumbnail checked: masthead + number strip + lead headlines remain
distinguishable; small text unreadable at 300px (same as leaders).
