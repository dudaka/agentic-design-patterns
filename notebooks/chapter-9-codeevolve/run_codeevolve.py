"""Launch CodeEvolve with Linux-like multiprocessing semantics on macOS.

CodeEvolve assumes the 'fork' start method (shared mp.Value defaults and an
import-time mp.Manager in islands/sync.py) and calls os.sched_getaffinity,
which only exists on Linux. This launcher applies both shims, then runs the
normal CLI. Usage is identical to the `codeevolve` command.
"""
import multiprocessing as mp
import os
import sys

if sys.platform == "darwin":
    mp.set_start_method("fork", force=True)
if not hasattr(os, "sched_getaffinity"):
    os.sched_getaffinity = lambda pid: set(range(os.cpu_count()))

from codeevolve.cli import main  # noqa: E402  (must come after the shims)

if __name__ == "__main__":
    sys.exit(main())
