# news-image-20261122 — Concept

**Concept A: editorial broadsheet** (ChatGPT concept review 22 Nov 18:01 WIB:
A wins; 5 conditions: date prominent, event recognition, regional breadth,
factual integrity, 300px legibility test). Rizky 18:02 picked the dense
32–33 story version. Top-8 leaderboard entries studied before building
(ranks 1, 2, 5, 8 read in full): all use masthead + number strip + region
bar + UTC timeline + 3 illustrated leads + small cards + map + ALSO list +
DATE CHECK box. This entry follows that proven structure with its own
verified story set.

**Stories: 30 image items** from 30 verified research stories + 3 new
parent-supplementary stories (S1 Bahrain claim, S3 Sparta II, S4
Wembanyama; S2 barrage figures frame story A4, not a separate item),
minus 2 dropped (A13 Bessent partisan item, A24 Hazlewood minor item),
with A2 (COP31 plenary) folded into lead 1, minus 2 duplicates removed
on ChatGPT final-review advice (COP31 finance detail, Pant/Rahul
centuries — both already in their lead/card), plus 1 split
(Bedard shoulder surgery / MacKinnon out 12 weeks as separate items),
minus 1 removed on ChatGPT confirmation advice (Nigeria boat toll —
the toll was announced Saturday, not a Sunday item; Africa now has no
story, so the edition covers 5 regions).
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
1024x1024, 183,214 bytes (v4). main.ts copies the pinned render after
sha256 verification. v2 fixed card caption spacing (both caption lines
fit). v3 applied all ChatGPT final-review fixes (see main.ts header):
Bahrain attribution, COP31 wording, Kyiv wording, 06:00 UTC drone tally,
defensible top-band/footer claims, dedup, Saturday-event labelling,
verified-only timeline (the unverified "03:00 objections close" and
"08:05 Sparta II" items were removed; "02:30 S. Korea minister resigns"
added from verified 11:30 KST). Card headlines enlarged 10→11px.
v4 applied the ChatGPT confirmation-round fixes: Nigeria removed,
Bahrain date-check wording, Wadkute Sunday-reports wording, Sparta II
caption polish. 300px thumbnail checked: masthead + number strip + lead
headlines remain distinguishable; small text unreadable at 300px (same
as leaders).

**v5 (23 Nov, autonomous revision under the Champion-Mode mandate):**
v4 sat at provisional rank 819/12,860 (12-0 in judge matches, but a
wide true-rank range) — the leaders all had 7 regions and 35–39
stories. ChatGPT's revision review said: go CLEANER, not denser —
32 stories, 7 regions, reject the 42-story plan and the tiny appendix.
v5: 32 stories, 7 regions (Asia-Pacific 9 · Middle East 6 · Americas 6
· Europe 5 · Africa 2 · Oceania 1 · World 3). COP31 lead re-framed on
the Sunday collapse (NO DEAL stamp, empty chairs, cracked globe);
Alcaraz + Merkury cards replace Adnoc + OpenRouter; list grows to 17
(Kenya-DRC, Melbourne, BepiColombo, Skubal, Trump gala, Liverpool,
markets snapshot added; Shukla, Ghostscript, Wadkute, Bedard, MacKinnon
cut). DATE CHECK's 3 undecided items resolved; Bayelsa-29 and the FBI
pause HELD on sourcing caution. Timeline gains the evening events
(ATP final 18:16, COP31 collapse 19:17). Research: RESEARCH-v5.md
(12 accepted, 11 rejected, 3 spot-checks). Render: 194,577 bytes,
sha256 917bc35e…, verified byte-identical across two runs.
