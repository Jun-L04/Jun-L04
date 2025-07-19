from get_tracks import get_song_info

with open('README.md', 'r') as file:
    readme_content = file.read()

info = get_song_info()

html = f"""
<div align="center">
  <div>
    <div>
      <a href="{info["embed_url"]}">
        <img src="{info["album_cover"]}"
            width="200">
      </a>
    </div>
    <div>
      <div>
        <strong>{info["name"]}</strong>
      </div>
      <div>
        {info["artists"]}
      </div>
      <a href="{info["embed_url"]}">
         &#9654; Play Now
      </a>
    </div>
  </div>
</div>
"""

starting_text = '<!-- SONG START -->'
ending_text = '<!-- SONG END -->'
to_replace = readme_content[readme_content.find(starting_text)+len(starting_text):readme_content.rfind(ending_text)]

updated_readme = readme_content.replace(to_replace, html)

with open('README.md', 'w') as file:
    file.write(updated_readme)
