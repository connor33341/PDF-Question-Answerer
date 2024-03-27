#!/bin/bash
url="https://raw.githubusercontent.com/connor33341/PDF-Question-Answerer/main/cmd/version.txt"
file="version.txt"
repo="connor33341/PDF-Question-Answerer"

response=$(curl -s "$url")
contents=$(cat "$file")

if [ "$response" != "$contents" ]; then
  echo "$response" > "$file"
  #cd "$repo"
  git pull
  git add "$file"
  pip install -r requirements.txt
  git commit -m "Update Version"
fi
