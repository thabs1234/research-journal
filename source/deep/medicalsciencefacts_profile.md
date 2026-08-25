# @medicalsciencefacts — Creator Intelligence Profile

> Researched 2026-08-25. TikTok web gateway was bot-blocked, so initial build
> used terminal DuckDuckGo HTML + TikTok oEmbed. Real engagement metrics were then
> pulled LIVE from the user's logged-in TikTok tab via cua (computer_use AX-tree),
> since the Gecho Bridge MCP wasn't loaded into the session. Metrics below are
> REAL (32 videos captured from the profile grid, with per-video like counts).

## Who they are
- **Handle:** `@medicalsciencefacts`
- **Display name:** Scientific Facts
- **Niche:** General human-body & health-science education — documentary-style
  explainer shorts. (Note: NOT the "how medicines/drugs work" niche — that is a
  *different* creator who happens to share a near-identical name; see Caveats.)
- **Language:** English
- **Primary platform:** TikTok (vertical short-form). No confirmed YouTube/IG
  mirror — captions say "Follow for more…" and funnel to TikTok follows only.

## Content pillars (REAL data — 32 videos, per-video likes captured from live profile)

| Pillar | Example topics | Videos | Total likes (captured) | Note |
|---|---|---|---|---|
| **Hernia / abdominal** | "what really happens when a hernia forms?", inguinal hernia, repair surgery, emergency | 5 | **623,553** | 🔥 VIRAL ENGINE — one video = 574.1K |
| **Cancer explainers** | breast (formation/diagnosis/signs), cervical, blood/leukemia, melanoma | 6 | **288,680** | Strong, esp. breast diagnosis (213K) |
| **Reproductive** | pregnancy, lactation, sperm, fibroids, menstrual cycle, fertilization | ~9 | **36,437** | ⚠️ UNDERPERFORMS — pregnancy/milk 1.3K each |
| **Brain/Neuro + Mental health** | migraine, panic attack | 2 | 36,739 | Panic 5.2K, migraine 31.5K |
| **Kidney/Urinary** | dialysis, kidney stone, BPH | 3 | 9,527 | Mid-low |
| **Heart/Circulatory** | hypertension, heart bypass | 2 | 2,876 | Weak (bypass 1.4K) |
| **Digestive** | swallow coin, hemorrhoids | 2 | 4,574 | Low |
| **Bones/Spine** | herniated disc, sciatica | 2 | 3,923 | Low |
| **Metabolic** | obesity | 1 | 860 | Lowest |

**Data-driven insight:** the audience rewards **specific condition explainers with
a "what really happens" / surgery-inside hook** — hernia and cancer dominate.
**Reproductive/general-body facts underperform** despite high posting volume.
Avg likes/video (captured 32) = ~31,300; median is far lower (the 574K hernia
is a massive outlier skewing the mean).

Top 5 by likes:
1. What really happens when a hernia forms? — **574.1K**
2. Breast cancer diagnosis (mammogram→biopsy) — **213K**
3. Understanding blood cancer / leukemia — **37.7K**
4. Brain during a migraine — **31.5K**
5. Breast cancer (formation→treatment) — **25K**

Recurring framing: "Understanding X — how it develops", "What really happens
when you…?", "A journey through the human body."

## Hook & format formula
1. **Curiosity gap title** + emoji (😮 🧠 🩺 🔬 🎀).
2. **Documentary/explainer voice** — calm, educational, "ScienceExplained".
3. **Awareness angle** on sensitive topics (cancer screening, safe medicine use).
4. **CTA:** "Follow for more amazing body facts!" + consistent hashtag block.

## Hashtag strategy
- **Always-on core cluster:** `#HumanBody #ScienceExplained #HealthEducation
  #MedicalFacts #BodyFacts #ScienceFacts`
- **Topic tags layered on:** `#BreastCancerAwareness #WomensHealth #MensHealth
  #CancerAwareness #HPVAwareness #KidneyHealth #PregnancyJourney` etc.
- Heavy use of `#foryou #facts #science #viral #shorts` for reach.

## Engagement snapshot (REAL, captured 2026-08-25 from live profile)
- **Videos captured:** 32 (first grid page — full account likely larger).
- **Per-video likes captured:** 860 → 574,100. Sum of captured likes ≈ 1,002,293.
- **Avg likes/video (captured):** ~31,300 (mean skewed by the 574K hernia outlier;
  median is much lower, ~2–4K).
- **Top performer:** "What really happens when a hernia forms?" = **574.1K likes**.
- **Follower count / total account likes / play counts: NOT captured** — the stat
  numbers render inside a shadow-DOM container the AX-tree didn't expose as labeled
  text. To get them: restart Hermes (loads Gecho MCP) → `tiktok_influencer`, OR
  scroll the profile header and re-capture. Treat follower count as still UNKNOWN.
- The "Medical Science Facts" YouTube channel (UCM4xWEF8pF2rvm_s10pyPIQ, 23
  followers, 7 Hindi tablet videos) is a **different creator** — name collision.

**Actionable takeaway for the content pack:** lead with hernia + cancer
"what really happens / inside the body" angles (proven viral); de-emphasize
generic reproductive/body facts (pregnancy, milk = ~1.3K, weakest). See revised
calendar weighting in SA_health_content_calendar.md (v2 notes).

## Method transparency (what worked / what didn't)
| Method | Result |
|---|---|
| `web_extract` on tiktok.com | ❌ 0 content (bot-blocked via gateway) |
| Terminal DuckDuckGo HTML (`html.duckduckgo.com/html`) | ✅ Surfaced handle + ~10 video URLs |
| TikTok **oEmbed** (`/oembed?url=…/video/ID`) | ✅ Returned real captions; rate-limited (HTTP 429) after ~8 calls |
| YouTube pivot (`@medicalSciencefacts`) | ⚠️ False match — different (Hindi) creator |
| `yt-dlp` on TikTok | ❌ Slardar WAF ("unable to extract universal data") |
| **cua `computer_use` AX-tree on live logged-in tab** | ✅ **WORKED** — captured 32 videos + real per-video like counts. Follower/stat totals in shadow-DOM (not exposed); needs Gecho MCP or header re-capture |

## Caveats
- Catalog is now **32 videos with REAL like counts** (captured live), not the
  earlier 15–16 oEmbed sample — TikTok blocks full enumeration, so the true
  account size is still unknown (likely larger).
- **Follower count / total account likes / play counts NOT captured** — they render
  in a shadow-DOM container the AX-tree didn't expose as labeled text.
- Captions are the script (short-form); no transcript mining was possible without
  Gecho MCP.
- Engagement rates cannot be computed without play-count data.

## Suggested next steps
1. **Authenticate Gecho Bridge** (Chrome ext + logged-in TikTok) to pull the
   full catalog + real like/play/comment counts → true engagement analysis.
2. **Build a content calendar** mirroring their format for a SA health-education
   brand (SiteCraft client or Come & Buy adjacent).
3. **Transcript mine** top videos once a live session exists, to extract their
   exact hook/body/CTA structure.
4. Save this research + workaround flow as a reusable skill.

---
Files in `C:/Users/Thabang/msf_research/`:
- `channel.json` — the (unrelated) YouTube channel metadata
- `channel_videos.json` — empty (flat-playlist blocked)
- `medicalsciencefacts_profile.md` — this file
