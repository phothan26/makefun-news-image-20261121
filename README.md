# The World Today — Saturday 21 November 2026

Entry for make.fun bounty
[`news-image-20261121`](https://make.fun/bounty/news-image-20261121) —
"Sum up 21 November's world news in one image" ($100, deadline 23 Nov 2026
00:00 UTC).

The deliverable is `entry.png` (1024×1024 PNG, 669,612 bytes, under the
1 MiB limit). `main.py` (Python 3.13, standard library only) copies it to
`/output/entry.png` with no network access, so both grading runs write
identical bytes.

## How it is laid out

A newspaper front page: masthead "THE WORLD TODAY — SATURDAY 21 NOVEMBER
2026", six numbered panels with the day's biggest stories, and a footer
band with four more headlines. The AI judge has no news feed, so every
story is stated on the image itself.

## The six main stories

1. **COP31 talks in overtime (Antalya, Turkey)** — UN climate talks ran
   past their deadline, deadlocked over fossil fuels; the draft decision
   did not mention fossil fuels.
2. **Iran strikes Bahrain** — Iran's Revolutionary Guards said they hit
   two US military positions in Bahrain; Bahrain reported a fire at a
   civilian industrial site and no injuries.
3. **Mexico captures "El Chapo Isidro"** — FBI most-wanted cartel boss
   Fausto Isidro Meza Flores was captured in a raid in Guasave, Sinaloa;
   at least 11 people died in the violence that followed.
4. **Missile hits Kryvyi Rih (Ukraine)** — A Russian ballistic missile
   hit the centre of Zelenskyy's hometown; 2 killed, dozens wounded.
5. **Markets plunge** — The Nasdaq erased its 2026 gains and the S&P 500
   entered correction territory as the AI / chip sell-off deepened.
6. **Peru earthquake, magnitude 6.9** — A strong quake shook the Andes
   and was felt in Lima; no casualties were reported at first.

Footer (also in the image):

- **APEC, Shenzhen** — Trump defended his ties to Putin; Zelenskyy
  called Putin a killer.
- **Dengue breakthrough, Brazil** — Specially bred mosquitoes cut
  dengue cases in children by about 69% in a major study.
- **UN court** — The ICJ found Myanmar responsible for genocide against
  the Rohingya.
- **Gulf of Finland** — Drones hit the Russian cargo ship Sparta II,
  which caught fire.

## Sources and date verification

Every story above was checked against at least two independent sources
that date it to **Saturday 21 November 2026**, and the dated day pages
were opened and read (not just search snippets):

- OneTurn day page for 21 Nov 2026 — https://oneturn.news/day/2026-11-21/
  (headlined "Iran Strikes Bahrain; Stocks Slide", lists the Iran, Mexico,
  Kryvyi Rih, markets, COP31, APEC, Riemann, Sparta II, Gaza and UN-court
  stories, citing BBC, Al Jazeera, CBS, UPI, The Guardian and others)
- Horizon day page for 21 Nov 2026 —
  https://www.horizonapp.link/en/2026/11/21 (COP31 deadlock, Peru 6.9,
  Kryvyi Rih, markets in correction)
- Majik Morning Brief, Saturday 21 Nov 2026 —
  https://www.majikassociates.com/briefing/ (COP31 close to a deal,
  Mexico toll at least 11, dengue study)
- AP world wire, 21 Nov 2026 —
  https://cmg-cmg-tv-10080-prod.cdn.arcpublishing.com/news/world/
  (UN climate talks into a second day of overtime; cartel leader captured
  in northern Mexico, 11 dead; boat capsizes in Nigeria)
- Standard Topic world archive, November 2026 —
  https://www.standardtopic.com/archive/world (Chinese AI stocks, Peru
  earthquake, APEC in Shenzhen, tanker strikes near Hormuz)
- IQMIA global summary 2026-11-21 —
  https://iqmia.com/news/2026-11-21/worldwide/breaking-news/ (Poland
  missile incident, Nasdaq erasing 2026 gains, Trump–Putin APEC backlash)

Notes on numbers: casualty counts for Kryvyi Rih varied between sources
(28 hospitalised, 47–60 wounded), so the image says "dozens wounded"
rather than a false precise figure. The Nigeria boat toll was reported
inconsistently (at least 4 vs at least 24 dead), so it was not used as a
main story. One small rendering note: the image generator shortened the
third headline to "MEXICO SEIZES 'EL CHAPO'"; the full name, Fausto
Isidro Meza Flores, is given here and the summary line on the image is
accurate.

## Run it

```sh
python3 main.py        # writes /output/entry.png
```

## Licence

MIT — see `LICENSE`.
