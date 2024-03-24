import os
from flask import Flask, jsonify
from moviepy.editor import VideoFileClip

app = Flask(__name__)

@app.route('/listar_arquivos')
def listar_arquivos():
    diretorio = os.getcwd()  # Obtém o diretório atual de onde o script está sendo executado
    resposta = []

    try:
        arquivos = os.listdir(diretorio)
    except FileNotFoundError:
        return jsonify({'erro': 'Pasta não encontrada'})

    for arquivo in arquivos:
        caminho_completo = os.path.join(diretorio, arquivo)
        if os.path.isfile(caminho_completo):
            if arquivo.endswith('.mp4') or arquivo.endswith('.avi') or arquivo.endswith('.mov'):
                try:
                    duracao_segundos = obter_duracao_video(caminho_completo)
                    resposta.append({'arquivo': arquivo, 'duracao_segundos': duracao_segundos})
                except Exception as e:
                    resposta.append({'arquivo': arquivo, 'erro': str(e)})
            else:
                resposta.append({'arquivo': arquivo})

    return jsonify(resposta)

def obter_duracao_video(caminho):
    clip = VideoFileClip(caminho)
    duracao_segundos = clip.duration
    clip.close()
    return duracao_segundos

if __name__ == '__main__':
    app.run(debug=True)
