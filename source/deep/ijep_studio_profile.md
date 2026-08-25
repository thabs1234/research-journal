# iJEP Studio — Creator Research Pack

> Researched 2026-08-25. Handle requested: `@ijep.studio` (TikTok).
> **Method note:** TikTok's web/API gateway blocked this host with a Slardar WAF
> bot-challenge (web, m.tiktok.com, oEmbed, and the post-list API all refused
> without a logged-in session). The **tiktokv.com mirror** served a real static
> profile payload, and the **YouTube channel** (`@ijepstudio`) confirmed the niche.
> Per-video TikTok like counts were NOT retrievable (no live logged-in TikTok tab
> was open in Chrome, and the Gecho Bridge MCP is registered but not loaded into
> this session — requires a Hermes restart we can't trigger mid-session).

## 1. Who / Niche
| Field | Value |
|---|---|
| Display name | **iJEP Studio** |
| TikTok handle | `@ijep.studio` |
| Bio (verbatim) | "PhD Biochemistry Structural Biology Animations" |
| Website | https://www.ijepstudio.com |
| Business email | contact@ijepstudio.com |
| Location | Boston, MA, United States |
| Business | Professional structural-biology animation services — research, education, scientific communication |
| Content type | 3D molecular / structural-biology animation explainers (cinematic, no face) |

## 2. Audience & Funnel
- **Primary platform:** TikTok (top-of-funnel, discovery)
- **Mirror:** YouTube `@ijepstudio` — ~1,630 subs, 7 long-form videos (same molecular-machinery niche)
- **Conversion:** TikTok/YouTube → `ijepstudio.com` contact form → paid animation services (B2B: labs, universities, journals, pharma comms)

## 3. Verified Metrics (cross-platform)
| Metric | Source | Value |
|---|---|---|
| TikTok followers | tiktokv static payload | **31.4K** (header said 31K) |
| TikTok total likes | tiktokv (`heartCount`) | **429.4K** |
| TikTok video count | tiktokv | **98** |
| Following | tiktokv | 0 (pure broadcaster) |
| YouTube subs | yt-dlp | ~1,630 |
| YouTube videos | yt-dlp (flat) | 7 |
| **Per-video TikTok likes** | — | **UNKNOWN** (WAF + no live tab) |

> Likes/follower ratio is exceptional (~13.7 likes per follower lifetime) — signature of
> high-share, "wow" educational content rather than personality-driven following. Treat
> as a reach signal, not a full engagement rate.

## 4. Content Pillars (inferred from the 7 YouTube titles + bio)
1. **Molecular Machines** — ATP synthase, bacterial flagellar motor, ribosome, spliceosome, CRISPR-Cas9, DNA helicase, photosystem II. The signature pillar.
2. **Infectious Disease / Virology** — HIV entry, SARS-CoV-2 spike, influenza neuraminidase, Zika, TB, E. coli fimbriae.
3. **Immune System** — inflammasome, T-cell activation, complement cascade, antibody generation, macrophage engulfment, cytokine storm.
4. **Biophysics / Mechanism** — hydrogen bonds, protein folding, electrostatic forces, entropy, lipid-bilayer self-assembly, molecular docking.
5. **Journey / Process POV** — "A Water's Journey into HIV", "Oxygen's Ride on Hemoglobin", "A Glucose Molecule's Journey", "A Virus's Journey to the Nucleus". Narrative first-person framing of a molecule's path.

## 5. Format & Hook Formula (from titles + niche)
- **Cinematic 3D animation**, no talking head, no voiceover needed (visual-first).
- **Title pattern:** `[Molecule/Machine] | [Optional punchy subtitle]`
  - e.g. "ATP synthase", "bacteria flagellar motor - The Most Powerful Molecular Motor Ever Discovered 🔬⚙️"
- **Hook levers observed:** superlative ("Most Powerful… Ever Discovered"), mystery ("Inside Salmonella's Injectisome | Molecular Machinery Explained"), scale awe.
- **Caption style:** short, keyword-dense, emoji-light (🔬⚙️). Likely uses #biology #chemistry #science #structuralbiology #biochemistry #molecularbiology #sciencetok.

## 6. Hashtag Strategy (recommended cluster — NOT scraped, best-practice for this niche)
Always-on base: `#structuralbiology #biochemistry #molecularbiology #science #sciencetok #biology #chemistry #animation`
Pillar modifiers:
- Machines → `#atpsynthase #molecularmachine #nanotech`
- Infectious → `#virology #covid #hiv #microbiology`
- Immune → `#immunology #immunesystem #inflammasome`
- Biophysics → `#physics #chemistry #protein`

## 7. Why This Works (positioning takeaway)
iJEP wins by making **invisible molecular scale cinematic and beautiful** — the "wow"
factor drives shares, and the B2B website converts the credibility into paid animation
gigs. It is a *studio brand*, not a persona: 0 following, pure broadcast. The model to
clone is **"stunning 3D science, no face, strong title, consistent pillar rotation."**

## 8. Method Transparency & Caveats
- ✅ Profile + bio + follower/like counts: **verified** from tiktokv.com static payload.
- ✅ Niche + pillars: **verified** from 7 YouTube titles (yt-dlp, no WAF).
- ⚠️ Per-video performance, posting cadence, exact captions: **NOT available** — TikTok
  WAF blocked all API/list endpoints from this host; no logged-in TikTok tab was open.
- ⚠️ Hashtags above are **best-practice recommendations**, not scraped from the creator.
- 🔄 To get per-video like counts: open the creator's TikTok profile in a **logged-in
  Chrome tab** and ask Hermes to capture the AX tree (Stage 3.5 of the
  `tiktok-creator-research-blocked` skill), OR restart Hermes to load the Gecho Bridge
  MCP and run `tiktok_influencer`.
