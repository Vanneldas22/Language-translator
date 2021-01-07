from googletrans import Translator

translator = Translator()

out = translater.translate(""क्या हाल है", dest = "en")

print(out.text)