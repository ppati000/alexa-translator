import requests
from HTMLParser import HTMLParser
h = HTMLParser()

payload = { "txt": "Hello test", "language": "english", "alphabet": "IPA" }
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
 'Cache-Control': 'no-cache', 'Host': 'tom.brondsted.dk', 'Content-Type': 'application/x-www-form-urlencoded',
  'Referer': 'http://tom.brondsted.dk/text2phoneme/transcribeit.php'}

r = requests.post("http://tom.brondsted.dk/text2phoneme/transcribeit.php", data=payload, headers=headers)


second_half = r.text.split("<b>IPA transcription (phonemes):</b><br />")[1]
phonemes = second_half.split("</p>")[0]
phonemes = h.unescape(phonemes)
phonemes = phonemes.replace(" ", "")

print(phonemes)

 