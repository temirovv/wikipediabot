def get_info(title, language):
    import wikipedia
    wikipedia.set_lang(language)

    text = wikipedia.summary(title, sentences=1)
    return text
