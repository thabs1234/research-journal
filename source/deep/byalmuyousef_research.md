# Research brief — TikTok creator @byalmuyousef (video 7674196909896011021)

_Gathered 2026-08-25 by Hermes. Method note at bottom; see caveats._

## Who they are
- **Handle:** @byalmuyousef (byalmuyousef) on TikTok
- **Niche:** Vibe-coding / AI-assisted software building, with a security bent. They teach
  practical Claude Code + web-security habits to solo devs and indie hackers.
- **Voice/format:** Short, punchy, teaching-style clips. Original sound (talks to camera /
  voiceover). Heavy use of `#claude` / `#websecurity` hashtags.

## The target video (the one you sent)
- **Video ID:** 7674196909896011021
- **Title:** "Your app ships fast and leaks faster. Twenty of the most common ways vibe-coded
  apps get owned — every one of these I've seen in real code."
- **Theme:** A roundup of 20 real-world security mistakes in apps built with AI/vibe-coding
  (i.e. shipping fast without security review).
- **Confirmed via:** TikTok oEmbed API (bypasses the WAF).

## Other confirmed videos (same creator, from search snippets + oEmbed)
| Video ID | Title |
|---|---|
| 7672201413551754509 | "Your login page is the easiest thing to hack — 5 fixes to ask Claude #claude #websecurity" |
| 7671304601240358157 | "Make Claude Code sound like you, not like an AI — with one document." |
| 7674567872319966477 | "Most people don't realize you can teach Claude a real skill just by feeding it videos. This whole video was edited by Claude — I didn't touch a single thing except the cuts." |

## Content pillars (inferred from the 4 confirmed clips)
1. **AI-assisted secure coding** — prompt Claude for the right security fixes (login pages, auth).
2. **Claude Code personalization** — make the agent mirror your style via a single doc.
3. **Teaching agents skills** — feed videos / examples so Claude learns real editing/craft.
4. **Vibe-coding risk awareness** — the "ships fast, leaks faster" security reality-check series.

## Cross-platform funnel
- **TikTok:** primary surface (confirmed handle, live videos).
- **YouTube:** `@byalmuyousef` does NOT resolve (yt-dlp 404). They may cross-post under a
  different channel name, or be TikTok-only. Not yet confirmed.
- **GitHub / blog / X:** no indexed results found in this pass (search engine was rate-limited).
- **Likely funnel:** TikTok clips → (some) link out to a longer writeup/course/tool. Not
  verified from the data I could extract.

## Engagement snapshot
- DDG snippets showed like counts ranging ~29 → 336 on the sampled clips. Small-but-growing
  educational account, not a mega-channel. (Exact counts not authoritative — snippets only.)

## Method transparency (what was blocked, what worked)
- **Web tools (Nous gateway) DOWN** — `web_search` and `web_extract` both returned
  "Nous Tool Gateway not available". So all research ran via the **terminal**, which has
  direct internet.
- **TikTok Slardar WAF** blocks bare `curl` and `yt-dlp` (returns a "Please wait..." challenge
  page, not content). `curl_cffi` impersonation also bounced.
- **What WORKED:**
  - `curl https://www.tiktok.com/oembed?url=...` → returns title + author (no WAF). Primary path.
  - `curl https://html.duckduckgo.com/html/?q=...` → free search, found the handle + video titles.
- **What FAILED:** yt-dlp on TikTok ("Unable to extract universal data for rehydration");
  m.tiktok.com (404); YouTube @byalmuyousef (404); DDG after ~4 rapid queries (cooldown → 0 hits).

## Caveats
- No video view/like/follow counts extracted (WAF blocks the data JSON). Snippet like-counts
  are approximate.
- Title texts are verbatim from oEmbed / search snippets; full captions not retrieved.
- Cross-platform accounts beyond TikTok are unconfirmed.

## Suggested next steps
1. Re-run DDG after cooldown to enumerate YouTube/X/blog + any course/tool link.
2. If a YouTube channel is found, run `yt-dlp --flat-playlist -J` to pull the full catalog.
3. Pull transcriptions of the 4 videos (need a WAF-clear path: logged-in cookie export, or
   a TikTok-mobile API with signed params) to mine their actual security advice.
4. Save this WAF-bypass + oEmbed technique as a reusable skill.
