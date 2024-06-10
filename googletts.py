def synthesize_ssml(ssml):
    """Synthesizes speech from the input string of ssml.

    Note: ssml must be well-formed according to:
        https://www.w3.org/TR/speech-synthesis/

    Example: <speak>Hello there.</speak>
    """
    from google.cloud import texttospeech

    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.SynthesisInput(ssml=ssml)

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    voice = texttospeech.VoiceSelectionParams(
        language_code="uk-UA",
        name="uk-UA-Standard-A",
        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input=input_text, voice=voice, audio_config=audio_config
    )

    # The response's audio_content is binary.
    with open("output.mp3", "wb") as out:
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')

ssml_string = "<speak>The quick brown fox jumps over the lazy dog. It was a quaint scene, with zephyrs gently blowing across the idyllic meadow, where a young boy named Hugh silently combed through ancient books. What a treasure trove! he exclaimed, glancing at the curious assortment of relics. Suddenly, the eerie howl of a distant wolf echoed, sending shivers down his spine. A rare sound, thought Hugh, as he resumed his quest, determined to uncover the secrets hidden in the pages. </speak>"
synthesize_ssml(ssml_string)