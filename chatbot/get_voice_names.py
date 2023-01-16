from AppKit import NSSpeechSynthesizer

def getvoicenames():
    """I am returning the names of the voices available on Mac OS X."""
    voices = NSSpeechSynthesizer.availableVoices()
    voicenames = []
    for voice in voices:
        voiceattr = NSSpeechSynthesizer.attributesForVoice_(voice)
        voicename = voiceattr['VoiceName']
        if voicename not in voicenames:
            voicenames.append(voicename)
    print( voicenames)


getvoicenames()