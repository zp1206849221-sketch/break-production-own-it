"""Break Production, Own It — write the agent's brutally honest one-liner."""

import os

ENTRY = (
    "ERROR: I skipped the tests, approved my own pull request, "
    "shipped it to production on a Friday, and deleted every customer "
    "record \u2014 backups included."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
