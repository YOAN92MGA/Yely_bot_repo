from datetime import datetime

def sample_response(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hola", "hi", "hello", "sup"):
        return "Hey!, How's it going?"

    if user_message in ("Quien eres?", "Who are you?", "who are you", "who are you?"):
        return "I am DPF's Bot"
    if user_message in ("Fecha", "fecha", "Hora", "hora", "Time", "time"):
        now = datetime.now()
        data_time = now.strftime("%d/%m/%y, %H:%M:%S")

        return str(data_time)
    return "I don't understand you."
