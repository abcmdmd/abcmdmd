"""
All of my commonly-used functions!

Import as: 
! wget -q -nc https://raw.githubusercontent.com/abcmdmd/abcmdmd/refs/heads/main/funs.py

Table of contents (ctrl+F):
1. read in google sheets from urls: google_sheet_to_input(url)
"""

import polars as pl
import re


# --------------------------------------- 1 ------------------------------------ 
# read in google sheets from urls
# note: make sure you set viewing permissions to public...
def google_sheet_to_input(url):
  url_clean = url.strip()

  # extract sheet ID
  sheet_match = re.search(r"/spreadsheets/d/([^/]+)", url_clean)
  if not sheet_match:
      raise ValueError("Could not find sheet ID!!! Make sure the input URL looks like: https://docs.google.com/spreadsheets/d/{sheet_id}/edit?gid={gid}")

  sheet_id = sheet_match.group(1)

  # extract gid
  gid_match = re.search(r"gid=([0-9]+)", url_clean)
  if not gid_match:
      raise ValueError("Could not find GID code. Make sure the URL includes something like: gid=1458194591")
  gid_code = gid_match.group(1)

  # building export url
  csv_url = (f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid_code}#gid={gid_code}")
  readable_df = pl.read_csv(csv_url)
  return readable_df
