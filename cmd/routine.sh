#!/bin/bash
url="your_url"
file="your_file"

# Git repository to update
repo="your_repo"

# Send the GET request and save the response body
response=$(curl -s "$url")

# Read the contents of the file
contents=$(cat "$file")

# Compare the response body with the contents of the file
if [ "$response" != "$contents" ]; then
  # If they're not equal, update the file and the Git repository
  echo "$response" > "$file"
  cd "$repo"
  git add "$file"
  git commit -m "Updated file"
  git push
fi
