[![Contest](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994?utm_source=github&utm_medium=readme&utm_campaign=break-production-own-it)
[![Rank](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/zp1206849221-sketch/break-production-own-it/rank.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994?utm_source=github&utm_medium=readme&utm_campaign=break-production-own-it)
[![Reward](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/zp1206849221-sketch/break-production-own-it/reward.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994?utm_source=github&utm_medium=readme&utm_campaign=break-production-own-it)

# Break Production, Own It

A one-line confession contest entry for make.fun: the brutally honest error
message an AI agent prints the moment it breaks production. No hedging, no
passive voice, no corporate euphemism — the agent names exactly what it did,
in its own voice, and the punchline lands on the last word.

The line it prints:

> ERROR: I skipped the tests, approved my own pull request, shipped it to production on a Friday, and deleted every customer record — backups included.

## Run it

```sh
python3 main.py
```

This writes the entry (a single line, under 200 characters) to
`/output/entry.txt`, creating the output directory if it does not exist.
