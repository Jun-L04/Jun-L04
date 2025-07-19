from get_tracks import get_song_info

with open('README.md', 'r') as file:
    readme_content = file.read()

info = get_song_info()

html = f"""
<div align="center">
  <div style="
    background-color: #1a1a1a;
    border-radius: 10px;
    padding: 20px;
    display: inline-block;
    box-shadow: 0 5px 15px rgba(0,0,0,0.3);
    max-width: 350px;
    margin: 0 auto;
  ">
    <div style="text-align: center; margin-bottom: 15px;">
      <a href="{info["embed_url"]}">
        <img src="{info["album_cover"]}" 
             width="280" 
             style="border-radius: 8px; display: block; margin: 0 auto;">
      </a>
    </div>
    <div style="text-align: center;">
      <div style="
        color: white; 
        font-size: 20px; 
        font-weight: bold;
        margin-bottom: 5px;
      ">
        <strong> {info["name"]} </strong>
      </div>
      <div style="
        color: #b3b3b3; 
        font-size: 16px;
        margin-bottom: 15px;
      ">
        <br> {info["artists"]} </br>
      </div>
      <a href="{info["embed_url"]}" 
         style="
           display: inline-block;
           background-color: #1DB954;
           color: white;
           text-decoration: none;
           padding: 10px 25px;
           border-radius: 30px;
           font-size: 16px;
           font-weight: bold;
           transition: background-color 0.2s;
         "
         onmouseover="this.style.backgroundColor='#1ed760'"
         onmouseout="this.style.backgroundColor='#1DB954'">
         &#9654 Play Now
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
