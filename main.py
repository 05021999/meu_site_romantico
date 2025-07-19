from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

inicio_relacionamento = datetime(2024, 9, 7, 18, 0)

@app.route('/')
def index():
    agora = datetime.now()
    tempo_juntos = agora - inicio_relacionamento

    dias = tempo_juntos.days
    horas = tempo_juntos.seconds // 3600
    minutos = (tempo_juntos.seconds % 3600) // 60
    segundos = tempo_juntos.seconds % 60

    fotos = [
        'foto1.jpg', 'foto2.jpg', 
        'foto3.jpg', 'foto4.jpg', 
        'foto5.jpg', 'foto6.jpg', 
        'foto7.jpg', 'foto8.jpg', 
        'foto9.jpg', 'foto10.jpg',
        'foto11.jpg', 'foto12.jpg'
    ]

    frases = [
        "Ao seu lado, todo lugar vira paraíso. 🏝️💑",
        "Seu sorriso é meu cantinho de paz. 😊❤️",
        "Te amar é a melhor viagem da minha vida. ✈️💘",
        "No mar da vida, sou feliz porque tenho você. 🌊💕",
        "Nosso amor é aventura, coragem e liberdade. 🧗‍♂️💞",
        "Cada beijo teu é um salto de felicidade. 💋✨",
        "Amor simples, sorriso largo, vida linda contigo. 🌤️💖",
        "Nosso amor é saúde pra alma e coração. 🏃‍♀️❤️",
        "Com você, qualquer caminho é poesia. 🌙🌺",
        "Meu porto seguro, meu abrigo, meu amor. 🌴💘",
        "Com você, até o horizonte parece mais perto. 🌅✨",
        "Seu sorriso é o meu presente favorito. 🎁✨"
    ]

    return render_template(
        'index.html',
        dias=dias,
        horas=horas,
        minutos=minutos,
        segundos=segundos,
        fotos=zip(fotos, frases)  # <-- junta foto + frase
    )

if __name__ == "__main__":
    app.run(debug=True)
