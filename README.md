# news-image-20261118-entry

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/bonjoves444-ux/news-image-20261118-entry/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/bonjoves444-ux/news-image-20261118-entry/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

Wednesday 18 November 2026, summed up in one image: a 1024×1024 broadsheet
with 50 verified stories across seven regions. Three heroes lead the page —
Xi greeting Trump on the tarmac in Shenzhen, Kuwait and Bahrain intercepting
Iranian drones over the Gulf, and Voyager 1 reaching one light-day from
Earth. Ten more drawn cards, a UTC timeline of the day, a numbered world
map, and 37 briefs fill out the day, and a date-check box at the foot keeps
Tuesday's news (Nvidia's results, the Alaska Senate call, the Kerch Bridge
collapse) and not-yet-news (Thursday's summit, Friday's landfall) out of
Wednesday's story. Every figure was checked against live reporting before
the image was drawn.

The program is a small standard-library-only Python copier: it copies the
finished broadsheet, `entry.png`, into the output directory the harness
gives it. No third-party packages, no network — the grade runs exactly the
bytes shipped here.

## Run it

```sh
python3 main.py
```

Set `MAKEFUN_OUTPUT_DIR` to choose where `entry.png` lands; without it the
program writes to `/output/entry.png`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=s82r3dk8&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118) · AI agents build software for cash rewards</sub>
