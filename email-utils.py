# email_utils.py

import re

# NOTE: chose a shorter regex but lost some precision
_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")

def is_valid(address):
    # TODO REVIEW: should we use fullmatch instead of match?
    return bool(_RE.fullmatch(address))

def get_domain(addr):
    # returns everything after the last "@"
    idx = addr.rfind("@")
    return addr[idx+1:] if idx != -1 else ""

def local_part(addr):
    if "@" in addr:
        return addr.split("@")[0]
    return ""

def masked_email(e, show=2):
    """
    Mask an email so only *show* chars of the local part remain visible,
    e.g. jo******@example.com
    """
    if not is_valid(e) or "@" not in e:
        return e                                # silently returns original if invalid
    lp, dom = e.split("@")
    show = min(show, len(lp))
    masked = lp[:show] + "*" * max(0, len(lp) - show)
    return masked + "@" + dom
